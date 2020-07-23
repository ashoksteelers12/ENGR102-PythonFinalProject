import matplotlib.pyplot as plt
import numpy as np
from math import *
import csv
#EnergyConsumers.txt

consumers =[]

data = open("EnergyConsumers.txt")
spaces = data.readline()
spaces = data.readline()

years = data.readline()
yearsdat = years.split("\t")
del yearsdat[0]
for i in range(len(yearsdat)):
    yearsdat[i] = int(yearsdat[i])
years_data = yearsdat.copy()
del years_data[-1]
countries =[]

for line in data:
    linedata = line.split("\t")
    countries.append(linedata[0])
    del linedata[0]
    for i in range(len(linedata)):
        linedata[i] = float(linedata[i])
    consumers.append(linedata)


for i in range(len(consumers)):
    plt.hist(consumers[i],bins=50)
    plt.xlabel('Energy Consumption')
    plt.ylabel('Number of Years')
    plt.title(countries[i])
    plt.grid(True)
    plt.show()
data.close()

#EnergyRawDataFinal.txt

data1 = open("EnergyRawDataFinal.txt")
header = data1.readline()

countrydata=[]

linecount = 0
for line in data1:
    linecount += 1
    linedata = line.split(",")
    countrydata.append(linedata)

energytype = []
for i in range(len(countries)):
    j = 1
    while j < len(countrydata):
        if countrydata[j][0] == countries[i]:
            energytype.append([int(countrydata[j-1][3]),float(countrydata[j-1][1]),float(countrydata[j][1])])
        j+=2

tracker = 0
for i in range(len(countries)):
    electricity = []
    natural_gas = []
    for j in range(26):
        electricity.append(energytype[j+tracker][1])
        natural_gas.append(energytype[j+tracker][2])
    tracker += 26
    fig, ax1 = plt.subplots()
    ax1.plot(years_data,electricity, 'r-')
    ax1.set_xlabel('Years (1990-2015)')
    ax1.set_ylabel('Electricity')
    ax2 = ax1.twinx()
    ax2.plot(years_data,natural_gas, 'b-')
    ax2.set_ylabel('Natural Gas')
    plt.title('Electricity vs Natural Gas for %s' %(countries[i]))
    fig.tight_layout()
    plt.show()

data1.close()
#EnergyCOnsumers.txt for Ind
ind = np.arange(len(consumers)*len(consumers[0])).reshape(len(consumers), len(consumers[0]))
for i in range(len(consumers)):
    for j in range(len(consumers[0])):
        ind[i][j] = consumers[i][j]
for i in range(len(consumers)):
    for j in range(len(yearsdat)):
        if yearsdat[j] <= 2000:
            ind[i][j] *= .15
        else:
            ind[i][j] *= .35

for i in range(len(consumers)):
    plt.hist(ind[i],bins=50)
    plt.xlabel('Industrial Usage')
    plt.ylabel('Number of Years')
    plt.title(countries[i])
    plt.grid(True)
    plt.show()

#China consumption

for i in range(len(countries)):
    if countries[i] == 'China':
        plt.hist(consumers[i], bins=50)
        plt.xlabel('Consumption')
        plt.ylabel('Number of Years')
        plt.title(countries[i])
        plt.grid(True)
        plt.show()

#Continents
euro = np.zeros(len(yearsdat))
n_amer = np.zeros(len(yearsdat))
s_amer = np.zeros(len(yearsdat))
asia = np.zeros(len(yearsdat))
africa = np.zeros(len(yearsdat))
m_east = np.zeros(len(yearsdat))
for i in range(len(consumers)):
    for j in range(len(yearsdat)):
        if i < 18:
            euro[j] += consumers[i][j]
        elif i < 20:
            n_amer[j] += consumers[i][j]
        elif i < 26:
            s_amer[j] += consumers[i][j]
        elif i < 36:
            asia[j] += consumers[i][j]
        elif i < 40:
            africa[j] += consumers[i][j]
        else:
            m_east[j] += consumers[i][j]
continents = [euro, n_amer, s_amer, asia, africa, m_east]
continent_names = ['Europe', 'North America', 'South America', 'Asia', 'Africa', 'Middle East']
res = continents.copy()

for i in range(len(continents)):
    for j in range(len(yearsdat)):
        if yearsdat[j] <= 2000:
            res[i][j] *= .35
        else:
            res[i][j] *= .15
for i in range(len(continents)):
    plt.hist(res[i],bins=50)
    plt.xlabel('Only Residential')
    plt.ylabel('Number of Years')
    plt.title(continent_names[i])
    plt.grid(True)
    plt.show()

#CarbonEmmissions.txt

data2 = open('CarbonEmissions.txt')
header = data2.readline()
carbon_emissions = []
countries_emissions = []
for line in data2:
    linedata = line.split("\t")
    countries_emissions.append(linedata[1])
    del linedata[0]
    del linedata[0]
    for i in range(len(linedata)):
        linedata[i] = float(linedata[i])
    carbon_emissions.append(linedata)
consumers_2015 = []
i = 0
while i < 26:
    i+=1
    if i == 25:
        for j in range(len(countries)):
            for k in range(len(countries_emissions)):
                if j == k:
                    consumers_2015.append(consumers[j][i])
num1 = np.array([9040.74, 4997.5, 2066.01, 1468.99, 1141.58, 729.77, 585.99, 552.4, 549.23, 531.46, 450.79, 442.31,
               441.91, 427.57, 389.75, 380.93, 330.75, 317.22, 290.49, 282.4])
num2 = np.array([53.258962, 40.74455738, 246.2017574, 308.1048467, 151.9761675, 72.82964335, 95.56215343, 22.04019689,
               32.40854265, 120.1138679, 47.18147931, 181.1045349, 29.74420869, 129.7818635, 74.68421425, 689.7145147,
               90.77124003, 44.91438528, 274.0976469, 2203.006871])
val = np.arange(len(carbon_emissions))
length = 0.45
fig, axes = plt.subplots(ncols=1, nrows=1)
plt.title('Carbon Emissions vs Consumption for 2015')
plt.xlabel('20 Countries')
plt.ylabel('Mt/Yr')
axes.bar(val, num1, width=-1.*length, align='edge', label="Carbon Emissions")
axes.bar(val, num2, width=length, align='edge', label="Consumption for 2015")
axes.set_xticks(val)
axes.set_xticklabels(['CN', 'US', 'IN', 'RU', 'JP', 'HR', 'SK', 'IR', 'CA', 'SC', 'BR', 'MX', 'ID', 'SA', 'UK', 'AU',
                      'IT', 'TR', 'FR', 'PO'])
plt.legend()
plt.show()

#Answering Questions
print("What countries had the highest energy usage? India, China, and USA were shown to have the highest.")
print("In what continent are they located? The higher energy users are primarily located in Asia, except with USA"
      "in North America. One can argue USA makes up a lot of North America geographical wise, thus claiming both"
      "North America and Asia to have high energy uses out of the other continents, closely followed by Europe.")
