import eqanalysis
import turtle
import math

cities = []
fd = open("NWCities.csv", "r")
for line in fd:
    v = line.rstrip('\n').split(',')
    cities.append((v[0], float(v[1]), float(v[2]), float(v[3])))
fd.close()

eqanalysis.prepare_turtle()
win = turtle.Screen()

for i in range(len(cities)):
    x,y = eqanalysis.xy_calculate(cities[i][1], cities[i][2])
    eqanalysis.eq_turtle.goto(x. y)
    size = math.ceil(math.sqrt(cities[i][3]) / 20)
    print(cities[i][0], cities[i][3], size)
    eqanalysis.eq_turtle.dot(size)
win.exitonclick()
