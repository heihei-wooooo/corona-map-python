import matplotlib.pyplot as plt
from japanmap import picture
from pylab import rcParams

rcParams['figure.figsize'] = (8, 8)
plt.imshow(picture())
plt.savefig('japanmap.png')