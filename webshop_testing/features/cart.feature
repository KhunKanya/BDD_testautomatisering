Feature: Hantering av varukorg i webbutik

  Scenario Outline: Användaren lägger en bok i varukorgen
    Given varukorgen är tom
    When användaren lägger till "<bok>" som kostar "<pris>"
    Then varukorgen ska innehålla "<antal>" av "<bok>"
    And totalsumman ska vara "<totalpris>"

    Examples:
      | bok          | pris | antal | totalpris |
      | Python 101   | 200  | 1     | 200       |

  Scenario Outline: Användaren tar bort en bok från varukorgen
    Given varukorgen innehåller <antal> av "<bok>"
    When användaren tar bort "<bok>"
    Then varukorgen innehåller 0 av "<bok>"
    And totalsumman ska vara 0

    Examples:
      | bok          | antal | nytt_antal | total_pris  |
      | Python 101   | 1     | 1          | 200         |

  Scenario: Varukorgen visar alltid aktuell summa och antal böcker
    Given varukorgen innehåller 1 av "Python 101" och 1 av "Data Science"
    When användaren tittar i varukorgen
    Then varukorgen ska visa totalt 2 böcker
    And totalsumman ska vara 400
#

  Scenario: Om en bok redan finns i varukorgen ska antalet ökas
    Given varukorgen innehåller redan 1 av "Python 101"
    When användaren lägger till "Python 101" igen
    Then varukorgen ska innehålla 2 av "Python 101"
#
  Scenario: Användaren kan tömma varukorgen
    Given varukorgen innehåller böcker
    When användaren tömmer varukorgen
    Then varukorgen ska vara tom
