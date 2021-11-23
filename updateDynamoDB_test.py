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


client = boto3.resource('dynamodb')
table = client.Table('testdb')

# for i in range(10):
for i in range(len(res)):
    input2 = {  "pkey":i+1,
                "section_1_school_name":res[i]['What is the name of your school? '],
                "section1_time_stamp": res[i]['Timestamp'],
                "section1_email":res[i]['Email Address'],
                "section1_green_school_certification":res[i]['Does your school have a MD Green School Certification?'],
                "section1_active_garden_vegetable_garden":getValuesForActiveGargen(res[i]['Does your school have an active garden? (Check all that apply)'], ACTIVE_GARDENS[0]),
                "section1_active_garden_native_garden":getValuesForActiveGargen(res[i]['Does your school have an active garden? (Check all that apply)'], ACTIVE_GARDENS[1]),
                "section1_active_garden_butterfly_garden":getValuesForActiveGargen(res[i]['Does your school have an active garden? (Check all that apply)'], ACTIVE_GARDENS[2]),
                "section1_active_garden_rain_garden":getValuesForActiveGargen(res[i]['Does your school have an active garden? (Check all that apply)'], ACTIVE_GARDENS[3]),
                "section1_active_garden_zen_garden":getValuesForActiveGargen(res[i]['Does your school have an active garden? (Check all that apply)'], ACTIVE_GARDENS[4]),
                "section1_active_garden_herb_garden":getValuesForActiveGargen(res[i]['Does your school have an active garden? (Check all that apply)'], ACTIVE_GARDENS[5]),
                "section1_active_garden_no_gardens_on_campus":getValuesForActiveGargen(res[i]['Does your school have an active garden? (Check all that apply)'], ACTIVE_GARDENS[6]),
                "section1_active_garden_dont_know":getValuesForActiveGargen(res[i]['Does your school have an active garden? (Check all that apply)'], ACTIVE_GARDENS[7]),
                "section1_recycle_at_breakfast":getValuesForRecycle(res[i]['Does your school actively recycle? (Check all that apply)'], RECYCLE[0]),
                "section1_recycle_at_lunch":getValuesForRecycle(res[i]['Does your school actively recycle? (Check all that apply)'], RECYCLE[1]),
                "section1_recycle_in_the_classroom":getValuesForRecycle(res[i]['Does your school actively recycle? (Check all that apply)'], RECYCLE[2]),
                "section1_recycle_not_at_all":getValuesForRecycle(res[i]['Does your school actively recycle? (Check all that apply)'], RECYCLE[3]),
                "section1_recycle_dont_know":getValuesForRecycle(res[i]['Does your school actively recycle? (Check all that apply)'], RECYCLE[4]),
                "section1_recycling_program_ink_cartridge_recycling":getValuesForRecyclingProgram(res[i]['Does your school participate in any of the following Recycling Programs/Activities? (Check all that apply)'],RECYCLING_PROGRAMS[0]),
                "section1_recycling_program_phones_batteries_other":getValuesForRecyclingProgram(res[i]['Does your school participate in any of the following Recycling Programs/Activities? (Check all that apply)'],RECYCLING_PROGRAMS[1]),
                "section1_recycling_program_terra_cycling":getValuesForRecyclingProgram(res[i]['Does your school participate in any of the following Recycling Programs/Activities? (Check all that apply)'],RECYCLING_PROGRAMS[2]),
                "section1_recycling_program_color_cycle_crayola":getValuesForRecyclingProgram(res[i]['Does your school participate in any of the following Recycling Programs/Activities? (Check all that apply)'],RECYCLING_PROGRAMS[3]),
                "section1_recycling_program_pepsi_recycle_rally":getValuesForRecyclingProgram(res[i]['Does your school participate in any of the following Recycling Programs/Activities? (Check all that apply)'],RECYCLING_PROGRAMS[4]),
                "section1_recycling_program_none_programs_activities":getValuesForRecyclingProgram(res[i]['Does your school participate in any of the following Recycling Programs/Activities? (Check all that apply)'],RECYCLING_PROGRAMS[5]),
                "section1_recycling_program_dont_know":getValuesForRecyclingProgram(res[i]['Does your school participate in any of the following Recycling Programs/Activities? (Check all that apply)'],RECYCLING_PROGRAMS[6]),
                "section1_composting_we_did_not_compost_at_our_school":getValuesForComposting(res[i]['What type of composting is implemented at your school? '],COMPOSTING[0]),
                "section1_composting_vermiculture":getValuesForComposting(res[i]['What type of composting is implemented at your school? '],COMPOSTING[1]),
                "section1_composting_drum_compost":getValuesForComposting(res[i]['What type of composting is implemented at your school? '],COMPOSTING[2]),
                "section1_composting_open_frame":getValuesForComposting(res[i]['What type of composting is implemented at your school? '],COMPOSTING[3]),
                "section1_composting_send_compost_local_facility_farm":getValuesForComposting(res[i]['What type of composting is implemented at your school? '],COMPOSTING[4]),
                "section1_composting_dont_know":getValuesForComposting(res[i]['What type of composting is implemented at your school? '],COMPOSTING[5]),
                "section1_cleanup_volunteer_effort":res[i]['Does your school participate in environmental cleanup volunteer efforts?'],
                "section1_waste_reduction_comments":res[i]['Waste Reduction:  Other and Comments, also please explain if your school participates in other waste reduction efforts. '],
                "section2_reducing_water_strategy":res[i]['Are strategies implemented to reduce water use in your school? '],
                "section2_stream":res[i]['Do you have a stream located on your school grounds? '],
                "section2_water_prevention_stream_bank_planting":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Stream Bank Planting (Riparian Buffer)]'],
                "section2_water_prevention_erosion_control_project":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Erosion Control Project other than Stream Bank Planting]'],
                "section2_water_prevention_painted_storm_drains":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Painted Storm Drains]'],
                "section2_water_prevention_raingarden_bioretention_area_planted":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Raingarden/bioretention area planted]'],
                "section2_water_prevention_no_mow_zone":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [No-mow zone installed ]'],
                "section2_water_prevention_rain_barrels":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Rain barrels installed]'],
                "section2_water_prevention_stream_cleaning":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Stream Cleaning (at your school or in the community)]'],
                "section2_water_prevention_collected_litter":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Collected litter to prevent water pollution]'],
                "section2_water_prevention_turf_eduction":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Turf Eduction]'],
                "section2_water_prevention_surface_reduction":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Impervious surface reduction]'],
                "section2_water_prevention_green_roof":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Green Roof]'],
                "section2_water_prevention_retrofitted_sink_toilet_showers":res[i]['Has your school completed any of the following Water Conservation/Water Pollution Prevention actions? Please provide an answer in each row.  [Retrofitted sinks, toilets, showers]'],
                "section2_runoff_strategy":res[i]['Does your school implement strategies to reduce or improve runoff from the school grounds?'],
                "section2_water_conservation_comments":res[i]['Water Conservation:  Other and Comments, also please indicate if storm water management has been done or is taking place at your school on what has been/is being done.'],
                "section3_reduce_energy_strategy":res[i]['Does your school implement strategies to reduce energy use?'],
                "section3_energy_conservation_installed_efficient_lighting":res[i]['Has your school completed the following Energy Conservation actions? Please provide an answer in each row.  [Installed efficient lighting]'],
                "section3_energy_conservation_use_daylighting":res[i]['Has your school completed the following Energy Conservation actions? Please provide an answer in each row.  [Use Daylighting most of the day]'],
                "section3_energy_conservation_delamped":res[i]['Has your school completed the following Energy Conservation actions? Please provide an answer in each row.  [Delamped]'],
                "section3_energy_conservation_planted_tree_shading":res[i]['Has your school completed the following Energy Conservation actions? Please provide an answer in each row.  [Planted trees to shade building]'],
                "section3_energy_conservation_use_of_blinds":res[i]['Has your school completed the following Energy Conservation actions? Please provide an answer in each row.  [Use of blinds in the classroom to control daylight and temperature]'],
                "section3_renewable_energy":res[i]['Does your school use renewable energy sources?'],
                "section3_renewable_source_solar":res[i]['Please indicate the renewable energy sources that your school uses? Please provide an answer for each row.  [Solar]'],
                "section3_renewable_source_wind":res[i]['Please indicate the renewable energy sources that your school uses? Please provide an answer for each row.  [Wind]'],
                "section3_renewable_source_geothermal":res[i]['Please indicate the renewable energy sources that your school uses? Please provide an answer for each row.  [Geothermal]'],
                "section3_energy_conservation_comments":res[i]['Energy Conservation:  Other and Comments, also please indicate if additional energy conservation practices or renewable energy sources are being implemented at your school. '],
                "section4_restore_habitat":res[i]['Did you restore habitat on your school grounds? '],
                "section4_habitat_restoration_created_bird_houses":res[i]['Please indicate the habitat restoration actions that your school has implemented? Please provide an answer for each row.  [Created/Installed bird houses]'],
                "section4_habitat_restoration_planted_native_trees":res[i]['Please indicate the habitat restoration actions that your school has implemented? Please provide an answer for each row.  [Planted Native Trees]'],
                "section4_habitat_restoration_planted_native_shrubs":res[i]['Please indicate the habitat restoration actions that your school has implemented? Please provide an answer for each row.  [Planted Native Shrubs]'],
                "section4_habitat_restoration_removal_invasive_species":res[i]['Please indicate the habitat restoration actions that your school has implemented? Please provide an answer for each row.  [Removal of invasive species]'],
                "section4_habitat_restoration_created_native_habitat":res[i]['Please indicate the habitat restoration actions that your school has implemented? Please provide an answer for each row.  [Created native habitat - meadows, wetlands or forests]'],
                "section4_habit_restoration_comments":res[i]['Habitat Restoration:  Other and Comments, please describe other habitat restoration efforts at your school or that your school has done in the community. '],
                "section4_enviro_learning_structures":res[i]['Does your school have structures for environmental learning on the school grounds? '],
                "section4_env_learn_struct_interpretive_signage":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Interpretive signage]'],
                "section4_env_learn_struct_trails_pathways":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Trails, pathways]'],
                "section4_env_learn_struct_boardwalk_bridges":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Boardwalk, bridges]'],
                "section4_env_learn_struct_tree_plant_id_tags":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Tree/Plant ID Tags]'],
                "section4_env_learn_struct_outdoor_classroom":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Outdoor Classroom]'],
                "section4_env_learn_struct_outdoor_environmental_art":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Outdoor environmental art]'],
                "section4_env_learn_struct_greenhouse":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Greenhouse]'],
                "section4_env_learn_struct_tower_garden":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Tower garden]'],
                "section4_env_learn_struct_weather_station":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Weather Station]'],
                "section4_env_learn_struct_pond":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Pond]'],
                "section4_env_learn_struct_hydroponics":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Hydroponics ]'],
                "section4_env_learn_struct_aquaponics":res[i]['Please indicate the structures for environmental learning located on your school grounds. Please provide an answer for each row.  [Aquaponics]'],
                "section4_enviro_structure_comments":res[i]['Structures for Environmental Learning:  Other and Comments, please describe other structures for environmental learning located on your school campus. '],
                "section5_no_idle_zone":res[i]['Does your school have a No Idle Zone?'],
                "section5_formal_carpooling":res[i]['Does your school have a formal carpooling program? '],
                "section5_electric_hybrid_parking":res[i]['Does your school have parking spaces designated for electric, hybrid, or energy efficient vehicles? '],
                "section5_grow_donate_eat_garden":res[i]['Does your school grow and donate and/or eat healthy food in school gardens?'],
                "section5_green_cleaning_products":res[i]['Does your school utilize green cleaning products?'],
                "section5_community_science_program":res[i]['Does your school participate in one or more Citizen Science/Community Science programs such as GLOBE, GLOBE Observer, iTree, iNaturalist or other citizen science/ community science protocol to better understand the school environment and how citizen science/community science is used?'],
                "section6_enviro_awards":res[i]['Has your school received any awards or special recognition based on your enviornmental actions or instruction? '],
                "section6_actions_not_mentioned":res[i]['Are there any other environmentally friendly actions your school takes that have not been mentioned in this survey?']
                
              }
    table.put_item(Item=input2)

# for i in range(10):
# q= table.scan(
#         # KeyConditionExpression = Key('pkey').eq(i) & Key('section1_green_school_certification')
#     FilterExpression = Attr('section1_green_school_certification').eq('No')
# )

# res_len =   len(q['Items'])
# for i in range(res_len):
#     # print(q[i])
#     print(q['Items'][i]['pkey'],q['Items'][i]['section1_green_school_certification'])
#     # print(q['Items'][i]['pkey'])




# ,
                # "latitude":res[i][''],
                # "longitude":res[i][''],
                # "picture":res[i][''],
                # "website":res[i]['']