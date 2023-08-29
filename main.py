import math
import matplotlib.pyplot as plt

n = input("Maximum n: ")
while not n.isdigit():
    n = input("Invalid input. Enter integer value.\n"
              "Maximum n: ")
n = int(n)

n_list = []
x_list = []
x1_list = []
x2_list = []

x = 0
for i in range(1, n+1):
    i = int(i)
    x += 1/(i**3*math.sin(i)**2)
    x1 = -(2*i/math.tan(i)+3)/(i**4*math.sin(i)**2)
    x2 = 2*(i*(i/(math.sin(i)**2)+2*i/(math.tan(i)**2)+6/(math.tan(i)))+6)/(i**5*math.sin(i)**2)

    n_list.append(i)
    x_list.append(x)
    x1_list.append(x1)
    x2_list.append(x2)

plt.plot(n_list, x_list,
         color="blue",
         label="Flint Hill series",
         zorder=2)

plt.plot(n_list, x1_list,
         color="red",
         label="First derivative",
         zorder=1)

plt.plot(n_list, x2_list,
         color="green",
         label="Second derivative",
         zorder=0)

plt.title(f"Flint Hill Series for 1 ≤ n ≤ {n}")
plt.xlabel("Integer")
plt.ylabel("Value")

plt.xscale("log")
plt.xlim(1, n)
plt.ylim(-40, 40)

plt.legend()

plt.show()
