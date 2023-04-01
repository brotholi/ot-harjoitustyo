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
  main->>Lataajalaite: Lataajalaite
  main->>Lukijalaite: Lukijalaite()
  main->>Lukijalaite: Lukijalaite()
 
  main->>HKLLaitehallinto: lisaa_lataaja(rautatientori)
  main->>HKLLaitehallinto: lisaa_lukija(ratikka6)
  main->>HKLLaitehallinto: lisaa_lukija(bussi244)
  
  main->>Kioski: Kioski()
  activate Kioski
  main->>Kioski: osta_matkakortti("Kalle")
  Kioski-->>main: Matkakortti("Kalle")
  deactivate Kioski
  
  main->>Lataajalaite: lataa_arvoa(kallen_kortti, 3)
  activate Lataajalaite
  Lataajalaite->>Matkakortti: Matkakortti("Kalle")
  Lataajalaite->>Matkakortti: kasvata_arvoa(3)
  Lataajalaite-->>main:   
  deactivate Lataajalaite
  
  
  main->>Lukijalaite: ostalippu(kallen_kortti, 0)
  activate Lukijalaite
  Lukijalaite->>Matkakortti: vahenna_arvoa(RATIKKA)
  Lukijalaite-->>main: True
  deactivate Lukijalaite
  
  main->>Lukijalaite: osta_lippu(kallen_kortti, 2)
  activate Lukijalaite
  Lukijalaite-->>main: False
  deactivate Lukijalaite
  
  
  ```
  
  
  
  
