#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        return sorted(a_dictionary, reverse=True)[0]
    else:
        return None
