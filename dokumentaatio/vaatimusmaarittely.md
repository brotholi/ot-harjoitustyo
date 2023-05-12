# Vaatimusmäärittely
## Sovelluksen tarkoitus

*Lihasloki*-sovelluksella pidetään kirjaa kuntosalitreeneistä. Sovellukseen kirjataan yksittäisiä tehtyjä treenejä. Sovellusta voivat käyttää useat eri käyttäjät luomalla käyttäjätunnuksen. Jokaiselle käyttäjätunnukselle tallennetaan käyttäjän oma treenihistoria.

## Käyttäjäroolit

Sovelluksessa on tavallisia käyttäjiä ja pääkäyttäjä. Tavallinen käyttäjä voi luoda uuden käyttäjätilin, jolle täytyy lisätä käyttäjätunnus ja salasana. Pääkäyttäjällä on enemmän oikeuksia kuin tavallisella käyttäjällä. Pääkäyttäjä voi muun muassa nähdä, kuinka monta käyttäjää sovelluksella on kokonaisuudessaan.

## Käyttöliittymä
  
 
![](./kuvat/kayttoliittyma-luonnoksia.jpg)  
*Käyttöliittymän luonnos*

**Alkunäkymä**
- Kirjautumisvaiheessa käyttäjä syöttää käyttäjätunnuksen ja salasanan
- Kirjautumisnäytöltä pääsee luomaan uuden käyttäjätunnuksen

**Uuden käyttäjätunnuksen luonti**
- Kun käyttäjä luo uuden tunnuksen, syötetään käyttäjätunnus ja salasana 
- Uusi tunnus luodaan painamalla *luo käyttäjä*

**Kaikki kirjaukset**
- Kirjausnäkymässä käyttäjä näkee aikaisemmin kirjaamansa treenit
- Kirjausnäkymästä pääsee yksittäisen treenin kirjaamiseen painamalla *uusi*
- Kirjausnäkymästä käyttäjä pääsee kirjautumaan ulos

**Treenin kirjaus**
- Treeninkirjausnäkymässä käyttäjä voi syöttää uusia liikkeitä treeniin
- Treeninkirjausnäkymästä käyttäjä pääsee takaisin yleisnäkymään painamalla *tallenna*
- Treenin nimeä ja päivämäärää voi muuttaa


## Toiminnallisuus perusversiossa
- Käyttäjä voi luoda sovellukseen tunnuksen **(tehty)**
  - Käyttäjätunnuksen on oltava vähintään 5 merkkiä pitkä ja uniikki **(tehty)**
- Käyttäjä voi kirjautua sovellukseen **(tehty)**
- Käyttäjälle näkyvät vain käyttäjän itse kirjaamat treenit **(tehty)**
- Käyttäjä voi kirjata yksittäisen treenin, jolle voi määritellä nimen **(tehty)**
- Yksittäiseen treeniin voi kirjata päivämäärän **(tehty)**
- Jokaiseen treeniin voi kirjata useita liikkeitä **(tehty)**
- Käyttäjä voi lisätä jokaiselle treenin liikkeelle nimen ja sarjojen (settien) määrän (**tehty**)
- Jokaiselle setille voi kertoa toistojen määrä ja lisäpainon kilogrammoina (**tehty**)
- Käyttäjä voi kirjautua ulos järjestelmästä **(tehty)**

## Lisätoiminnallisuus - jatkokehittelyideoita
- Sovellus tilastoi käyttäjän ennätyksiä yhdessä liikkeessä. Ennätys eli personal best lasketaan sekä kilojen että toistojen avulla.
- Sovellus ilmoittaa jokaisen kirjatun treenin kohdalla personal best:ien määrän. 
- Omien ennätysten tarkastelu: Sovellus kertoo käyttäjälle henkilökohtaisen ennätyksen jokaisessa liikkeessä treenihistorian perusteella.  
- Sovellus kertoo, kuinka monta treeniä käyttäjä on kirjannut viikossa.
- Käyttäjä voi asettaa tavoitteeksi tietyn määrän treenejä viikossa ja sovellus ilmoittaa aina, milloin tavoitteeseen on päästy. Ilmoittaminen tapahtuu treenin kirjaamisen päättyessä. Samassa kohtaa ilmoitetaan henkilökohtaisista ennätyksistä.
- Treenien poistaminen historiasta
- Käyttäjätunnuksen poistaminen
