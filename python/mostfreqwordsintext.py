# https://www.codewars.com/kata/51e056fe544cf36c410000fb/

import re


def top_3_words(text: str) -> list:
    words_dict: dict = {}
    word: str = ''
    anyletter = re.compile(r"[a-zA-Z']")
    wordchecker = re.compile(r"[a-zA-Z]+[']?[a-zA-Z]?")
    nonwordchars = [' ', ',', '#', '!', '&', '-', '_',
                    ';', '.', '=', '$', '@', '^', '?', '*', ':', '/']
    for letter in text:
        if letter in nonwordchars:
            if not word or not wordchecker.findall(word):
                word = ''
                continue
            print(word.lower())
            if word.lower() in words_dict.keys():
                words_dict[word.lower()] += 1
            else:
                words_dict[word.lower()] = 1
            word = ''
        else:
            if anyletter.findall(letter):
                word += letter
    if word and wordchecker.findall(word):
        if word.lower() in words_dict.keys():
            words_dict[word.lower()] += 1
        else:
            words_dict[word.lower()] = 1
    top_score = sorted(words_dict.values(), reverse=True)[0:3]
    top_words: list = []
    for score in top_score:
        for key, value in words_dict.items():
            if score == value and key not in top_words:
                top_words.append(key)
                break
            if len(top_words) > 2:
                return top_words
    return top_words
