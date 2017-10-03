from date_extractor.date_extractor import DateExtractor
import json


def test_date_extract():
    extractor = DateExtractor()
    test_sentences = []
    test_sentences.append('it was 25th may, 1990.')
    test_sentences.append('it was may 25th, 1990')
    test_sentences.append('it was 25th may')
    test_sentences.append('the year was 1990')
    test_sentences.append('in 1990, it happened')
    test_sentences.append('it was just may 25')
    test_sentences.append('1st june')
    test_sentences.append('2nd june')
    test_sentences.append(
        'The main headquarters of NATO is located on Boulevard L\u00e9opold III/Leopold III-laan, B-1110 Brussels, which is in Haren, part of the City of Brussels municipality. '
    )
    test_sentences.append('from 1990-2000, its all ok')
    test_sentences.append('i am planning to go to my hometown on july 2nd.')
    test_sentences.append(
        'born on 2 october 1869. on 12th dec that year, it rained')
    dates = []
    for sentence in test_sentences:
        d = extractor.extract_dates(sentence)
        dates = dates + d
        print('done: ' + sentence + json.dumps(d))

    with open('dates.json', 'a+') as outfile:
        json.dump(dates, outfile)


test_date_extract()
