hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Sum up total made for haircuts
total_price = 0
for price in prices:
  total_price += price

# Find average price across all haircuts
average_price = total_price / len(prices)
print("Average Haircut Price: ${0}".format(average_price))

# Reduce all haircut prices by 5 as owner feels prices are a little too high
new_prices = [price - 5 for price in prices]
print(new_prices)

# Find how much revenue was brought in last week
total_revenue = 0
for i in range(0,len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("\nTotal Revenue: ${0}".format(total_revenue))

# Average Daily Revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue  ${0}".format(average_daily_revenue))

# Find all haircuts under $30 for targeted advertisement
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(f"\nHaircuts under $30: {cuts_under_30}")

