const express = require("express");
const mongoose = require("mongoose");
const Volunteer = require("./models/volunteer.model.js");
const volunteerRoute = require('./routes/volunteer.route.js')
const app = express();

//Middleware
app.use(express.json());

//Routes
app.use("/api/volunteers", volunteerRoute);

//Database connection
mongoose.connect("mongodb+srv://njvinny:fuN3JWwBpvQQxlDg@backenddb.mvdlpjt.mongodb.net/NodeAPI?retryWrites=true&w=majority&appName=BackendDB")
  .then(() => {
    console.log("Connected to database.");
    app.listen(3000, () => console.log("Server is running on port 3000"));
  })
  .catch(() => {
    console.log("Database connection failed.");
  });