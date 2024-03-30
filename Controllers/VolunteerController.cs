using blueprint_backend_challenge.Data;
using blueprint_backend_challenge.DTOs;
using blueprint_backend_challenge.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace blueprint_backend_challenge.Controllers;

[Route("/api/volunteers")]
[ApiController]
public class VolunteerController(Context context) : ControllerBase
{
    [HttpGet]
    public async Task<IActionResult> GetVolunteers()
    {
        var volunteers = await context.Volunteers.ToListAsync();

        return Ok(volunteers);
    }

    [HttpGet("{id:Guid}")]
    public async Task<IActionResult> GetVolunteer([FromRoute] Guid id)
    {
        var volunteer = await context.Volunteers.FindAsync(id);

        if (volunteer is null) return NotFound();

        return Ok(volunteer);
    }

    [HttpPost]
    public async Task<IActionResult> AddVolunteer([FromBody] CreateVolunteerDTO createVolunteerDTO)
    {
        if (!ModelState.IsValid) return BadRequest(ModelState);

        var volunteer = new Volunteer
        {
            FirstName = createVolunteerDTO.FirstName,
            LastName = createVolunteerDTO.LastName,
            Email = createVolunteerDTO.Email,
            PhoneNumber = createVolunteerDTO.PhoneNumber,
            DateOfBirth = createVolunteerDTO.DateOfBirth,
            Skills = createVolunteerDTO.Skills,
            Availability = createVolunteerDTO.Availability,
            DateJoined = DateTime.Now,
            BackgroundCheck = false
        };

        var newVolunteer = await context.Volunteers.AddAsync(volunteer);
        await context.SaveChangesAsync();

        return Created(nameof(AddVolunteer), newVolunteer.Entity);
    }


    [HttpPut("{id:Guid}")]
    public async Task<IActionResult> UpdateVolunteer(
        [FromRoute] Guid id,
        [FromBody] UpdateVolunteerDTO updateVolunteerDTO)
    {
        if (!ModelState.IsValid) return BadRequest(ModelState);

        var volunteer = await context.Volunteers.FindAsync(id);
        if (volunteer is null) return NotFound();

        volunteer.FirstName = updateVolunteerDTO.FirstName;
        volunteer.LastName = updateVolunteerDTO.LastName;
        volunteer.Email = updateVolunteerDTO.Email;
        volunteer.PhoneNumber = updateVolunteerDTO.PhoneNumber;
        volunteer.Skills = updateVolunteerDTO.Skills;
        volunteer.Availability = updateVolunteerDTO.Availability;

        await context.SaveChangesAsync();

        return NoContent();
    }

    [HttpDelete("{id:Guid}")]
    public async Task<IActionResult> DeleteVolunteer([FromRoute] Guid id)
    {
        var volunteer = await context.Volunteers.FindAsync(id);
        if (volunteer is null) return NotFound();

        context.Volunteers.Remove(volunteer);
        await context.SaveChangesAsync();

        return NoContent();
    }
}