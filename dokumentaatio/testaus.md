# Testausdokumentti

Testaus on suoritettu automaattisilla yksikkötesteillä unittestilla sekä manuaalisesti järjestelmätasolla.


## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
UserService-luokkaa testataan antamalla sille riippuvuuksiksi repository-olio `FakeUserRepository`. 
Samalla tavoin LogbookService-luokkaa testataan antamalla sille riippuvuuksiksi oliot `FakeLogbookRepository` ja `FakeExerciseRepository`. 
Oliot talentavat tietoa muistiin eivätkä pysyväistallennukseen.

### Testauskattavuus
Sovelluksen testien haaraumakattaavuus on [?], kun käyttöliittymää ei oteta mukaan.

[tähän testikattavuuskuva]

## Järjestelmätestaus

### Asennus ja konfigurointi

Asennusta on testattu lataamalla sovellus Linux-ympäristöön. (lisäksi windows?)
- konfiguraatiotestit (eri nimet)
- (tiedostot olemassa ja ei)

### Toiminnallisuudet

Käyttöohjeen ja määrittelydokumentin toiminnallisuudet on käyty läpi. 
Kaikki toiminnallisuudet on myös testattu virheellisillä arvoilla, tyhjillä ja vääränmuotoisilla arvoilla.

## Sovellukseen jääneet laatuongelmat

Sovellus heittää käyttäjän ulos (virheilmoituksen kera), kun SQlite-tietokantaa ei ole alustettu poetry run invoke build -komennolla.
Hakutoiminnossa voi hakea ainoastaan täsmällisillä hakusanoilla ja haun tulokset eivät välttämättä mahdu ikkunalle, jos niitä on liikaa
