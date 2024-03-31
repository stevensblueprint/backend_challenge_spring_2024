const mongoose = require('mongoose');

const validateEmail = function(email){
    const val = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/; // Corrected regular expression
    return val.test(email);
}

const VolunteerSchema = mongoose.mongoose.Schema(
    {
        first_name: {
            type: String,
            required: [true, 'First name is required']
        },

        last_name: {
            type: String,
            required: [true, 'Last name is required']
        },

        email: {
            type: String,
            trim: true,
            lowercase: true,
            unique: true,
            required: [true, 'Email address is required'],
            validate: [validateEmail, 'Please provide a valid email address']
        },

        phone_number: {
            type: String,
            required: [true, 'Phone number is required']
        },

        date_of_birth: {
            type: Date,
            required: [true, 'Date of birth is required']
        },

        address: {
            type: String,
            required: [true, 'Address is required']
        },

        skills: {
            type: [String],
            required: false,
            default: []
        },

        availability: {
            type: Object,
            required: false,
            default: {
                "Sunday": [],
                "Monday": [],
                "Tuesday": [],
                "Wednesday": [],
                "Thursday": [],
                "Friday": [],
                "Saturday": []
            }
        },
        
        date_joined: {
            type: Date,
            default: () => new Date().toISOString().split('T')[0]
        },

        background_check: {
            type: Boolean,
            required: false,
            default: false
        }
    }
);

const Volunteer = mongoose.model("Volunteer", VolunteerSchema);

module.exports = Volunteer;