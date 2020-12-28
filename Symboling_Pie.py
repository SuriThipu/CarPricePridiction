import Header as m

m.df_sym = m.pd.DataFrame(m.df['symboling'].value_counts())
m.df_sym.plot.pie(subplots=True,labels = m.df_sym.index.values, autopct='%1.1f%%', figsize = (15,7.5))
# Unsquish the pie.
m.plt.gca().set_aspect('equal')
m.plt.show()
m.plt.tight_layout()
