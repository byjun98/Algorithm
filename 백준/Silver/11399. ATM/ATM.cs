using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine()!);
        int[] p = Console.ReadLine()!.Split().Select(int.Parse).ToArray();

        Array.Sort(p);

        int prefix = 0;
        int total = 0;
        foreach (int x in p)
        {
            prefix += x;
            total += prefix;
        }

        Console.WriteLine(total);
    }
}
