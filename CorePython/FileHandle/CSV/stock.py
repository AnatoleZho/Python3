from time import ctime
from urllib.request import urlopen
from distutils.log import warn as printf

TICKs = ('yhoo', 'dell', 'cost', 'adbe', 'intc')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sllc1p2'

printf('\nPrices quoted as of: %s PDT\n' % ctime())
printf("TICKer  PRICE CHANGE %AGE")
printf("------  ----- ------ ----")
str = URL % ','.join(TICKs)
printf(str)

u = urlopen(URL % ','.join(TICKs))

for row in u:
	tick, pirce, chg, per = row.split(',')
	printf(tick, '%.2f' % float(price), chg, per,)

u.close()

