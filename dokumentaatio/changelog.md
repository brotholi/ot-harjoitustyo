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
