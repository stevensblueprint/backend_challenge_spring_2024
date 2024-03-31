const Volunteer = require("../models/volunteer.model.js");

const getAllVolunteers = async (req, res) => {
    try {
      const volunteers = await Volunteer.find({});
      res.status(200).json(volunteers)
    } catch (error) {
      res.status(500).json({ message: error.mesage });
    }
  };

  const addVolunteer = async (req, res) => {
    try {
      const volunteer = await Volunteer.create(req.body);
      res.status(200).json(volunteer);
    }
    catch (error) {
      res.status(500).json({ mesage: error.message });
    }
  };

  const getOneVolunteer = async (req, res) => {
    try {
      res.status(200).json(await Volunteer.findById(req.params.volunteerId));
    } catch (error) {
      res.status(500).json({ message: error.mesage });
    }
  };

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

  const getSkills = async (req, res) => {
    try {
      res.status(200).json((await Volunteer.findById(req.params.volunteerId)).skills);
    } catch (error) {
      res.status(500).json({ message: error.mesage });
    }
  };

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