using System.ComponentModel.DataAnnotations;

namespace blueprint_backend_challenge.DTOs;

public class UpdateVolunteerDTO
{
    [Required]
    [StringLength(30, MinimumLength = 3)]
    public required string FirstName { get; set; }

    [Required]
    [StringLength(30, MinimumLength = 3)]
    public required string LastName { get; set; }

    [Required]
    [EmailAddress]
    [StringLength(30, MinimumLength = 3)]
    public required string Email { get; set; }

    [Required]
    [Phone]
    [StringLength(30, MinimumLength = 10)]
    public required string PhoneNumber { get; set; }

    [Required] public required string[] Skills { get; set; }

    [Required] public required string Availability { get; set; }
}