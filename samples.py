from date_extractor.date_extractor import DateExtractor
import json


def test_date_extract():
    extractor = DateExtractor()

    infile = open('data/sample_sentences.txt', 'r')
    dates = []
    
    for sentence in infile:
        d = extractor.extract_dates(sentence)
        dates = dates + d
        print('done:', sentence, json.dumps(d))

    with open('data/dates.json', 'a+') as outfile:
        json.dump(dates, outfile)

test_date_extract()
