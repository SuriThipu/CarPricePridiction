import Header as m


fig, axs = m.plt.subplots(3,2,figsize=(20,20))
#
m.plt1 = m.sns.scatterplot(x = 'enginesize', y = 'price', data = m.df, ax = axs[0,0])
m.plt1.set_xlabel('Size of Engine (Cubic Inches)')
m.plt1.set_ylabel('Price of Car (Dollars)')
#
m.plt2 = m.sns.scatterplot(x = 'boreratio', y = 'price', data = m.df, ax = axs[0,1])
m.plt2.set_xlabel('Bore Ratio')
m.plt2.set_ylabel('Price of Car (Dollars)')
#
m.plt3 = m.sns.scatterplot(x = 'stroke', y = 'price', data = m.df, ax = axs[1,0])
m.plt3.set_xlabel('Stroke')
m.plt3.set_ylabel('Price of Car (Dollars)')
#
m.plt4 = m.sns.scatterplot(x = 'compressionratio', y = 'price', data = m.df, ax = axs[1,1])
m.plt4.set_xlabel('Compression Ratio')
m.plt4.set_ylabel('Price of Car (Dollars)')
#
m.plt5 = m.sns.scatterplot(x = 'horsepower', y = 'price', data = m.df, ax = axs[2,0])
m.plt5.set_xlabel('Horsepower')
m.plt5.set_ylabel('Price of Car (Dollars)')
#
m.plt5 = m.sns.scatterplot(x = 'peakrpm', y = 'price', data = m.df, ax = axs[2,1])
m.plt5.set_xlabel('Peak RPM')
m.plt5.set_ylabel('Price of Car (Dollars)')
m.plt.tight_layout()
m.plt.show()
