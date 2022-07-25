// ----------------- Variables and Objects --------------
const fs = require( "fs" );
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
});

// --------------- Middleware --------------------

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS student_details (  
        surname text not null,
        first_name text not null,
        other_names text,
        course array not null,
        class text,
        index_number text primary key not null,
        year_completed text not null,
        electives array not null,
        school text not null,
        gender array not null,
        parent_contact text not null,
        date_of_birth text,
        signature blob,
        image blob,
        fingerprint blob
  )`);
});

app.use(bodyParser.json());
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));


// --------- Server Requests ---------------
app.post( "/api/student/create", function ( req, res, next ) {
  
  // Adding data to databse goes here...

  console.log(req.body); // req.body contains the parsed body of the request.

  let content = req.body;

  let sql = "INSERT INTO student_details (surname,first_name, other_names,course, class, index_number, year_completed, electives, school, gender, parent_contact, date_of_birth, signature, 'image', fingerprint ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";

  db.run(
    sql,
    [
      content.surname,
      content.first_name,
      content.other_names,
      content.course,
      content.class,
      content.index_number,
      content.year_completed,
      content.electives,
      content.school,
      content.gender,
      content.parent_contact,
      content.date_of_birth,
      content.signature,
      content.image,
      content.fingerprint,
    ],
    (err) => {
      if (err) console.error(err.message);
    }
  );

  // End Request
  res.send("Data received");
} );

app.get( '/api/schools', ( req, res ) => {
  res.send( "The data is being sent to the client" );
})

app.listen(8080, () => console.log("listening on localhost 8080"));
