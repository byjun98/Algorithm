using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[] A = Console.ReadLine().Split().Select(int.Parse).ToArray();

        int[] dp = new int[N];
        int answer = 0;

        for (int i = 0; i < N; i++)
        {
            dp[i] = 1; // 자기만 쓰는 경우
            for (int j = 0; j < i; j++)
            {
                if (A[j] < A[i])
                {
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
                }
            }
            if (dp[i] > answer) answer = dp[i];
        }

        Console.WriteLine(answer);
    }
}