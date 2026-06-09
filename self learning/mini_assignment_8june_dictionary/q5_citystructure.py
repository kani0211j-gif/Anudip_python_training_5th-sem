#----------------------------------------------------------------------------------------
# City Population & Development Dashboard
# database of 30 cities
cities = {
    "Delhi":{"population":32000000,"area":1484,"literacy":89},
    "Mumbai":{"population":21000000,"area":603,"literacy":91},
    "Bangalore":{"population":13000000,"area":741,"literacy":88},
    "Hyderabad":{"population":11000000,"area":650,"literacy":87},
    "Chennai":{"population":10500000,"area":426,"literacy":90},
    "Kolkata":{"population":15000000,"area":205,"literacy":88},
    "Pune":{"population":7500000,"area":331,"literacy":91},
    "Ahmedabad":{"population":8500000,"area":505,"literacy":86},
    "Jaipur":{"population":4200000,"area":467,"literacy":84},
    "Lucknow":{"population":3800000,"area":631,"literacy":82},
    "Kanpur":{"population":3200000,"area":403,"literacy":80},
    "Nagpur":{"population":3100000,"area":218,"literacy":89},
    "Indore":{"population":3400000,"area":530,"literacy":87},
    "Bhopal":{"population":2500000,"area":285,"literacy":85},
    "Patna":{"population":2800000,"area":250,"literacy":81},
    "Surat":{"population":7000000,"area":461,"literacy":89},
    "Vadodara":{"population":2200000,"area":235,"literacy":88},
    "Agra":{"population":1800000,"area":188,"literacy":79},
    "Nashik":{"population":2000000,"area":264,"literacy":86},
    "Meerut":{"population":1700000,"area":141,"literacy":78},
    "Rajkot":{"population":1600000,"area":170,"literacy":87},
    "Varanasi":{"population":1900000,"area":153,"literacy":83},
    "Ludhiana":{"population":1800000,"area":159,"literacy":85},
    "Jodhpur":{"population":1500000,"area":233,"literacy":82},
    "Amritsar":{"population":1400000,"area":139,"literacy":84},
    "Ranchi":{"population":1500000,"area":175,"literacy":81},
    "Raipur":{"population":1300000,"area":226,"literacy":86},
    "Guwahati":{"population":1200000,"area":216,"literacy":88},
    "Dehradun":{"population":1100000,"area":196,"literacy":89},
    "Shimla":{"population":900000,"area":35,"literacy":92}
}
#----------------------------------------------------------------------------------------
# menu driven system
while True:
    print("\n========== CITY DASHBOARD MENU ==========")
    print("1. Display all city details")
    print("2. Find most populated city")
    print("3. Find least populated city")
    print("4. Calculate average population")
    print("5. Cities with literacy above 90%")
    print("6. Cities with literacy below average")
    print("7. Calculate population density")
    print("8. Highest density city")
    print("9. Categorize cities")
    print("10. Development priority list")
    print("11. High/Low literacy dictionaries")
    print("12. National summary report")
    print("13. Rank cities by density")
    print("14. Exit")

    choice = input("Enter your choice : ")
 #------------------------------------------------
    # display all cities
    if choice == '1':

        print("\n--- ALL CITY DETAILS ---")

        for city in cities:
            print(city, ":", cities[city])
 #------------------------------------------------
    # most populated city
    elif choice == '2':

        dict1 = list(cities.items())

        highest_city = dict1[0][0]
        highest_population = dict1[0][1]["population"]

        for city in cities:

            if cities[city]["population"] > highest_population:

                highest_population = cities[city]["population"]
                highest_city = city

        print("Most Populated City :", highest_city)
        print("Population :", highest_population)
#------------------------------------------------
    # least populated city
    elif choice == '3':

        dict1 = list(cities.items())

        lowest_city = dict1[0][0]
        lowest_population = dict1[0][1]["population"]

        for city in cities:

            if cities[city]["population"] < lowest_population:

                lowest_population = cities[city]["population"]
                lowest_city = city

        print("Least Populated City :", lowest_city)
        print("Population :", lowest_population)
#------------------------------------------------
    # average population
    elif choice == '4':

        total = 0
        count = 0

        for city in cities:

            total += cities[city]["population"]
            count += 1

        print("Average Population :", total / count)
#------------------------------------------------
    # literacy above 90%
    elif choice == '5':

        print("\n--- HIGH LITERACY CITIES ---")

        for city in cities:

            if cities[city]["literacy"] > 90:

                print(city, ":", cities[city])
