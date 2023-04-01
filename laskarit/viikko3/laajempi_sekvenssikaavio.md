## Tehtävä 4: Laajempi sekvenssikaavio

```mermaid
sequenceDiagram
  participant main
  participant HKLLaitehallinto
  participant Lataajalaite
  participant Lukijalaite
  participant Kioski
  participant Matkakortti
  
  main->>HKLLaitehallinto:   
  activate HKLLaitehallinto

 
  main->> HKLLaitehallinto: lisaa_lataaja(rautatientori)
  main->> HKLLaitehallinto: lisaa_lukija(ratikka6)
  main->> HKLLaitehallinto: lisaa_lukija(bussi244)
  
  main-->>Kioski: Kioski()
  main->>osta_matkakortti("Kalle")
  Kioski->>main: Matkakortti("Kalle")
  
  
  
  
  
  
  
  
  
