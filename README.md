# Cos'è questo progetto?
Questo progetto in Python è un gioco dell'impiccato creato utilizzando i **socket** e l'architettura **client-server**. Ho deciso di lasciarlo incompleto per mancanza di tempo/volontà.

## Cosa è completo?
- Tutto il lato server è praticamente completo. 
- Nota sul server: potrei aver lasciato in sospeso la risoluzione di un bug all'interno della funzione `gioco()`, dove c'è il rischio che il server esegua due `send()` consecutive senza una `recv()` in mezzo, nonostante richieda l'input del client.

## Cosa è rimasto incompleto?
- Risoluzione del bug menzionato sopra.
- L'intero lato client.

## Cosa ho imparato da questo progetto?
- **Sintassi e basi di Python:**
  - Definizione di funzioni (`def`) e gestione del flusso di controllo (`if`, `while`, `break` ecc.).
  - Manipolazione delle stringhe (sostituzione delle lettere indovinate, formattazione dei messaggi di gioco).
  - Logica di input (`input()`) e output(`print()`)
  - Gestione delle strutture dati per tenere traccia dello stato della partita (tentativi, parole, input).
  - L'uso e la funzione dei commenti nei linguaggi di programmazione.
- **Programmazione di rete e Socket:**
  - Creazione e configurazione di socket con il modulo nativo `socket` di Python.
  - Gestione del ciclo di vita della connessione lato server (`bind()`, `listen()`, `accept()`).
  - Scambio di dati tramite `send()` e `recv()` e relativa codifica/decodifica del testo (`encode()` / `decode()`).
- **Architettura Client-Server e Protocollo:**
  - Come strutturare la logica di un gioco multiplayer/remoto separando l'elaborazione (Server) dall'interfaccia (Client).
  - L'importanza del sincronismo nei protocolli di rete: coordinare ogni `send()` con una rispettiva `recv()` per evitare che il flusso di comunicazione si blocchi o si desincronizzi.
