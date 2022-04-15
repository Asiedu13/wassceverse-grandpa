const fs = require("fs");

var bodyParser = require('body-parser');

const express = require('express');

const app = express();

// Parses the body for POST, PUT, DELETE, etc.
app.use(bodyParser.json());
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/post', function(req, res, next){

    console.log( req.body ); // req.body contains the parsed body of the request.
    

    const content =JSON.stringify(req.body)

    fs.appendFile("details.txt", content, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      //file written successfully
    });

});

app.listen(8080, 'localhost', ()=> console.log('Running on port 8080'));