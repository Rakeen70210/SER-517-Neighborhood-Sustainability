import os

import pandas as pd

states = ["New York", "California", "Illinois", "Florida", "Texas", "Pennsylvania", "Texas", "Georgia",
          "District of Columbia", "Massachusetts", "Arizona", "Washington", "California", "Michigan", "California",
          "Minnesota", "Florida", "Colorado", "California", "Maryland", "Nevada", "Oregon", "Texas", "Missouri",
          "California", "Florida", "California", "Ohio", "Pennsylvania", "Texas", "Ohio", "Missouri", "Indiana", "Ohio",
          "North Carolina", "Virginia", "Wisconsin", "Rhode Island", "Florida", "Utah", "Tennessee", "Virginia",
          "Tennessee", "North Carolina", "Louisiana", "Kentucky", "Oklahoma", "Connecticut", "New York", "Texas",
          "Connecticut", "Arizona", "Nebraska", "Texas", "Hawaii", "Texas", "New Mexico", "Alabama", "Ohio", "New York",
          "California", "Pennsylvania", "Oklahoma", "Florida", "California", "Colorado", "South Carolina",
          "Massachusetts", "Michigan", "California", "New York", "Tennessee", "California", "Utah", "Louisiana", "Ohio",
          "Connecticut", "South Carolina", "Arizona", "Florida", "Utah", "Massachusetts", "California", "Kansas",
          "Ohio", "Iowa", "California", "Florida", "Texas", "Wisconsin", "Nevada", "Arkansas", "California",
          "North Carolina", "North Carolina", "California", "Florida", "Tennessee", "Washington", "New York", "Texas",
          "California", "Georgia", "Idaho", "California", "Pennsylvania", "California", "Colorado", "Ohio", "Arkansas",
          "California", "California", "California", "North Carolina", "Texas", "Indiana", "California", "Michigan",
          "North Carolina", "Mississippi", "California", "Michigan", "Kentucky", "Michigan", "Nevada", "Alabama",
          "Alabama", "Colorado", "North Carolina", "California", "Minnesota", "California", "Florida", "New Jersey",
          "Nebraska", "Missouri", "Alaska", "Texas", "California", "Iowa", "Illinois", "New Jersey", "Indiana",
          "Louisiana", "Georgia", "California", "Oregon", "Ohio", "Texas", "Pennsylvania", "Oregon", "Florida",
          "Louisiana", "Texas", "New Jersey", "North Carolina", "Georgia", "Arizona", "Texas", "Arizona", "Texas",
          "Florida", "Illinois", "North Carolina", "Alabama", "Arizona", "Arizona", "Nevada", "Virginia", "Virginia",
          "California", "Washington", "Texas", "Texas", "California", "New Hampshire", "Florida", "Indiana", "Arizona",
          "Texas", "Mississippi", "Wisconsin", "Washington", "California", "Texas", "Michigan", "California",
          "Virginia", "California", "California", "North Dakota", "Wisconsin", "Texas", "Maine", "California",
          "Florida", "Texas", "New York", "California", "California", "Florida", "Illinois", "Arizona", "Kansas",
          "Texas", "Texas", "California", "Connecticut", "Tennessee", "Iowa", "South Dakota", "California",
          "Pennsylvania", "Washington", "Idaho", "North Carolina", "Florida", "Tennessee", "North Carolina", "Virginia",
          "California", "California", "Connecticut", "Arizona", "California", "California", "Florida", "California",
          "California", "Oregon", "North Carolina", "California", "New Hampshire", "Illinois", "Virginia", "California",
          "Illinois", "Colorado", "Indiana", "Louisiana", "Texas", "Alabama", "Georgia", "California", "Florida",
          "Texas", "Georgia", "Kansas", "California", "California", "California", "Texas", "Massachusetts",
          "California", "Illinois", "Washington", "Kansas", "Illinois", "Texas", "New Jersey", "California", "Colorado",
          "Texas", "California", "Arizona", "Arizona", "Missouri", "Georgia", "California", "Colorado", "Florida",
          "California", "Texas", "California", "Kansas", "Texas", "West Virginia", "California", "California",
          "Colorado", "New Mexico", "Utah", "Virginia", "Michigan", "Illinois", "Florida", "Texas", "Washington",
          "Michigan", "Washington", "Washington", "California", "Wisconsin", "North Carolina", "Connecticut",
          "New Jersey", "Virginia", "California", "Arkansas", "Wisconsin", "Oklahoma", "Colorado", "Texas", "Texas",
          "California", "Texas", "California", "Colorado", "Utah", "Montana", "Minnesota", "Minnesota",
          "South Carolina", "Massachusetts", "Texas", "Iowa", "California", "Florida", "Missouri", "Utah", "Indiana",
          "California", "California", "South Carolina", "California", "California", "Idaho", "Colorado", "California",
          "Florida", "Florida", "Iowa", "Washington", "New Mexico", "California", "Massachusetts", "Colorado",
          "Illinois", "California", "Oklahoma", "Florida", "Oregon", "Vermont", "Georgia", "Oregon", "Texas", "Oregon",
          "California", "North Carolina", "California", "Texas", "California", "Iowa", "Florida", "California", "Texas",
          "California", "Nevada", "Texas", "California", "California", "California", "California", "California",
          "California", "Colorado", "Washington", "California", "California", "Texas", "Indiana", "Washington", "Texas",
          "Texas", "California", "Florida", "Missouri", "New Mexico", "Oregon", "Kansas", "Utah", "California", "Utah",
          "Washington", "California", "Massachusetts", "California", "Indiana", "Florida", "Georgia", "California",
          "Florida", "Massachusetts", "Virginia", "California", "Massachusetts", "Oklahoma", "Michigan", "Michigan",
          "California", "Oklahoma", "Montana", "South Dakota", "Virginia", "South Carolina", "California", "California",
          "California", "California", "Massachusetts", "Georgia", "Florida", "Connecticut", "California", "Missouri",
          "Massachusetts", "Indiana", "California", "Illinois", "Texas", "Illinois", "California", "California",
          "Alabama", "California", "California", "California", "New Jersey", "Florida", "Minnesota", "Georgia",
          "California", "Texas", "California", "Michigan", "California", "California", "Florida", "California",
          "California", "California", "Michigan", "Washington", "Rhode Island", "Massachusetts", "California",
          "Arkansas", "Florida", "Rhode Island", "Illinois", "Michigan", "Minnesota", "Massachusetts", "Minnesota",
          "Wyoming", "California", "California", "California", "Missouri", "Texas", "Colorado", "Florida", "New York",
          "Arkansas", "Ohio", "Utah", "California", "Texas", "California", "California", "California", "Pennsylvania",
          "Michigan", "Indiana", "Texas", "California", "Indiana", "Illinois", "Illinois", "Michigan", "California",
          "New Jersey", "Illinois", "California", "Illinois", "Michigan", "Connecticut", "Wisconsin", "Rhode Island",
          "Florida", "California", "Delaware", "California", "New Jersey", "New Jersey", "Illinois", "New York",
          "California", "Louisiana", "New York", ]

