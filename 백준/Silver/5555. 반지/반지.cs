using System;

class Program
{
    static void Main()
    {
        string p = Console.ReadLine().Trim();
        int n = int.Parse(Console.ReadLine().Trim());

        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            string r = Console.ReadLine().Trim();
            string doubled = r + r;
            if (doubled.Contains(p))
                ans++;
        }

        Console.Write(ans);
    }
}