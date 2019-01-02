import random, numpy, math, copy, matplotlib.pyplot as plt
cities = [random.sample(range(100), 2) for x in range(15)]
tour = random.sample(range(15), 15)

def Distance(city1, city2):
    xDis = abs(city1[0] - city2[0])
    yDis = abs(city1[1] - city2[1])
    distance = math.sqrt((xDis**2) + (yDis**2))
    return distance
    
def DistanceChange(tours, new_way):
    DistanceChange = 0
    for k in new_way:
        DistanceChange += Distance(cities[tours[(k+1) % 15]], cities[tours[k % 15]]) 
#    print(DistanceChange)
    return DistanceChange
    
    
    
#def delta_E() 
for temperature in numpy.logspace(0, 5, num = 100000)[::-1]:
    [i, j] = sorted(random.sample(range(15), 2))
    newTour = copy.copy(tour)
    newTour[j], newTour[i] = newTour[i], newTour[j] 
#    newTour = tour[:i] + tour[j:j+1] + tour[i+1:j] + tour[i:i+1] + tour[j+1:]

    P = math.exp((DistanceChange(tour,[j, j-1, i, i-1]) - DistanceChange(newTour,[j, j-1, i, i-1])) / temperature)


    if P > random.random():
        tour = copy.copy(newTour);
plt.plot([cities[tour[i % 15]][0] for i in range(16)], [cities[tour[i % 15]][1] for i in range(16)], 'xb-')
plt.show()
