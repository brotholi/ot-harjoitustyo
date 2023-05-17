# Lihasloki-sovellus

Lihasloki-sovelluksella pidetään kirjaa kuntosalitreeneistä. Sovellukseen kirjataan yksittäisiä tehtyjä treenejä. Sovellusta voivat käyttää useat eri käyttäjät luomalla käyttäjätunnuksen. Jokaiselle käyttäjätunnukselle tallennetaan käyttäjän oma treenihistoria.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Release](https://github.com/brotholi/ot-harjoitustyo/releases/tag/loppupalautus)

## Asennus


1. Asenna riippuvuudet komennolla 
```bash
poetry install
```
2. Suorita alustukset komennolla 
```bash
poetry run invoke build
```
3. Käynnistä sovellus komennolla 
```bash
poetry run invoke start
```

## Käyttö
- Tarvittavat alustukset tehdään komennolla 
```bash
poetry run invoke build
```
- Sovellus käynnistetään komennolla 
```bash
poetry run invoke start
```
- Testejä voi ajaa komennolla 
```bash
poetry run invoke test
```
- Testikattavuusraportin voi muodostaa komennolla 
```bash
poetry run invoke coverage-report
```
- Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla
```bash
poetry run invoke lint
```
