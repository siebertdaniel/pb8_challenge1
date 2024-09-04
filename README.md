Bevor es losgehen kann lade dir bitte unser Repo von herunter. \
Im Terminal: `git clone git@github.com:siebertdaniel/pb8_challenge1.git` \
Oder alternativ im Browser: https://github.com/siebertdaniel/pb8_challenge1 -> Code -> Download ZIP

Benötigte Programme:
- Python
- drawIO (Webseite-Interface reicht zum hochladen der bereitgestellten Dateien) \
https://app.diagrams.net/

**Willkommen zu unserem Workshop zu dem Softwaredesign Pattern "Abstract Factory"!**
\
Nachdem du nun einen Einblick in die Funktionsweise der Abstract Factory bekommen hast soll es nun darum gehen etwas Praxis in der Implementierung und Anwendung zu bekommen:

Als Software Entwickler in Hollywood hast du die ehrenvolle Aufgabe bekommen, den Prozess der Filmentwicklung für verschiedene Publisher zu digitalisieren.

**Aufgabe 1** \
Dein Vorgänger Max Movie hat bereits den größten Teil der Entwicklung abgeschlossen.
Mit dem Programm im Git Repo lassen sich bereits Action und Drama Filme sowie dazugehörige Trailer erstellen.
Nun meint der Verantwortliche aber, dass die angesprochene Zielgruppe der Filme noch zu gering ist. 
Schließlich muss der Gewinn maximiert werden, denn der Lambo bezahlt sich nicht von alleine!
Deine erste Aufgabe ist daher, das Programm dahingehend anzupassen, dass jetzt auch Comedy Filme nach demselben Schema erstellt werden können, wenn das Studio (Client) dies wünscht.  
Passe den Code also innerhalb des Ordners "Aufgabe 1" dahingehend an.

**Aufgabe 2**\
Nach Abschluss der Aufgabe hat der Verantwortliche wieder eine neue Anforderung.
Es sollen nun auch Serien produziert werden können. Hierbei sollen alle Genres erhalten bleiben. 
Der Aufwand soll so gering wie Möglich gehalten werden und die Dokumentation des Programms in Form eines UML-Klassendiagramms soll geupdatet werden.
Passe beides dahingehend im Ordner "Aufgabe 2" an!

Die Aufgaben werden am besten im jeweiligen Aufgabenordner bearbeitet.
Alternativ kann das Beispielprojekt genutzt werden, zu beachten ist nur, dass dies die Aufgaben komplexer macht, da das Beispiel umfangreicher ist.
Zum Schluss kann die Aufgabe auch außerhalb des Projektes durchgeführt werden.

**Aufgabe 3** (optional)\
Ich höre von draußen die Bremsen des neuen Sportwagens vom Chef.
Auf was für eine Schnapsidee wird er wohl dieses mal gekommen?!? \
"Immer diese scheiß Tiere und diese unfähigen Trainer ..." \
schnaufte er, nachdem er ohne anzuklopfen ins Büro gestürmt ist.\
"... Weißt du eigentlich wie schwer es ist einen Trainer für einen Braunbären zu finden?! Das ganze Set hat mir das Viech zerstört! Woher soll ich den wissen, das der nur mit Koalas arbeiten kann. 
Los Los, bau mir was! Warum haben wir kein System, welches mir Tierschauspieler und passende Trainer bereitstellt? Das kann doch nicht sein. 
Bis morgen hast du Zeit, sonst rollen hier Köpfe. Das ist mir hier alles schon wieder viel zu stressig, ich mach' erstmal Feierabend."\
Uuund da stürmt er auch wieder aus dem Büro. Toll. Ich darf Chef's Probleme lösen während er nach einem harten 5-minütigen Arbeitstag erstmal Feierabend macht. 
Aber so schwer kann das doch nicht sein. 
Vielleicht kann ich das Abstract Factory Pattern bei diesem Problem anwenden... \
Wenn die Tiere und ihre Trainer jeweils Produkte sind....\
Und es verschiedene Tierarten wie Vögel, Kleintiere und Wildtiere gibt...\
Vielleicht könnte ja eine Firma beides bereitstellen...\
Und ein Kunde müsste dann nur angeben, was er haben möchte...\
Das ist es, ich sollte zuerst ein Klassendiagramm erstellen. Danach kann ich es in Code umsetzen. Vielleicht werde ich ja morgen doch nicht gefeuert.