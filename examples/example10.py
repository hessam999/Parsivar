from parsivar import Tokenizer
from parsivar import POSTagger
from parsivar import FindChunks
from parsivar import DependencyParser
my_tokenizer = Tokenizer()
my_parser = DependencyParser()

sents = "به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کار کرد. این سمینار تا ۱۳ شهریور ادامه می یابد"
sent_list = my_tokenizer.tokenize_sentences(sents)
parsed_sents = my_parser.parse_sents(sent_list)
for depgraph in parsed_sents:
	print(depgraph.tree())
# (به (گزارش (ایسنا (سمینار (شیمی آلی)))))
# (یابد (سمینار این) (تا (شهریور ۱۳)) ادامه می)