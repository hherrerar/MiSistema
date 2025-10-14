BEGIN TRANSACTION;
DROP TABLE IF EXISTS "students";
CREATE TABLE "students" (
	"id"	INTEGER,
	"name"	TEXT,
	"course"	TEXT,
	"mobile"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "students" VALUES (1,'John Smith','Math',49111222333);
INSERT INTO "students" VALUES (2,'Asha Patel','Astronomy',49222333444);
INSERT INTO "students" VALUES (3,'Lokesh Rana','Biology',49333444555);
INSERT INTO "students" VALUES (4,'Andy Johnson','Physics',4811001100);
INSERT INTO "students" VALUES (5,'Kasia Popescu','Astronomy',42001001111);
INSERT INTO "students" VALUES (6,'Paula Zephyr','Astronomy',4901011100);
INSERT INTO "students" VALUES (10,'Jane Crow','Astronomy',123456);
INSERT INTO "students" VALUES (11,'John Deer','Physics',1234);
INSERT INTO "students" VALUES (12,'John Smith','Biology',123);
COMMIT;
