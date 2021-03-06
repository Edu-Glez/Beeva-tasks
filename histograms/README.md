# Python histograms with matplotlib

This folder contains some screenshots of the different histograms obtained from the movies.py script from the data-storage repo, and the commands introduced in order to get those histograms. This commands should be run in the python shell and in order from the first histogram to the second because they use the information obtained from the one before. Be sure to have your "movies" script ready so it can be run like it is shown below. You could also paste the script 'histograms.py' that is in this folder into the python_scripts folder in the data-storage repo and run it from there.

## Histogram #1
With this histogram we show the amount of people that gave a specific rating to the top five movies altogether.

```python
#Import necessary libraries
from movies import *
from matplotlib import pyplot as plt
import numpy as np

#Initialize arrays to be used to store the ratings of the movies
rat_shaw=[]
rat_forr=[]
rat_pulp=[]
rat_sile=[]
rat_star=[]


#Get the ratings of each movie
for i in range(0,len(rated_movies)):
	if rated_movies['title'][i] == 'Shawshank Redemption, The (1994)':
		rat_shaw.append(rated_movies['rating'][i])
	elif rated_movies['title'][i] == 'Forrest Gump (1994)':
		rat_forr.append(rated_movies['rating'][i])
	elif rated_movies['title'][i] == 'Pulp Fiction (1994)':
		rat_pulp.append(rated_movies['rating'][i])
	elif rated_movies['title'][i] == 'Silence of the Lambs, The (1991)':
		rat_sile.append(rated_movies['rating'][i])
	elif rated_movies['title'][i] == 'Star Wars: Episode IV - A New Hope (1977)':
		rat_star.append(rated_movies['rating'][i])
	else:
		pass

#Create figure to plot first histogram
plt.figure()

#Establish the position of the bars that are going to be used for the histogram
bins=np.arange(0,5+2,0.5)
#Send info and configure the figure of the histogram
plt.hist([rat_shaw,rat_forr,rat_pulp,rat_sile,rat_star], bins=bins, 
	rwidth=0.8, align='left', edgecolor='black', 
	color=['crimson', 'burlywood', 'chartreuse','blue','yellow'],
	label=['The Shawshank Redemption', 'Forrest Gump', 'Pulp Fiction', 'The Silence of the Lambs','Star Wars: Episode IV - A New Hope'])
plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6])
plt.title("Top 5 Movies Histogram")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.legend()
plt.show()
```

### Results

![alt text](https://github.com/Edu-Glez/Beeva-tasks/blob/master/histograms/HIST1.png)


## Histogram #2
With this histogram we show the same information as above but with each movie in a different subplot

```python
#Create figure to plot the second histogram
plt.figure()

#Select subplot
plt.subplot(231)

#Send info and configure the subplot of the histogram
plt.hist(rat_shaw, bins=bins, 
	rwidth=0.8, align='left', edgecolor='black', 
	color='crimson')
plt.title("The Shawshank Redemption",size=9)
plt.xlabel("Rating",size=9)
plt.ylabel("Frequency",size=9)
plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6],size=7,rotation='vertical')

#Select subplot
plt.subplot(232)

#Send info and configure the subplot of the histogram
plt.hist(rat_forr, bins=bins, 
	rwidth=0.8, align='left', edgecolor='black', 
	color='burlywood')
plt.title("Forrest Gump",size=9)
plt.xlabel("Rating",size=9)
plt.ylabel("Frequency",size=9)
plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6],size=7,rotation='vertical')

#Select subplot
plt.subplot(234)

#Send info and configure the subplot of the histogram
plt.hist(rat_pulp, bins=bins, 
	rwidth=0.8, align='left', edgecolor='black', 
	color='chartreuse')
plt.title("Pulp Fiction",size=9)
plt.xlabel("Rating",size=9)
plt.ylabel("Frequency",size=9)
plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6],size=7,rotation='vertical')

#Select subplot
plt.subplot(235)

#Send info and configure the subplot of the histogram
plt.hist(rat_sile, bins=bins, 
	rwidth=0.8, align='left', edgecolor='black', 
	color='blue')
plt.title("The Silence of the Lambs",size=9)
plt.xlabel("Rating",size=9)
plt.ylabel("Frequency",size=9)
plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6],size=7,rotation='vertical')

#Select subplot
plt.subplot(133)

#Send info and configure the subplot of the histogram
plt.hist(rat_star, bins=bins, 
	rwidth=0.8, align='left', edgecolor='black', 
	color='yellow')
plt.title("Star Wars: Episode IV - A New Hope",size=9)
plt.xlabel("Rating",size=9)
plt.ylabel("Frequency",size=9)
plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6],size=7,rotation='vertical')

plt.suptitle("Top 5 Movies Histogram",size=9)
plt.tight_layout()

plt.show()
```

### Results

![alt text](https://github.com/Edu-Glez/Beeva-tasks/blob/master/histograms/HIST2.png)
