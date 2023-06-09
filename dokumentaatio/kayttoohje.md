# Käyttöohje

Lataa viimeisimmän [releasen](https://github.com/brotholi/ot-harjoitustyo/releases) lähdekoodi Source code -kohdasta Assets-osion alta

## Ohjelman käynnistäminen

Asenna riippuvuudet ennen ohjelman käynnistystä seuraavalla komennolla:

```bash
poetry install
```

Tämän jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Lopuksi käynnistä ohjelma komennolla:

```
poetry run invoke start
```

## Kirjautuminen

Sovellus avautuu kirjautumisnäkymään:

![](./kuvat/kirjautuminen.png)

Voit kirjautua sisään kirjoittamalla olemassaolevan käyttäjätunnuksen ja salasanan kenttiin. Tämän jälkeen paina *kirjaudu*.

Kirjautumisnäkymästä pääsee luomaan uuden käyttäjän painamalla *Luo uusi käyttäjä*. Tämä avaa uuden näkymän, josta pääsee takaisin painamalla *takaisin*.

![](./kuvat/luo_kayttaja.png)

Uuden käyttäjän voi luoda syöttämällä tiedot kenttiin. Käyttäjätunnuksen on oltava vähintään 5 merkkiä pitkä.

## Aloitusnäkymä

Kirjautuminen avaa käyttäjälle oman näkymän: 

![](./kuvat/logbook_view.png)

*Kirjaudu ulos*-nappula kirjaa käyttäjän ulos.

Jos käyttäjällä on yli viisi aikaisempaa kirjausta, viiden viimeisimmän treenikirjauksen päivämäärä ja nimi näytetään *Aikaisemmat treenit* -otsikon alla.
Muutoin näytetään kaikki aiemmat kirjaukset.

Aikaisempien treenien tarkempia tietoja voi saada kirjoittamalla alhaalla olevaan kenttään treenin nimen. 

Tällöin tuodaan näkyviin lista tällä nimellä olevista treeneistä ja niiden liikkeistä.

[kuva]

## Uuden treenin kirjaus

Uuden kirjauksen voi luoda painamalla *Luo uusi treeni*. Tämä avaa uuden kirjausnäkymän:

![](./kuvat/logentry_view.png)

Painamalla *Peruuta*, käyttäjä pääsee takaisin aloitusnäkymään.

Treenin nimi syötetään *Otsikko*-kenttään. Nimi ei saa olla tyhjä.

Oletusarvoisesti päivämäärä on kuluva päivä. Päivää pääsee muuttamaan painamalla *Muuta päivämäärää*. Tällöin avautuu syöttökenttä, johon päivämäärän voi syöttää. Päivämäärä on syötettävä muodossa pp.kk.vvvv. Jos kenttään ei syötä mitään, on päivämäärä edelleen kuluva päivä.

![](./kuvat/logentry_view_date.png)

Jos päivämäärän syöttää väärässä muodossa, ei pääse siirtymään liikkeidenkirjausnäkymään, vaan näytetään virheviesti:

![](./kuvat/logentry_view_error.png)

Painamalla *Ok* käyttäjä pääsee kirjaamaan yksittäiset liikkeet treenille. Tämä avaa uuden näkymän.

## Liikkeiden kirjaus treenille

Liikkeet kirjataan liikkeiden kirjausnäkymässä. 

![](./kuvat/exercise_view.png)

Liikkeelle on syötettävä nimi ja kolmelle sarjalle sekä lisäpaino että toistot.

![](./kuvat/exercise_view_error.png)

Liike tallennetaan painamalla *Lisää*. Tällöin se tulee näkyviin liikkeen kirjausnäkymän yläpuolelle.

![](./kuvat/exercise_view_list.png)

Treenin voi tallentaa kirjatuilla liikkeillä painamalla *Tallenna treeni*, joka vie käyttäjän takaisin aloitusnäkymään. 
**Huom!** muista tallentaa myös viimeisenä kirjauksessa oleva liike painamalla *Lisää* ennen kuin tallennat treenin





