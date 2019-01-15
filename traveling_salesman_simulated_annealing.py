import random, numpy, math, copy, matplotlib.pyplot as plt
cities = [[0, 84], [45, 53], [17, 53], [89, 5], [24, 66], [98, 35], [38, 18], [90, 89], [8, 12], [96, 47]]
tour = random.sample(range(10),10)

def dist(city1, city2):
    xDist = abs(city1[0] - city2[0])
    yDist = abs(city1[1] - city2[1])
    distance = math.sqrt(xDist**2 + yDist**2)
    return distance

def distChange(tour, new_way):
    distanceChange = 0
    for k in new_way:
        distanceChange += dist(cities[tour[(k+1)%10]], cities[tour[k]])
    return distanceChange

for temp in numpy.logspace(0, 5, num = 100000)[::-1]:
    [i, j] = sorted(random.sample(range(10), 2))
    newTour = copy.deepcopy(tour)
    newTour[i], newTour[j] = newTour[j], newTour[i]
    P = math.exp((distChange(tour,[j, j-1, i, i-1])) - distChange(newTour, [j, j-1, i, i-1]) / temp)
    
    if P > random.random():
        tour = copy.copy(newTour)
plt.plot([cities[tour[i%10]][0] for i in range(11)], [cities[tour[i%10]][1] for i in range(11)], 'xb-')
