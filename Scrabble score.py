def scrabble_score(st):
    score = int(0)
    for i in st:
        if str(i.upper()) in {'A','E','I','O','U','L','N','R','S','T'}:
            score += 1
        elif str(i.upper()) in {'D','G'}:
            score += 2
        elif str(i.upper()) in {'B','C','M','P'}:
            score += 3
        elif str(i.upper()) in {'F','H','V','W','Y'}:
            score += 4
        elif str(i.upper()) == 'K':
            score += 5
        elif str(i.upper()) in {'J','X'}:
            score += 8
        elif str(i.upper()) in {'Q','Z'}:
            score += 10
    return score
    
#@test.describe('"Basic tests')
#def example_tests():
    #test.assert_equals(scrabble_score(""), 0, "returns 0 for ''")
    #test.assert_equals(scrabble_score('a'), 1, 'returns 1 for a')
    #test.assert_equals(scrabble_score("street"), 6, 'returns 6 for street')
    #test.assert_equals(scrabble_score("STREET"), 6, 'returns 6 for STREET')
    #test.assert_equals(scrabble_score(' a'), 1, 'returns score of " a" (with space)')
    #test.assert_equals(scrabble_score("st re et"), 6, 'returns 6 for street with whitespaces')
