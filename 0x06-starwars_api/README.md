# 0x06. Star Wars API

<kbd>Algorithm</kbd> &middot; <kbd>API</kbd> &middot; <kbd>JavaScript</kbd>

[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

## Tasks

### 0. Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
- Display one character name per line **in the same order as the “characters” list in the `/films/` endpoint**
- You must use the [Star wars API](https://swapi-api.alx-tools.com/)
- You must use the `request` module

```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
$
```