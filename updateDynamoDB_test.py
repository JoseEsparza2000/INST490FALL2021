import gspread
import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr
import pprint
import time
import json

gc = gspread.service_account(filename='keys.json')

spread = gc.open_by_key('1w1X00YL2uV_inK-l4VVbGXOXQpW1XoXlqkHFwDcJ-kc')

worksheet = spread.sheet1

res = worksheet.get_all_records()
num_of_cols = worksheet.col_count
with open ('column_names.json', 'r') as f:
    col_names = json.load(f)
    

for i in range(10):
    if res[i]["Does your school have an active garden? (Check all that apply)"].find('Vegetable garden') == -1:
        print(res[i]["Does your school have an active garden? (Check all that apply)"])


        
ACTIVE_GARDENS = [
    "Vegetable garden", "Native garden", "Butterfly garden", "Rain garden", 
    "Zen garden", "Herb garden", "No gardens on campus", "I don't know"
]

RECYCLE = [
    "At breakfast", "At lunch", "In the classroom", "Not at all", "I don't know"
]

RECYCLING_PROGRAMS = [
    "Ink Cartridge Recycling", "Cell Phones, Batteries and Other Electronics", 
    "Terra Cycling", "Color Cycle (Crayola)", "Pepsi Recycle Rally", 
    "None of these Programs/Activities", "I don't know"
]

COMPOSTING = [
     "We did not compost at our school", "Vermiculture", "Drum compost", 
     "Open frame", "Send Compost to Local Composting Facility/Farm", "I don't know" 
]

def getValuesForActiveGargen(googleValue, gardenType):
    if googleValue.find(gardenType) != -1:
        return "Yes"    
    return "No"

def getValuesForRecycle(googleValue, recycle):
    if googleValue.find(recycle) != -1:
        return '"Yes",'    
    return '"No",'

def getValuesForRecyclingProgram(googleValue, recyclingProgram):
    if googleValue.find(recyclingProgram) != -1:
        return '"Yes",'    
    return '"No",'

def getValuesForComposting(googleValue, composting):
    if googleValue.find(composting) != -1:
        return '"Yes",'    
    return '"No",'

# def getSchoolAdditionalInfo(schoolName):
#     for schoolInfo in KNOWN_SCHOOLS_INFO:
#         if schoolInfo[0].find(schoolName) != -1:
#             return str(schoolInfo[1]) + "," + str(schoolInfo[2]) + ",\"" + str(schoolInfo[3]) + "\",\"" + str(schoolInfo[4]) + "\"," 

#     return "38.7849,-76.8721,'Data Not Available','Data Not Available',"  
## Default value if we don't find the school
db_columnNames = [
    "section1_time_stamp",
    "section1_email",
    "section1_school_name",
    "section1_green_school_certification",
    "section1_active_garden_vegetable_garden",
    "section1_active_garden_native_garden",
    "section1_active_garden_butterfly_garden",
    "section1_active_garden_rain_garden",
    "section1_active_garden_zen_garden",
    "section1_active_garden_herb_garden",
    "section1_active_garden_no_gardens_on_campus",
    "section1_active_garden_dont_know",
    "section1_recycle_at_breakfast",
    "section1_recycle_at_lunch",
    "section1_recycle_in_the_classroom",
    "section1_recycle_not_at_all",
    "section1_recycle_dont_know",
    "section1_recycling_program_ink_cartridge_recycling",
    "section1_recycling_program_phones_batteries_other",
    "section1_recycling_program_terra_cycling",
    "section1_recycling_program_color_cycle_crayola",
    "section1_recycling_program_pepsi_recycle_rally",
    "section1_recycling_program_none_programs_activities",
    "section1_recycling_program_dont_know",
    "section1_composting_we_did_not_compost_at_our_school",
    "section1_composting_vermiculture",
    "section1_composting_drum_compost",
    "section1_composting_open_frame",
    "section1_composting_send_compost_local_facility_farm",
    "section1_composting_dont_know",
    "section1_cleanup_volunteer_effort",
    "section1_waste_reduction_comments",
    "section2_reducing_water_strategy",
    "section2_stream",
    "section2_water_prevention_stream_bank_planting",
    "section2_water_prevention_erosion_control_project",
    "section2_water_prevention_painted_storm_drains",
    "section2_water_prevention_raingarden_bioretention_area_planted",
    "section2_water_prevention_no_mow_zone",
    "section2_water_prevention_rain_barrels",
    "section2_water_prevention_stream_cleaning",
    "section2_water_prevention_collected_litter",
    "section2_water_prevention_turf_eduction",
    "section2_water_prevention_surface_reduction",
    "section2_water_prevention_green_roof",
    "section2_water_prevention_retrofitted_sink_toilet_showers",
    "section2_runoff_strategy",
    "section2_water_conservation_comments",
    "section3_reduce_energy_strategy",
    "section3_energy_conservation_installed_efficient_lighting",
    "section3_energy_conservation_use_daylighting",
    "section3_energy_conservation_delamped",
    "section3_energy_conservation_planted_tree_shading",
    "section3_energy_conservation_use_of_blinds",
    "section3_renewable_energy",
    "section3_renewable_source_solar",
    "section3_renewable_source_wind",
    "section3_renewable_source_geothermal",
    "section3_energy_conservation_comments",
    "section4_restore_habitat",
    "section4_habitat_restoration_created_bird_houses",
    "section4_habitat_restoration_planted_native_trees",
    "section4_habitat_restoration_planted_native_shrubs",
    "section4_habitat_restoration_removal_invasive_species",
    "section4_habitat_restoration_created_native_habitat",
    "section4_habit_restoration_comments",
    "section4_enviro_learning_structures",
    "section4_env_learn_struct_interpretive_signage",
    "section4_env_learn_struct_trails_pathways",
    "section4_env_learn_struct_boardwalk_bridges",
    "section4_env_learn_struct_tree_plant_id_tags",
    "section4_env_learn_struct_outdoor_classroom",
    "section4_env_learn_struct_outdoor_environmental_art",
    "section4_env_learn_struct_greenhouse",
    "section4_env_learn_struct_tower_garden",
    "section4_env_learn_struct_weather_station",
    "section4_env_learn_struct_pond",
    "section4_env_learn_struct_hydroponics",
    "section4_env_learn_struct_aquaponics",
    "section4_enviro_structure_comments",
    "section5_no_idle_zone",
    "section5_formal_carpooling",
    "section5_electric_hybrid_parking",
    "section5_grow_donate_eat_garden",
    "section5_green_cleaning_products",
    "section5_community_science_program",
    "section6_enviro_awards",
    "section6_actions_not_mentioned",
    "latitude",
    "longitude",
    "picture",
    "website"
]
# print(res[65])
# for i in range(len(res)):
#     print(i)

