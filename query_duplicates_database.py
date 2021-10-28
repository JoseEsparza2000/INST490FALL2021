import json
import pymysql
import pymysql.cursors


# Read ALL data from database and convert it to a JSON structure
def convertDataToJson(mycursor):
    
    query = "SELECT *, COUNT(section1_school_name) FROM pgcps_environmental_info GROUP BY section1_school_name HAVING COUNT(section1_school_name) > 1"
    mycursor.execute(query)
    result = mycursor.fetchall()

    return json.dumps(result)



################
## MAIN PROGRAM
################
mydb = pymysql.connect(host='localhost',
                      user='root',
                      password='Inst#490',
                      db='pgcps_environmental_lit',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
mycursor = mydb.cursor()
jsonValue = convertDataToJson(mycursor)
print(jsonValue)
mydb.close()
