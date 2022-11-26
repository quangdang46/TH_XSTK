import matplotlib.pyplot as plt

# thay doi file mau
# file goc:company-sales_data.csv


# file tam:company-sales.csv
file = open('company-sales.csv', 'r')
lines = file.readlines()
file.close()

toothpaste = []
shampoo = []
facecream = []

for line in lines[1:]:
  toothpaste.append(int(line.split(',')[1]))
  shampoo.append(int(line.split(',')[2]))
  facecream.append(int(line.split(',')[3]))

plt.plot(toothpaste, label='Toothpaste')
plt.plot(shampoo, label='Shampoo')
plt.plot(facecream, label='Facecream')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales data')
plt.legend()
plt.show()
