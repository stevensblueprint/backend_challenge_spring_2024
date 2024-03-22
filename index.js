const express = require("express");
const app = express();

app.get("/api/volunteers", (req, res) => {
  res.send("Implement");
});

app.post("/api/volunteers", (req, res) => {
  res.send("Implement");
});

app.get("/api/volunteers/:volunteerId", (req, res) => {
  res.send("Implement");
});

app.put("/api/volunteers/:volunteerId", (req, res) => {
  res.send("Implement");
});

app.delete("/api/volunteers/:volunteerId", (req, res) => {
  res.send("Implement");
});

app.get("/api/volunteers/:volunteerId/skills", (req, res) => {
  res.send("Implement");
});

app.post("/api/volunteers/:volunteerId/skills", (req, res) => {
  res.send("Implement");
});

app.delete("/api/volunteers/:volunteerId/skills/:skillId", (req, res) => {
  res.send("Implement");
});

app.get("/api/volunteers/:volunteerId/events", (req, res) => {
  res.send("Implement");
});

app.post("/api/events/{eventId}/volunteers/:volunteerId", (req, res) => {
  res.send("Implement");
});

app.delete("/api/events/{eventId}/volunteers/:volunteerId", (req, res) => {
  res.send("Implement");
});

app.listen(3000, () => console.log("Server is running on port 3000"));
