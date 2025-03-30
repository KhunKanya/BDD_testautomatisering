# Behave webshop testing

## Scenarios
Alla scenarion finns beskrivna i ./features/*.feature

## Hur jag löste uppgifterna
Jag formulerade Gherkin scenarion på vanligt vardagsspråk i svenska, sedan bröt upp till behave i Python, steg för steg.
Extrauppgifterna jag valde var
* Rabbatfunktion
* Lagerstatusfunktion
* Krävande inloggning
* Lösenord

### Vad var det mest utmanande?
Det mest utmanande var definitivt att fånga stdout-text från en funktion som också returnerar något
```python
        print("Boken lades i varukorgen")
        return {book: stock.pop(book)} 
```
Detta tvingade mig att lära mig om IOredirect och nya bibliotek jag ej använt tidigare.

En annan nämnvärd utmanande sak var att formulera behave-koden när man hade flera exempel från Gherkin. har man till exempel flera böcker så skapas flera Scenarion så man måste duplicera en del kod.

### Vilka resurser använde du för att lösa del 2?
Jag använde stackoverflow, GeeksforGeeks och lite AI för att generera Gherkin examples från mina formulerade outlines. 