using System;

public class Program
{
    public static void Main()
    {
        const int MOD = 9901;
        int n = int.Parse(Console.ReadLine()!);

        int dp0 = 1, dp1 = 1, dp2 = 1; // i=1

        for (int i = 2; i <= n; i++)
        {
            int new0 = (dp0 + dp1 + dp2) % MOD;
            int new1 = (dp0 + dp2) % MOD;
            int new2 = (dp0 + dp1) % MOD;

            dp0 = new0;
            dp1 = new1;
            dp2 = new2;
        }

        int ans = (dp0 + dp1 + dp2) % MOD;
        Console.WriteLine(ans);
    }
}