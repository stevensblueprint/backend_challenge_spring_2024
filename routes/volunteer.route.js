const express = require('express');
const Volunteer = require('../models/volunteer.model.js')
const router = express.Router();
const {getAllVolunteers, addVolunteer, getOneVolunteer, updateVolunteer, deleteVolunteer, getSkills, updateSkills, deleteSkill} = require("../controllers/volunteer.controller.js")

router.get("/", getAllVolunteers);
router.post("/", addVolunteer);

router.get("/:volunteerId", getOneVolunteer);
router.put('/:volunteerId', updateVolunteer);
router.delete('/:volunteerId', deleteVolunteer);

router.get('/:volunteerId/skills', getSkills)
router.post('/:volunteerId/skills', updateSkills)
router.delete('/:volunteerId/skills/:skillId', deleteSkill)

module.exports = router;