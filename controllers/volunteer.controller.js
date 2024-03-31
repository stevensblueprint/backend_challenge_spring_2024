const Volunteer = require("../models/volunteer.model.js");


//Get all volunteers
const getAllVolunteers = async (req, res) => {
    try {
      const volunteers = await Volunteer.find({});
      res.status(200).json(volunteers)
    } catch (error) {
      res.status(500).json({ message: error.mesage });
    }
  };

  //Add new volunteer
  const addVolunteer = async (req, res) => {
    try {
      const volunteer = await Volunteer.create(req.body);
      res.status(200).json(volunteer);
    }
    catch (error) {
      res.status(500).json({ mesage: error.message });
    }
  };

  //Get one volunteer by ID
  const getOneVolunteer = async (req, res) => {
    try {
      res.status(200).json(await Volunteer.findById(req.params.volunteerId));
    } catch (error) {
      res.status(500).json({ message: error.mesage });
    }
  };

  //Update a volunteer by ID
  const updateVolunteer = async (req, res) => {
    try {
      const volunteer = await Volunteer.findByIdAndUpdate(req.params.volunteerId, req.body);
  
      if (!volunteer) {
        return res.status(404).json({ message: "Volunteer not found" });
      }
  
      res.status(200).json(await Volunteer.findById(req.params.volunteerId));
  
    } catch (error) {
      res.status(500).json({ message: error.mesage });
    }
  };

  //Delete a volunteer by ID
  const deleteVolunteer = async (req, res) => {
    try {
      const volunteer = await Volunteer.findByIdAndDelete(req.params.volunteerId);
  
      if(!volunteer) {
        return res.status(404).json({message: "Volunteer not found."});
      }
  
      res.status(200).json({message: "Volunteer deleted successfully."})
    } catch (error) {
      res.status(500).json({message: error.message}); 
    }
  };

  //Get volunteer's skills by ID
  const getSkills = async (req, res) => {
    try {
      res.status(200).json((await Volunteer.findById(req.params.volunteerId)).skills);
    } catch (error) {
      res.status(500).json({ message: error.mesage });
    }
  };

  //Update a volunteer's skills by ID
  const updateSkills = async (req, res) => {
    try {
      const updatedVolunteer = await Volunteer.findByIdAndUpdate(req.params.volunteerId,{$push: {skills: {$each: req.body.skills}}},{new: true});
  
      if (!updatedVolunteer) {
        return res.status(404).json({ message: "Volunteer not found" });
      }
  
      res.status(200).json(updatedVolunteer);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };

  //Delete a specific skill from a volunteer by their ID
  const deleteSkill = async (req, res) => {
    try {
      const updatedVolunteer = await Volunteer.findByIdAndUpdate(req.params.volunteerId,{$pull: {skills: req.params.skillId}},{new: true});
  
      if (!updatedVolunteer) {
        return res.status(404).json({ message: "Volunteer not found" });
      }
  
      res.status(200).json(updatedVolunteer);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };

  //Export all modules
  module.exports = {
    getAllVolunteers,
    addVolunteer,
    getOneVolunteer,
    updateVolunteer,
    deleteVolunteer,
    getSkills,
    updateSkills,
    deleteSkill
  };