import Header as m

m.df_drivewheel_avg_price = m.df[['drivewheel','price']].groupby("drivewheel", as_index = False).mean().rename(columns={'price':'drivewheel_avg_price'})
m.plt1 = m.df_drivewheel_avg_price.plot(x = 'drivewheel', kind='bar', sort_columns = True,legend = False,)
m.plt1.set_xlabel("Drive Wheel Type")
m.plt1.set_ylabel("Avg Price (Dollars)")
m.xticks(rotation = 0)
m.plt.show()
