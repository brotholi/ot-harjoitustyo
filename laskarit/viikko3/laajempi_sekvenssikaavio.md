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
  
  HKLLaitehallinto-->>Lataajalaite: Lataajalaite()   
  HKLLaitehallinto-->>Lukijalaite: Lukijalaite()
  HKLLaitehallinto-->>Lukijalaite: Lukijalaite()
 
  HKLLaitehallinto->>Lataajalaite: lisaa_lataaja(rautatientori)
  HKLLaitehallinto->>Lukijalaite: lisaa_lukija(ratikka6)
  HKLLaitehallinto->>Lukijalaite: lisaa_lukija(bussi244)
  
  HKLLaitehallinto-->>Kioski: Kioski()
  
  
  
  
  
  
  
  
