using System;
using System.Text;

class Program
{
    const int MOD = 1000;

    static int[,] Mul(int[,] A, int[,] B, int n)
    {
        var C = new int[n, n];

        // i-k-j 순서
        for (int i = 0; i < n; i++)
        {
            for (int k = 0; k < n; k++)
            {
                int aik = A[i, k];
                if (aik == 0) continue;

                for (int j = 0; j < n; j++)
                {
                    C[i, j] = (C[i, j] + aik * B[k, j]) % MOD;
                }
            }
        }
        return C;
    }

    static int[,] Pow(int[,] A, long exp, int n)
    {
        // 항등행렬
        var result = new int[n, n];
        for (int i = 0; i < n; i++) result[i, i] = 1;

        // base = A % MOD
        var baseM = new int[n, n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                baseM[i, j] = A[i, j] % MOD;

        while (exp > 0)
        {
            if ((exp & 1L) == 1L)
                result = Mul(result, baseM, n);

            baseM = Mul(baseM, baseM, n);
            exp >>= 1;
        }
        return result;
    }

    static void Main()
    {
        var first = Console.ReadLine().Split();
        int n = int.Parse(first[0]);
        long b = long.Parse(first[1]);

        var A = new int[n, n];
        for (int i = 0; i < n; i++)
        {
            var parts = Console.ReadLine().Split();
            for (int j = 0; j < n; j++)
                A[i, j] = int.Parse(parts[j]);
        }

        var ans = Pow(A, b, n);

        var sb = new StringBuilder();
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (j > 0) sb.Append(' ');
                sb.Append(ans[i, j]);
            }
            sb.Append('\n');
        }
        Console.Write(sb.ToString());
    }
}
