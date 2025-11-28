using System;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[] T = new int[N + 1];
        int[] P = new int[N + 1];

        for (int i = 1; i <= N; i++)
        {
            var parts = Console.ReadLine().Split();
            T[i] = int.Parse(parts[0]);
            P[i] = int.Parse(parts[1]);
        }

        int[] dp = new int[N + 2];

        for (int i = N; i >= 1; i--)
        {
            int end = i + T[i];

            if (end <= N + 1)
                dp[i] = Math.Max(P[i] + dp[end], dp[i + 1]);
            else
                dp[i] = dp[i + 1];
        }

        Console.WriteLine(dp[1]);
    }
}