#------------------------------------------------
    # literacy below average
    elif choice == '6':

        total = 0
        count = 0

        for city in cities:

            total += cities[city]["literacy"]
            count += 1

        avg = total / count

        print("\n--- BELOW AVERAGE LITERACY ---")

        for city in cities:

            if cities[city]["literacy"] < avg:

                print(city, ":", cities[city])
#------------------------------------------------
    # population density
    elif choice == '7':

        print("\n--- POPULATION DENSITY ---")

        for city in cities:

            density = cities[city]["population"] / cities[city]["area"]

            print(city, ":", density)
    #------------------------------------------------
    # highest density city
    elif choice == '8':

         dict1 = list(cities.items())

         highest_city = dict1[0][0]

         highest_density = (dict1[0][1]["population"] /dict1[0][1]["area"])
    
         for city in cities:

              density = (cities[city]["population"] /cities[city]["area"] )

              if density > highest_density:

                 highest_density = density
                 highest_city = city

         print("Highest Density City :", highest_city)
         print("Density :", highest_density)
 #------------------------------------------------
 #categorize cities
    elif choice == '9':

        print("\n--- CITY CATEGORIES ---")

        for city in cities:

            population = cities[city]["population"]

            if population >= 15000000:

                category = "Large"

            elif population >= 5000000:

                category = "Medium"

            else:

                category = "Small"

            print(city, "-",category)
#------------------------------------------------
    # development priority list
    elif choice == '10':

        print("\n--- DEVELOPMENT PRIORITY CITIES ---")

        for city in cities:

            if cities[city]["literacy"] < 85:

                print(city, ":", cities[city])
                #------------------------------------------------
    # high literacy and low literacy dictionaries
    elif choice == '11':

        high_literacy = {}
        low_literacy = {}

        for city in cities:

            if cities[city]["literacy"] >= 90:

                high_literacy[city] = cities[city]

            else:

                low_literacy[city] = cities[city]

        print("\n--- HIGH LITERACY CITIES ---")

        for city in high_literacy:

            print(city, ":", high_literacy[city])

        print("\n--- LOW LITERACY CITIES ---")

        for city in low_literacy:

            print(city, ":", low_literacy[city])
#------------------------------------------------
    # national summary report
    elif choice == '12':

        dict1 = list(cities.items())

        highest_city = dict1[0][0]
        lowest_city = dict1[0][0]

        highest_population = dict1[0][1]["population"]
        lowest_population = dict1[0][1]["population"]

        total_population = 0
        total_area = 0
        total_literacy = 0
        city_count = 0

        high_literacy_count = 0
        low_literacy_count = 0

        for city in cities:

            total_population += cities[city]["population"]
            total_area += cities[city]["area"]
            total_literacy += cities[city]["literacy"]
            city_count += 1

            if cities[city]["population"] > highest_population:

                highest_population = cities[city]["population"]
                highest_city = city

            if cities[city]["population"] < lowest_population:

                lowest_population = cities[city]["population"]
                lowest_city = city

            if cities[city]["literacy"] >= 90:

                high_literacy_count += 1

            else:

                low_literacy_count += 1

        avg_population = total_population / city_count
        avg_literacy = total_literacy / city_count
        print("      NATIONAL SUMMARY REPORT"           )

        print("Total Cities :", city_count)

        print("Most Populated City :", highest_city)
        print("Population :", highest_population)

        print("Least Populated City :", lowest_city)
        print("Population :", lowest_population)

        print("Average Population :", avg_population)

        print("Average Literacy :", avg_literacy)

        print("Total Population :", total_population)

        print("Total Area :", total_area)

        print("High Literacy Cities :", high_literacy_count)

        print("Low Literacy Cities :", low_literacy_count)
#------------------------------------------------
    # rank cities according to density
    elif choice == '13':

        temp = cities.copy()

        rank = 1

        print("\n--- CITY DENSITY RANKING ---")

        while len(temp) > 0:

            best_city = None
            best_density = -1

            for city in temp:

                density = (
                    temp[city]["population"] /
                    temp[city]["area"]
                )

                if density > best_density:

                    best_density = density
                    best_city = city

            print(rank, ".", best_city,
                  "Density =", best_density)

            del temp[best_city]

            rank += 1
#------------------------------------------------
    # exit program
    elif choice == '14':

        print("Exiting Program...")
        break
#------------------------------------------------
    else:

        print("Invalid Choice")
