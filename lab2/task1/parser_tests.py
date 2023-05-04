import unittest
import parser


class TestCountSentences(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = parser.calculate_sentences_num('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s great text!!'
        expected = 2
        actual = parser.calculate_sentences_num(text)
        self.assertEqual(actual, expected,
                         'Abbreviations test: number of sentences not ' + str(expected))

    def test_sample_text(self):
        text = 'Oh!!! Thats good idea; Oh no... I forgot my keys in the car. '
        expected = 3
        actual = parser.calculate_sentences_num(text)
        self.assertEqual(actual, expected,
                         'Sample text test: number of sentences not ' + str(expected))


class TestCountNonDeclarativeSentences(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = parser.non_declarative_sentences_num('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s greate text!!'
        expected = 1
        actual = parser.non_declarative_sentences_num(text)
        self.assertEqual(actual, expected,
                         'Abbreviations test: number of non decl. sentences not' + str(expected))

    def test_sample_text(self):
        text = 'Oh!!! Thats good idea; Oh no... I forgot my keys in the car. '
        expected = 1
        actual = parser.non_declarative_sentences_num(text)
        self.assertEqual(actual, expected,
                         'Sample text test: number of non decl. sentences not ' + str(expected))


class TestGetAverageSentenceLength(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = parser.average_length_of_sentence_chars('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s greate text!!'
        expected = round((47 / 2), 2)
        actual = parser.average_length_of_sentence_chars(text)
        self.assertEqual(actual, expected,
                         'Average len with abbreviations test: result isn\'t ' + str(expected))

    def test_text_with_numbers(self):
        text = 'Oh!!! 4 Heloo aaaa. asd6laa, 777; word?'
        expected = round(22 / 3, 2)
        actual = parser.average_length_of_sentence_chars(text)
        self.assertEqual(actual, expected,
                         'Average len with numbers test: result isn\'t ' + str(expected))


class TestAvgWordLength(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = parser.average_length_of_words_chars('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - its greate text!!'
        expected = round(47 / 14, 2)
        actual = parser.average_length_of_words_chars(text)
        self.assertEqual(actual, expected,
                         'Average len with abbreviations test: result isn\'t ' + str(expected))

    def test_text_with_numbers(self):
        text = 'Oh!!! 4 Heloo aaaa. asd6laa, 777; word?'
        expected = round(22 / 5, 2)
        actual = parser.average_length_of_words_chars(text)
        self.assertEqual(actual, expected,
                         'Average len with numbers test: result isn\'t ' + str(expected))


class TestGetTopKRepeatedNgram(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = parser.top_k_repeated_ngrams('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_text_without_repeated_anagrams(self):
        text = 'Hello, My name is Vadim. And theres no repeated words.'
        expected = [(('hello', 'my', 'name'), 1), (('my', 'name', 'is'), 1), (('name', 'is', 'vadim'), 1)]
        actual = parser.top_k_repeated_ngrams(text, 3, 3)
        self.assertListEqual(actual, expected,
                             'Average len with abbreviations test: result isn\'t ' + str(expected))

    def test_text_with_repeated_sequence(self):
        text = 'hello its repeated seq some text aaa its repeated seq some text aaa some text aaa'
        expected = [(('some', 'text', 'aaa'), 3), (('its', 'repeated', 'seq'), 2), (('repeated', 'seq', 'some'), 2)]
        actual = parser.top_k_repeated_ngrams(text, 3, 3)
        self.assertListEqual(actual, expected,
                             'Average len with numbers test: result isn\'t ' + str(expected))


if __name__ == '__main__':
    unittest.main()
