package be;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Personnel 
{
    public int ID;
    public String Name;
    public String Role;
    public float Salary;

    public Personnel(int id, String name, String role, float salary) 
    {
        this.ID = id;
        this.Name = name;
        this.Role = role;
        this.Salary = salary;
    }

    public static void main(String[] args) 
    {
        final int PERSONNEL_COUNT = 25;
        final Path OUTPUT = Path.of("personnel.csv");

        List<String> firstName = Arrays.asList("John", "Jane", "Alex", "Emily", "Chris", "Michael", "Jaiden", "Kevin", "Daniel", "Brendan");
        List<String> lastName = Arrays.asList("Smith", "Johnson", "Williams", "Ramirez", "Sidhu", "Chen", "Zhang", "Larson");

        Random rand = new Random();
        DecimalFormat money = new DecimalFormat("0.00");

        try (BufferedWriter w = Files.newBufferedWriter(OUTPUT, StandardCharsets.UTF_8)) 
        {
            w.write("id,name,role,salary");
            w.newLine();

            for (int i = 1; i <= PERSONNEL_COUNT; i++) 
            {
                String name = firstName.get(rand.nextInt(firstName.size())) + " " + lastName.get(rand.nextInt(lastName.size()));
                String role = rand.nextBoolean() ? "cashier" : "manager";
                float salary = role.equals("cashier") ? 15.00f : 25.00f;

                Personnel p = new Personnel(i, name, role, salary);

                String csvName = csvEscape(p.Name);

                String line = p.ID + "," + csvName + "," + p.Role + "," + money.format(p.Salary);
                w.write(line);
                w.newLine();
            }
        } 
        catch (IOException e) 
        {
            System.err.println("Failed to write CSV: " + e.getMessage());
            System.exit(1);
        }

        System.out.println("Wrote CSV to " + OUTPUT.toAbsolutePath());
    }

    private static String csvEscape(String s) 
    {
        boolean needsQuotes = s.contains(",") || s.contains("\"") || s.contains("\n") || s.contains("\r");
        if (!needsQuotes) return s;
        return "\"" + s.replace("\"", "\"\"") + "\"";
    }
}
