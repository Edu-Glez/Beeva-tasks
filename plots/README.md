# Python plots with matplotlib

This folder contains some screenshots of the different plots obtained from the movies.py script from the data-storage repo and the commands introduced. This commands should be run in the python shell and in order from plot 1 to 3 because the plots need the information obtained from the one before

## Plot #1
With this plot we obtained the average score of the top 5 movies

```python
from movies import *
from matplotlib import pyplot as plt
aux=[]
aux2=[]

for score in mean_ratings:
    aux.append(score)

for title in mean_ratings.keys():
    aux2.append(title)

xs = [i + 0.1 for i, _ in enumerate(aux)]

plt.bar(xs, aux)

plt.xticks([i for i, _ in enumerate(aux2)], aux2)

plt.show()
```

### Resultados

![alt text](https://github.com/Edu-Glez/Beeva-tasks/blob/master/plots/PLOT1.png)

## Plot #2
With this plot we can see the total sum of ratings for each genre

```python
sum_ratings2 = rated_movies.pivot_table(
    'rating',
    index='genres',
    aggfunc='sum')

top5genres=sum_ratings2.sort_values(ascending=False)[0:5]

aux3=[]
aux4=[]

for score2 in top5genres:
    aux3.append(score2)

for genre in top5genres.keys():
    aux4.append(genre)

xs2 = [i + 0.1 for i, _ in enumerate(aux3)]

plt.bar(xs2, aux3)

plt.xticks([i for i, _ in enumerate(aux4)], aux4)

plt.show()
```
### Resultados

![alt text](https://github.com/Edu-Glez/Beeva-tasks/blob/master/plots/PLOT2.png)


## Plot #3
With this plot we obtain the average points per genre

```python
mean_ratings2 = rated_movies.pivot_table(
    'rating',
    index='genres',
    aggfunc='mean')

# The mean of the hottest movies
mean_ratings2 = mean_ratings2.ix[aux4]

aux5=[]

for score3 in mean_ratings2:
    aux5.append(score3)

xs3 = [i + 0.1 for i, _ in enumerate(aux5)]

plt.bar(xs3, aux5)

plt.xticks([i for i, _ in enumerate(aux4)], aux4)

plt.show()
```

### Resultados

![alt text](https://github.com/Edu-Glez/Beeva-tasks/blob/master/plots/PLOT3.png)
