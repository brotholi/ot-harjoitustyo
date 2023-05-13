# Arkkitehtuurikuvaus


## Rakenne

Lihasloki-sovelluksen koodin pakkausrakenne on seuraava:
```mermaid
 flowchart TB
     ui --- services
     services --- repositories
     services --- entities
     repositories --- entities
```

Pakkaus *ui*-vastaa käyttöliittymästä, *services* sovelluslogiikasta ja *repositories* tietojen tallennuksesta tiedostoon ja tietokantaan. *Entities* sisältää sovelluksen logiikan kannalta oleellisia luokkia.

## Käyttöliittymä

Käyttöliittymällä on viisi erilaista näkymää:
- Kirjautuminen
- Uuden käyttäjän luonti
- Yhden käyttäjän näkymä / lista treeneistä
- Treeninkirjausnäkymä
- Liikkeidenkirjausnäkymä

Kaikki käyttöliittymän näkymät ovat erillisiä luokkia, joita hallitsee UI-luokka. UI-luokka vastaa siitä, mikä näkymä näytetään. Näkymät kutsuvat aina services-luokkia.


## Sovelluslogiikka

Lihasloki-sovelluksen kolme luokkaa ovat User, LogEntry ja Exercise. User-luokka kuvaa yhtä käyttäjää, LogEntry yhtä yhden käyttäjän treenikirjausta ja Exercise yhtä liikettä, joita voi olla yhdessä treenissä useita.

```mermaid
 classDiagram
      User "1" <-- "*" LogEntry
      Exercise "*" --> "1" LogEntry
      class User{
          username
          password
      }
      class LogEntry{
          user
          logtitle
          logdate
          logentry_id
      }
      class Exercise{
          name
          weigth
          reps
      }
```

Luokat UserService ja LogbookService vastaavat sovelluksen toiminnallisuudesta. UserService tarjoaa käyttöliittymälle erilaisia käyttäjiin liittyviä metodeita:

- `login(username, password)`
- `get_current_user()`
- `create_new_user(username, password)`

Logbookservice tarjoaa kaikki treenin kirjaukseen liittyvät toiminnot. Niihin kuuluvat esimerkiksi
- `create_new_entry(username, logtitle, time)`
- `find_user_logs(username)`
- `find_current_log(username)`
- `find_log_by_logtitle(logtitle)`
- `create_new_exercise(exercise_name, weigth, reps)`
- `find_logentry_exercises(logentry_id)`
- `check_date_format(date)`

Services-luokat pääsevät repositories-kansiossa sijaitseviin luokkiin käsiksi. Repositories-luokat vastaavat tiedon tallennuksesta. Kun service-luokka luodaan, sille annetaan tarvittavat repositories-luokat konstruktorissa.

UserService- ja LogbookService -luokkien suhdetta muihin ohjelman osiin kuvaa pakkauskaavio:


### Tiedon tallennus
Repositories-luokat UserRepository, LogbookRepository ja ExerciseRepository vastaavat Lihaslokin tietojen tallennuksesta. UserRepository ja ExerciseRepository tallentavat tietoa SQLite-tietokantaan. LogbookRepository tallentaa tietoa csv-tiedostoon. Tiedon tallennus on suunniteltu repositories-mallin avulla, eli tiedon tallennus on eriytetty sovelluslogiikasta.

### Tiedostot

Käyttäjien ja liikkeiden sekä treenikirjausten tiedot talletetaan erillisiin tiedostoihin. Sovelluksen juuressa on konfiguraatiotiedosto(https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/.env), joka määrittelee eri tiedostojen nimet.

Sovelluksen käyttäjien tiedot tallennetaan SQLite-tietokannan tauluun `lihasloki_users`, joka alustetaan initialize_database.py-tiedostossa.

Treenit talletetaan csv-tiedostoon logentries.csv. Tiedostossa treenikirjausten yleiset tiedot on talletettu seuraavasti:

```
ruusa;jalkapäivä;13.05.2023;12d5f963-cfff-4141-b569-af5fdcbb3385
ruusa;Selkä;03.05.2023;bee7fea2-b5bc-4dd7-a622-b2a02cbc0798
```
Rivillä on ensin käyttäjätunnus, sitten treenikirjauksen nimi, päivämäärä ja kirjauksen yksilöivä id-tunnus.

Yksittäisten liikkeiden tiedot talletetaan SQLite-tietokannan tauluun `lihasloki_exercises`, joka on samassa tiedostossa database.sqlite kuin käyttäjätiedot. Yksi rivi taulussa on aina yksi sarja, joka sisältää liikkeen nimen, toistot ja lisäpainon. Tietokantaan tallettaessa liikkeellä on aina rivinumero (määritellään tauluun kirjattujen liikkeiden pohjalta), treenikirjauksen id (sama kuin csv-tiedostossa), nimi, lisäpaino ja toistot. Alla on testikäyttäjän ruusa-kirjaaman jalkapäivä-treenin liikkeitä:

