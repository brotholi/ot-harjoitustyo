# Lihasloki-sovellus

Lihasloki-sovelluksella pidetään kirjaa kuntosalitreeneistä. Sovellukseen kirjataan yksittäisiä tehtyjä treenejä. Sovellusta voivat käyttää useat eri käyttäjät luomalla käyttäjätunnuksen. Jokaiselle käyttäjätunnukselle tallennetaan käyttäjän oma treenihistoria.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [release](./dokumentaatio/arkkitehtuuri.md)

## Käyttö
- Tarvittavat alustukset tehdään komennolla *poetry run invoke build*
- Sovellus käynnistetään komennolla *poetry run invoke start*
- Testejä voi ajaa komennolla *poetry run invoke test*
- Testikattavuusraportin voi muodostaa komennolla *poetry run invoke coverage-report*
- Komennolla *poetry run invoke lint* voi suorittaa tiedoston .pylintrc määrittelemät tarkistukset
