# Sovelluksen logiikka

## Pakkauskaavio


## Luokkakaavio

```mermaid
 classDiagram
      User "1" <-- "*" LogEntry
      Exercise "*" --> "1" LogEntry
      class User{
          username
          password
      }
      class LogEntry{
          logtitle
          logdate
      }
      class Exercise{
          name
          weigth
          reps
      }
```
