import Header as m

m.df_aspir_avg_price = m.df[['aspiration','price']].groupby("aspiration", as_index = False).mean().rename(columns={'price':'aspir_avg_price'})
m.plt1 = m.df_aspir_avg_price.plot(x = 'aspiration', kind='bar',legend = False, sort_columns = True)
m.plt1.set_xlabel("Aspiration")
m.plt1.set_ylabel("Avg Price (Dollars)")
m.xticks(rotation = 0)
m.plt.show()