cities = ["New York", "Los Angeles", "Chicago", "Miami", "Dallas", "Philadelphia", "Houston", "Atlanta", "Washington",
          "Boston", "Phoenix", "Seattle", "San Francisco", "Detroit", "San Diego", "Minneapolis", "Tampa", "Denver",
          "Riverside", "Baltimore", "Las Vegas", "Portland", "San Antonio", "St. Louis", "Sacramento", "Orlando",
          "San Jose", "Cleveland", "Pittsburgh", "Austin", "Cincinnati", "Kansas City", "Indianapolis", "Columbus",
          "Charlotte", "Virginia Beach", "Milwaukee", "Providence", "Jacksonville", "Salt Lake City", "Nashville",
          "Richmond", "Memphis", "Raleigh", "New Orleans", "Louisville", "Oklahoma City", "Bridgeport", "Buffalo",
          "Fort Worth", "Hartford", "Tucson", "Omaha", "El Paso", "Honolulu", "McAllen", "Albuquerque", "Birmingham",
          "Dayton", "Rochester", "Fresno", "Allentown", "Tulsa", "Cape Coral", "Concord", "Colorado Springs",
          "Charleston", "Springfield", "Grand Rapids", "Mission Viejo", "Albany", "Knoxville", "Bakersfield", "Ogden",
          "Baton Rouge", "Akron", "New Haven", "Columbia", "Mesa", "Palm Bay", "Provo", "Worcester", "Murrieta",
          "Wichita", "Toledo", "Des Moines", "Long Beach", "Port St. Lucie", "Denton", "Madison", "Reno", "Little Rock",
          "Oakland", "Durham", "Winston-Salem", "Indio", "Palm Coast", "Chattanooga", "Spokane", "Syracuse",
          "Arlington", "Stockton", "Augusta", "Boise", "Oxnard", "Scranton", "Modesto", "Aurora", "Youngstown",
          "Fayetteville", "Anaheim", "Victorville", "Lancaster", "Greensboro", "Corpus Christi", "Fort Wayne",
          "Santa Ana", "Flint", "Fayetteville", "Jackson", "Santa Rosa", "Lansing", "Lexington", "Ann Arbor",
          "Henderson", "Huntsville", "Mobile", "Fort Collins", "Asheville", "Santa Clarita", "St. Paul", "Antioch",
          "Lakeland", "Trenton", "Lincoln", "Springfield", "Anchorage", "Plano", "Irvine", "Davenport", "Rockford",
          "Newark", "South Bend", "Shreveport", "Savannah", "Chula Vista", "Eugene", "Canton", "Lubbock", "Reading",
          "Salem", "St. Petersburg", "Lafayette", "Laredo", "Jersey City", "Concord", "Columbus", "Chandler",
          "McKinney", "Scottsdale", "Killeen", "Tallahassee", "Peoria", "Wilmington", "Montgomery", "Gilbert",
          "Glendale", "North Las Vegas", "Chesapeake", "Norfolk", "Fremont", "Kennewick", "Garland", "Irving",
          "Visalia", "Nashua", "Hialeah", "Evansville", "Avondale", "Brownsville", "Gulfport", "Appleton", "Tacoma",
          "San Bernardino", "College Station", "Kalamazoo", "Thousand Oaks", "Roanoke", "Fontana", "Moreno Valley",
          "Fargo", "Green Bay", "Amarillo", "Portland", "Santa Barbara", "Gainesville", "Frisco", "Yonkers", "Glendale",
          "Huntington Beach", "Deltona", "Aurora", "Tempe", "Overland Park", "Grand Prairie", "Waco", "Salinas",
          "Waterbury", "Clarksville", "Cedar Rapids", "Sioux Falls", "Ontario", "Erie", "Vancouver", "Nampa",
          "Gastonia", "Fort Lauderdale", "Murfreesboro", "High Point", "Newport News", "Rancho Cucamonga", "Hemet",
          "Danbury", "Peoria", "Oceanside", "Elk Grove", "Pembroke Pines", "Vallejo", "Garden Grove", "Medford", "Cary",
          "Corona", "Manchester", "Champaign", "Alexandria", "Hayward", "Springfield", "Lakewood", "Lafayette",
          "Lake Charles", "Odessa", "Tuscaloosa", "Warner Robins", "Palmdale", "Hollywood", "Midland", "Macon",
          "Kansas City", "Sunnyvale", "Pomona", "Escondido", "Pasadena", "New Bedford", "Fairfield", "Naperville",
          "Bellevue", "Topeka", "Joliet", "Beaumont", "Paterson", "Merced", "Pueblo", "Tyler", "Torrance", "Yuma",
          "Surprise", "Columbia", "Athens", "Roseville", "Thornton", "Miramar", "Pasadena", "Mesquite", "Santa Maria",
          "Olathe", "Carrollton", "Charleston", "Orange", "Fullerton", "Greeley", "Las Cruces", "West Valley City",
          "Hampton", "Warren", "Bloomington", "Coral Springs", "Round Rock", "Yakima", "Sterling Heights", "Kent",
          "Bellingham", "Santa Clara", "Racine", "Greenville", "Stamford", "Elizabeth", "Lynchburg", "Simi Valley",
          "Fort Smith", "Kenosha", "Norman", "Boulder", "Abilene", "Pearland", "Berkeley", "Richardson", "Redding",
          "Arvada", "St. George", "Billings", "Rochester", "Duluth", "Rock Hill", "Cambridge", "Sugar Land",
          "Iowa City", "Chico", "Clearwater", "Independence", "West Jordan", "Bloomington", "El Monte", "Carlsbad",
          "North Charleston", "Temecula", "Clovis", "Meridian", "Westminster", "Costa Mesa", "Pompano Beach",
          "West Palm Beach", "Waterloo", "Everett", "Santa Fe", "Downey", "Lowell", "Centennial", "Elgin", "Richmond",
          "Broken Arrow", "Miami Gardens", "Bend", "Burlington", "Sandy Springs", "Gresham", "Lewisville", "Hillsboro",
          "San Buenaventura", "Jacksonville", "Inglewood", "League City", "Turlock", "Sioux City", "Davie", "Daly City",
          "Allen", "West Covina", "Sparks", "Wichita Falls", "San Mateo", "Norwalk", "Rialto", "Manteca", "El Cajon",
          "Burbank", "Longmont", "Renton", "Vista", "Vacaville", "Edinburg", "Carmel", "Spokane Valley", "San Angelo",
          "Longview", "Tracy", "Boca Raton", "Lee's Summit", "Rio Rancho", "Beaverton", "Lawrence", "Orem",
          "San Marcos", "Sandy", "Federal Way", "Hesperia", "Brockton", "Compton", "Fishers", "Sunrise", "Roswell",
          "Menifee", "Plantation", "Quincy", "Portsmouth", "Chino", "Lynn", "Edmond", "Dearborn", "Livonia",
          "South Gate", "Lawton", "Missoula", "Rapid City", "Suffolk", "Mount Pleasant", "Carson", "Livermore",
          "Westminster", "Santa Monica", "Fall River", "Albany", "Miami Beach", "Norwalk", "San Leandro", "O'Fallon",
          "Newton", "Muncie", "Citrus Heights", "Decatur", "Bryan", "Waukegan", "Hawthorne", "Redwood City", "Hoover",
          "Lake Forest", "Napa", "Whittier", "Clifton", "Largo", "Bloomington", "Johns Creek", "Newport Beach",
          "Mission", "Milpitas", "Troy", "Chino Hills", "Alhambra", "Melbourne", "Mountain View", "Buena Park",
          "Pleasanton", "Westland", "Auburn", "Cranston", "Somerville", "Folsom", "Springdale", "Deerfield Beach",
          "Warwick", "Cicero", "Farmington Hills", "Brooklyn Park", "Lawrence", "Plymouth", "Cheyenne", "Tustin",
          "Lakewood", "Perris", "St. Joseph", "Pharr", "Loveland", "Boynton Beach", "New Rochelle", "Jonesboro",
          "Parma", "Layton", "Alameda", "Baytown", "Upland", "Bellflower", "San Ramon", "Bethlehem", "Wyoming",
          "Hammond", "Missouri City", "Baldwin Park", "Gary", "Arlington Heights", "Bolingbrook", "Rochester Hills",
          "Union City", "Camden", "Evanston", "Apple Valley", "Schaumburg", "Southfield", "New Britain", "Waukesha",
          "Pawtucket", "Lauderhill", "Redlands", "Wilmington", "Lynwood", "Passaic", "Union City", "Palatine",
          "Mount Vernon", "Redondo Beach", "Kenner", "Schenectady"]

