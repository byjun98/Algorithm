using System;

class Program
{
    static void Main()
    {
        string s = Console.ReadLine().Trim();
        string[] parts = s.Split(',');

        long sum = 0;
        foreach (var p in parts)
        {
            sum += long.Parse(p);
        }

        Console.WriteLine(sum);
    }
}