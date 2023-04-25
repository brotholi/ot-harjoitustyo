# Sovelluksen logiikka

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

## Sekvenssikaaviot

# Kirjautuminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UserService
  participant UserRepository
  User->>UI: press "Kirjaudu" button
  UI->>UserService: login("Mollamaija", "heppa2")
  UserService->>UserRepository: find_by_username("Mollamaija")
  UserRepository-->>UserService: user
  UserService-->>UI: user
  UI->>UI: show_logbook_view()
```

# Uuden käyttäjän luominen

```mermaid
  actor User
  participant UI
  participant UserService
  participant UserRepository
  User->>UI: press "Luo käyttäjä" button
  UI->>UserService: create_new_user("Mollamaija", "1244")
  UserService->>UserRepository: find_by_username("Mollamaija")
  UserRepository-->>UserService: user
  UserService-->>UI: user
  UI->>UI: show_login_view()
  

