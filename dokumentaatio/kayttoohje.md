# Käyttöohje

Lataa viimeisimmän [releasen](https://github.com/brotholi/ot-harjoitustyo/releases) lähdekoodi Source code -kohdasta Assets-osion alta

## Ohjelman käynnistäminen

Asenna ennen ohjelman käynnistystä riippuvuudet seuraavalla komennolla:

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
