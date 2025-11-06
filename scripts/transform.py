import pandas as pd

df = pd.read_csv("data/delivery_data.csv")

#Avg Delivery Days

avg_days = df["delivery_days"].mean()

print(avg_days)

# on time delivery rate
on_time_rate = (df["delivered_on_time"].str.lower() == "yes").mean() *100

# Average package weight
avg_weight = df['weight_kg'].mean()

print(f"Average Delivery Days: {avg_days:.2f}")
print(f"On-Time Delivery Rate:: {on_time_rate:.2f}%")
print(f"Average Package Weight: {avg_weight:.2f} kg")