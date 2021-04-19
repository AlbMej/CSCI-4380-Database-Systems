import psycopg2
import psycopg2.extras


def typeRatioToCrimeRatio(lType, conn):
    ids = []
    t = ""
    if lType == 1: # bars
        t= "bars"
        ids=[6,11,26,28,31,42,43,46,39,54,57,69,74,85, 87]
    if lType == 2: # restaurants
        t= "restaurants"
        ids= [3,9,14,12,13,25,42,44,53,77,84,88]
    if lType == 3: # stores
        t = "stores"
        ids=[1,2,4,5,7,8,10,16,21,22,30,41,52,68]
    if lType == 4: # makers
        t="makers"
        ids=[18,32,33,35,38,45,50,51,55,53,59,60,62,66,72,75,78,83,82,71,90]
    if lType ==5: #rest
        t="other"
        ids = [15, 17, 19, 20, 23, 24, 27, 29, 34, 36, 37, 40, 47, 48, 49, 56, 58, 61, 63, 64, 65, 67, 70, 73, 76, 79, 80, 81, 86, 89]
    cursor = conn.cursor()
    #sql = "SELECT c.county, crime_ratio, (type_total * 1.0) / license_total FROM (SELECT county, round(sum(violent_total) * 1.0 / sum(total), 3) as crime_ratio FROM crimes WHERE  year = 2017 GROUP BY county) as c INNER JOIN ((SELECT count(*) as type_total, county FROM liquor WHERE license_type_id IN %s GROUP BY county) as t INNER JOIN (SELECT count(*) as license_total, county as countyName FROM liquor GROUP BY county) as f ON f.countyName = t.county) as g  ON lower(g.countyName) = lower(c.county)" % (str(tuple(ids)))
    cursor.execute("SELECT c.county, crime_ratio, round((type_total * 1.0) / license_total,3) as type_ratio FROM (SELECT county, round(sum(violent_total) * 1.0 / sum(total), 3) as crime_ratio FROM crimes WHERE  year = 2017 GROUP BY county) as c INNER JOIN ((SELECT count(*) as type_total, county FROM liquor WHERE license_type_id IN %s GROUP BY county) as t INNER JOIN (SELECT count(*) as license_total, county as countyName FROM liquor GROUP BY county) as f ON f.countyName = t.county) as g  ON lower(g.countyName) = lower(c.county) ORDER BY crime_ratio / ((type_total * 1.0) / license_total) DESC" % (str(tuple(ids))))
    records = cursor.fetchall()
    print ('county   \tviolent ratio\t {}\'s ratio of licenses'.format(t))
    for row in records:   
        print(row[0] + '    \t{}   \t{}'.format(row[1],row[2]))

def crimeChange(cType, numYears, county, conn):
    crime = ""
    if cType == 1: # all
        crime = "total"
    if cType == 2: #violent
        crime = "violent_total"
    if cType == 3:
        crime = "rape"
    if cType == 4:
        crime = "larceny"
    if cType == 5:
        crime = "property"

    cursor = conn.cursor()

    if county == "all":
        #sql = "SELECT a.county as county, round((new_crime*1.0) / old_crime, 3) as ratio FROM (SELECT sum(%s) as new_crime, county FROM crimes WHERE year = 2017 GROUP BY county) as a INNER JOIN (SELECT sum(%s) as old_crime, county FROM crimes WHERE year = %s GROUP BY county) as b ON a.county = b.county"
        cursor.execute("SELECT a.county as county, round((new_crime*1.0) / old_crime, 3) as ratio FROM (SELECT sum(%s) as new_crime, county FROM crimes WHERE year = 2017 GROUP BY county) as a INNER JOIN (SELECT sum(%s) as old_crime, county FROM crimes WHERE year = %s GROUP BY county) as b ON a.county = b.county WHERE old_crime != 0 ORDER BY ratio" % (crime, crime, 2017 - numYears))
    else:
        cursor.execute("""SELECT a.county as county, round((new_crime*1.0) / old_crime, 3) as ratio 
                        FROM (SELECT sum(%s) as new_crime, county FROM crimes WHERE year = 2017 and lower(county) = lower('%s') GROUP BY county) as a 
                        INNER JOIN (SELECT sum(%s) as old_crime, county FROM crimes WHERE year = %s  and lower(county) = ('%s') GROUP BY county) as b 
                        ON a.county = b.county WHERE old_crime != 0 ORDER BY ratio""" % (crime, county, crime, 2017 - numYears, county))
    records = cursor.fetchall()
    print ('county   \tchange in ' + crime)
    for row in records:
        print (row[0] + '    \t{}'.format(row[1]))

