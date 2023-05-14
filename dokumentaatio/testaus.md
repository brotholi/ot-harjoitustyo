# Testausdokumentti

Testaus on suoritettu automaattisilla yksikkötesteillä unittestilla sekä manuaalisesti järjestelmätasolla.


## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
UserService-luokkaa testataan antamalla sille riippuvuuksiksi repository-olio `FakeUserRepository`. 
Samalla tavoin LogbookService-luokkaa testataan antamalla sille riippuvuuksiksi oliot `FakeLogbookRepository` ja `FakeExerciseRepository`. 
Oliot talentavat tietoa muistiin eivätkä pysyväistallennukseen.

### Testauskattavuus
Sovelluksen testien haaraumakattaavuus on 91%, kun käyttöliittymää ei oteta mukaan.

![](./kuvat/test_coverage.png)

## Järjestelmätestaus

### Asennus ja konfigurointi

Asennusta on testattu lataamalla sovellus Linux-ympäristöön. Konfiguraatiotiedostoa on testattu laittamalla sinne eri tiedostonimet kuin alun perin
Ohjelman käynnistystä on testattu niin, että tiedostot ovat jo olemassa data-kansiossa ja niin, että ne luodaan alustuksen yhteydessä/ohjelmaa suoritettaessa.

### Toiminnallisuudet

Käyttöohjeen ja määrittelydokumentin toiminnallisuudet on käyty läpi. 
Kaikki toiminnallisuudet on myös testattu virheellisillä arvoilla, tyhjillä ja vääränmuotoisilla arvoilla.

## Sovellukseen jääneet laatuongelmat
Hakutoiminnossa voi hakea ainoastaan täsmällisillä hakusanoilla ja haun tulokset eivät välttämättä mahdu ikkunalle, jos niitä on liikaa.
Tällä hetkellä liikkeidenkirjausnäkymässä sarjojen done-nappulat eivät vielä tee mitään. Näihin mahdollisuus kehittää eteenpäin.
Sovellus heittää käyttäjän ulos (virheilmoituksen kera), kun SQlite-tietokantaa ei ole alustettu poetry run invoke build -komennolla.
