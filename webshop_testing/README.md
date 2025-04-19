#  🛒 Webshop Testing – Beteendedrivna tester med Behave
Detta projekt innehåller automatiserade BDD-tester (Behavior Driven Development) för en e-handelsplattform med fokus på varukorgens funktioner. Testerna är skrivna i Gherkin och körs med hjälp av Python-ramverket [Behave](https://behave.readthedocs.io/).

---
## 📋 Innehåll

## Scenarios
### Alla scenarion finns beskrivna i ./features/*.feature
### ✅ Uppgift 1 – Identifiera testtyper
- **Funktionella tester**: Säkerställer att användarens interaktion med varukorgen fungerar enligt kravspecifikation.
- **Integrationstester**: Kontroll av interaktionen mellan varukorgen och exempelvis lagerhantering.
- **Systemtester**: Testar hela varukorgsflödet som en helhet.
- **Regressions- och acceptanstester**: Säkerställer att ny funktionalitet inte bryter befintlig.

### ✅ Uppgift 2 – Testnivåer och testmetoder
- **Testnivåer**:
  - *Enhetstestning*: T.ex. kontroll av beräkningar för totalpris.
  - *Integrationstestning*: T.ex. samspel mellan varukorg och lagerstatus.
  - *Systemtestning*: Fullständigt flöde, från inloggning till köp.

- **Testmetoder**:
  - *Black-box*: Användarcentrerade scenarier utan att titta på implementation.
  - *White-box* (valfritt): För intern logik i exempelvis rabattberäkningar.

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

## 📁 Projektstruktur

``` text 
webshop_testing/
├── features/
│   ├── behave.ini                  # Konfiguration för Behave
│   ├── cart.feature                # Tester för grundläggande varukorgsfunktioner
│   └── extra_features.feature      # Tester för avancerade funktioner (rabatt, inloggning, lager)
│
├── steps/
│   ├── cart_steps.py               # Stegdefinitioner för cart.feature
│   └── extra_features_steps.py     # Stegdefinitioner för extra_features.feature
│
├── requirements.txt                # Lista över beroenden
├── README.md                       # Projektbeskrivning (du läser den nu)


```

## ⚙️ Verktyg och teknik

- **Språk:** Python  
- **BDD-ramverk:** Behave  
- **Specifikation:** Gherkin (`.feature`-filer)  
- **Struktur:** Feature-filer + matchande step-definitioner i Python