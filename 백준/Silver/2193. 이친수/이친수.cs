using System;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());

        long dp0 = 0;
        long dp1 = 1;

        for (int i = 2; i <= N; i++)
        {
            long new0 = dp0 + dp1;
            long new1 = dp0;
            dp0 = new0;
            dp1 = new1;
        }

        Console.WriteLine(dp0 + dp1);
    }
}