import matplotlib.pyplot as plt
import pandas as pd

# Load data from .csv file
data_csv = pd.read_csv('climate.csv')

# Extract into separate lists
years = data_csv['Year']
co2 = data_csv['CO2']
temp = data_csv['Temperature']

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_2.png")
