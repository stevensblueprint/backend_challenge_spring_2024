const mongoose = require('mongoose');

// The "Class" like in Java, the variables:
const VolunteerSchema = mongoose.Schema(
    {
        name: {
            type: String,
            required: [true, "Please enter a name"],
        },

        ID: {
            type: Number,
            required: true,
            default: 0
        },
    }
);

// Define and export the Volunteer model using mongoose.model
const Volunteer = mongoose.model("Volunteer", VolunteerSchema);
module.exports = Volunteer;