def getConn():
    connection_string = "host='localhost' dbname='project' user='crime' password='crime'"
    conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
    return conn

def counties_liq_crime(option, conn):
    cursor = conn.cursor()
    if option == 1: #counties with liquor/crime
        cursor.execute("SELECT crimes.county, (sum(crimes.violent_total)/count(liquor.ser_num))  FROM crimes INNER JOIN liquor ON lower(crimes.county) = lower(liquor.county) GROUP BY crimes.county ORDER BY county ASC;")
        result = cursor.fetchall()
        print("county      \t Ratio of Crimes to Liquor")
        for row in result:
            print(str(row[0]) + "    \t " + str(row[1]))
    elif option == 2: #most fun counties (most liquor least crime)
        cursor.execute("SELECT crimes.county, (sum(crimes.violent_total)/count(liquor.ser_num)) as cpl FROM crimes INNER JOIN liquor ON lower(crimes.county) = lower(liquor.county) GROUP BY crimes.county ORDER BY cpl ASC LIMIT 10;")
        result = cursor.fetchall()
        print("county      \t Ratio of Crimes to Liquor")
        for row in result:
            print(str(row[0]) + "    \t " + str(row[1]))
    elif option == 3: #least fun counties
        cursor.execute("SELECT crimes.county, (sum(crimes.violent_total)/count(liquor.ser_num)) as cpl FROM crimes INNER JOIN liquor ON lower(crimes.county) = lower(liquor.county) GROUP BY crimes.county ORDER BY cpl DESC LIMIT 10;")
        result = cursor.fetchall()
        print("county      \t Ratio of Crimes to Liquor")
        for row in result:
            print(str(row[0]) + "    \t " + str(row[1]))

def responsibleratio(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT agency.name, (sum(crimes.total)/count(liquor.ser_num))::float FROM agency, liquor, crimes WHERE agency.id = liquor.Agency_id AND lower(crimes.county) = lower(liquor.county) GROUP BY agency.name;")
    result = cursor.fetchall()
    print("Agency   \t Ratio of Total Crimes to Number of Liquor Stores")
    for row in result:
        print(str(row[0]) + "  \t " + str(row[1]))

def liquorstores(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT liquor.county, count(liquor.ser_num) as stores FROM liquor GROUP By liquor.county ORDER BY stores DESC;")
    result = cursor.fetchall()
    print("County Name   \t Number of Liquor Stores")
    for row in result:
        print(str(row[0]) + "    \t " + str(row[1]))

def liquor_crimes(crime, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT liquor.License_type_id, sum(crimes.%s)::float/sum(crimes.violent_total)::float as percent FROM crimes INNER JOIN liquor ON lower(crimes.county) = lower(liquor.county) GROUP By liquor.License_type_id ORDER BY liquor.License_type_id ASC;"  %(crime))
    result = cursor.fetchall()
    bars = 0.0
    restaurants = 0.0
    stores = 0.0
    makers = 0.0
    for row in result:
        if row[0] in [6,11,26,28,31,42,43,46,39,54,57,69,74,85,87]:
            bars += row[1]
        if row[0] in [3,9,14,12,13,25,42,44,53,77,84,88]:
            restaurants += row[1]
        if row[0] in [1,2,4,5,7,8,10,16,21,22,30,41,52,68]:
            stores += row[1]
        if row[0] in [18,32,33,35,38,45,50,51,55,53,59,60,62,66,72,75,78,83,82,71,90]:
            makers += row[1]
    print("License Type   \t Perecentage of Crimes that are %s" %(crime.capitalize()))
    print("Bars     \t", bars/15)
    print("Restaurants   \t", restaurants/12)
    print("Stores   \t", stores/14)
    print("Makers   \t", makers/21)