```mermaid
 classDiagram
    direction RL

    class Pelilauta {
     id: string   
    }


    class Pelaaja {
        id: pelaajan nimi
    }

    class Pelilauta "1" -- "2-8" class Pelaaja


```