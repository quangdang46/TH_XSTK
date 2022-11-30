import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('company-sales_data.csv',delimiter=',')
# 1
plt.plot(data['month_number'],data['total_profit'],label='Profit data of last year')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.xticks(data['month_number'])
plt.title('Company profit per month')
plt.legend(loc='upper left')
plt.show()
# 2
plt.scatter(data['month_number'],data['toothpaste'],label='Toothpaste Sales Data',color='r',marker='o',s=100)
plt.xlabel('Month Number')
plt.ylabel('Number of units sold')
plt.xticks(data['month_number'])
plt.title('Toothpaste Sales Data')
plt.legend(loc='upper left')
plt.grid(True,linewidth=1,linestyle="--")
plt.show()
# 3
plt.bar([a-0.25 for a in data['month_number']],data['facecream'],width=0.25,label='Facecream Sales Data',align='edge')
plt.bar([a+0.25 for a in data['month_number']],data['facewash'],width=-0.25,label='Facewash Sales Data',align='edge')
plt.xlabel('Month Number')
plt.ylabel('Number of units sold')
plt.xticks(data['month_number'])
plt.title('Facewash and Facecream Sales Data')
plt.legend(loc='upper left')
plt.grid(True,linewidth=1,linestyle="--")
plt.show()
