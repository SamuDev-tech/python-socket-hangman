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

# What is this project?
This Python project is a Hangman game built using **sockets** and a **client-server** architecture. I decided to leave it unfinished due to a lack of time/motivation.

## What is complete?
- Almost the entire server side is finished.
- Note on the server: I might have left a bug unresolved inside the `gioco()` function, where there is a risk that the server performs two consecutive `send()` calls without a `recv()` in between, even though it expects input from the client.

## What remains incomplete?
- Fixing the bug mentioned above.
- The entire client side.

## What did I learn from this project?
- **Python Syntax and Fundamentals:**
  - Defining functions (`def`) and managing control flow (`if`, `while`, `break`, etc.).
  - String manipulation (replacing guessed letters, formatting game messages).
  - Input (`input()`) and output (`print()`) logic.
  - Managing data structures to keep track of game state (attempts, words, inputs).
  - The use and purpose of comments in programming languages.
- **Network Programming and Sockets:**
  - Creating and configuring sockets using Python's native `socket` module.
  - Managing the server-side connection lifecycle (`bind()`, `listen()`, `accept()`).
  - Exchanging data via `send()` and `recv()`, along with text encoding/decoding (`encode()` / `decode()`).
- **Client-Server Architecture and Protocol:**
  - How to structure the logic of a multiplayer/remote game by separating processing (Server) from the interface (Client).
  - The importance of synchronization in network protocols: pairing every `send()` with a corresponding `recv()` to prevent the communication flow from stalling or becoming desynchronized.
