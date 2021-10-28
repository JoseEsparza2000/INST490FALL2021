import json
import pymysql
import pymysql.cursors


# Read ALL data from database and convert it to a JSON structure
def convertDataToJson(mycursor):
    query = "SELECT * FROM pgcps_environmental_info"
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
