```mermaid
 classDiagram
    direction RL

    class Pelilauta {
     id: string   
    }


    class Pelaaja {
        id: pelaajan nimi
    }

    Pelilauta "1" -- "2-8" Pelaaja


```
