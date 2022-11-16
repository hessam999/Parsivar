from parsivar import Tokenizer
from parsivar import POSTagger
from parsivar import FindChunks
my_tokenizer = Tokenizer()
my_chunker = FindChunks()
my_tagger = POSTagger(tagging_model="wapiti")  # tagging_model = "wapiti" or "stanford". "wapiti" is faster than "stanford"
text_tags = my_tagger.parse(my_tokenizer.tokenize_words("این سمینار تا 13 شهریور ادامه می‌یابد ."))

chunks = my_chunker.chunk_sentence(text_tags)
print(my_chunker.convert_nestedtree2rawstring(chunks))
# [این سمینار DNP] [تا 13 شهریور NPP] [ادامه می‌یابد VP] .