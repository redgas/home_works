import pandas as pd
import matplotlib.pyplot as plt

mounts = pd.read_csv('Mountains.csv')
mounts = mounts[mounts['First ascent'] != 'unclimbed']
mounts['First ascent'] = mounts['First ascent'].astype(int)
print(mounts['Mountain'][mounts['Height (m)'].idxmax()], mounts['Height (m)'].max())
print(f'наибольшие кол-во вершин было покорено в {mounts["First ascent"].value_counts().index[0]} году')
plt.hist(mounts['First ascent'])
plt.show()

