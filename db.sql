BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "registered_schools" (
	"id"	INTEGER UNIQUE,
	"school_name"	TEXT NOT NULL DEFAULT '',
	"location"	TEXT NOT NULL DEFAULT '',
	"country"	TEXT NOT NULL DEFAULT '',
	"school_code"	INTEGER NOT NULL UNIQUE,
	"school_logo"	BLOB,
	"school_email"	TEXT DEFAULT '',
	"password"	TEXT DEFAULT '',
	"verified"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "registered_students" (
	"id"	INTEGER NOT NULL,
	"surname"	text NOT NULL DEFAULT '',
	"first_name"	text NOT NULL DEFAULT '',
	"other_names"	text DEFAULT '',
	"course"	array NOT NULL,
	"class"	text DEFAULT '',
	"index_number"	text NOT NULL DEFAULT '' UNIQUE,
	"year_completed"	text NOT NULL DEFAULT '',
	"electives"	array NOT NULL,
	"school"	text NOT NULL DEFAULT '',
	"gender"	array NOT NULL,
	"parent_contact"	text NOT NULL DEFAULT '',
	"date_of_birth"	text DEFAULT '01/01/01',
	"signature"	blob,
	"image"	blob,
	"fingerprint"	blob,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "student_details" (
	"id"	INTEGER NOT NULL,
	"surname"	text NOT NULL DEFAULT '',
	"first_name"	text NOT NULL DEFAULT '',
	"other_names"	text DEFAULT '',
	"course"	array NOT NULL,
	"class"	text DEFAULT '',
	"index_number"	text NOT NULL DEFAULT '' UNIQUE,
	"year_completed"	text NOT NULL DEFAULT '',
	"electives"	array NOT NULL,
	"school"	text NOT NULL DEFAULT '',
	"gender"	array NOT NULL,
	"parent_contact"	text NOT NULL DEFAULT '',
	"date_of_birth"	text DEFAULT '01/01/01',
	"signature"	blob,
	"image"	blob,
	"fingerprint"	blob,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "registered_schools" ("id","school_name","location","country","school_code","school_logo","school_email","password","verified") VALUES (1,'Presbyterian Boys'' Secondary School','Legon, Accra','Ghana',1,NULL,'presbyterianboys@gmail.com','admin',0),
 (2,'Achimota School','Achimota','Ghana',2,NULL,'achimota@gmail.com',NULL,0),
 (3,'Wesley Girls High School','Cape Coast','Ghana',3,NULL,'wesleygirls@gmail.com',NULL,0),
 (4,'Prempeh College','Kumasi','Ghana',4,NULL,'prempeh@gmail.com','hello',0),
 (5,'Holy Child','Cape Coast','Ghana',5,NULL,'holychild@gmail.com',NULL,0),
 (6,'Robo.School','nowhere','Ghana',14,NULL,'school@robo.com','admin.admin',1);
INSERT INTO "registered_students" ("id","surname","first_name","other_names","course","class","index_number","year_completed","electives","school","gender","parent_contact","date_of_birth","signature","image","fingerprint") VALUES (1,'Engelberg','Davis','Kory','General Science','3 Science 15','0111010038','2020','Physics, Chemistry, Biology','Presbyterian Boy''s Secondary Schoool','Male','0344279809','30/05/2003','',' ',' '),
 (2,'Asiedu','Prince','Kofi','General Science','3 Science 5','019399209023','2019','E-Math,Physics,Chemistry,E-ICT','Presbyterian Boys'' Secondary School','male','+233244276809','27/02/2004',NULL,NULL,NULL);
INSERT INTO "student_details" ("id","surname","first_name","other_names","course","class","index_number","year_completed","electives","school","gender","parent_contact","date_of_birth","signature","image","fingerprint") VALUES (1,'Debrah','Derrick','Kofi','General Science','3 Science 1','0111010038','2019','E-Math,Physics,Chemistry,Biology','Presbyterian Boys'' Secondary School','Male','+233244276809','21/02/2004',NULL,NULL,NULL),
 (3,'Allan','Barry','Speed Force','General Science','3 Science 21','00123456789','2019','Chemistry,Biology,Business Management,Financial Accounting','Presbyterian Boys'' Secondary School','Male','+233244276809','12/08/2003',NULL,NULL,NULL),
 (5,'Asem','Flex','','General Science','3 Business 6','0102050002','2019','Business Management,Elective Mathematics,Economics,Financial Accounting','Presbyterian Boys'' Secondary School','Male','+233244789653','01/01/01',NULL,NULL,NULL),
 (6,'Biden','Joe','','General Science','3 Science 6','0020011023','','Biology,Chemistry,Elective ICT,Elective Mathematics','Presbyterian Boys'' Secondary School','Male','+1 344-7683','01/01/01',NULL,NULL,NULL),
 (7,'Doe','John','Kofi','Business','','','','Business Management,Principles of Costing,Elective Mathematics,Financial Accounting','Presbyterian Boys'' Secondary School','Male','+233 (0) 65435674','01/01/01',NULL,NULL,NULL);
COMMIT;
