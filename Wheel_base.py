import Header as m

m.plt1 = m.sns.scatterplot(x = 'wheelbase', y = 'price', data = m.df)
m.plt1.set_xlabel('Wheelbase (Inches)')
m.plt1.set_ylabel('Price of Car (Dollars)')
m.plt.show()