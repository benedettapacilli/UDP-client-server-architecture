<div>
<h1 style="text-align: center">Elaborato per il corso</h1>
<h1 style="text-align: center">di Programmazione di Reti</h1>
<h3 style="text-align: center">2021/2022</h3>
<br><br>
<h1 style="text-align: center">Architettura server client UDP</h1>
<br><br>
<h4 style="text-align: center">Benedetta Pacilli :   0000975296</h4>
</div>

	
## Descrizione
L'elaborato si compone di due script principali: 
- **server.py**
- **client.py**

### server.py
Ad inizio script viene creato il socket e vengono impostati *localhost* e *10000*, rispettivamente come indirizzo IP e porta. Questi due dati, che formano il server address, sono subito mostrati all'avvio del server, il quale poi fa il bind per associare il server address al socket e infine, si mette in ascolto.
Per poter gestire le richieste di più client è stato importato *threading* in modo da creare un thread per ogni richiesta che si riceve. 
Ogni richiesta di client viene gestita tramite la funzione *handler*: la funzione prende come argomenti l'operazione da svolgere e l'address del client che ha effettuato la richiesta; controlla se l'operazione è una di quelle ammissibili (list, get, put, exit) e in base a che operazione è viene chiamata un'apposita funzione presa da **server_library.py** (che viene importato in server.py).

