class DateTimeUtils():

    months = {
        'january': 1,
        'febuary': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october': 10,
        'november': 11,
        'december': 12,
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sept': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }

    allowed_year_prefixes = ['in', 'on', 'year', 'late', 'early']

    @staticmethod
    def isMonth(word: str):
        word = word.lower()
        if word in DateTimeUtils.months:
            return DateTimeUtils.months[word]
        else:
            return None

    @staticmethod
    def isYear(word: str, prev_word):
        if (prev_word == True
                or prev_word in DateTimeUtils.allowed_year_prefixes
                or prev_word.lower() in list(DateTimeUtils.months.keys())):
            if word.isnumeric() and int(word) < 2018 and int(word) > 1100:
                return int(word)
            else:
                return None
        else:
            return None

    @staticmethod
    def isDate(word):
        if word.endswith('th') or word.endswith('st') or word.endswith(
                'nd') or word.endswith('rd'):
            word = word[:-2]
        if word.isnumeric() and int(word) < 32 and int(word) > 0:
            return int(word)
        else:
            return None
