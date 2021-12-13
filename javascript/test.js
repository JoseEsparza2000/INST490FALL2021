async function displayMarkersByFeature() {
    let feature = 'section1_green_school_certification'
    const dropDown_query = 'https://voyn795bv9.execute-api.us-east-1.amazonaws.com/Dev/getDataByColumnName?columnName='
    const request = await fetch(dropDown_query + feature + "&value=Yes")   
    let response = await request.json()

    console.log(response)
}