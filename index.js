const express = require('express')
const mongoose = require('mongoose');
const Volunteer = require('./volunteer.model.js');
const app = express()


app.use(express.json());
app.use(express.urlencoded({extended: false}));


app.get('/', (req, res) => {
    res.send("Hello from Node API");
});

//POST VOLUNTEER
app.post('/api/volunteers', async (req, res) => {
    try {
        const volunteer = await Volunteer.create(req.body);
        res.status(200).json(volunteer);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

//GET VOLUNTEER
app.get('/api/volunteers', async (req, res) => {

    try {
        const volunteers = await Volunteer.find({});
        res.status(200).json(volunteers);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }

});

//GET ID
app.get('/api/volunteer/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const volunteer = await Volunteer.findById(id);
        res.status(200).json(volunteer);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

//UPDATE VOLUNTEER (ID)
app.put('/api/volunteer/:id', async (req, res) => {
    try {
        const { id } = req.params;

        const volunteer = await Volunteer.findByIdAndUpdate(id, req.body);

        if (!volunteer) {
            return res.status(404).json({ message: "Volunteer not found" });
        }

        const updatedVolunteer = await Volunteer.findById(id);
        res.status(200).json(updatedVolunteer);

    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// DELETE Volunteer
app.delete("/api/volunteer/:id", async (req, res) => {
    try {
        const { id } = req.params;

        const volunteer = await Volunteer.findByIdAndDelete(id);

        if (!volunteer) {
            return res.status(404).json({ message: "Volunteer not found" });
        }

        res.status(200).json({ message: "Volunteer deleted successfully" });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});


//Web
app.listen(3000, () => {
    console.log('Server is running on port 3000')
});

mongoose.connect("mongodb+srv://ayushmisra71:Omshanti%4005@backenddb.cdivndj.mongodb.net/backendDB?retryWrites=true&w=majority&appName=BackendDB")
    .then(() => {
        console.log("Connected to database!");
    })
    .catch((error) => {
        console.log("Connection failed!", error);

    })


