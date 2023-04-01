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
  
  HKLLaitehallinto->>Lataajalaite:    
  HKLLaitehallinto->>Lukijalaite:    
  HKLLaitehallinto-->>Lukijalaite:   
  
  
  
  
  
  
  
