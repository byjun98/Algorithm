using System;
using System.Linq;

public class Program
{
    public static void Main()
    {
        int n = int.Parse(Console.ReadLine()!);
        int[] a = Console.ReadLine()!.Split().Select(int.Parse).ToArray();

        int[] dp = new int[n];
        for (int i = 0; i < n; i++) dp[i] = 1;

        int ans = 1;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (a[j] < a[i])
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
            }
            ans = Math.Max(ans, dp[i]);
        }

        Console.WriteLine(ans);
    }
}