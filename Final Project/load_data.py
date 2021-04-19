import psycopg2
import psycopg2.extras
import requests
import csv

if __name__ == '__main__':
    connection_string = "host='localhost' dbname='project' user='crime' password='crime'"
    conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
    cursor = conn.cursor()
    licrim_schema = open('project.sql', 'r')
    cursor.execute(licrim_schema.read())
	
    count = int(0)
    with open('Liquor_Authority_Quarterly_List_of_Active_Licenses.csv', 'r') as liquor_data:
        reader = csv.reader(liquor_data)
        next(reader)  # Skip the header row.
        for row in reader:
            count += 1
            serial_num= row[0]

            lat = row[18]
            if lat == '': lat= None

            lon = row[19]
            if lon == '': lon = None

            exp_date = row[17]
            if exp_date == '': exp_date = None
            
            eff_date = row[16]
            if eff_date == '': eff_date = None
            
            issue_date = row[15]
            if issue_date == '': issue_date = None
            
            cert_number = row[14]
            zipcode = row[13]
            state = row[12]
            city = row[11]
            adress = None
            
            address2 = row[10] 
            address1 = row[9]
            dba = None
            
            dba = row[8]
            premises_name = row[7]
            county = row[6]
            office_num = row[5]
            office_name = row[4]
            type_code = row[3]
            class_code = row[2]
            if class_code == '':
                class_code = None
            type_name = row[1]
            locationID = None
            cursor.execute("SELECT id FROM locations WHERE city = %s AND state=%s AND zip = %s", (city, state, zipcode))
            if cursor.rowcount == 0:
                locationID = cursor.execute("INSERT INTO locations (city, state, zip) VALUES (%s, %s, %s) RETURNING id",(city, state, zipcode))
            else:
                locationID = cursor.fetchone()[0]

            agencyID = None
            cursor.execute("SELECT id FROM agency WHERE name = %s AND num=%s", (office_name, office_num))
            if cursor.rowcount == 0:
                agencyID = cursor.execute("INSERT INTO agency (name, num) VALUES (%s, %s) RETURNING id",(office_name, office_num))
            else:
                agencyID = cursor.fetchone()[0]

            licenseID = None
            if class_code == None:
                cursor.execute("SELECT id FROM license_types WHERE type_name = %s AND class_code is NULL AND type_code=%s", (type_name, type_code))
            else:
                cursor.execute("SELECT id FROM license_types WHERE type_name = %s AND class_code=%s AND type_code=%s", (type_name, class_code, type_code))
            if cursor.rowcount == 0:
                licenseID = cursor.execute("INSERT INTO license_types (type_name, class_code, type_code) VALUES (%s, %s, %s) RETURNING id",(type_name, class_code, type_code))
            else:
                licenseID = cursor.fetchone()[0]
            
            
            cursor.execute("""INSERT INTO liquor 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                            (serial_num, licenseID, agencyID, county, premises_name, dba, address1, address2, locationID, 
                            cert_number, issue_date, eff_date, exp_date, lat, lon))
            conn.commit()
   
    with open('Index_Crimes_by_County_and_Agency__Beginning_1990.csv','r') as crime_data:
        reader = csv.reader(crime_data)
        next(reader)  # Skip the header row.
        for row in reader:
            county = row[0]
            if county == '': county = None

            agency = row[1]
            if agency =='': agency = None

            year = row[2]
            if year == '': year = None

            months_reported = row[3]
            if months_reported == '': months_reported = None

            index_total = row[4]
            if index_total =='': index_total = None

            violent_total = row[5]
            if violent_total == '': violent_total = None

            murder = row[6]
            if murder == '': murder = None

            rape = row[7]
            if rape == '': rape = None

            robbery = row[8]
            if robbery == '': robbery = None

            aggravated_assault= row[9]
            if aggravated_assault  == '': aggravated_assault = None

            Property= row[10]
            if Property == '': Property = None

            burglary = row[11]
            if burglary == '': burglary = None

            larceny = row[12]
            if larceny == '': larceny = None

            motor_vehicle_theft= row[13]
            if motor_vehicle_theft == '': motor_vehicle_theft = None

            region = row[14]
            if region == '': region = None
            cursor.execute(
                   "INSERT INTO crimes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (county, agency, year, months_reported, index_total, violent_total, murder, rape, robbery, aggravated_assault, Property, burglary, larceny, motor_vehicle_theft, region)
            )
            conn.commit()

