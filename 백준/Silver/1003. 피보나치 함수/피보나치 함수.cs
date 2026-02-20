using System;

class Program
{
    static void Main()
    {
        int[,] dp = new int[41, 2];

        dp[0, 0] = 1; // 0 출력
        dp[0, 1] = 0;

        dp[1, 0] = 0;
        dp[1, 1] = 1; // 1 출력

        for (int i = 2; i <= 40; i++)
        {
            dp[i, 0] = dp[i - 1, 0] + dp[i - 2, 0];
            dp[i, 1] = dp[i - 1, 1] + dp[i - 2, 1];
        }

        int T = int.Parse(Console.ReadLine());

        for (int t = 0; t < T; t++)
        {
            int n = int.Parse(Console.ReadLine());
            Console.WriteLine($"{dp[n, 0]} {dp[n, 1]}");
        }
    }
}