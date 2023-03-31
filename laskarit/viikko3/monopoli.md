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
     +Ruututyyppi 
    
    }
    
    class Ruututyyppi {
     Aloitusruutu
     Vankila
     Sattuma
     Yhteismaa
     Asemat
     Laitokset
   
    }
    
    

    class Normaalit kadut {
    id : string nimi
    }
         
    class Pelinappula {
    }
    

    Pelilauta "1" -- "2-8" Pelaaja

    Pelaaja "1" --> "1" Pelinappula : omistaa
    Pelilauta "1" --> "40" Ruutu : sisältää
    Pelinappula "1" --> "1" Ruutu : sijaitsee


    
    Ruututyyppi --> Sijainti
    Ruutu "1" ..> "1" Ruututyyppi 
    Ruututyyppi -- Normaalit kadut
    Ruutu "1" -- "1" Sijainti
    
    Pelilauta -- Sijainti : Tietää aloitusruudun sijainnin
    Pelilauta -- Sijainti : Tietää vankilan sijainnin
    
    


    
```
