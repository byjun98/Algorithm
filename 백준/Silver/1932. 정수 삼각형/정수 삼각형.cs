using System;
using System.IO;

class Program
{
    static void Main()
    {
        using var sr = new StreamReader(Console.OpenStandardInput());

        int n = int.Parse(sr.ReadLine());
        int[] dp = new int[n];

        for (int i = 0; i < n; i++)
        {
            string[] parts = sr.ReadLine().Split();
            // i번째 줄은 길이가 i+1
            for (int j = i; j >= 0; j--)
            {
                int val = int.Parse(parts[j]);

                if (j == 0)
                {
                    dp[j] = dp[j] + val;
                }
                else if (j == i)
                {
                    dp[j] = dp[j - 1] + val;
                }
                else
                {
                    dp[j] = Math.Max(dp[j - 1], dp[j]) + val;
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++)
            if (dp[i] > ans) ans = dp[i];

        Console.WriteLine(ans);
    }
}
