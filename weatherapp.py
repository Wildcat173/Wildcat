import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
weather = pd.read_csv ('Weather Dataset - Trial Activity DataSet.csv.csv')

print (weather.head())
print (weather.info())
sns.barplot(x=weather['humidity'], y=weather['temperature'])
plt.show()
sns.distplot(weather['humidity'], rug=True);

plt.show()


sns.jointplot(x=weather['humidity'], y=weather['temperature'])

plt.show()