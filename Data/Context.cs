using blueprint_backend_challenge.Models;
using Microsoft.EntityFrameworkCore;

namespace blueprint_backend_challenge.Data;

public class Context : DbContext
{
    public Context(DbContextOptions<Context> options) : base(options)
    {
        AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);
    }

    public DbSet<Volunteer> Volunteers { get; set; }
}