import Header as m

m.plt1 = m.sns.countplot(m.df['symboling'])
m.plt1.set(xlabel = 'Symbol', ylabel= 'Count of Cars')
m.plt.show()
m.plt.tight_layout()