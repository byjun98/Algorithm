using System;
using System.Linq;

public class Program
{
    public static void Main()
    {
        int N = int.Parse(Console.ReadLine()!);
        int[,] a = new int[N, N];
        for (int i = 0; i < N; i++)
        {
            var parts = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
            for (int j = 0; j < N; j++) a[i, j] = parts[j];
        }

        long[,,] dp = new long[N, N, 3];
        dp[0, 1, 0] = 1;

        for (int r = 0; r < N; r++)
        {
            for (int c = 0; c < N; c++)
            {
                if (a[r, c] == 1) continue;

                long w = dp[r, c, 0];
                if (w != 0)
                {
                    int nc = c + 1;
                    if (nc < N && a[r, nc] == 0) dp[r, nc, 0] += w;

                    int nr = r + 1; nc = c + 1;
                    if (nr < N && nc < N &&
                        a[r, c + 1] == 0 && a[r + 1, c] == 0 && a[r + 1, c + 1] == 0)
                    {
                        dp[nr, nc, 2] += w;
                    }
                }

                long v = dp[r, c, 1];
                if (v != 0)
                {
                    int nr = r + 1;
                    if (nr < N && a[nr, c] == 0) dp[nr, c, 1] += v;

                    nr = r + 1; int nc = c + 1;
                    if (nr < N && nc < N &&
                        a[r, c + 1] == 0 && a[r + 1, c] == 0 && a[r + 1, c + 1] == 0)
                    {
                        dp[nr, nc, 2] += v;
                    }
                }

                long d = dp[r, c, 2];
                if (d != 0)
                {
                    int nc = c + 1;
                    if (nc < N && a[r, nc] == 0) dp[r, nc, 0] += d;

                    int nr = r + 1;
                    if (nr < N && a[nr, c] == 0) dp[nr, c, 1] += d;

                    nr = r + 1; nc = c + 1;
                    if (nr < N && nc < N &&
                        a[r, c + 1] == 0 && a[r + 1, c] == 0 && a[r + 1, c + 1] == 0)
                    {
                        dp[nr, nc, 2] += d;
                    }
                }
            }
        }

        long ans = dp[N - 1, N - 1, 0] + dp[N - 1, N - 1, 1] + dp[N - 1, N - 1, 2];
        Console.WriteLine(ans);
    }
}
