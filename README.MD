# README

Python password generator based on https://xkcd.com/936/.

Allows for generating with capitals, digits and special characters to satisfy common password requirements.

usage: passgen.py [-h] [-C] [-s] [-i] [--max_length=] [--min_length=] [n]

`n               number of words to generate

-h, --help      show this help message and exit

-C              allow capitalized words

-s              append special character

-i              append digit

--max_length=   maximum length of generated words

--min_length=   minimum length of generated words`