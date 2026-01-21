using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        long[] dist = Console.ReadLine().Split().Select(long.Parse).ToArray();   // N-1
        long[] price = Console.ReadLine().Split().Select(long.Parse).ToArray(); // N

        long minPrice = long.MaxValue;
        long ans = 0;

        for (int i = 0; i < N - 1; i++)
        {
            if (price[i] < minPrice) minPrice = price[i];
            ans += minPrice * dist[i];
        }

        Console.WriteLine(ans);
    }
}
