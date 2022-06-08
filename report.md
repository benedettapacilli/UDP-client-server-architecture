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

### server_library.py
File python usato come libreria per il Server. 
Contiene le seguenti funzioni:
+ **list :**
	Viene creata una lista di stringhe contenente i nomi dei file nell'apposita cartelle *server_files* (qui vengono salvati i file che arrivano da client o che devono essere inviati)
	Ogni nome di file presente in questa lista viene poi inviato al client che ne ha fatto richiesta. 
+ **send :**
	Se un client richiede l'operazione *get \<fileName>*  il server utilizza la funzione *send* alla quale vengono passati il socket, l'address del server e l'operazione richiesta. Viene presa l'operazione, composta di due parole e con una split, si prende il secondo termine, rappresentante il nome del file richiesto. Se è presente in *server_files*, il file  viene aperto in modalità di lettura e viene inviato a pacchetti di dimensioni della costante *BUFFERSIZE*.  Una volta finito di inviare il file, come ultima cosa, viene inviata la costante EOF.
+ **receive :**
	La funzione receive viene chiamata quando un client sceglie l'operazione *put \<fileName>*.  A questa funzione vengono passati l'address del server e l'operazione del client, di quest'ultima viene presa in considerazione la seconda parola(il nome del file da inviare al server). In *server_files* viene aperto, in modalità scrittura, un file con lo stesso nome del file richiesto dal client. Finchè il file non finisce (ovvero quando si rlegge la costante EOF), questo viene inviato a pacchetti di dimensione *BUFFERSIZE* e scirtto sul file creato in *server_files*; dopo di chè il file viene chiuso. In questo modo, se quel file scelto dal client esiste già in *server_files* , questo viene sovrascritto.
+ **end_process :**
	Quando un client sceglie la funzione *exit* sia il socket che il processo del server vengono chiusi.