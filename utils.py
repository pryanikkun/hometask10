import json
from classes.candidates_getter import CandidatesGetter


def read_json():
    file = open('candidates.json', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data


def make_objects():
    data = read_json()
    list_candidates = []
    for candidate in data:
        list_candidates.append(CandidatesGetter(candidate))
    return list_candidates
