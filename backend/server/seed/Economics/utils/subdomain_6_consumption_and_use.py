# This script will read add average_domestic_production_to_consumption_ratio_2020 column to the CSV using
# https://datausa.io. Script aggregates values for keys present in "key_cols"
#
# It finds the "city, state-id" mapping from datausa_location_ids.json file.
# NOTE: There are some exception mapping added in map= "id_exceptions"

import time
from datetime import date

import requests
import json
import csv

string = open("data-usa-ids/datausa_location_ids.json", "r").read()

dic = json.loads(string)
datausa_map = {}
id_exceptions = {'indianapolis, in': 'indianapolis city (balance), in',
                 'nashville, tn': 'nashville-davidson metropolitan government (balance), tn',
                 'louisville, ky': 'louisville/jefferson county metro government (balance), ky',
                 'honolulu, hi': 'urban honolulu, hi', 'winston salem, nc': 'winston-salem, nc',
                 'augusta, ga': 'augusta-richmond county consolidated government (balance), ga',
                 'boise, id': 'boise city, id', 'lexington, ky': 'lexington-fayette, ky',
                 'macon, ga': 'macon-bibb county, ga',
                 'athens, ga': 'athens-clarke county unified government (balance), ga',
                 'san buenaventura, ca': 'san buenaventura (ventura), ca'}
to_check = []
data_year = ["2020"]

# [prod, consum, prod/consum] for 2020
key_cols = {"live animals/fish": [0, 0], "cereal grains": [0, 0], "other ag prods.": [0, 0], "animal feed": [0, 0],
            "meat/seafood": [0, 0], "milled grain prods.": [0, 0], "other foodstuffs": [0, 0],
            "alcoholic beverages": [0, 0], "tobacco prods.": [0, 0], "building stone": [0, 0], "natural sands": [0, 0],
            "gravel": [0, 0], "nonmetallic minerals": [0, 0], "metallic ores": [0, 0], "coal": [0, 0],
            "crude petroleum": [0, 0], "gasoline": [0, 0], "fuel oils": [0, 0], "coal-n.e.c.": [0, 0],
            "basic chemicals": [0, 0], "pharmaceuticals": [0, 0], "fertilizers": [0, 0], "chemical prods.": [0, 0],
            "plastics/rubber": [0, 0], "logs": [0, 0], "wood prods.": [0, 0], "newsprint/paper": [0, 0],
            "paper articles": [0, 0], "printed prods.": [0, 0], "textiles/leather": [0, 0],
            "nonmetal min. prods.": [0, 0], "base metals": [0, 0], "articles-base metal": [0, 0], "machinery": [0, 0],
            "electronics": [0, 0], "motorized vehicles": [0, 0], "transport equip.": [0, 0],
            "precision instruments": [0, 0], "furniture": [0, 0], "misc. mfg. prods.": [0, 0], "waste/scrap": [0, 0],
            "mixed freight": [0, 0]}


# creates a lookup dictionary "datausa_map" using "dic"
def update_datausa_id_map():
    for row in dic["results"]:
        datausa_map[row["name"].lower()] = row


# returns the average score for the city
# NOTE: It also does "not_considered" if any of the values is not present or 0
def get_average_prod_cons_ratio():
    ratio_sum = 0
    not_considered = 0

    for key, (v1, v2) in key_cols.items():
        if v1 and v2:
            ratio_sum += (v1 / v2)
            # print(key, (v1, v2), ratio_sum)
            # reset
            key_cols[key] = [0, 0]
        else:
            not_considered -= 1

    n = len(key_cols) - not_considered
    return ratio_sum / n

# Calls updateData consumption values
def update_row_consumption(key):
    details = datausa_map[key] if key in datausa_map else datausa_map[id_exceptions[key]]
    location_id = details['id']

    base = f'https://datausa.io/api/data?Destination State={location_id}&measure=Millions%20Of%20Dollars,' \
           f'Thousands%20Of%20Tons&drilldowns=SCTG2'
    data = requests.get(base).text
    time.sleep(1)
    try:
        # 1 for consumption index
        updateData(data, 1, data_year[0])
    except json.decoder.JSONDecodeError:
        print(data)
        to_check.append([key, "json.decoder.JSONDecodeError " + data, base])

# Calls updateData production values
def update_row_production(key):
    details = datausa_map[key] if key in datausa_map else datausa_map[id_exceptions[key]]
    location_id = details['id']

    base = f'https://datausa.io/api/data?Origin State={location_id}&measure=Millions%20Of%20Dollars,' \
           f'Thousands%20Of%20Tons&drilldowns=SCTG2'
    data = requests.get(base).text
    time.sleep(1)
    try:
        # 0 for production index
        updateData(data, 0, data_year[0])

    except json.decoder.JSONDecodeError:
        print(data)
        to_check.append([key, "json.decoder.JSONDecodeError " + data, base])


# Creates/Appends output/output.csv with new columns
def update_500_cities():
    passed = 0
    # name of csv output file
    output_file = open("output/output.csv", 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(output_file)

    # new columns
    new_cols = ["average_domestic_production_to_consumption_ratio_2020"]

    with open("../../final500Cities.csv", "r") as readObj:
        csvReader = csv.reader(readObj)
        headers = next(csvReader)

        # write headers
        headers.extend(new_cols)
        csv_writer.writerow(headers)

        row_count = 0
        for row in csvReader:
            # preprocessing for id lookups
            cityName = row[1].lower().replace("-", " ")
            stateID = row[3].lower()
            key = cityName + ", " + stateID

            if key in datausa_map or key in id_exceptions:
                update_row_production(key)
                update_row_consumption(key)
                row.append(get_average_prod_cons_ratio())
                passed += 1
            else:
                # default values
                row.append("N")
                to_check.append([key, "Key(city) not found"])

            row_count += 1
            print(f'Writing details for: {row_count} {key}')
            csv_writer.writerow(row)
            # break

    print("Found cities: ", passed - len(to_check), " \n Errors: ", to_check)


# Updates values in "key_cols" at index
def updateData(data, index, year):
    data_list = json.loads(data)["data"]
    data_map_year = {}

    # parses response in "data_map_year"
    for item in data_list:
        data_map_year[item["SCTG2"].lower() + "_" + item["Year"]] = item

    for key in key_cols.keys():
        if key + "_" + year in data_map_year:
            key_cols[key][index] = data_map_year[key + "_" + year]["Thousands Of Tons"]

update_datausa_id_map()
update_500_cities()
