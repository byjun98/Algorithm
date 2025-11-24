using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] score = new int[n + 1];
        for (int i = 1; i <= n; i++)
            score[i] = int.Parse(Console.ReadLine());

        if (n == 1)
        {
            Console.WriteLine(score[1]);
            return;
        }

        int[] dp = new int[n + 1];
        dp[1] = score[1];
        dp[2] = score[1] + score[2];

        if (n >= 3)
        {
            dp[3] = Math.Max(score[1] + score[3], score[2] + score[3]);
        }

        for (int i = 4; i <= n; i++)
        {
            dp[i] = Math.Max(
                dp[i - 2] + score[i],
                dp[i - 3] + score[i - 1] + score[i]
            );
        }

        Console.WriteLine(dp[n]);
    }
}
