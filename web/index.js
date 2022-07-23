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
});

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS student_details (  
        surname text not null,
        first_name text not null,
        other_names text,
        course text not null,
        class text not null,
        index_number text primary key not null,
        year_completed text not null,
        electives text not null,
        school text not null,
        gender text not null,
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

app.post("/post", function (req, res, next) {
  // Posting data to the database
  console.log(req.body); // req.body contains the parsed body of the request.

  let content = req.body;
  // parsed = JSON.parse(content)

  // Adding data to databse goes here...
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
});

app.listen(8080, () => console.log("listening on localhost 8080"));
