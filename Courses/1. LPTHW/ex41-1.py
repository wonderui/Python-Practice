import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASE = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	""
}