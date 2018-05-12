# Attres

**English version below!**
## Was tut Attres

Attres sucht zu einem Koordinatenpaar die erste passende Adresse. 

## Wie macht Attres das?

Schlecht. Attres arbeitet nicht mit mathematischen Funktionen, sondern mit den Daten der Overpass-API. Natürlich geht es bestimmt irgendwie effizienter, allerdings stand in diesem Projekt simple benutzung im vordergrund.

## Usage
Importiere Attres mit `import Attres` oder wie auch immer du die Python-Datei nach dem Download nennst.
Danach kannst du mit `attres.getAddress(longitude, latitude)` nach der Adresse zu diesem Punkt fragen. 
Als Antwort erhäkst du einen String, die Adresse enthät, und außerdem den Namen des Objekts, wenn es einen hat. Der zweite übergabeparameter ist die genauigkeit. Sie gibt an, in welchem Umkreis sich die Adresse befinden musste, um angenommen zu werden. Werte ab 70 sind nicht mehr als zuverlässig einzuschätzen.


Searches for nearest Address for coordinates.
