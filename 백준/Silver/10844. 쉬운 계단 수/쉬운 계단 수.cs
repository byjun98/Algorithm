using System;

class Program
{
    static void Main()
    {
        const long MOD = 1000000000;
        int N = int.Parse(Console.ReadLine());

        long[,] dp = new long[N + 1, 10];

        for (int d = 1; d <= 9; d++)
        {
            dp[1, d] = 1;
        }

        for (int i = 2; i <= N; i++)
        {
            dp[i, 0] = dp[i - 1, 1] % MOD;
            dp[i, 9] = dp[i - 1, 8] % MOD;

            for (int d = 1; d <= 8; d++)
            {
                dp[i, d] = (dp[i - 1, d - 1] + dp[i - 1, d + 1]) % MOD;
            }
        }

        long answer = 0;
        for (int d = 0; d <= 9; d++)
        {
            answer = (answer + dp[N, d]) % MOD;
        }

        Console.WriteLine(answer);
    }
}