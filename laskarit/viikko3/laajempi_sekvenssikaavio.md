## Tehtävä 4: Laajempi sekvenssikaavio

```mermaid
sequenceDiagram
  participant main
  participant HKLLaitehallinto
  participant Lataajalaite
  participant Lukijalaite
  participant Kioski
  participant Matkakortti
  
  main->>HKLLaitehallinto: HKLLaitehallinto()
  activate HKLLaitehallinto

 
  main->> HKLLaitehallinto: lisaa_lataaja(rautatientori)
  main->> HKLLaitehallinto: lisaa_lukija(ratikka6)
  main->> HKLLaitehallinto: lisaa_lukija(bussi244)
  
  main-->>Kioski: Kioski()
  activate Kioski
  main->>Kioski: osta_matkakortti("Kalle")
  deactivate Kioski
  Kioski->>main: Matkakortti("Kalle")
  
  main->>Lataajalaite: lataa_arvoa(kallen_kortti, 3)
  activate Lataajalaite
  Lataajalaite->>Matkakortti: kasvata_arvoa(3)
  Lataajalaite-->>main:   
  deactivate Lataajalaite
  
  main->>Lukijalaite: ratikka6.ostalippu(kallen_kortti, 0)
  activate Lukijalaite
  Lukijalaite->>Matkakortti: vahenna_arvoa(RATIKKA)
  dectivate Lukijalaite
  Lukijalaite-->>main:  
  
  
  main->>Lukijalaite: bussi244.osta_lippu(kallen_kortti, 2)
  
  
  
  
  
  
  
  
  
  
  
  
  
