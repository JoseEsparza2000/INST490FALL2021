import gspread
import boto3

gc = gspread.service_account(filename='keys.json')

spread = gc.open_by_key('1w1X00YL2uV_inK-l4VVbGXOXQpW1XoXlqkHFwDcJ-kc')

worksheet = spread.sheet1

res = worksheet.get_all_records()

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('testdb')

KNOWN_SCHOOLS_INFO = [
    ["International High School at Largo", '38.8859', '-76.8234',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Largo%20HS.jpg?n=7335", "https://www.pgcps.org/ihslargo"],
    ["Gwynn Park High School", '38.7016', '-76.8697',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Gwynn%20Park%20HS.jpg", "https://www.pgcps.org/gwynnparkhs/"],
    ["Potomac High School", '38.8212', '-76.9792',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Potomac%20HS.jpg", "https://www.pgcps.org/potomac"],
    ["Woodridge", '38.9507', '-76.8937',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/collage%20(1).png", "https://www.pgcps.org/woodridge/"],
    ["Cherokee Lane ES", '39.0051', '-76.9656',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/IMG_4538.JPG?n=7987", "https://www.pgcps.org/cherokeelane/"],
    ["Suitland HS", '38.8535', '-76.9198',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Suitland%20HS.jpg", "https://www.pgcps.org/suitlandhs/"],
    ["Melwood Elementary School", '38.7907', '-76.8404',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Melwood%20new%20front%20entrance%20pic.jpg", "https://www.pgcps.org/melwood/"],
    ["Paint Branch Elementary", '38.9868', '-76.9285',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Paint%20Branch%20ES.jpg", "https://www.pgcps.org/paintbranch/"],
    ["Langley Park - McCormick ES", '38.9940', '-76.9831',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Langley%20Park.jpg", "https://www.pgcps.org/langleyparkmccormick/"],
    ["Robert R Gray Elementary School", '38.9088', '-76.9247',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Robert%20R%20Gray.jpg", "https://www.pgcps.org/robertrgray/"],
    ["Berwyn Heights ES", '38.9921', '-76.9114',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/berwyn.jpg?n=1766", "https://www.pgcps.org/berwynheights/"],
    ["Oaklands Elementary", '39.0789', '-76.8512',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Oaklands%20ES.jpg", "https://www.pgcps.org/oaklands/"],
    ["Deerfield Run ES",' 39.0711', '-76.8487',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Deerfield%20Run.jpg", "https://www.pgcps.org/deerfieldrun/"],
    ["Highland Park ES", '38.9035', '-76.8960',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Highland%20Park%20ES.jpg", "https://www.pgcps.org/highlandpark/"],
    ["Templeton ES", '38.9525', '-76.9168',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Templeton%20ES.jpg", "https://www.pgcps.org/templeton/"],
    ["Bladensburg HS", '38.942617', '-76.9206946',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Bladensburg%20High.jpg", "https://www.pgcps.org/bladensburghs/"],
    ["Kingsford Elementary School", '38.9086', '-76.7990',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Kingsford%20ES.jpg", "https://www.pgcps.org/kingsford"],
    ["Robert Goddard Montessori", '38.9883', '-76.8447',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Robert%20Goddard%20Montessori.jpg", "https://www.pgcps.org/robertgoddardmontessori/"],
    ["Rose Valley Elementary School", '38.7550', '-76.9620',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Rose%20Valley%20photo.jpg", "https://www.pgcps.org/rosevalley/"],
    ["Bond Mill Elementary", '39.1094', '-76.8974',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/bondmill.jpg", "https://www.pgcps.org/bondmill"],
    ["Patuxent Elementary", '38.8274', '-76.7119',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Patuxent%20ES.jpg", "https://www.pgcps.org/patuxent/"],
    ["University Park Elementary School", '38.9706181', '-76.9456526',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/University%20Park%20ES.jpg", "https://www.pgcps.org/universitypark/"],
    ["Chesapeake Math and IT - South (CMIT-South)", '38.8031642', '-76.8424456',"https://www.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Charter/cmite.jpg?n=7731", "https://www.pgcps.orghttp://www.cmitsouthelementary.org/"],
    ["Ernest E. Just Middle School", '38.9072', '-76.8319',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Middle/Ernest%20Everett%20Just.jpg", "https://www.pgcps.org/ernesteverettjust/"],
    ["Panorama Elementary School", '38.8356', '-76.9720',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Panorama%20ES.jpg", "https://www.pgcps.org/panorama/"],
    ["Greenbelt Elementary", '39.0123162', '-76.8793746',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Greenbelt%20ES.jpg", "https://www.pgcps.org/greenbeltes/"],
    ["High Bridge Elementary", '38.9868884', '-76.7745284',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/High%20Bridge%20ES.jpg", "https://www.pgcps.org/highbridge/"],
    ["Fort Foote Elementary", '38.7758', '-77.0070',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/fortefoote.jpg", "https://www.pgcps.org/fortfoote/"],
    ["Benjamin Foulois CPAA", '38.8269309', '-76.8888203',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Academies/benjamin%20foulois.jpg", "https://www.pgcps.org/benjaminfoulois/"],
    ["Gwynn Park MS", '38.7069', '-76.8709',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Middle_Schools/Gwynn_Park/Rotating_Stories/schoolphoto%202.jpg?n=9313", "https://www.pgcps.org/gwynnparkms/"],
    ["Laurel High School", '39.0942', '-76.8702',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Laurel%20HS.jpg", "https://www.pgcps.org/largo/"],
    ["Kenilworth Elementary", '38.9591', '-76.7368',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Kenilworth%20ES.jpg", "https://www.pgcps.org/kenilworth/"],
    ["Benjamin Tasker MS", '38.9580', '-76.7477',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Middle/Benjamin%20Tasker%20MS.jpg", "https://www.pgcps.org/benjamintasker/"],
    ["Dodge Park Elementary", '38.9335', '-76.8779',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/dodge%20park.jpg", "https://www.pgcps.org/dodgepark/"],
    ["Buck Lodge Middle School", '39.0108', '-76.9617',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Middle/Buck%20Lodge.jpg", "https://www.pgcps.org/bucklodge/"],
    ["Nicholas Orem", '38.9641', '-76.9621',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Middle/Nicholas%20Orem%20MS.jpg", "https://www.pgcps.org/nicholasorem/"],
    ["Marlton Elementary School", '38.7725', '-76.7913',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Marlton%20ES.jpg", "https://www.pgcps.org/marlton/"],
    ["Gladys Noon Spellman Elementary", '38.9308', '-76.9095',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Gladys%20Noon%20Spellman.jpg", "https://www.pgcps.org/gladysnoonspellman/"],
    ["Hollywood Elementary", '39.0151', '-76.9250',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Hollywood%20ES.jpg", "https://www.pgcps.org/hollywood/"],
    ["Stephen Decatur Middle School", '38.7766004', '-76.9106298',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Middle/Stephen%20Decatur%20MS.jpg", "https://www.pgcps.org/stephendecatur/"],
    ["Laurel High School2", '39.0942', '-76.8702',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Laurel%20HS.jpg", "https://www.pgcps.org/largo/"],
    ["Glassmanor Elementary", '38.8171', '-76.9924',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Glassmanor%20ES.jpg", "https://www.pgcps.org/glassmanor/"],
    ["CMIT South Public Charter School", '38.8050457','-76.8409654',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Charter/cmit_ms.png?n=3662", "http://www.cmitsouthelementary.org"],
    ["Thomas Johnson Middle School",  '38.960509', '-76.843261',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Middle/Thomas%20Johnson%20MS.jpg", "https://www.pgcps.org/thomasjohnson/"],
    ["Bond Mill",  '38.960509', '-76.843261',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Middle/Thomas%20Johnson%20MS.jpg", "https://www.pgcps.org/thomasjohnson/"],
    ["Annapolis Road Academy", '38.9192886', '-76.7611796',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/High_Schools/Annapolis_Road/Pictures/IMG_0134.jpg", "https://www.pgcps.org/annapolisroad/"],
    ["Rogers Heights Elementary School", '38.9451163', '-76.9148903',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Rogers%20Heights%20ES.jpg", "https://www.pgcps.org/rogersheights/"],
    ["Whitehall Elementary School", '38.9895601', '-76.7534197',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Whitehall%20ES.jpg", "https://www.pgcps.org/whitehall/"],
    ["Suitland Elementary School", '38.8528125', '-76.9295593',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Suitland%20Picture.jpg", "https://www.pgcps.org/suitlandes/"],
    ["Eleanor Roosevelt High School", '38.9940431', '-76.8716383',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Eleanor%20Roosevelt%20HS.jpg", "https://www.pgcps.org/eleanorroosevelt"],
    ["Dr. Henry A Wise Jr. High School", '38.8337263', '-76.7908283',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Dr.%20Henry%20A.%20Wise%20HS.jpg", "https://www.pgcps.org/drhenrywisejr/"],
    ["Fairmont Heights High School", '38.9177687', '-76.8966939',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/FHHS_7551.JPG", "https://www.pgcps.org/fairmontheights/"],
    ["CENTRAL HS@Forestvill", '38.836129', '-76.8875897',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Central%20HS.jpg", "https://www.pgcps.org/central/"],
    ["Friendly High School", '38.7519549', '-76.9706354',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Friendly%20HS.jpg", "https://www.pgcps.org/friendly/"],
    ["Magnolia ES", '38.9838055', '-76.8642313',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/Magnolia%20ES.jpg", "https://www.pgcps.org/magnolia/"],
    ["Parkdale High School", '38.9696933', '-76.9068296',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/parkdale.jpg", "https://www.pgcps.org/parkdale/"],
    ["Gwynn Park High School2", '38.7016', '-76.8697',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Gwynn%20Park%20HS.jpg", "https://www.pgcps.org/gwynnparkhs/"],
    ["Laurel High School3", '39.0942', '-76.8702',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Laurel%20HS.jpg", "https://www.pgcps.org/largo/"],
    ["Frederick Douglass High School", '38.7815367', '-76.7838189',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/douglass.jpg", "https://www.pgcps.org/douglass/"],
    ["Northwestern HS", '38.9752874', '-76.9562757',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Northwestern%20HS(1).jpg", "https://www.pgcps.org/northwestern"],
    ["Dora Kennedy French Immersion", '38.9975238', '-76.9046507',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Academies/dkfi-sign_1_orig.jpg", "https://www.pgcps.org/dorakennedy/"],
    ["Andrew Jackson Academy", '38.8404724', '-76.9106414',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Academies/New%20AJA%20Building%20pic1.png", "https://www.pgcps.org/andrewjackson/"],
    ["Eleanor Roosevelt High School2", '38.9940431', '-76.8716383',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Eleanor%20Roosevelt%20HS.jpg", "https://www.pgcps.org/eleanorroosevelt"],
    ["Concord ES", '38.8629843', '-76.9101987',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/Elementary/concord.jpg", "https://www.pgcps.org/concord/"],
    ["Charles Herbert Flowers High School", '38.9315768', '-76.8373013',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Splash_Pages/High/Charles%20H.%20Flowers.jpg", "https://www.pgcps.org/charleshflowers/"],
    ["Cool Spring ES", '39.0021151','-76.9759007',"https://schools.pgcps.org/uploadedImages/Schools_and_Centers/Elementary_Schools/Cool_Spring/b56a4bc68bac4e11941c2644f0c71d61.jpg", "https://www.pgcps.org/coolspring/"]
]
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

# position = 0
for index in range(len(res)):

    valueList = list(res[index].values())


    
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
            'latitude' : KNOWN_SCHOOLS_INFO[index][1],
            'longitude' : KNOWN_SCHOOLS_INFO[index][2],
            'picture' : KNOWN_SCHOOLS_INFO[index][3],
            'website' : KNOWN_SCHOOLS_INFO[index][4]
        }
    )

    


    