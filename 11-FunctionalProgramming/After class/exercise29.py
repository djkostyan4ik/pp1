import matplotlib.pyplot as plt
countries = [
    {"country":"Denmark","gold":2,"silver":4,"bronze":6},
    {"country":"Finland","gold":5,"silver":0,"bronze":4},
    {"country":"USA","gold":12,"silver":5,"bronze":11},
    {"country":"Peru","gold":0,"silver":1,"bronze":7}
]

x_values = [item['country'] for item in countries]
y_values = [item['gold'] + item['silver'] + item['bronze'] for item in countries]


plt.bar(x_values,y_values)
plt.title = 'Olympics'
plt.xlabel = 'Countries'
plt.ylabel = 'Medals'

plt.show()
