import Header as m

auto = m.df[['fueltype', 'aspiration', 'carbody', 'drivewheel', 'wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginetype',
       'cylindernumber', 'enginesize',  'boreratio', 'horsepower', 'price',  ]]


m.plt.figure(figsize=(10, 20))
m.plt.subplot(4,2,1)
m.sns.boxplot(x = 'fueltype', y = 'price', data = auto)
m.plt.subplot(4,2,2)
m.sns.boxplot(x = 'aspiration', y = 'price', data = auto)
m.plt.subplot(4,2,3)
m.sns.boxplot(x = 'carbody', y = 'price', data = auto)
m.plt.subplot(4,2,4)
m.sns.boxplot(x = 'drivewheel', y = 'price', data = auto)
m.plt.subplot(4,2,5)
m.sns.boxplot(x = 'enginetype', y = 'price', data = auto)
# m.plt.subplot(4,2,6)
# m.sns.boxplot(x = 'brand_category', y = 'price', data = auto)
m.plt.subplot(4,2,7)
m.sns.boxplot(x = 'cylindernumber', y = 'price', data = auto)
m.plt.tight_layout()
m.plt.show()