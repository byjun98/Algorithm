using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();

        int cur = a[0];
        int best = a[0];

        for (int i = 1; i < n; i++)
        {
            cur = Math.Max(a[i], cur + a[i]);
            best = Math.Max(best, cur);
        }

        Console.WriteLine(best);
    }
}
