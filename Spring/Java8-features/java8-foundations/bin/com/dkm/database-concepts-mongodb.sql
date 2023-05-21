-- MongoDB (document based)
-- don't use spring data jpa as dependency while using mongodb

-- start mongodb (install & see path variable -> env-> path-> new-> paste your path -> ok->ok)
-- sudo service mongod start
-- sudo service mongod status
-- mongo

-- to stop database => sudo service mongod stop









-- NoSQL (data is distributed)
-- -> Unstructured data format(document based data)
-- -> data will be in form of key-value pair


-- Feature of NoSQL
-- Non relational
-- schema Featuredistributed
-- response time is less
-- performance is high







-- to create a database (to create and use)
use databasename

-- to see the current database name
db

-- to view all the databases
show dbs;

-- collection:- is a set of rows of data(table)
-- to view all the collections created in a database
show collections


-- to insert  a row in the collection
db.emp.insert({
    regNo: "3014",
    name: "deepak"
});

-- to view the data from the collection
db.emp.find();

-- to display data in neet form
db.emp.find().pretty();


-- to insert a single record
db.emp.insertOne({
    regNo: "3014",
    name: "deepak"
});

-- to insert multiple records
db.emp.insertMany([
    {
        regNo: "3014",
    name: "deepak"
    },
    {
        regNo: "304514",
    name: "deepak5"
    }
]);

-- to delete rows
db.emp.remove({"regNo": "3014"});


-- to update row
db.emp.update({
    "regNo": "3014"
}, {$set: {"name": "dkmandal"}});




-- to drop a collection
db.emp.drop();



-- * spring boot application linked with mongodb ----> Microservice
