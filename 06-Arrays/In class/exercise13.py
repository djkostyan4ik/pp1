# arr = [25, 19, 32, 7]
# print("By car: ", arr[0])
# print("By public transport: ", arr[1])
# print("By bike: ", arr[2])
# print("By foot: ", arr[3])

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["By car", "By public transport", "By bike", "On foot"])
y = np.array([25, 19, 32, 7])
plt.title('How empoyees commute')
plt.bar(x, y)
plt.show()