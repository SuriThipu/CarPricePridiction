import Header as m
fig, axs = m.plt.subplots(1,3,figsize=(20,5))
#
m.df_engine_avg_price = m.df[['enginetype','price']].groupby("enginetype", as_index = False).mean().rename(columns={'price':'engine_avg_price'})
m.plt1 = m.df_engine_avg_price.plot(x = 'enginetype', kind='bar', sort_columns = True, legend = False, ax = axs[0])
m.plt1.set_xlabel("Engine Type")
m.plt1.set_ylabel("Avg Price (Dollars)")
m.xticks(rotation = 0)
#
m.df_cylindernumber_avg_price = m.df[['cylindernumber','price']].groupby("cylindernumber", as_index = False).mean().rename(columns={'price':'cylindernumber_avg_price'})
m.plt1 = m.df_cylindernumber_avg_price.plot(x = 'cylindernumber', kind='bar', sort_columns = True,legend = False, ax = axs[1])
m.plt1.set_xlabel("Cylinder Number")
m.plt1.set_ylabel("Avg Price (Dollars)")
m.xticks(rotation = 0)
#
m.df_fuelsystem_avg_price = m.df[['fuelsystem','price']].groupby("fuelsystem", as_index = False).mean().rename(columns={'price':'fuelsystem_avg_price'})
m.plt1 = m.df_fuelsystem_avg_price.plot(x = 'fuelsystem', kind='bar', sort_columns = True,legend = False, ax = axs[2])
m.plt1.set_xlabel("Fuel System")
m.plt1.set_ylabel("Avg Price (Dollars)")
m.xticks(rotation = 0)
m.plt.show()