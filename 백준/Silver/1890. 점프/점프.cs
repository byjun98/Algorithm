using System;
using System.Linq;

public class Program
{
    public static void Main()
    {
        int n = int.Parse(Console.ReadLine()!);
        int[][] board = new int[n][];
        for (int i = 0; i < n; i++)
            board[i] = Console.ReadLine()!.Split().Select(int.Parse).ToArray();

        long[,] dp = new long[n, n];
        dp[0, 0] = 1;

        for (int r = 0; r < n; r++)
        {
            for (int c = 0; c < n; c++)
            {
                long ways = dp[r, c];
                if (ways == 0) continue;

                int k = board[r][c];
                if (k == 0) continue;

                int nc = c + k;
                int nr = r + k;

                if (nc < n) dp[r, nc] += ways;
                if (nr < n) dp[nr, c] += ways;
            }
        }

        Console.WriteLine(dp[n - 1, n - 1]);
    }
}