```
```
0|12d5f963-cfff-4141-b569-af5fdcbb3385|kyykky|45|12
1|12d5f963-cfff-4141-b569-af5fdcbb3385|kyykky|50|8
2|12d5f963-cfff-4141-b569-af5fdcbb3385|kyykky|55|6
3|12d5f963-cfff-4141-b569-af5fdcbb3385|maastaveto|65|8
4|12d5f963-cfff-4141-b569-af5fdcbb3385|maastaveto|70|5
5|12d5f963-cfff-4141-b569-af5fdcbb3385|maastaveto|0|0

```
```

## Päätoiminnallisuudet

### Kirjautuminen

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
Painamalla kirjaudu-nappulaa tapahtumankäsittelijä kutsuu UserService-luokan metodia. Parametriksi annetaan käyttäjätunnus ja salasana. Tämän jälkeen sovellus tutkii, UserRepositoryn avulla, että käyttäjä on olemassa ja että salasana on oikein. Jos kaikki on ok, kirjautuminen onnistuu ja käyttöliittymä UI-luokka näyttää treeninkirjausnäkymän kirjautuneelle käyttäjälle.

### Uuden käyttäjän luominen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UserService
  participant UserRepository
  User->>UI: press "Luo käyttäjä" button
  UI->>UserService: create_new_user("Mollamaija", "1244")
  UserService->>UserService: check_if_user_exists()
  UserService->>UserRepository: find_by_username("Mollamaija")
  UserRepository-->>UserService: None
  UserService->>UserRepository: create_new_user(user)'
  UserRepository-->>UserService: user
  UserService-->>UI: user
  UI->>UI: show_login_view()
 ```
Ennen uuden käyttäjän luomisessa käyttöliittymältä tehdään tarkistus, että käyttäjätunnus on vähintään 5 merkkiä ja salana täsmää salasana uudelleen -kentän kanssa. Tämän jälkeen käyttöliittymältä kutsutaan Luo käyttäjä -painiketta painettaessa UserServiceä, joka etsii, onko käyttäjää jo olemassa. Tämä tehdään UserRepository-luokan avulla, jolle annetaan käyttäjän käyttöliitymällä kenttiin syöttämät arvot parametreina. Jos samannimistä käyttäjää ei löydy, lisätään käyttäjä sqlite-tietokantaan. Tämän jälkeen käyttöliittymä palaa kirjautumisnäkymään. 

 
 ### Uuden treenin lisääminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant LogbookService
  participant LogbookRepository
  User->>UI: press "Ok" button
  UI->>LogbookService: check_date_format(date)
  LogbookService-->>UI: date
  UI->>LogbookService: create_new_entry("Mollamaija", "jalkapäivä", "3.4.2023")
  LogbookService->>LogbookService: create_logentry_id()
  LogbookService->>LogbookRepository: create_new_entry(entry)
  LogbookRepository-->>LogbookService: entry
  LogbookService-->>UI: entry
  UI->>UI: show_exercise_view()
 ```
 
Uusi treeni luodaan painamalla Luo uusi treeni, jolloin tapahtumankäsittelijä avaa uuden näkymän. Painamalla ok-uusi treeni tallennettaan ja siirrytään liikkeiden kirjaus -näkymään. Ennen uuden treenin luomista käyttöliittymältä tehdään kuitenkin tarkistus, että päivämäärä on syötetty oikeassa muodossa (pp.kk.vvvv). UI kutsuu tapahtumankäsittelijän avulla LogbookService-luokkaa, joka tekee tarkistuksen. Jos tarkistus menee läpi,  LogbookServise-luokka luo uuden LogEntry-olion luomalla ensin sille uniikin id:n, jonka jälkeen se kutsuu LogbookRepositorya. LogbookRepository-luokka vie olion csv-tiedostoon. Tämän jälkeen käyttäjä pääsee siirtymään kirjaamaan liikkeet.

### Liikkeen kirjaus

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant LogbookService
  participant ExerciseRepository
  User->>UI: press "Lisää liike" button
  UI->>LogbookService: create_new_exercise("kyykky", "50", "8")
  LogbookService->>LogbookService: find_current_log()
  LogbookService->>ExerciseRepository: create_new_exercise(logentry.id, exercise)
  ExerciseRepository-->>LogbookService: exercise
  LogbookService-->>UI: exercise
  UI->>UI: _initialize_exercise_list()
 ```


Uusi liike luodaan painamalla 'Lisää liike'. Tapahtumankäsittelijän avulla LogbookService-luokkaa, joka hakee nykyisen logentry-kirjauksen oliona. Luokka luo uuden Exercise-olion ja kutsuu ExerciseRepositorya, jolle se antaa myös nykyisen kirjauksen id:n. LogbookRepository-luokka vie olion ja id:n tietokantaan. Tämän jälkeen liike näytetään käyttäjälle liikkeiden kirjausnäkymällä, nykyisen näkymän "alinäkymällä", joka näkyy kirjausikkunan yläpuolella. 
