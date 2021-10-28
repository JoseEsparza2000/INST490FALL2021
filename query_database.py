import json
import pymysql
import pymysql.cursors
import sys


# Read ALL data from database and convert it to a JSON structure
def convertDataToJson(mycursor, columnName, value):    
    query = "SELECT * FROM pgcps_environmental_info WHERE %s like '%s'" % (columnName, value)
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
columnName = sys.argv[1]
value = sys.argv[2]
jsonValue = convertDataToJson(mycursor, columnName, value)
print(jsonValue)
mydb.close()
