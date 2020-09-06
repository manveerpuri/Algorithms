import matplotlib.pyplot as plt

from numpy.random import default_rng

rng = default_rng()
num = int(input("Please enter number of rain drops: "))
x = rng.uniform(-1, 1, num)
y = rng.uniform(-1, 1, num)
r = 1
circle1 = plt.Circle((0, 0), r, fill=False)
ax = plt.gca()

ax.add_artist(circle1)

x_in = []
x_out = []
y_in = []
y_out = []

num_in = 0
for i in range(num):
    if x[i]*x[i] + y[i]*y[i] <= r*r:
        x_in.append(x[i])
        y_in.append(y[i])
        num_in += 1
    else:
        x_out.append(x[i])
        y_out.append(y[i])


ax.plot(x_in, y_in, '.', color='r')
ax.plot(x_out, y_out, '.', color='b')

plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()

print(4*num_in/num)
