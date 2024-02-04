import numpy as np
import matplotlib.pyplot as plt

# Données
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Tracer la courbe
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.title('My graphs')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

# save figure to a file
plt.savefig("graph1.png")

#show graph
plt.show()