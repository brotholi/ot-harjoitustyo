TESTI

```mermaid
sequenceDiagram
  participant main
  participant Machine
  participant FuelTank
  main->>Machine: Machine() 
  Machine->>FuelTank: FuelTank()
  Machine->>FuelTank: tank.fill(40)
  
  
```
