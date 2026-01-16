using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[] req = Console.ReadLine().Split().Select(int.Parse).ToArray();
        long M = long.Parse(Console.ReadLine());

        long total = 0;
        int mx = 0;
        foreach (var x in req)
        {
            total += x;
            if (x > mx) mx = x;
        }

        if (total <= M)
        {
            Console.WriteLine(mx);
            return;
        }

        int lo = 0, hi = mx;
        int ans = 0;

        while (lo <= hi)
        {
            int mid = lo + (hi - lo) / 2;

            long s = 0;
            foreach (var x in req)
                s += (x < mid) ? x : mid;

            if (s <= M)
            {
                ans = mid;
                lo = mid + 1;
            }
            else
            {
                hi = mid - 1;
            }
        }

        Console.WriteLine(ans);
    }
}
