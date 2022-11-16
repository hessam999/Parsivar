tmp_text = "به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کار کرد. این سمینار تا ۱۳ شهریور ادامه می یابد."
from parsivar import Normalizer
my_normalizer = Normalizer(statistical_space_correction=True)
print(my_normalizer.normalize(tmp_text))
# 'به گزارش ایسنا سمینار شیمی آلی از امروز 11 شهریور 1396 در دانشگاه علم و صنعت ایران آغاز به کار کرد . این سمینار تا 13 شهریور ادامه می‌یابد .'
