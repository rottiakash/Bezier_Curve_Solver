import numpy as np
import matplotlib.pyplot as plt

us = input("Enter the values of u: ")

p0 = np.array([1, 1])
p1 = np.array([2, 3])
p2 = np.array([4, 3])
p3 = np.array([3, 1])

coords = []

us = us.split(" ")
us = list(map(lambda u: float(u), us))
print(us)
for u in us:
    b0 = (1 - u) ** 3
    b1 = 3 * u * (1 - u) ** 2
    b2 = 3 * u ** 2 * (1 - u)
    b3 = u ** 3
    print("For u=%f" % (u))
    print("B0,3=%f" % (b0))
    print("B1,3=%f" % (b1))
    print("B2,3=%f" % (b2))
    print("B3,3=%f" % (b3))
    value = (b0 * p0) + (b1 * p1) + (b2 * p2) + (b3 * p3)
    coords.append(value)
    print("P(%f)=" % (u) + str(value))
    print("*******")
    print()

xs = list(map(lambda co: co[0], coords))
ys = list(map(lambda co: co[1], coords))

plt.plot(xs, ys)
for i_x, i_y in zip(xs, ys):
    plt.text(i_x, i_y, "({}, {})".format(round(i_x, 3), round(i_y, 3)))
plt.show()
