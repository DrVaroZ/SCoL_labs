import re
import constants


def remove_russian_chars(text):
    for i in range(0, len(text)):
        if re.search(r'[а-яА-Я]', text[i]):
            text = text.replace(text[i], ' ')

    return text


def calculate_sentences_num(text):
    # text = remove_russian_chars(text).lower()
    # sentences = re.split(constants.ALL_SENTENCES_PATTERN, text.replace('\n', ''))
    # print(sentences)
    # sentences = sentences[:-1]
    # print(sentences)
    text = remove_russian_chars(text).lower()
    sentences_amount = len(re.findall(constants.ALL_SENTENCES_PATTERN, text))
    #sentences_amount -= len(re.findall(constants.INITIALS, text)) * 2

    for abbreviation in constants.ONE_WORD_ABBREVIATIONS:
        sentences_amount -= text.count(abbreviation)  # + " [A-Z]{1,}"

    for abbreviation in constants.TWO_WORDS_ABBREVIATIONS:
        sentences_amount -= text.count(abbreviation) * 2

    # return len(sentences)
    return sentences_amount


def declarative_sentences_num(text):
    # text = remove_russian_chars(text).lower()
    # sentences = re.split(constants.DECLARATIVE_SENTENCES_PATTERN, text.replace('\n', ''))
    # sentences = sentences[:-1]
    # print(sentences)

    text = remove_russian_chars(text).lower()
    sentences_amount = len(re.findall(constants.DECLARATIVE_SENTENCES_PATTERN, text))
    #sentences_amount -= len(re.findall(constants.INITIALS, text)) * 2

    for abbreviation in constants.ONE_WORD_ABBREVIATIONS:
        sentences_amount -= text.count(abbreviation)  # + " [A-Z]{1,}"

    for abbreviation in constants.TWO_WORDS_ABBREVIATIONS:
        sentences_amount -= text.count(abbreviation) * 2

    # return len(sentences)
    return sentences_amount


def non_declarative_sentences_num(text):
    #  text = remove_russian_chars(text).lower()
    return calculate_sentences_num(text) - declarative_sentences_num(text)


def average_length_of_sentence_chars(text):
    text = remove_russian_chars(text).lower()
    nums = re.findall(constants.NUMBERS_PATTERN, text.replace('\n', ''))
    words = [word for word in re.findall(constants.WORDS_PATTERN, text.replace('\n', '')) if word not in nums]
    # print(words)
    if calculate_sentences_num(text):
        return round(sum(len(word) for word in words) / calculate_sentences_num(text), 2)
    else:
        return 0


def average_length_of_words_chars(text):
    text = remove_russian_chars(text).lower()
    nums = re.findall(constants.NUMBERS_PATTERN, text.replace('\n', ''))
    words = [word for word in re.findall(constants.WORDS_PATTERN, text.replace('\n', '')) if word not in nums]
    # print(words)
    if len(words):
        return round(sum(len(word) for word in words) / len(words), 2)
    else:
        return 0


def top_k_repeated_ngrams(text: str, k=10, n=4):
    text = remove_russian_chars(text).lower()
    words = re.findall(constants.WORDS_PATTERN, text)
    seq = [words[i:] for i in range(n)]
    ngrams = list(zip(*seq))
    dict_temp = {}

    for ngram in ngrams:
        if ngram not in dict_temp:
            dict_temp[ngram] = 1
        else:
            dict_temp[ngram] += 1

    return sorted(dict_temp.items(), key=lambda x: x[1], reverse=True)[0:k] if len(ngrams) != 0 else 0
