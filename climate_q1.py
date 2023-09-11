import matplotlib.pyplot as plt
import sqlite3



conn = sqlite3.connect("climate.db") # Connector
cursor = conn.cursor() # Cursor for queries
cursor.execute("SELECT year, co2, temperature FROM ClimateData ")
data = cursor.fetchall() # Fetchall rows from results
conn.close() # Close conn


years = [row[0] for row in data]
co2 = [row[1] for row in data]
temp = [row[2] for row in data]

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
plt.savefig("co2_temp_1.png") 
