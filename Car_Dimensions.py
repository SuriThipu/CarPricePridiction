import Header as m

# Let's see how price varies with Car's length, width,height and weight.

fig, axs = m.plt.subplots(2,2,figsize=(15,10))
m.plt1 = m.sns.scatterplot(x = 'carlength', y = 'price', data = m.df, ax = axs[0,0])
m.plt1.set_xlabel('Length of Car (Inches)')
m.plt1.set_ylabel('Price of Car (Dollars)')
m.plt2 = m.sns.scatterplot(x = 'carwidth', y = 'price', data = m.df, ax = axs[0,1])
m.plt2.set_xlabel('Width of Car (Inches)')
m.plt2.set_ylabel('Price of Car (Dollars)')
m.plt3 = m.sns.scatterplot(x = 'carheight', y = 'price', data = m.df, ax = axs[1,0])
m.plt3.set_xlabel('Height of Car (Inches)')
m.plt3.set_ylabel('Price of Car (Dollars)')
m.plt3 = m.sns.scatterplot(x = 'curbweight', y = 'price', data = m.df, ax = axs[1,1])
m.plt3.set_xlabel('Weight of Car (Pounds)')
m.plt3.set_ylabel('Price of Car (Dollars)')
m.plt.tight_layout()
m.plt.show()
