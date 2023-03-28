import parser

f = open("/home/vadim_zhur/scol_labs/lab2/task1/text.txt", "r")
file_text = f.read()
print(file_text)

print("All sentences number:")
print(parser.calculate_sentences_num(file_text))
print("Declarative sentences number:")
print(parser.declarative_sentences_num(file_text))
print("Non-declarative sentences number:")
print(parser.non_declarative_sentences_num(file_text))
print("Average length of sentence in chars:")
print(parser.average_length_of_sentence_chars(file_text))
print("Average length of word in chars:")
print(parser.average_length_of_words_chars(file_text))
print("Top k repeated ngrams:")
print(parser.top_k_repeated_ngrams(file_text, 10, 1))
