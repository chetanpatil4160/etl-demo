import pandas as pd
import csv

df = pd.read_csv("data/delivery_data.csv")

#Avg Delivery Days
avg_days = df["delivery_days"].mean()


# on time delivery rate
on_time_rate = (df["delivered_on_time"].str.lower() == "yes").mean() *100

# Average package weight
avg_weight = df['weight_kg'].mean()

with open("data/summary.csv","w",newline="") as outfile:
    file = csv.writer(outfile)

    header = file.writerow(["metric_name","metric_value"])

    file.writerows([["Average Delivery Days",round(avg_days,2)],
                    ["On-Time Delivery Rate (%)",round(on_time_rate,2)],
                    ["Average Package Weight (kg)",round(avg_weight,2)]])
    
    print("Summary file saved successfully!")

