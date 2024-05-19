# Life simulation

## Run

Use PO1.sin with Visual Studio. Program created on Python 3.12.

## Description

This repository contains a program that simulates lives of animals and plants. All of these have self statistics.
Player can move on board using arrows. If collision occurs, compare the object statistics, and one of these is removed.

## Rules

1. The game is played in turns.
2. The order of moves depends on the initiative.
3. Organisms are aging.
4. Contact of the same species (if mature) leads to a new animal.
5. The collision of different species leads to the death of one of them. The one with the greater strength or the one that defends itself survives.

## Statistics

| Name                | Symbol | Strength | Initiative | Special                                                  |
|---------------------|--------|----------|------------|----------------------------------------------------------|
| Zolw                | Z      | 2        | 1          | Have a lower strength to attack than to defend.          |
| Wilk                | W      | 9        | 5          | -----------                                              |
| Owca                | O      | 4        | 4          | -----------                                              |
| Lis                 | L      | 3        | 7          | Avoids stronger creatures.                               |
| Antylopa            | Z      | 2        | 1          | Moves on two fields, have a half chance to dodge attack. |
| CyberOwca           | CO     | 11       | 4          | Finds the nearest pine borscht and to eat it.            |
| BarszczSosnowskiego | s      | 10       | 0          | Attacks neighboring animals.                             |
| Guarana             | g      | 0        | 0          | Add 3 strength.                                          |
| Mlecz               | m      | 0        | 0          | Three times the reproduction.                            |
| Trawa               | t      | 0        | 0          | -----------                                              |
| WilczaJagoda        | j      | 99       | 0          | Kills organism that ate it.                              |
| Czlowiek            | @      | 5        | 4          | Player controls it. Has a special ability.               |

## Player

- Arrows: movement
- Esc: stop game
- Key P: use skill

The game is saved in the data.dat file. 
Special skill removes neighboring organisms.