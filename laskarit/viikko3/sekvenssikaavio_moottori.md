Tehtävä 3: Sekvenssikaavio

```mermaid
sequenceDiagram
  participant main
  participant Machine
  participant FuelTank
  participant Engine
  main->>Machine: Machine() 
  Machine->>FuelTank: FuelTank()
  Machine->>FuelTank: tank.fill(40)
  Machine->>Engine: Engine()
  
  main->>+Machine: drive()
  Machine-->>+Engine: start()
 
  Engine-->>FuelTank: consume(5)
  Machine->>Engine: is_running()
  Engine->>Machine: True
  Machine->>Engine: use_energy()
  Engine->>FuelTank: consume(10)
  E
  
  
  
  
```
