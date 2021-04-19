You are working in a firm that requires you to perform an engineering analysis of energy consumption in
the world, with particular emphasis on potential impact on the levels of carbon dioxide distributed in the
atmosphere.
With the help of the analysis tools provided by Python and various packages, your team will perform the
following engineering evaluation: You will analyze a set of data, and produce a professional abstract report
using engineering language and clear organization of your work. This report should enhance your employer’s
understanding of the topic.
This is a Team project. During the grading process, your code will be scrutinized in MOSS for possible
plagiarism. The overall structure of the script your team creates can naturally be divided into different functions.
This is an especially practical technique for larger files where you may just want to focus on one area, such as
adjusting a plot. Functions allow you to modify and re-evaluate the code in a top-down design approach.

### Instructions
1.  Load the file EnergyConsumers.txt into a 2D array named Consumers.
2.  Using Matplotlib, create a single histogram of the consumption for each country and each year from
    Consumers. Create a logical bin size, and give a title to the figure of your histogram.
3.  Load the file EnergyRawDataFinal.txt into any container(list, tuple, numpy array, etc.) named
    EnergyType.
4.  Using Matplotlib, make a single creative graph comparing the Electricity and Natural Gas for each
    country and each year from EnergyType. You can create any type of graph, just make sure you compare
    the two types of consumption.
5.  Save a 2D array named Ind with all the data corresponding to the industrial usage type in Consumers.
    The industrial usage is accounted for 15% of the total energy consumption up to the year 2000 and 35%
    of the total energy consumption after the year 2000. For example, if the energy consumption during the
    year 1999 is 30 MTOE then 4.5 MTOE (15 % of 30 ) would be the industrial usage.
6.  Using Matplotlib, create a single histogram of Ind for each country and each year. Make the color of the
    graph different for the two time periods (before and after 2000).
7.  Make a histogram of the consumption for China only from Consumers.
8.  Create a new numpy object array variable named Continent for usage by continent data from
    Consumers. This variable should have the following categories: (Note, use your own discretion when
    deciding which continent certain border countries belong to, such as Turkey)
      a. Europe
      b. North America
      c. South America
      d. Asia
      e. Africa
      f. Middle east
9.   Create a histogram of Continents for Only Residential usage (Residential is the opposite of Industrial).
10.  Load the file CarbonEmissions.txt into a list named CarbonEmissions.
11.  Using a double bar graph, compare the twenty countries’ carbon emissions (million metric tons) from
     CarbonEmissions to their respective consumption in Consumers for the year 2015.
12.  What are the countries with the highest energy usage? In what continent are they located? Use print() to
     answer this question.
