const fs = require("fs");
// var http = require('http');

// var nStatic = require('node-static');

// var fileServer = new nStatic.Server('./public');

// http.createServer(function (req, res) {
//     fileServer.serve(req, res);

//     if ( req.method == 'POST' ) {
//         console.log(req.body)
//     }

// }).listen(5500);

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

    fs.appendFile("details.json", content, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      //file written successfully
    });

});

app.listen(8080, 'localhost');