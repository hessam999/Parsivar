tmp_text = "به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کار کرد. این سمینار تا ۱۳ شهریور ادامه می یابد."
from parsivar import Normalizer
my_normalizer = Normalizer(date_normalizing_needed=True)
print(my_normalizer.normalize(tmp_text))
# 'به گزارش ایسنا سمینار شیمی آلی از امروز y1396m6d11 در دانشگاه علم و صنعت ایران آغاز به کار کرد . این سمینار تا y0m6d13 ادامه می‌یابد .'
