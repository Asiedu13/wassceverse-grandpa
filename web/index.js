const fs = require("fs");
const sql = require("sqlite3").verbose();

var bodyParser = require("body-parser");

const express = require("express");
const { exit } = require("process");

const app = express();
const db = new sql.Database("../server2.db", (err) => {
  if (err) {
    console.log("Getting Error: ", err);
    exit(1);
  }
} );

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS student_details (  
        surname text not null,
        firstname text not null,
        other_names text

  )`);

  const stmt =
    db.run(`INSERT INTO "student_details" (surname, firstname, other_names) 
    VALUES('Prince', 'John', 'Doe')`);


  db.each("SELECT * FROM student_details", (err, row) => {
    console.log(row.firstname + ": " + row.surname);
  });
});

app.use(bodyParser.json());
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.post("/post", function (req, res, next) {
  console.log(req.body); // req.body contains the parsed body of the request.

  const content = JSON.stringify( req.body );
  console.log(content)
  
  // Adding data to databse goes here...


});

app.listen(8080, () => console.log("listening on localhost 8080"));
