# Author name : Kote Seema M ('https://github.com/seema-kote/')
# Created Date : 12th Sep 2017

import json
import difflib

def load_data(file):
    # load data from data.json file into variable dict
    with open(file, 'r') as json_file:
        dict = json.load(json_file)
    return dict

def get_meaning(word,dict):
    word=word.lower()

    # check existence of word in dict
    if word in dict:
        return [word,dict[word][0]]

    # else suggest similar word for given word.
    else:
        similar_words = difflib.get_close_matches(word, dict, 5, 0.6)

        # check if similar word is found
        if len(similar_words) > 0:
            return [similar_words[0],dict[similar_words[0]][0]]

        # else return empty.
        else:
            return []
