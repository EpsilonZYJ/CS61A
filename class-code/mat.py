import matplotlib.pyplot as plt
import numpy as np

""""""
fig = plt.figure()
ax = fig.add_subplot(111)

plt.show()
""""""

""""""
fig = plt.figure()

#Creating subplot/axes
ax = fig.add_subplot(111)

#Setting polt title
ax.set_title('My plot title')

#Setting X-axis and Y-axis labels
ax.set_xlim([0, 10])
ax.set_ylim([-5, 5])

#Setting X-axis and Y-axis labels
ax.set_ylabel('My y-axis label')
ax.set_xlabel('My x-axis label')

#Showing the plot
plt.show()
""""""


""""""
fig = plt.figure()

#Creating subplot/axes
ax = fig.add_subplot(111)

#Setting title and axes properties
ax.set(title='An Axes Title', xlim=[0, 10], ylim=[-5, 5], ylabel='My y-axis label')

fig.show()
""""""

""""""
#Creating subplots, setting title and axes labels using 'pyplot'
plt.subplots()
plt.title('Plot using pyplot')
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.show()
""""""

""""""
#Creating subplots with 2 rows and 2 columns
fig, axes = plt.subplots(nrows=2, ncols=2)
plt.show()

""""""

""""""
#Create a figure with four subplots and shared axes
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
axes[0, 0].set(title='Upper Left', ylabel='Y-Axis Label')
axes[0, 1].set(title='Upper Right')
axes[1, 0].set(title='Lower Left')
axes[1, 1].set(title='Lower Right')
plt.show()
""""""

""""""
x = [1.3, 2.9, 3.1, 4.7, 5.6, 6.5, 7.4, 8.8, 9.2, 10]
y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 64]

#Plot lists 'x' and 'y'
plt.plot(x, y)

#Plot axes labels and show the plot
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Lbel')
plt.show()
""""""

""""""
#Defining 'y' coordinates
y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]

#Plot list'y'
plt.plot(y)

#Plot axes labels and show the plot
plt.xlabel('Index Values')
plt.ylabel('Elements in List Y')
plt.show()
""""""

""""""
#Plot line with green color
plt.plot(y, 'g')

#Plot axes labels and show the plot
plt.xlabel('Index Values')
plt.ylabel('Elements in List Y')
plt.show()
""""""

""""""
#Plot continuous green line with circle markers
plt.plot(y, 'go-')

#Plot axes labels and show the plot
plt.xlabel('Index Values')
plt.ylabel('Elements in List Y')
plt.show()
""""""

""""""
#Plot list 'y'
plt.plot(y, 'g')

#Plot red circle markers
plt.plot(y, 'ro')

#Plot axes labels and show the plot
plt.xlabel('Index Values')
plt.ylabel('Elements in List Y')
plt.show()
""""""


""""""
#Define two lists
y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]
y2 = [35, 52, 96, 77, 36, 66, 50, 12, 35, 63]
print(type(y))

#Plot lists and show them
plt.plot(y, 'go-')
plt.plot(y2, 'b*--')

#Plot axes labels and show the plot
plt.xlabel('Index Values')
plt.ylabel('Elements in Lists')
plt.show()
""""""

""""""
#Importing NumPy library
import numpy as np

#Drawing 30 samples from a standard normal distribution into an array
arr = np.random.normal(size=30)
print(arr)

#Plotting 'arr' with dashed line-style and * markers
plt.plot(arr, color='teal', marker='*', linestyle='dashed')
""""""

""""""
#Data points for scatter plot
x = [1.3, 2.9, 3.1, 4.7, 5.6, 6.5, 7.4, 8.8, 9.2, 10]
y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]

color = np.random.rand(10)
size = np.random.randint(50, 100, 10)

#Creating a scatter plot
plt.scatter(x, y, s=size, c=color)

#Labeling the plot and showing it
plt.xlabel('Values from list x')
plt.ylabel('Values from list y')
plt.show()
""""""

""""""
#Creating a scatter plot without color and same
plt.scatter(x, y)

#Labeling the plot and showing it
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()
""""""





"""
Histograms
"""

""""""
#Data values for creating a histogram
y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]

#Creating a histogram
plt.hist(y)
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.show()
""""""

""""""
#Creating an array
array = np.random.normal(0, 1, 10000)

#Creating a histogram
plt.hist(array)
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.show()
""""""

""""""
#Creating an array
array = np.random.normal(0, 1, 10000)

#Creating a histogram
plt.hist(array, color='purple', histtype='step')
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.show()
""""""


""""""
#Creating an array
array = np.random.normal(0, 1, 10000)

