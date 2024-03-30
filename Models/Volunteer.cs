using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace blueprint_backend_challenge.Models;

public class Volunteer
{
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    [Key]
    public Guid Id { get; init; }

    [Required]
    [MaxLength(30)]
    [StringLength(30, MinimumLength = 3)]
    public required string FirstName { get; set; }

    [Required]
    [MaxLength(30)]
    [StringLength(30, MinimumLength = 3)]
    public required string LastName { get; set; }

    [Required]
    [EmailAddress]
    [MaxLength(30)]
    [StringLength(30, MinimumLength = 3)]
    public required string Email { get; set; }

    [Required]
    [Phone]
    [MaxLength(15)]
    [StringLength(30, MinimumLength = 10)]
    public required string PhoneNumber { get; set; }

    [Required] public required DateTime DateOfBirth { get; init; }

    [Required] public required string[] Skills { get; set; }
    
    [Required]
    [Column(TypeName = "jsonb")]
    public required string Availability { get; set; }

    [Required] public required DateTime DateJoined { get; init; }

    [Required] public required bool BackgroundCheck { get; set; }
}