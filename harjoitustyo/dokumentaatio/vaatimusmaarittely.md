# Vaatimusmäärittely
## Sovelluksen tarkoitus

Lihasloki-sovelluksella pidetään kirjaa kuntosalitreeneistä. Sovellukseen kirjataan yksittäisiä tehtyjä treenejä. Sovellusta voivat käyttää useat eri käyttäjät luomalla käyttäjätunnuksen. Jokaisen käyttäjätunnuksen taakse tallennetaan käyttäjän treenihistoria.

## Käyttäjäroolit

Sovelluksessa on tavallisia käyttäjiä ja pääkäyttäjä. Tavallinen käyttäjä voi luoda uuden käyttäjätilin, jolle täytyy lisätä käyttäjätunnus ja salasana. Pääkäyttäjällä on enemmän oikeuksia kuin tavallisella käyttäjällä. Pääkäyttäjä voi muun muassa nähdä, kuinka monta käyttäjää sovelluksessa on.

## Käyttöliittymä

Lihasloki sisältää ainakin 4 eri näkymää.

### Alkunäkymä
- Kirjautumisvaiheessa käyttäjä syöttää  käyttäjätunnuksen. Kirjautumisnäytöltä pääsee luomaan uuden käyttäjätunnuksen

### Uuden käyttäjätunnuksen luonti
- Uuden käyttäjätunnuksen luomisessa kerrotaan käyttäjätunnus

### Kaikki kirjaukset
- Kirjausnäkymässä käyttäjä näkee aikaisemmin kirjaamansa treenit
- Kirjausnäkymästä pääsee yksittäisen treenin kirjaamiseen painamalla uusi

### Treenin kirjaus
- Treeninkirjausnäkymässä käyttäjä voi syöttää uusia liikkeitä treeniin
- Treeninkirjausnäkymästä käyttäjä pääsee takaisin yleistreeniin painamalla lopeta/tallenna


## Toiminnallisuus perusversiossa
- Käyttäjä voi luoda sovellukseen tunnuksen
- Käyttäjätunnuksen on oltava vähintään 6 merkkiä pitkä ja uniikki
- Käyttäjä voi kirjautua sovellukseen käyttäjätunnuksella ja salasanalla
- Kirjautuminen onnistuu, jos käyttäjätunnus ja salasana täsmäävät
- Sovellus ilmoittaa, jos käyttäjätunnus tai salasana on väärin

- Käyttäjä voi kirjata uuden treenin
- Käyttäjä näkee aiemmin kirjatut treenit
	- Kirjatut treenit näkyvät vain käyttäjälle itselleen
- Käyttäjä voi kirjata jokaiseen treeniin useita eri treeniliikkeitä
- Käyttäjä voi lisätä jokaisen tehdyn liikkeen nimen ja kyseisen liikkeen kierrosten (settien) lukumäärän
- Jokaisen liikeen yksittäisen setin kohdalle käyttäjä voi kirjata toistojen määrän ja lisäpainon kilogrammoina. 
- Käyttäjä voi kirjautua ulos järjestelmästä



## Lisätoiminnallisuus - jatkokehittelyideoita
- Omien ennätysten tarkastelu: Sovellus kertoo käyttäjälle henkilökohtaisen ennätyksen jokaisessa liikkeessä treenihistorian perusteella. Ennätys eli personal best lasketaan sekä kilojen että toistojen avulla. 
- Sovellus ilmoittaa jokaisen kirjatun treenin kohdalla personal best:ien määrän. 
- Sovellukseen voi tallentaa treeniohjelmapohjia, jotka sisältävät käyttäjän valmiiksi määrittelemiä liikkeitä. Treeniohjelmapohjien avulla voi suoraan kirjata tehdyn treenin. 
- Treeniohjelman kirjaamisen voi aloittaa myös ilman pohjaa.
- Mahdollisesti käyttäjä kirjata myös lämmittelykierrokset erillisinä jokaisen liikeen kohdalle. 
- Sovellus kertoo, kuinka monta treeniä käyttäjä on kirjannut viikossa.

**Omien käyttäjätietojen muutokset:**

- Käyttäjä voi asettaa tavoitteeksi tietyn määrän treenejä viikossa ja sovellus ilmoittaa, jos tavoitteeseen on päästy. Ilmoitus näkyy käyttäjälle treenin kirjaamisen päättyessä, samassa kohtaa jossa ilmoitetaan henkilökohtaisista ennätyksistä.
- Treenien poistaminen historiasta
- Käyttäjätunnuksen poistaminen