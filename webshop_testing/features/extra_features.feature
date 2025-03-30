Feature: Hantering av avancerade funktioner i varukorg

  Scenario Outline: Användaren får rabatt vid köp av fler än 3 böcker
    Given varukorgen är tom
    When användaren lägger till 2 av "Python 101" som kostar "200"
    And användaren lägger till 3 av "Dragonball Z" som kostar "150"
    Then totalsumman ska vara 765

        Examples:
      | bok         | pris | antal | rabatterat_pris |
      | Python 101  | 200  | 2     | 720             |
      | Dragonball Z| 150  | 3     | 450             |


  Scenario Outline: Begränsa köp baserat på lagerstatus
    Given lagret innehåller "<lagerantal>" av "<bok>"
    When användaren försöker köpa "<köpantal>" av "<bok>"
    Then varukorgen ska innehålla "<förväntat_antal>" av "<bok>"
    And ett meddelande ska visas <meddelande>

    Examples:
      | bok         | lagerantal | köpantal | förväntat_antal | meddelande                |
      | Python 101  | 5          | 3        | 3               | Boken lades i varukorgen  |
      | Dragonball Z| 2          | 5        | 2               | Endast 2 exemplar i lager |

  Scenario Outline: Inloggning krävs innan köp
    When användaren försöker köpa en bok utan att vara inloggad
    Then ett meddelande ska visas Du måste logga in först

    Examples:
      | bok          |
      | Dragonball Z |

  Scenario Outline: Lyckad och misslyckad inloggning
    When en användare med användarnamn "<användarnamn>" och lösenord "<lösenord>"
#    And användaren loggar in
    Then inloggningen ska vara "<status>"

    Examples:
      | användarnamn | lösenord | status  |
      | user1       | password | lyckad  |
      | user2       | fel      | misslyckad |