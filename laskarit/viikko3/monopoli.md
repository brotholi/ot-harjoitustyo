```mermaid
 classDiagram
    
    
    class Pelaaja {
        id: pelaajan nimi
    }

    class Pelilauta {
     id: string   
    }
    
    
    class Ruutu {
    - id : int n
    - seur : n + 1
     }
    

    class Normaalit kadut {
    id : string nimi
    }
         
    class Pelinappula {
    }
    
    direction LR
    Pelilauta "1" -- "2-8" Pelaaja
    direction TD
    Pelaaja "1" --> "1" Pelinappula
    Pelilauta "1" --> "40" Ruutu
    Pelinappula "1" --> "1" Ruutu
    Ruutu --> Aloitusruutu
    Ruutu --> Vankila
    Ruutu --> Sattuma
    Ruutu --> Yhteismaa
    Ruutu --> Asemat
    Ruutu --> Laitokset
    Ruutu --> Normaalit kadut
    
    
    Pelilauta -- Sijainti --> Ruutu


    
```