client = boto3.resource('dynamodb')
table = client.Table('testdb')
input = {"section1_time_stamp":"test",
        "section1_email":"test",
        "section1_school_name":"test",
        "section1_green_school_certification":"test",
        "section1_active_garden_vegetable_garden":"test",
        "section1_active_garden_native_garden":"test",
        "section1_active_garden_butterfly_garden":"test",
        "section1_active_garden_rain_garden":"test",
        "section1_active_garden_zen_garden":"test",
        "section1_active_garden_herb_garden":"test",
        "section1_active_garden_no_gardens_on_campus":"test",
        "section1_active_garden_dont_know":"test",
        "section1_recycle_at_breakfast":"test",
        "section1_recycle_at_lunch":"test",
        "section1_recycle_in_the_classroom":"test",
        "section1_recycle_not_at_all":"test",
        "section1_recycle_dont_know":"test",
        "section1_recycling_program_ink_cartridge_recycling":"test",
        "section1_recycling_program_phones_batteries_other":"test",
        "section1_recycling_program_terra_cycling":"test",
        "section1_recycling_program_color_cycle_crayola":"test",
        "section1_recycling_program_pepsi_recycle_rally":"test",
        "section1_recycling_program_none_programs_activities":"test",
        "section1_recycling_program_dont_know":"test",
        "section1_composting_we_did_not_compost_at_our_school":"test",
        "section1_composting_vermiculture":"test",
        "section1_composting_drum_compost":"test"
        
    }

# for i in range(10):
# for i in range(len(res)):
#     input2 = {'pkey':i,
#               'section1_time_stamp': res[i]['Timestamp'],
#               "section1_email":res[i]['Email Address'],
#               "section1_green_school_certification":res[i]['Does your school have a MD Green School Certification?'],
#               "section1_active_garden_vegetable_garden":getValuesForActiveGargen(res[i]['Does your school have an active garden? (Check all that apply)'], "Vegetable garden")
#               }
#     table.put_item(Item=input2)

# for i in range(10):
q= table.scan(
        # KeyConditionExpression = Key('pkey').eq(i) & Key('section1_green_school_certification')
    FilterExpression = Attr('section1_green_school_certification').eq('No')
)

res_len =   len(q['Items'])
for i in range(res_len):
    # print(q[i])
    print(q['Items'][i]['pkey'],q['Items'][i]['section1_green_school_certification'])
    # print(q['Items'][i]['pkey'])

