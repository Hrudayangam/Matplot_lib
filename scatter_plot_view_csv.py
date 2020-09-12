

import pandas as pd
from matplotlib import pyplot as plt




data = pd.read_csv(r'C:\Users\Asus\Desktop\resulting_data.csv')





plt.scatter(data.Net_Score,data.Number_Retweet)


plt.title('Net-score to Retweets')
plt.xlabel('Net_score')
plt.ylabel('Total retweets')

plt.tight_layout()

plt.show()

