# Vaatimusmäärittely
## Sovelluksen tarkoitus

*Lihasloki*-sovelluksella pidetään kirjaa kuntosalitreeneistä. Sovellukseen kirjataan yksittäisiä tehtyjä treenejä. Sovellusta voivat käyttää useat eri käyttäjät luomalla käyttäjätunnuksen. Jokaiselle käyttäjätunnukselle tallennetaan käyttäjän oma treenihistoria.

## Käyttäjäroolit

Sovelluksessa on tavallisia käyttäjiä ja pääkäyttäjä. Tavallinen käyttäjä voi luoda uuden käyttäjätilin, jolle täytyy lisätä käyttäjätunnus ja salasana. Pääkäyttäjällä on enemmän oikeuksia kuin tavallisella käyttäjällä. Pääkäyttäjä voi muun muassa nähdä, kuinka monta käyttäjää sovelluksella on kokonaisuudessaan.

## Käyttöliittymä
  
  
![](./kuvat/kayttoliittyma-luonnoksia.jpg)  
  

**Alkunäkymä**
- Kirjautumisvaiheessa käyttäjä syöttää käyttäjätunnuksen ja salasanan
- Kirjautumisnäytöltä pääsee luomaan uuden käyttäjätunnuksen

**Uuden käyttäjätunnuksen luonti**
- Kun käyttäjä luo uuden tunnuksen, syötetään käyttäjätunnus ja salasana 
- Uusi tunnus luodaan painamalla *luo tunnus*

**Kaikki kirjaukset**
- Kirjausnäkymässä käyttäjä näkee aikaisemmin kirjaamansa treenit
- Kirjausnäkymästä pääsee yksittäisen treenin kirjaamiseen painamalla *uusi*
- Kirjausnäkymästä käyttäjä pääsee kirjautumaan ulos

**Treenin kirjaus**
- Treeninkirjausnäkymässä käyttäjä voi syöttää uusia liikkeitä treeniin
- Treeninkirjausnäkymästä käyttäjä pääsee takaisin yleisnäkymään painamalla *tallenna*
- Treenin nimeä ja päivämäärää voi muuttaa


## Toiminnallisuus perusversiossa
- Käyttäjä voi luoda sovellukseen tunnuksen
  - Käyttäjätunnuksen on oltava vähintään 5 merkkiä pitkä ja uniikki
- Käyttäjä voi kirjautua sovellukseen
- Käyttäjälle näkyvät vain käyttäjän itse kirjaamat treenit
- Käyttäjä voi kirjata yksittäisen treenin, jolle voi määritellä nimen
- Yksittäiseen treeniin voi kirjata päivämäärän
- Jokaiseen treeniin voi kirjata useita liikkeitä
- Käyttäjä voi lisätä jokaiselle treenin liikkeelle nimen ja sarjojen (settien) määrän
- Jokaiselle setille voi kertoa toistojen määrä ja lisäpainon kilogrammoina
- Käyttäjä voi kirjautua ulos järjestelmästä

## Lisätoiminnallisuus - jatkokehittelyideoita
- Sovellus tilastoi käyttäjän ennätyksiä yhdessä liikkeessä. Ennätys eli personal best lasketaan sekä kilojen että toistojen avulla.
- Sovellus ilmoittaa jokaisen kirjatun treenin kohdalla personal best:ien määrän. 
- Sovellukseen voi tallentaa treeniohjelmapohjia, jotka sisältävät käyttäjän valmiiksi määrittelemiä liikkeitä. Treeniohjelmapohjien avulla voi suoraan kirjata tehdyn treenin. 
- Treeniohjelmapohjan luonti tapahtuu mahdollisesti suoraan kirjausnäkymältä
- Yksittäisen treenin kirjaamisen voi aloittaa myös ilman pohjaa.
- Käyttäjä voi mahdollisesti kirjata myös lämmittelykierrokset erillisinä jokaisen liikeen kohdalle.
- Lämmittelyliikkeitä ei huomioida ennätysten tilastoinnissa

**Omien käyttäjätietojen katselu ja muutokset:**
- Oma näkymänsä, johon voi siirtyä kirjausnäkymästä
- Omien ennätysten tarkastelu: Sovellus kertoo käyttäjälle henkilökohtaisen ennätyksen jokaisessa liikkeessä treenihistorian perusteella.  
- Sovellus kertoo, kuinka monta treeniä käyttäjä on kirjannut viikossa.
- Käyttäjä voi asettaa tavoitteeksi tietyn määrän treenejä viikossa ja sovellus ilmoittaa aina, milloin tavoitteeseen on päästy. Ilmoittaminen tapahtuu treenin kirjaamisen päättyessä. Samassa kohtaa ilmoitetaan henkilökohtaisista ennätyksistä.
- Treenien poistaminen historiasta
- Käyttäjätunnuksen poistaminen
