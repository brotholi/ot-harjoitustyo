## Viikko 3
- Luotu pohja seuraaville kokonaisuuksille:
- ui
	- login_view
	- create_user_view
	- ui (käyttöliittymää hallitseva kokonaisuus)
- entities
	- user
- services
	- user_service
- repositories
	- user_repository
- alustavaa runkoa sqlite3 tietokantojen käsittelylle
- Kun Lihasloki sovellus käynnistyy, tulee create_user-näkymä esiin
- Käyttäjä voi luoda uuden käyttäjätunnuksen, user_service luo siitä User-luokan olion
- Käyttäjätietoja ei vielä tallenneta mihinkään, tulevaisuudessa ne lisätään SQLite-tietokantaan

## Viikko 4
- poetry run invoke start-komento avaa login-näkymän, josta pääsee siirtymään create_user-näkymälle painamalla "luo käyttäjä"
- create_user-näkymässä User-olioon liittyvät käyttäjätunnus ja salasana talletetaan tietokantaan
- jos käyttäjätunnus on jo olemassa, käyttäjätunnusta ei voi luoda ja sovellus ilmoittaa siitä
- käyttäjän luonti vie takaisin login-näkymään
- user_reposiotoria laajennettu, palauttaa tarvittaessa kaikki käyttäjät tai yhden käyttäjän käyttäjänimellä
- testattu, että user_repository luo käyttäjän ja vie sen tietokantaan sekä palauttaa kaikki käyttäjät


## Viikko 5
- korjattu tyhjän data-kansion aiheuttamia ongelmia
- käyttäjä voi kirjautua sisään. Kirjautuminen tarkistaa, että käyttäjätunnus ja salasana ovat oikein.
- Sisäänkirjautuminen näyttää logbook-näkymän
- Logbook-näkymästä voi siirtyä yksittäisen treenin kirjaamiseen painamalla "lisää uusi treeni"
	- luotu pohjaa logbook-repositorylle, joka tallentaa treenit tiedostoon (ei vielä toimi)
- käyttäjä voi kirjautua ulos painamalla "kirjaudu ulos"
- lisätty takaisin-nappula create-user -näkymään, joka vie takaisin kirjautumiseen
- testattu, että user_servicen login toimii
