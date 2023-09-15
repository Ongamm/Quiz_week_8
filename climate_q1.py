import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect(r'climate.db')
cursor = connection.cursor()

sql_command = """
CREATE TABLE if not exists ClimateData (
Year INT PRIMARY KEY,
CO2 INT,
Temperature FLOAT(2,1));"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData(Year, CO2, Temperature)
VALUES ('1950', '250', '14.1');"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData(Year, CO2, Temperature)
VALUES ('1960', '265', '15.5');"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData(Year, CO2, Temperature)
VALUES ('1970', '272', '16.3');"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData(Year, CO2, Temperature)
VALUES ('1980', '260', '18.1');"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData(Year, CO2, Temperature)
VALUES ('1990', '300', '17.3');"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData(Year, CO2, Temperature)
VALUES ('2000', '320', '19.1');"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData(Year, CO2, Temperature)
VALUES ('2010', '389', '20.2');"""
cursor.execute(sql_command)

connection.commit()

years = []
co2 = []
temp = []

cursor.execute("SELECT * FROM ClimateData")
result = cursor.fetchall()

for r in result:
    years.append(result[r, 0])
    co2.append(result[r, 1])
    temp.append(result[r, 2])

connection.close()

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
