import requests
import matplotlib.pyplot as plt
from japanmap import picture
from pandas import DataFrame
from pylab import rcParams

url = 'https://www.stopcovid19.jp/data/covid19japan.json'

coviddata = requests.get(url).json()
df = DataFrame(coviddata['area'])

max = df['npatients'].max()
covidpatients = {}
for item in coviddata['area']:
    n = 255 - item['npatients'] / max*510
    covidpatients[item['name_jp']] = (255, n, n)

rcParams['figure.figsize'] = (8, 8)
plt.imshow(picture(covidpatients))
plt.savefig('covid_japanmap.png')