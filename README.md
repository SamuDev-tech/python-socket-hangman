# Cos'è questo progetto?
Questo progetto in Python è un gioco dell'impiccato creato utilizzando i **socket** e l'architettura **client-server**. Ho deciso di lasciarlo incompleto per mancanza di tempo/volontà.

## Cosa è completo?
- Tutto il lato server è praticamente completo. 
- Nota sul server: potrei aver lasciato in sospeso la risoluzione di un bug all'interno della funzione `gioco()`, dove c'è il rischio che il server esegua due `send()` consecutive senza una `recv()` in mezzo, nonostante richieda l'input del client.

## Cosa è rimasto incompleto?
- Risoluzione del bug menzionato sopra.
- L'intero lato client.