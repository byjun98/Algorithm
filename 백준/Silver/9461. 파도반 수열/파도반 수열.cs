using System;
using System.Text;

class Program
{
    static void Main()
    {
        int T = int.Parse(Console.ReadLine());

        long[] dp = new long[101];
        dp[1] = dp[2] = dp[3] = 1;

        for (int n = 4; n <= 100; n++)
            dp[n] = dp[n - 2] + dp[n - 3];

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++)
        {
            int N = int.Parse(Console.ReadLine());
            sb.AppendLine(dp[N].ToString());
        }

        Console.Write(sb.ToString());
    }
}
