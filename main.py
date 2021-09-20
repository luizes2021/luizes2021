import pandas as pd
df = pd.read_csv("advertising.csv")
print(df)

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.corr(), annot =True, cmap="Wistia")
plt.show()
sns.pairplot(df)
plt.show()