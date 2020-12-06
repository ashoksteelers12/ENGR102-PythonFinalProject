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
consumption_2015 = []

for line in data:
    linedata = line.split("\t")
    countries.append(linedata[0])
    consumption_2015.append(linedata[26])
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
    #plt.savefig('EnergyConsumption_' + countries[i] + '.png')
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
    #plt.savefig('Electricity_NaturalGas_' + countries[i] + '.png')
    plt.show()

data1.close()

#EnergyCOnsumers.txt for Industrial Usage

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
    #plt.savefig('IndustrialUsage_' + countries[i] + '.png')
    plt.show()

#China Consumption

for i in range(len(countries)):
    if countries[i] == 'China':
        plt.hist(consumers[i], bins=50)
        plt.xlabel('Consumption')
        plt.ylabel('Number of Years')
        plt.title(countries[i])
        plt.grid(True)
        #plt.savefig('ChinaConsumption.png')
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
    #plt.savefig('OnlyResidential_' + continent_names[i] + '.png')
    plt.show()

#CarbonEmmissions.txt

data2 = open("CarbonEmissions.txt")

categs = data2.readline()
countries_emissions = []
carbon_emissions = []

for line in data2:
    linedata = line.split("\t")
    num = linedata[2]
    if "\n" in linedata[2]:
        num = linedata[2][:-1]
    countries_emissions.append(linedata[1])
    carbon_emissions.append(num)

countries_list_2015 = []
consumption_list_2015 = []

for e_name in countries_emissions:
  for name in countries:
    if name == e_name:
      countries_list_2015.append(e_name)
      consumption_list_2015.append(consumption_2015[countries.index(name)])
      
consumption_list_2015 = list(map(float, consumption_list_2015))
carbon_emissions = list(map(float, carbon_emissions))

val = np.arange(len(carbon_emissions))
length = 0.45
fig, axes = plt.subplots(ncols=1, nrows=1, figsize=(30,10))
plt.title('Carbon Emissions vs Consumption for 2015')
plt.xlabel('20 Countries')
plt.ylabel('Mt/Yr')
axes.bar(val, carbon_emissions, width=-1.*length, align='edge', label="Carbon Emissions")
axes.bar(val, consumption_list_2015, width=length, align='edge', label="Consumption for 2015")
axes.set_xticks(val)
axes.set_xticklabels(countries_list_2015)
plt.legend()
#plt.savefig('CarbonEmissions_vs_Consumption2015.png')
plt.show()

data2.close()

#Answering Questions

print("What countries had the highest energy usage? India, China, and USA were shown to have the highest.")
print("In what continent are they located? The higher energy users are primarily located in Asia, except with USA"
      "in North America. One can argue USA makes up a lot of North America geographical wise, thus claiming both"
      "North America and Asia to have high energy uses out of the other continents, closely followed by Europe.")
