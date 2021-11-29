import gspread
import boto3

gc = gspread.service_account(filename='keys.json')

spread = gc.open_by_key('1w1X00YL2uV_inK-l4VVbGXOXQpW1XoXlqkHFwDcJ-kc')

worksheet = spread.sheet1

res = worksheet.get_all_records()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('testdb')

# index = 0
for index in range(len(res)):

    valueList = list(res[index].values())

    activeGardens = ["Vegetable garden", "Native garden", "Butterfly garden", "Rain garden", 
    "Zen garden", "Herb garden"]
    noGardens = ["No gardens on campus", "I don't know."]

    recycle = ['At breakfast', 'At lunch', 'In the classroom']
    noRecycle = ['Not at all', "I don't know."]

    recyclingPrograms = ["Ink Cartridge Recycling", "Cell Phones, Batteries and Other Electronics", 
    "Terra Cycling", "Color Cycle (Crayola)", "Pepsi Recycle Rally"]
    noPrograms = ["None of these Programs/Activities", "I don't know."]

    composting = ["Vermiculture", "Drum compost", "Open frame", "Send Compost to Local Composting Facility/Farm"]
    noComposting = ["We did not compost at our school", "I don't know."]

    table.put_item(
        Item={
            "pkey":index+1,
            'schoolName' : valueList[2],
            'Timestamp' : valueList[0],
            'Email Address': valueList[1],
            'section1_green_school_certification' : valueList[3],
            'section1_active_garden_vegetable_garden' : 'Yes' if valueList[4] in activeGardens else 'No',
            'section1_active_garden_native_garden' : 'Yes' if valueList[4] in activeGardens else 'No',
            'section1_active_garden_butterfly_garden' : 'Yes' if valueList[4] in activeGardens else 'No',
            'section1_active_garden_rain_garden' : 'Yes' if valueList[4] in activeGardens else 'No',
            'section1_active_garden_zen_garden' : 'Yes' if valueList[4] in activeGardens else 'No',
            'section1_active_garden_herb_garden' : 'Yes' if valueList[4] in activeGardens else 'No',
            'section1_active_garden_no_gardens_on_campus' : 'Yes' if valueList[4] in noGardens else 'No',
            'section1_active_garden_dont_know' : 'Yes' if valueList[4] in noGardens else 'No',
            'section1_recycle_at_breakfast' : 'Yes' if valueList[5] in recycle else 'No',
            'section1_recycle_at_lunch' : 'Yes' if valueList[5] in recycle else 'No',
            'section1_recycle_in_the_classroom' : 'Yes' if valueList[5] in recycle else 'No',
            'section1_recycle_not_at_all' : 'Yes' if valueList[5] in noRecycle else 'No',
            'section1_recycle_dont_know' : 'Yes' if valueList[5] in noRecycle else 'No',
            'section1_recycling_program_ink_cartridge_recycling' : 'Yes' if valueList[6] in recyclingPrograms else 'No',
            'section1_recycling_program_phones_batteries_other' : 'Yes' if valueList[6] in recyclingPrograms else 'No',
            'section1_recycling_program_terra_cycling' : 'Yes' if valueList[6] in recyclingPrograms else 'No',
            'section1_recycling_program_color_cycle_crayola' : 'Yes' if valueList[6] in recyclingPrograms else 'No',
            'section1_recycling_program_pepsi_recycle_rally' : 'Yes' if valueList[6] in recyclingPrograms else 'No',
            'section1_recycling_program_none_programs_activities' : 'Yes' if valueList[6] in noPrograms else 'No',
            'section1_recycling_program_dont_know' : 'Yes' if valueList[6] in noPrograms else 'No',
            'section1_composting_we_did_not_compost_at_our_school' : 'Yes' if valueList[7] in noComposting else 'No',
            'section1_composting_vermiculture' : 'Yes' if valueList[7] in composting else 'No',
            'section1_composting_drum_compost' : 'Yes' if valueList[7] in composting else 'No',
            'section1_composting_open_frame' : 'Yes' if valueList[7] in composting else 'No',
            'section1_composting_send_compost_local_facility_farm' : 'Yes' if valueList[7] in composting else 'No',
            'section1_composting_dont_know' : 'Yes' if valueList[7] in noComposting else 'No',
            'section1_cleanup_volunteer_effort' : valueList[8],
            'section1_waste_reduction_comments' : valueList[9],
            'section2_reducing_water_strategy' : valueList[10],
            'section2_stream' : valueList[11],
            'section2_water_prevention_stream_bank_planting' : valueList[12],
            'section2_water_prevention_erosion_control_project' : valueList[13],
            'section2_water_prevention_painted_storm_drains' : valueList[14],
            'section2_water_prevention_raingarden_bioretention_area_planted' : valueList[15],
            'section2_water_prevention_no_mow_zone' : valueList[16],
            'section2_water_prevention_rain_barrels' : valueList[17],
            'section2_water_prevention_stream_cleaning' : valueList[18],
            'section2_water_prevention_collected_litter' : valueList[19],
            'section2_water_prevention_turf_eduction' : valueList[20],
            'section2_water_prevention_surface_reduction' : valueList[21],
            'section2_water_prevention_green_roof' : valueList[22],
            'section2_water_prevention_retrofitted_sink_toilet_showers' : valueList[23],
            'section2_runoff_strategy' : valueList[24],
            'section2_water_conservation_comments' : valueList[25],
            'section3_reduce_energy_strategy': valueList[26],
            'section3_energy_conservation_installed_efficient_lighting' : valueList[27],
            'section3_energy_conservation_use_daylighting' : valueList[28],
            'section3_energy_conservation_delamped' : valueList[29],
            'section3_energy_conservation_planted_tree_shading' : valueList[30],
            'section3_energy_conservation_use_of_blinds' : valueList[31],
            'section3_renewable_energy' : valueList[32],
            'section3_renewable_source_solar' : valueList[33],
            'section3_renewable_source_wind' : valueList[34],
            'section3_renewable_source_geothermal' : valueList[35],
            'section3_energy_conservation_comments' : valueList[36],
            'section4_restore_habitat' : valueList[37],
            'section4_habitat_restoration_created_bird_houses' : valueList[38],
            'section4_habitat_restoration_planted_native_trees' : valueList[39],
            'section4_habitat_restoration_planted_native_shrubs' : valueList[40],
            'section4_habitat_restoration_removal_invasive_species' : valueList[41],
            'section4_habitat_restoration_created_native_habitat' : valueList[42],
            'section4_habit_restoration_comments' : valueList[43],
            'section4_enviro_learning_structures' : valueList[44],
            'section4_env_learn_struct_interpretive_signage' : valueList[45],
            'section4_env_learn_struct_trails_pathways' : valueList[46],
            'section4_env_learn_struct_boardwalk_bridges' : valueList[47],
            'section4_env_learn_struct_tree_plant_id_tags' : valueList[48],
            'section4_env_learn_struct_outdoor_classroom' : valueList[49],
            'section4_env_learn_struct_outdoor_environmental_art' : valueList[50],
            'section4_env_learn_struct_greenhouse' : valueList[51],
            'section4_env_learn_struct_tower_garden' : valueList[52],
            'section4_env_learn_struct_weather_station' : valueList[53],
            'section4_env_learn_struct_pond' : valueList[54],
            'section4_env_learn_struct_hydroponics' : valueList[55],
            'section4_env_learn_struct_aquaponics' : valueList[56],
            'section4_enviro_structure_comments' : valueList[57],
            'section5_no_idle_zone' : valueList[58],
            'section5_formal_carpooling' : valueList[59], 
            'section5_electric_hybrid_parking' : valueList[60],
            'section5_grow_donate_eat_garden' : valueList[61],
            'section5_green_cleaning_products' : valueList[62],
            'section5_community_science_program' : valueList[63],
            'section6_enviro_awards' : valueList[64],
            'section6_actions_not_mentioned' : valueList[65],
        }
    )




    