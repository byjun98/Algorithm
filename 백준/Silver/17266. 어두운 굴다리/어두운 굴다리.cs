using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int M = int.Parse(Console.ReadLine());
        int[] x = Console.ReadLine().Split().Select(int.Parse).ToArray();

        int ans = Math.Max(x[0], N - x[M - 1]);

        for (int i = 0; i < M - 1; i++)
        {
            int d = x[i + 1] - x[i];
            int need = (d + 1) / 2; // ceil(d/2)
            if (need > ans) ans = need;
        }

        Console.WriteLine(ans);
    }
}
