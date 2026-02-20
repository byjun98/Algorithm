using System;

class Program
{
    static void Main()
    {
        const int MOD = 10007;
        int n = int.Parse(Console.ReadLine());

        if (n == 1)
        {
            Console.WriteLine(1);
            return;
        }

        int a = 1; // dp[1]
        int b = 3; // dp[2]

        for (int i = 3; i <= n; i++)
        {
            int next = (b + 2 * a) % MOD; // dp[i] = dp[i-1] + 2*dp[i-2]
            a = b;
            b = next;
        }

        Console.WriteLine(b % MOD);
    }
}