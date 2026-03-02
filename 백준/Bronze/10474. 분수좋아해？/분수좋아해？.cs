using System;
using System.Text;

class Program
{
    static void Main()
    {
        var sb = new StringBuilder();

        while (true)
        {
            string line = Console.ReadLine();
            if (line == null) break;

            var parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
            long a = long.Parse(parts[0]);
            long b = long.Parse(parts[1]);

            if (a == 0 && b == 0) break;

            long q = a / b;
            long r = a % b;

            sb.AppendLine($"{q} {r} / {b}");
        }

        Console.Write(sb.ToString());
    }
}