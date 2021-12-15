<p>Title of Project: PGCPS Environmental and Outdoor Learning Map and Database Update</p>
<p>Description of Project: Update of a map visualization depicting completion of environmental activities across PGCPS and hosting it on AWS.</p>
<p>Link to App: http://pgcpshost.s3-website-us-east-1.amazonaws.com</p>
<p>Target Browsers: Google Chrome, Mozilla Firefox, Safari, Microsoft Edge</p>
<p>Link to Website Training Slides: https://docs.google.com/presentation/d/1OQ-8fBUHc2Ix9d-vUoNaXNLmy-5ytW6aA5e7cpvRRtM/edit?usp=sharing</p><br/>

# Developer Manual
<h1>Libraries, Frameworks and SDKs Used</h1>
  <ol>
    <li>Bulma (CSS Framework)</li>
    <li>Express (JavaScript Framework)</li>
    <li>Leaflet (JavaScript Library)</li>
    <li>boto3 (Python SDK) </li>
    <li>gspread (Python Library) </li>
  </ol>
<h1>How to run application on a local server </h1>
  <ol>
    <li>Execute 'npm install' command in a terminal inside the appropriate directory</li>
    <li>Execute 'npm start' command next in the same terminal</li>
    <li>Open browser and connect to the local host</li>
    <li>http://localhost/index.html</li>
  </ol>
<h1>How to run tests </h1>
  <ol>
    <li>Click through the various drop down menus and markers should appear on the visualization.</li>
  </ol>
<h1>The AWS API Gateway Endpoints for the database access </h1>  
  <ol>
    <li>Getting all data from database</li>
      <ul> `https://voyn795bv9.execute-api.us-east-1.amazonaws.com/Dev/read_all_database` </ul>
    <li>To update database with all data from Google surveys</li>
      <ul> `https://voyn795bv9.execute-api.us-east-1.amazonaws.com/Dev/update_database` </ul>
    <li>Getting data based on columns name and value, used for querying based on activities or section</li>
      <ul> `https://voyn795bv9.execute-api.us-east-1.amazonaws.com/Dev/getdatabycolumnname?columnName=<activity_name>` </ul>
  </ol>
