using System;
using Microsoft.EntityFrameworkCore;

namespace TranslationApp
{
    // Model class for English table
    public class English
    {
        public int Id { get; set; }
        public string Word { get; set; }
        public int LineNumber { get; set; }
        public bool Translatable { get; set; }
    }

    // DbContext class for database operations
    public class TranslationContext : DbContext
    {
        public DbSet<English> English { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            string connectionString = "Data Source=DESKTOP-9FBPMP7\\SQLEXPRESS;Initial Catalog=Translate;Integrated Security=True;Pooling=False;Encrypt=False";

            optionsBuilder.UseSqlServer(connectionString);
        }
    }

    // Main program class for execution
    class Program
    {
        static void Main(string[] args)
        {
            using (var context = new TranslationContext())
            {
                context.Database.EnsureCreated(); // Create the database and tables if they don't exist

                // Usage example: Adding a new entry to English table
                var newEnglish = new English
                {
                    Word = "example",
                    LineNumber = 1,
                    Translatable = true
                };

                context.English.Add(newEnglish);
                context.SaveChanges();

                Console.WriteLine("English word added successfully.");
            }
        }
    }
}
