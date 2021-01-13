import os
import time
#Hier wird die ip abgefragt
ip_addr = input("Bitte die IP-Adresse eingeben:")
#Hier kann der Dateiname geändert werden. INFO: Datei wird überschrieben wenn sie bereits vorhanden ist!!!
dateiname = "log"
#Der Abstand zwischen den den Pings (in Sekunden)
abstand = "60"
#Maximale pings, auf None lassen wenn unbegrenzt
max_ping = None
#Hier muss man "1" eintragen wenn man auch die Erfolgreichen Pings geloggt haben möchte, bei einem anderen Wert werden nur die fehlgeschlagenen Pings geloggt
log_level = "1"
if (log_level == "0"):
    temp = "Das Loglevel ist bei 0, daher werden nur fehlgeschlagene Pings geloggt."
else:
    temp = "Das Loglevel ist bei 1, heißt es werden alle Pings geloggt."
file = ("./"+dateiname+".txt")
if os.path.isfile(file):
       os.remove(file)
datei = open(file, "w")
startzeit = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
datei.write("Startzeit: "+startzeit+"\nGepingt wurde: "+ip_addr+"\nDer Abstand zwischen den Pings betrug jeweils "+abstand+" Sekunden.\n"+temp+"\n------------\n")
datei.close()
(Fehlgeschlagen) = int("0")
(Erfolgreich) = int("0")
if max_ping is None:
    max_ping2 = 2
else:
    max_ping2 = max_ping
try:
    while not (max_ping2 == 0):
        response = os.system("ping " + ip_addr)
        aktuelle_zeit = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        datei = open(file, "a")
        if response == 0:
          Erfolgreich = (Erfolgreich + 1)
          if (log_level == "1"):
              datei.write(aktuelle_zeit+": Erfolgreich\n")
        else:
              datei.write(aktuelle_zeit+": Fehlgeschlagen\n")
              Fehlgeschlagen = (Fehlgeschlagen + int("1"))
        if max_ping is not None:
            max_ping2 = (int(max_ping2) -1)
        datei.close()
        print("Mit str+c kann man den Ping beenden. Bitte NICHT das Fenster schließen, sonst kommt keine Zusammenfassung ans Ende der Datei")
        print("Wartet "+abstand+" Sekunden")
        time.sleep(int(abstand))
except KeyboardInterrupt:
    print("Abgebrochen:")
datei = open(file, "a")
Erfolgsquote = round(((Erfolgreich / (Fehlgeschlagen+Erfolgreich))*100),2)
aktuelle_zeit = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
datei.write("\n------------\nDer Ping wurde um "+aktuelle_zeit+" abgeschlossen\nZusammenfassung: Es wurden "+str(Fehlgeschlagen+Erfolgreich)+" Pings gesendet. Davon sind "+str(Fehlgeschlagen)+" fehlgeschlagen und "+str(Erfolgreich)+" erfolgreich gewesen. Die Erfolgsquote liegt bei: "+str(Erfolgsquote)+"%")
datei.close()
