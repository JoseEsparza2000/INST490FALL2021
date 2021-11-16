import gspread
import boto3

gc = gspread.service_account(filename='keys.json')

spread = gc.open_by_key('1w1X00YL2uV_inK-l4VVbGXOXQpW1XoXlqkHFwDcJ-kc')

worksheet = spread.sheet1

res = worksheet.get_all_records()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pgcpsDB')

index = 0
while index < len(res):

    valueList = list(res[index].values())

    table.put_item(
        Item={
            'Timestamp' : valueList[0],
            'Email Address': valueList[1],
            'School Names' : valueList[2],
            'MD Green School Certification' : valueList[3],
            'Active Garden' : valueList[4],
            'Actively Recycle' : valueList[5],
            'School participation in the following Recycling Programs/Activities?' : valueList[6],
            'Type of composting implemented in school' : valueList[7],
            'School participation in environmental cleanup volunteer efforts' : valueList[8],
            'Waste Reduction:  Other and Comments, other waste reduction efforts' : valueList[9],
            'Are strategies implemented to reduce water use in your school' : valueList[10],
            'Do you have a stream located on your school grounds' : valueList[11],
            'Completed Water Conservation/Water Pollution Prevention actions [Stream Bank Planting (Riparian Buffer)]' : valueList[12],
            'Completed Water Conservation/Water Pollution Prevention actions [Erosion Control Project other than Stream Bank Planting]' : valueList[13],
            'Completed Water Conservation/Water Pollution Prevention actions [Painted Storm Drains]' : valueList[14],
            'Completed Water Conservation/Water Pollution Prevention actions [Raingarden/bioretention area planted]' : valueList[15],
            'Completed Water Conservation/Water Pollution Prevention actions [No-mow zone installed ]' : valueList[16],
            'Completed Water Conservation/Water Pollution Prevention actions [Rain barrels installed]' : valueList[17],
            'Completed Water Conservation/Water Pollution Prevention actions [Stream Cleaning (at your school or in the community)]' : valueList[18],
            'Completed Water Conservation/Water Pollution Prevention actions [Collected litter to prevent water pollution]' : valueList[19],
            'Completed Water Conservation/Water Pollution Prevention actions [Turf Eduction]' : valueList[20],
            'Completed Water Conservation/Water Pollution Prevention actions [Impervious surface reduction]' : valueList[21],
            'Completed Water Conservation/Water Pollution Prevention actions [Green Roof]' : valueList[22],
            'Completed Water Conservation/Water Pollution Prevention actions? [Retrofitted sinks, toilets, showers]' : valueList[23],
            'Implement strategies to reduce or improve runoff from the school grounds?' : valueList[24],
            'Water Conservation: storm water management has been done or is taking place at your school on what has been/is being done' : valueList[25],
            'Does your school implement strategies to reduce energy use?': valueList[26],
            'Completed the following Energy Conservation actions? [Installed efficient lighting]' : valueList[27],
            'Completed the following Energy Conservation actions? Please provide an answer in each row.  [Use Daylighting most of the day]' : valueList[28],
            'Completed the following Energy Conservation actions? [Delamped]' : valueList[29],
            'Completed the following Energy Conservation actions? [Planted trees to shade building]' : valueList[30],
            'Completed the following Energy Conservation actions? [Use of blinds in the classroom to control daylight and temperature]' : valueList[31],
            'Does your school use renewable energy sources?' : valueList[32],
            'Please indicate the renewable energy sources that your school uses? [Solar]' : valueList[33],
            'Please indicate the renewable energy sources that your school uses? [Wind]' : valueList[34],
            'Please indicate the renewable energy sources that your school uses? [Geothermal' : valueList[35],
            'Energy Conservation: additional energy conservation practices or renewable energy sources are being implemented at your school' : valueList[36],
            'Did you restore habitat on your school grounds?' : valueList[37],
            'Habitat restoration actions that your school has implemented? [Created/Installed bird houses]' : valueList[38],
            'Habitat restoration actions that your school has implemented? [Planted Native Trees]' : valueList[39],
            'Habitat restoration actions that your school has implemented? [Planted Native Shrubs]' : valueList[40],
            'Habitat restoration actions that your school has implemented? [Removal of invasive species]' : valueList[41],
            'Habitat restoration actions that your school has implemented? [Created native habitat - meadows, wetlands or forests]' : valueList[42],
            'Habitat Restoration: other habitat restoration efforts at your school or that your school has done in the community.' : valueList[43],
            'Does your school have structures for environmental learning on the school grounds?' : valueList[44],
            'Please indicate the structures for environmental learning located on your school grounds. [Interpretive signage]' : valueList[45],
            'Please indicate the structures for environmental learning located on your school grounds. [Trails, pathways]' : valueList[46],
            'Please indicate the structures for environmental learning located on your school grounds. [Boardwalk, bridges]' : valueList[47],
            'Please indicate the structures for environmental learning located on your school grounds. [Tree/Plant ID Tags]' : valueList[48],
            'Please indicate the structures for environmental learning located on your school grounds. [Outdoor Classroom]' : valueList[49],
            'Please indicate the structures for environmental learning located on your school grounds. [Outdoor environmental art]' : valueList[50],
            'Please indicate the structures for environmental learning located on your school grounds. [Greenhouse]' : valueList[51],
            'Please indicate the structures for environmental learning located on your school grounds. [Tower garden]' : valueList[52],
            'Please indicate the structures for environmental learning located on your school grounds. [Weather Station]' : valueList[53],
            'Please indicate the structures for environmental learning located on your school grounds. [Pond]' : valueList[54],
            'Please indicate the structures for environmental learning located on your school grounds. [Hydroponics ]' : valueList[55],
            'Please indicate the structures for environmental learning located on your school grounds. [Aquaponics]' : valueList[56],
            'Structures for Environmental Learning: other structures for environmental learning located on your school campus.' : valueList[57],
            'Does your school have a No Idle Zone?' : valueList[58],
            'Does your school have a formal carpooling program?' : valueList[59], 
            'Does your school have parking spaces designated for electric, hybrid, or energy efficient vehicles?' : valueList[60],
            'Does your school grow and donate and/or eat healthy food in school gardens?' : valueList[61],
            'Does your school utilize green cleaning products?' : valueList[62],
            'Participate in Citizen/Community Science programs to understand the school environment, how science is used' : valueList[63],
            'Has your school received any awards or special recognition based on your enviornmental actions or instruction?' : valueList[64],
            'Are there any other environmentally friendly actions your school takes that have not been mentioned in this survey?' : valueList[65],
            }
        )
    index += 1




    