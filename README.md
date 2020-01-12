# recipedb

Idea for recipe database + very sexy LaTeX formatting 


## Storing recipes
The idea is that recipes are stored in database objects, most likely MongoDB:
https://docs.mongodb.com/manual/
We zijn niet de enige sukkels die dit proberen, zie: \n
https://tex.stackexchange.com/questions/222604/ways-to-parse-json-in-latex


## Features
- DB
  - object recipe
    - array met ingredienten
    - stappenplan
    - naam
    - tijd
    - scaleability
      - warning voor expentiele baktijd
- Print in fancy format
  - .tex
  - autoformatter
- Shell acces
