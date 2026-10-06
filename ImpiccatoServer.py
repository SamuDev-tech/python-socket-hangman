import socket
import random

# 1. Associamento dell' indirizzo IP al numero di porta del server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 9999
serversocket.bind((host, port))

# 2. Mettere in "ascolto" il server per permettere ai client di connettersi con esso (max 4)
serversocket.listen(4)

# 3. Accettare la richiesta di connessione da parte del client e
#    mandare la conferma che la connessione è stata effettuata
clientsocket, addr = serversocket.accept()
clientsocket.send(b"Server: La connessione e' stata effettuata")

# Funzione che ritorna il progresso del gioco
def messaggio(vite, parola, lettereElencate = None):
    if lettereElencate is None or not lettereElencate:
        lettereElencate = []
        messaggio = "_ " * len(parola)
        messaggio = messaggio + "\nVite in possesso: " + str(vite) + "\nLettere elencate: " + str(lettereElencate) + "\nInserisci una lettera o una parola: "
        return messaggio
    else:
        messaggio = ""
        for i in parola:
            if i.casefold() in [lettera.casefold() for lettera in lettereElencate]: 
                # [...] = Lista temporanea; 
                # for lettera in lettereElencate = prendi qualsiasi lettera 
                #                                  presente in lettereElencate; 
                # lettera.casefold() = trasforma lettera in un carattere minuscolo.
                messaggio += str(i.casefold()) + " "
            else:
                messaggio += "_ "
        messaggio = messaggio + "\nVite in possesso: " + str(vite) + "\nLettere elencate: " + str(lettereElencate) + "\nInserisci una lettera o una parola: "
        return messaggio            
    
# Funzione che avvia il gioco
def gioco():
    # 1. Seleziona una delle parole all' interno del file di testo per iniziare il gioco
    try:
        with (open("Parole.txt")) as f: # f = open("Parole.txt")
            parole = f.read().splitlines() # Crea una lista delle parole che sono dentro il file
            parola = random.choice(parole) # Sceglie a caso una delle parole
    except FileNotFoundError:
        clientsocket.send(b"Errore.")
        print("Errore.")
        return
    print(parola) # Solo per debugging

    # 2. Mostra al client la parola in maniera "oscurata" piu le sue vite iniziali
    #    e lo invita a giocare
    lettereElencate = [] # lista di lettere elencate dall' utente, servirà dopo
    vite = 6
    clientsocket.send(messaggio(vite, parola).encode())

    # 3. Il gioco inizia e continua finchè il client non vince o non perde
    gameOver = False
    while not gameOver:
        # Riceve l'input dal client e vede se la lettera inserita corrisponde alla parola o,
        # nel caso abbia inserito una parola, se corrisponde a quella corretta o no
        if vite <= 0:
            gameOver = True
            break
        if lettereElencate:
            if all(char.casefold() in [lettera.casefold() for lettera in lettereElencate] for char in parola):
                gameOver = True
                break      
        scelta = clientsocket.recv(1024).decode().strip()
        if len(scelta) > 1 and len(scelta) == len(parola):
            gameOver = True
            if scelta.casefold() != parola.casefold():
                vite = 0
                break
            break
        elif len(scelta) == 1:
            if lettereElencate:
                if scelta.casefold() in [lettera.casefold() for lettera in lettereElencate]:
                    clientsocket.send(b"Hai gia' inserito questa lettera, riprova!" + messaggio(vite, parola, lettereElencate).encode())
            letteraTrovata = False
            lettereElencate.append(scelta)
            if scelta.casefold() in [p.casefold() for p in parola]:
                clientsocket.send(b"Indovinato!\n\n" + messaggio(vite, parola, lettereElencate).encode())       
            else:
                vite -= 1
                clientsocket.send(b"Mi dispiace, hai sbagliato\n\n" + messaggio(vite, parola, lettereElencate).encode())
        else:
            clientsocket.send(b"Errore.")
    if gameOver and vite <= 0:
        clientsocket.send(b"Mi dispiace, hai perso.")
    elif gameOver and vite > 0:
        clientsocket.send(b"Congratulazioni, hai vinto!")
    else:
        clientsocket.send(b"Errore.")
        print("Errore.")

# Funzione che resistuisce le impostazioni del gioco.
def opzioni():
    while True:
        scelta = 0
        menu = """================= OPZIONI =================
        Premi:
        [] - Lava Mode (COMING SOON);
        1 - Regole di gioco;
        2 - Torna al menu iniziale;
        Scelta: """
        clientsocket.send(menu.encode())
        scelta = clientsocket.recv(1024).decode().strip()
        match scelta:
            case "1":
                regole = """================= REGOLE =================
                [NORMAL MODE]:
                L'Impiccato è un gioco di parole tradizionale che ho integrato in 
                questa app e l'obiettivo è indovinare una parola segreta una lettera 
                alla volta prima di esaurire le vite disponibili.

                Preparazione e svolgimento del gioco:
                    1. Scelta del paroliere: Il paroliere (il server) pensa a una parola
                    segreta e traccia una riga orizzontale per ogni lettera che la compone 
                    (es. _ _ _ _ _ per 5 lettere).
                    2. Proposta di una lettera: A turno, il giocatore (tu) che deve
                    indovinare la parola propone una lettera dell'alfabeto o, 
                    se si sente sicuro di quale è la parola segreta, può proporre la parola
                    che crede sia quella giusta.
                        - Lettera corretta: Se la lettera è presente nella parola, 
                          il paroliere la scrive su tutti gli spazi corrispondenti alle sue
                          posizioni.
                        - Lettera errata: Se la lettera non è presente, il paroliere 
                          trascrive la lettera proposta nell'elenco degli "errori" 
                          (per evitare di ripeterla) e toglie una vita al giocatore.
                        - Parola corretta: il giocatore vince istantaneamente.
                        - Parola errata: il giocatore perde instantaneamente.

                Condizioni di vittoria:
                    Il giocatore vince se riesce a completare l'intera parola o 
                    a indovinare la parola segreta prima che perda 
                    tutte le vite. Tuttavia, se il giocatore perde tutte le vite o 
                    dice la parola sbagliata, il giocatore ha perso e il paroliere rivelerà
                    la parola.
                
                Sistema di punteggio:
                [COMING SOON]

                [LAVA MODE]:
                [COMING SOON]
                """
                clientsocket.send(regole.encode())
            case "2":
                return
            case _:
                print("Errore.")

# Funzione che fa da menu di gioco.
def menu():
    lavaMode = None # Modalità di gioco che implementerò molto probabilmente in futuro.
    while True:
        scelta = 0
        menu = """================= IMPICCATO =================
        Premi: 
        1 - Gioca;
        2 - Opzioni;
        3 - Esci.
        Scelta: """
        clientsocket.send(menu.encode()) 
        scelta = clientsocket.recv(1024).decode().strip()
        match scelta:
            case "1":
                gioco()
            case "2":
                opzioni()
            case "3":
                clientsocket.send(b"Server: Grazie per aver giocato!")
                break
            case _:
                print("Errore.")

# 4. Mandare al client il menu di gioco e le scelte disponibili
try:
    menu()
# Si assicura che la connessione tra client e server venga chiusa anche 
# in casi di errore.
finally:
    clientsocket.close()
    serversocket.close()