import csv
import json

jFile = open('D:/Downloads/sales.json')
data = json.load(jFile)
jFile.close()

with open("D:/output.csv", "w") as cFile:
    csvWriter = csv.writer(cFile)
    csvWriter.writerow(['Item', ' Country', ' Year', ' Sales'])

    for item_data in data:
        for country, sales in item_data["sales_by_country"].items():
            for year, amount in sales.items():
                csvWriter.writerow([str(item_data["item"]), " "+str(country), " "+str(year), " "+str(amount)])
