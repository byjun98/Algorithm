using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[] a = new int[N];
        for (int i = 0; i < N; i++)
            a[i] = int.Parse(Console.ReadLine());

        long ans = 0;
        for (int i = N - 2; i >= 0; i--)
        {
            if (a[i] >= a[i + 1])
            {
                int target = a[i + 1] - 1;
                ans += (a[i] - target);
                a[i] = target;
            }
        }

        Console.WriteLine(ans);
    }
}