#Creating a histogram
plt.hist(array, color='teal', orientation='horizontal')
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.show()
""""""


""""""
from matplotlib.colors import LogNorm
import numpy as np

#create some data for plotting
num_particles = 1000
eta = np.zeros(1000)
phi = np.zeros(1000)
for i in range(1000):
    eta[i] = np.random.rand()*2.0 - 1.0
    phi[i] = np.random.rand()*2.0*3.14159*2

deta = []
dphi = []
for i in range(1000):
    for j in range(i+1, 1000):
        d1 = eta[i] - eta[j]
        d2 = phi[i] - phi[j]
        deta.append(d1)
        dphi.append(d2)

#separate the histogramming and plotting steps
#hist2d will do the binning, picking the axis range, counting and plotting
plt.subplot(121)
counts, xbins, ybins, image = plt.hist2d(deta, dphi, bins=100, norm=LogNorm(), cmap=plt.cm.rainbow)

#now take the counts and bins and usse contour() function to plot a nice

plt.colorbar()
plt.subplot(122)
plt.contour(counts, extent=[xbins[0], xbins[-1], ybins[0], ybins[-1]],
            linewidths=3, cmap=plt.cm.rainbow, levels=[1, 5, 10, 25, 50, 70, 80, 100])
plt.show()
""""""





"""
Data Analysis
"""

""""""
import numpy as np

def count_cars(days):
    x = np.random.normal(3000, np.sqrt(3000), days)
    cars_per_day = []
    for i in range(days):
        cars_per_day.append(int(x[i]))
    average = np.average(cars_per_day)
    return cars_per_day, average

days = 700
cars_per_day, average = count_cars(days)
print("cars per day = ", cars_per_day)
print("average number of cars per day over", days, "days = ", average)

import matplotlib.pyplot as plt

plt.hist(cars_per_day, bins = 100)
plt.xlabel('cars per day')
plt.show()


var = np.var(cars_per_day)
std = np.std(cars_per_day)
print("variance = ", var,", standard deviation = ", std, ", uncertainty = ", std/np.sqrt(days))


cars_per_week = []
for i in range(100):
    cars_per_day, average = count_cars(7)
    cars_per_week.append(average)
#   print("Week", i, ":", cars_per_week[-1])
print("standard deviation of cars_per_week:", np.std(cars_per_week))
plt.hist(cars_per_week)
plt.xlabel('cars_per_week')
plt.show()
""""""


"""
Distributions
"""

""""""
#Uniform distribution

x = np.random.rand(100000)*10 + 5
plt.hist(x)
plt.xlabel("value of x")
plt.ylabel("no of observations")
plt.show()

sigma = np.std(x)
print('Standard deviation of distribution from 5 to 15 is ', sigma)

print("(interval/std)^2 = ", np.square((15-5)/sigma))
"""
uncertainty of a single measurement, from a uniform distribution
of width b-a is sigma = (b-a)/sqrt(12)
"""
""""""

""""""
#Poisson distribution
cars_per_day, average = count_cars(1000)
print("Counting on average ", average, "cars per day")
accident_probabilty = 0.001
accidents_per_day = []
for i in range(len(cars_per_day)):

    no_of_accidents = 0
    for j in range(cars_per_day[i]):
        x = np.random.rand()
        if(x < accident_probabilty):
            no_of_accidents += 1
    if(i%100 == 0):
        print(no_of_accidents," accidents on day", i)
    accidents_per_day.append(no_of_accidents)

plt.hist(accidents_per_day)
plt.xlabel("accidents per day")
plt.ylabel("no of observations")
plt.show()
print("mean no of accident = ", np.average(accidents_per_day), ",", average*accident_probabilty, "expected")
print("standard deviation", np.var(accidents_per_day), ",", average*accident_probabilty, "expected")



cars_per_day, average = count_cars(1000)
print("Counting on average ", average, "cars per day")
accident_probabilty = 0.020
accidents_per_day = []
for i in range(len(cars_per_day)):

    no_of_accidents = 0
    for j in range(cars_per_day[i]):
        x = np.random.rand()
        if(x < accident_probabilty):
            no_of_accidents += 1
    if(i%100 == 0):
        print(no_of_accidents," accidents on day", i)
    accidents_per_day.append(no_of_accidents)

plt.hist(accidents_per_day)
plt.xlabel("accidents per day")
plt.ylabel("no of observations")
plt.show()
print("mean no of accident = ", np.average(accidents_per_day), ",", average*accident_probabilty, "expected")
print("standard deviation", np.var(accidents_per_day), ",", average*accident_probabilty, "expected")
""""""