# "section1_composting_open_frame",
        # "section1_composting_send_compost_local_facility_farm",
        # "section1_composting_dont_know",
        # "section1_cleanup_volunteer_effort",
        # "section1_waste_reduction_comments",
        # "section2_reducing_water_strategy",
        # "section2_stream",
        # "section2_water_prevention_stream_bank_planting",
        # "section2_water_prevention_erosion_control_project",
        # "section2_water_prevention_painted_storm_drains",
        # "section2_water_prevention_raingarden_bioretention_area_planted",
        # "section2_water_prevention_no_mow_zone",
        # "section2_water_prevention_rain_barrels",
        # "section2_water_prevention_stream_cleaning",
        # "section2_water_prevention_collected_litter",
        # "section2_water_prevention_turf_eduction",
        # "section2_water_prevention_surface_reduction",
        # "section2_water_prevention_green_roof",
        # "section2_water_prevention_retrofitted_sink_toilet_showers",
        # "section2_runoff_strategy",
        # "section2_water_conservation_comments",
        # "section3_reduce_energy_strategy",
        # "section3_energy_conservation_installed_efficient_lighting",
        # "section3_energy_conservation_use_daylighting",
        # "section3_energy_conservation_delamped",
        # "section3_energy_conservation_planted_tree_shading",
        # "section3_energy_conservation_use_of_blinds",
        # "section3_renewable_energy",
        # "section3_renewable_source_solar",
        # "section3_renewable_source_wind",
        # "section3_renewable_source_geothermal",
        # "section3_energy_conservation_comments",
        # "section4_restore_habitat",
        # "section4_habitat_restoration_created_bird_houses",
        # "section4_habitat_restoration_planted_native_trees",
        # "section4_habitat_restoration_planted_native_shrubs",
        # "section4_habitat_restoration_removal_invasive_species",
        # "section4_habitat_restoration_created_native_habitat",
        # "section4_habit_restoration_comments",
        # "section4_enviro_learning_structures",
        # "section4_env_learn_struct_interpretive_signage",
        # "section4_env_learn_struct_trails_pathways",
        # "section4_env_learn_struct_boardwalk_bridges",
        # "section4_env_learn_struct_tree_plant_id_tags",
        # "section4_env_learn_struct_outdoor_classroom",
        # "section4_env_learn_struct_outdoor_environmental_art",
        # "section4_env_learn_struct_greenhouse",
        # "section4_env_learn_struct_tower_garden",
        # "section4_env_learn_struct_weather_station",
        # "section4_env_learn_struct_pond",
        # "section4_env_learn_struct_hydroponics",
        # "section4_env_learn_struct_aquaponics",
        # "section4_enviro_structure_comments",
        # "section5_no_idle_zone",
        # "section5_formal_carpooling",
        # "section5_electric_hybrid_parking",
        # "section5_grow_donate_eat_garden",
        # "section5_green_cleaning_products",
        # "section5_community_science_program",
        # "section6_enviro_awards",
        # "section6_actions_not_mentioned",
        # "latitude",
        # "longitude",
        # "picture",
        # "website"













# res = table.get_item(
#     Key={
#         'schoolNames':'Parkdale High School'
#     }
# )
# print(res[0]['Completed Water Conservation/Water Pollution Prevention actions'])
# index = 0
# while index < len(res):

