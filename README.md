
# Long-term-ping-test
Pingt einen Host und loggt bei Fehler die Uhrzeit mit.
Script wurde geschrieben um einen Netzwerkswitch über längere Zeit zu testen.
Hinweis: Bitte nicht das Fenster schließen, einfach einmal Str+C drücken. Sonst wird die Zusammenfassung am Ende nicht richtig generiert
Bei Programmstart wird gefragt welcher Host gepingt werden soll, bsp: `192.168.178.1` oder `google.com`
## Einstellungen in der Python Datei:
-  `dateiname`: Wie die Datei heißen soll, default ist "log"=>log.txt.
 - `abstand`: In welchem Abstand ein ping gesendet werden soll.
 - `max_ping`: None für unbegrenzt. Sonst eine Nummer einfügen und nach der Anzahl an Pings wird das Programm beendet.
 - `log_level`: Es gibt 0 und 1, bei 0 werden nur die fehlgeschlagenen Pings mitgeloggt, bei 1 hingegen alle

* * *
## Beispiel log.txt Datei:

**Loglevel ist auf 1:**
```
Startzeit: 2021-01-13 14:22:14
Gepingt wurde: google.com
Der Abstand zwischen den Pings betrug jeweils 60 Sekunden.
Das Loglevel ist bei 1, heißt es werden alle Pings geloggt.
------------
2021-01-13 14:22:17: Erfolgreich
2021-01-13 14:23:20: Erfolgreich

------------
Der Ping wurde um 2021-01-13 14:23:31 abgeschlossen
Zusammenfassung: Es wurden 2 Pings gesendet. Davon sind 0 fehlgeschlagen und 2 erfolgreich gewesen. Die Erfolgsquote liegt bei: 100.0%
```

**Logelevel ist auf 0:**
```
Startzeit: 2021-01-13 14:23:42
Gepingt wurde: google.com
Der Abstand zwischen den Pings betrug jeweils 60 Sekunden.
Das Loglevel ist bei 0, daher werden nur fehlgeschlagene Pings geloggt.
------------
2021-01-13 14:24:46: Fehlgeschlagen

------------
Der Ping wurde um 2021-01-13 14:26:07 abgeschlossen
Zusammenfassung: Es wurden 3 Pings gesendet. Davon sind 1 fehlgeschlagen und 2 erfolgreich gewesen. Die Erfolgsquote liegt bei: 66.67%
```



