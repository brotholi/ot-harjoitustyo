## Tehtävä 4: Laajempi sekvenssikaavio

```mermaid
sequenceDiagram
  participant main
  participant HKLLaitehallinto
  participant Lataajalaite
  participant Lukijalaite
  participant Kioski
  participant Matkakortti
  
  main->>HKLlaitehallinto:   
  activate HKLlaitehallinto
  
  HKLlaitehallinto->>Lataajalaite:    
  HKLlaitehallinto->>Lukijalaite:    
  HKLlaitehallinto-->>Lukijalaite:   
  
  
  
  
  
  
  
