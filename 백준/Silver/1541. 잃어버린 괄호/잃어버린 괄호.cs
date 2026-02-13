using System;
using System.Linq;

class Program
{
    static int SumPlus(string chunk)
    {
        return chunk.Split('+').Select(int.Parse).Sum();
    }

    static void Main()
    {
        string expr = Console.ReadLine().Trim();
        string[] parts = expr.Split('-');

        int ans = SumPlus(parts[0]);
        for (int i = 1; i < parts.Length; i++)
            ans -= SumPlus(parts[i]);

        Console.WriteLine(ans);
    }
}
