// import express JS module into app and creates its variable. 
import express from 'express';
const app = express();
const port = process.env.PORT || 80;

app.use(express.static('./'))

// Creates a server which runs on port 80 and  
// can be accessed through localhost:80
app.listen(port, () => console.log(`Server app listening on port ${port}!`));
 

