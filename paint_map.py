import matplotlib.pyplot as plt
from japanmap import picture
from pylab import rcParams

rcParams['figure.figsize'] = (20, 20)
data = {
    '北海道': (255, 0, 0),
    '東京': (0, 255, 0),
    '愛知': (0, 0, 255),
    '大阪': 'Yellow',
    '愛媛': 'Purple',
    '香川': (255, 255, 0)
}

plt.imshow(picture(data))
plt.savefig('japan_colormap.png')