#     valueList = list(res[index].values())
#     print(valueList)
#     table.put_item(
#         Item={
#             'schoolName' : valueList[2],
#             'key' : valueList[0],
#             'Email Address': valueList[1],
#             'MD Green School Certification' : valueList[3],
#             'Active Garden' : valueList[4],
#             'Actively Recycle' : valueList[5],
#             'School participation in the following Recycling Programs/Activities?' : valueList[6],
#             'Type of composting implemented in school' : valueList[7],
#             'School participation in environmental cleanup volunteer efforts' : valueList[8],
#             'Waste Reduction:  Other and Comments, other waste reduction efforts' : valueList[9],
#             'Are strategies implemented to reduce water use in your school' : valueList[10],
#             'Do you have a stream located on your school grounds' : valueList[11],
#             'Completed Water Conservation/Water Pollution Prevention actions [Stream Bank Planting (Riparian Buffer)]' : valueList[12],
#             'Completed Water Conservation/Water Pollution Prevention actions [Erosion Control Project other than Stream Bank Planting]' : valueList[13],
#             'Completed Water Conservation/Water Pollution Prevention actions [Painted Storm Drains]' : valueList[14],
#             'Completed Water Conservation/Water Pollution Prevention actions [Raingarden/bioretention area planted]' : valueList[15],
#             'Completed Water Conservation/Water Pollution Prevention actions [No-mow zone installed ]' : valueList[16],
#             'Completed Water Conservation/Water Pollution Prevention actions [Rain barrels installed]' : valueList[17],
#             'Completed Water Conservation/Water Pollution Prevention actions [Stream Cleaning (at your school or in the community)]' : valueList[18],
#             'Completed Water Conservation/Water Pollution Prevention actions [Collected litter to prevent water pollution]' : valueList[19],
#             'Completed Water Conservation/Water Pollution Prevention actions [Turf Eduction]' : valueList[20],
#             'Completed Water Conservation/Water Pollution Prevention actions [Impervious surface reduction]' : valueList[21],
#             'Completed Water Conservation/Water Pollution Prevention actions [Green Roof]' : valueList[22],
#             'Completed Water Conservation/Water Pollution Prevention actions? [Retrofitted sinks, toilets, showers]' : valueList[23],
#             'Implement strategies to reduce or improve runoff from the school grounds?' : valueList[24],
#             'Water Conservation: storm water management has been done or is taking place at your school on what has been/is being done' : valueList[25],
#             'Does your school implement strategies to reduce energy use?': valueList[26],
#             'Completed the following Energy Conservation actions? [Installed efficient lighting]' : valueList[27],
#             'Completed the following Energy Conservation actions? Please provide an answer in each row.  [Use Daylighting most of the day]' : valueList[28],
#             'Completed the following Energy Conservation actions? [Delamped]' : valueList[29],
#             'Completed the following Energy Conservation actions? [Planted trees to shade building]' : valueList[30],
#             'Completed the following Energy Conservation actions? [Use of blinds in the classroom to control daylight and temperature]' : valueList[31],
#             'Does your school use renewable energy sources?' : valueList[32],
#             'Please indicate the renewable energy sources that your school uses? [Solar]' : valueList[33],
#             'Please indicate the renewable energy sources that your school uses? [Wind]' : valueList[34],
#             'Please indicate the renewable energy sources that your school uses? [Geothermal' : valueList[35],
#             'Energy Conservation: additional energy conservation practices or renewable energy sources are being implemented at your school' : valueList[36],
#             'Did you restore habitat on your school grounds?' : valueList[37],
#             'Habitat restoration actions that your school has implemented? [Created/Installed bird houses]' : valueList[38],
#             'Habitat restoration actions that your school has implemented? [Planted Native Trees]' : valueList[39],
#             'Habitat restoration actions that your school has implemented? [Planted Native Shrubs]' : valueList[40],
#             'Habitat restoration actions that your school has implemented? [Removal of invasive species]' : valueList[41],
#             'Habitat restoration actions that your school has implemented? [Created native habitat - meadows, wetlands or forests]' : valueList[42],
#             'Habitat Restoration: other habitat restoration efforts at your school or that your school has done in the community.' : valueList[43],
#             'Does your school have structures for environmental learning on the school grounds?' : valueList[44],
#             'Please indicate the structures for environmental learning located on your school grounds. [Interpretive signage]' : valueList[45],
#             'Please indicate the structures for environmental learning located on your school grounds. [Trails, pathways]' : valueList[46],
#             'Please indicate the structures for environmental learning located on your school grounds. [Boardwalk, bridges]' : valueList[47],
#             'Please indicate the structures for environmental learning located on your school grounds. [Tree/Plant ID Tags]' : valueList[48],
#             'Please indicate the structures for environmental learning located on your school grounds. [Outdoor Classroom]' : valueList[49],
#             'Please indicate the structures for environmental learning located on your school grounds. [Outdoor environmental art]' : valueList[50],
#             'Please indicate the structures for environmental learning located on your school grounds. [Greenhouse]' : valueList[51],
#             'Please indicate the structures for environmental learning located on your school grounds. [Tower garden]' : valueList[52],
#             'Please indicate the structures for environmental learning located on your school grounds. [Weather Station]' : valueList[53],
#             'Please indicate the structures for environmental learning located on your school grounds. [Pond]' : valueList[54],
#             'Please indicate the structures for environmental learning located on your school grounds. [Hydroponics ]' : valueList[55],
#             'Please indicate the structures for environmental learning located on your school grounds. [Aquaponics]' : valueList[56],
#             'Structures for Environmental Learning: other structures for environmental learning located on your school campus.' : valueList[57],
#             'Does your school have a No Idle Zone?' : valueList[58],
#             'Does your school have a formal carpooling program?' : valueList[59], 
#             'Does your school have parking spaces designated for electric, hybrid, or energy efficient vehicles?' : valueList[60],
#             'Does your school grow and donate and/or eat healthy food in school gardens?' : valueList[61],
#             'Does your school utilize green cleaning products?' : valueList[62],
#             'Participate in Citizen/Community Science programs to understand the school environment, how science is used' : valueList[63],
#             'Has your school received any awards or special recognition based on your enviornmental actions or instruction?' : valueList[64],
#             'Are there any other environmentally friendly actions your school takes that have not been mentioned in this survey?' : valueList[65],
#             }
#         )
#     index += 1




    