Tehtävä 3: Sekvenssikaavio

```mermaid
sequenceDiagram
  participant main
  participant Machine
  participant FuelTank
  participant Engine
  main->>Machine: Machine() 
  Machine->>FuelTank: FuelTank()
  FuelTank->>FuelTank: fuel.contents = 0
  Machine->>FuelTank: tank.fill(40)
  Machine-->>Engine engine.start()
  Engine-->>FuelTank: tank.consume(5)
  
  
  
```
