// document.addEventListener('DOMContentLoaded', ()=>{
async function schoolNamesDropDown(readAPI){
    const request = await fetch(readAPI)
    const response = await request.json()
    // console.log(response)
    const schoolNames = response.map((item)=>{return item.schoolName})
    // console.log(schoolNames)
    return schoolNames
    
}

function populateDropDown(schoolNames, dropDown){
    
    schoolNames.forEach((item)=>{

        let opt = document.createElement('option')
        opt.value = item
        opt.innerHTML = item

        dropDown.appendChild(opt)
    })

}

async function populateSurvey(event,results){
    console.log(event.target.value)
    const name = event.target.value
    const dropDown_query = 'https://voyn795bv9.execute-api.us-east-1.amazonaws.com/Dev/getDataByColumnName?columnName='
    const request = await fetch(dropDown_query + 'schoolName' + '&value='+name)
    let response = await request.json()
    response = response[0]
    res_arr = Object.entries(response)
    // console.log(Object.entries(response))
    const html = `
    <p> Section 1: School Name - ${response.schoolName}</p><br>
    <p>Section 1: Green School Certification - ${response.section1_green_school_certification}</p>`
    results.innerHTML=html
    // res_arr.forEach((item)=>{
    //     let p = document.createElement('p')
    //     console.log(item)
    //     p.innerHTML=(item[0]+'  '+item[1])
    //     results.appendChild(p)
    // })

}

async function mainThread(){
    
    const readAPI = 'https://voyn795bv9.execute-api.us-east-1.amazonaws.com/Dev/read_all_dynamodb'
    let schoolNames = await schoolNamesDropDown(readAPI)
    let dropDown = document.querySelector('.survey-dropDown')
    let results = document.querySelector('.results')
    const selection = document.addEventListener('change',event =>{
        populateSurvey(event, results)
    })

    populateDropDown(schoolNames, dropDown)
}

window.onload=mainThread
// })
