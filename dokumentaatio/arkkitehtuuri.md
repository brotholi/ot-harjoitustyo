```mermaid
 classDiagram
      User "1" <-- "*" Logentry
      Exercise "*" --> "1" Logentry
      class User{
          username
          password
      }
      class Logentry{
          logtitle
          logdate
      }
      class Exercise{
          name
          weigth
          reps
      }
```
