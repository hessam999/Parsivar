from parsivar import Tokenizer
from parsivar import POSTagger
my_tokenizer = Tokenizer()
my_tagger = POSTagger(tagging_model="wapiti")  # tagging_model = "wapiti" or "stanford". "wapiti" is faster than "stanford"
text_tags = my_tagger.parse(my_tokenizer.tokenize_words("این سمینار تا 13 شهریور ادامه می‌یابد ."))
print(text_tags)
# [('این', 'DET'), ('سمینار', 'N_SING'), ('تا', 'P'), ('13', 'NUM'), ('شهریور', 'N_SING'), ('ادامه', 'N_SING'), ('می\u200cیابد', 'V_PRS'), ('.', '.')]
 