# Read each of the specified csv files into a pandas dataframe
# The row number and new column name are specified.
def process_csv():
    os.chdir("..")
    foreign = pd.read_csv("data/Culture/ForeignBorn.csv")
    education = pd.read_csv("data/Culture/Educational Attainment.csv")
    languages = pd.read_csv('data/Culture/Identity and Engagement - Languages.csv')
    race = pd.read_csv('data/Culture/Age, Gender, and Race.csv')
    preprocess(foreign, 104, "Foreign Born")
    preprocess(education, 15, "Bachelor's Degree or Higher")
    preprocess(languages, 23, 'Speak A Language Other Than English')
    preprocess(race, 36, "Two or More Races")


# Compare all the city/states in each csv file with the list of 500 cities that we have.
# Only store the cities that are matching with our 500 list.
def preprocess(df, row_number, column_name):
    # Get a list columns from dataset containing city names
    list_of_city_names = list([col for col in df.columns if "!!Percent" in col])
    if len(list_of_city_names) == 0:
        list_of_city_names = list([col for col in df.columns if "!!Percent!!Estimate" in col])

    # store the value when cities match
    city_values = []

    # lists of cities and states that are not a direct match
    unmatched_cities = []

    # compare cities by doing a direct match using ==
    for x in range(500):
        found = False
        for column in list_of_city_names:
            # column = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', column)
            # print(column.split(',')[0].replace('city', ''))
            city = column.split(',')[0].replace('city', '').strip()
            state = column.split(',')[1]
            if cities[x].strip() == city.split('-')[0]:
                if states[x] in state:
                    city_values.append(df[column].values[row_number])
                    found = True
                    break
        if found is False:
            city_values.append(' ')
            unmatched_cities.append(x)

    # x is index in array cities/states, used to track which city or state was not matched
    # e.g. if x is 4 that means index 4 in array cities/states was not matched
    for index, x in enumerate(unmatched_cities):
        for column in list_of_city_names:
            city = column.split(',')[0].replace('city', '').strip()
            state = column.split(',')[1]
            # match cities by checking if it exists as the first # of characters
            if cities[x].strip() == city[:len(cities[x])]:
                if states[x] in state:
                    city_values[x] = (df[column].values[row_number])
                    # replace matched cities with empty string
                    unmatched_cities[index] = ''
                    break

    # remove cities that were just matched
    unmatched_cities = [x for x in unmatched_cities if x != '']

    # match remaining cities by checking if it exists anywhere else
    for index, x in enumerate(unmatched_cities):
        for column in list_of_city_names:
            city = column.split(',')[0].replace('city', '').strip()
            state = column.split(',')[1]
            if cities[x].strip() in city:
                if states[x] in state:
                    city_values[x] = (df[column].values[row_number])
                    unmatched_cities[index] = ''
                    break
    print(city_values)

    df = pd.read_csv('data/final500Cities.csv')
    df[column_name] = city_values
    print(df)
    df.to_csv('data/final500Cities.csv', mode='w', index=False)


process_csv()
