from date_extractor.date_utils import DateTimeUtils
import re


class DateExtractor():

    def extract_dates(self, text):

        # split the text into words
        words = re.findall(r"[\w']+", text)

        # tag the words as potential date/month/year
        potential_dates = self._tag_words(words)

        # extract dates_to_return
        dates_to_return = []
        processed_list = []
        current_year = None
        for i, curr in enumerate(potential_dates):
            if curr in processed_list:
                continue

            n1 = self._get_next_valid_tag(i, words, potential_dates)
            n2 = self._get_next_valid_tag(i + 1, words, potential_dates)

            # (d, m, y)
            if curr['type'] == 'd' and n1 is not None and n1['type'] == 'm' and n2 is not None and n2['type'] == 'y':
                dates_to_return.append({
                    'd': curr['val'],
                    'm': n1['val'],
                    'y': n2['val']
                })
                processed_list.append(curr)
                processed_list.append(n1)
                processed_list.append(n2)
                current_year = n2['val']

            # (m, d, y)
            elif curr['type'] == 'm' and n1 is not None and n1['type'] == 'd' and n2 is not None and n2['type'] == 'y':
                dates_to_return.append({
                    'd': n1['val'],
                    'm': curr['val'],
                    'y': n2['val']
                })
                processed_list.append(curr)
                processed_list.append(n1)
                processed_list.append(n2)
                current_year = n2['val']

            # (m, y)
            elif curr['type'] == 'm' and n1 is not None and n1['type'] == 'y':
                dates_to_return.append({
                    'd': 0,
                    'm': curr['val'],
                    'y': n1['val']
                })
                processed_list.append(curr)
                processed_list.append(n1)
                current_year = n1['val']

            # (m, d)
            elif curr['type'] == 'm' and n1 is not None and n1['type'] == 'd':
                if current_year is not None:
                    dates_to_return.append({
                        'd': n1['val'],
                        'm': curr['val'],
                        'y': current_year
                    })
                else:
                    dates_to_return.append({
                        'd': n1['val'],
                        'm': curr['val'],
                        'y': 0
                    })
                processed_list.append(curr)
                processed_list.append(n1)

            # (d, m)
            elif curr['type'] == 'd' and n1 is not None and n1['type'] == 'm':
                if current_year is not None:
                    dates_to_return.append({
                        'd': curr['val'],
                        'm': n1['val'],
                        'y': current_year
                    })
                else:
                    dates_to_return.append({
                        'd': curr['val'],
                        'm': n1['val'],
                        'y': 0
                    })
                processed_list.append(curr)
                processed_list.append(n1)

            # curr = y
            elif curr['type'] == 'y':
                dates_to_return.append({'d': 0, 'm': 0, 'y': curr['val']})
                processed_list.append(curr)
                current_year = curr['val']

        return dates_to_return

    def _tag_words(self, words):
    
        potential_dates = [];
    
        for i, word in enumerate(words):

            if (i > 0):
                prev_word = words[i - 1]
            else:
                prev_word = None

            dayNo = DateTimeUtils.getDate(word)
            monthNo = DateTimeUtils.getMonth(word)
            yearNo = DateTimeUtils.getYear(word, prev_word)

            if monthNo is not None:
                potential_dates.append({
                    'index': i,
                    'word': word,
                    'type': 'm',
                    'val': monthNo
                })
                continue

            if yearNo is not None:
                potential_dates.append({
                    'index': i,
                    'word': word,
                    'type': 'y',
                    'val': yearNo
                })
                continue

            if dayNo is not None:
                potential_dates.append({
                    'index': i,
                    'word': word,
                    'type': 'd',
                    'val': dayNo
                })
                continue
        return potential_dates

    def _get_next_valid_tag(self, index, words, potential_dates):
        if index < len(potential_dates) - 1:
            tag = potential_dates[index]
            word_index = tag['index']
            next_word = words[word_index + 1]
            next_tag = potential_dates[index + 1]
            if next_tag['index'] == word_index + 1:
                return next_tag
            else:
                return None
        else:
            return None

    def get_printable_date(self, obj):
        printable_date = ''
        if obj['d'] != 0:
            printable_date = str(obj['d'])
        if obj['m'] != 0:
            key = next(key for key, value in DateTimeUtils.months.items()
                       if value == obj['m'])
            printable_date = printable_date + ' ' + str(key)
        if obj['y'] != 0:
            if obj['m'] != 0:
                printable_date = printable_date + ', '
            printable_date = printable_date + str(obj['y'])
        return printable_date
