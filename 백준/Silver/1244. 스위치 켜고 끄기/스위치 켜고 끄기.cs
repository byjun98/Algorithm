using System;
using System.Linq;
using System.Text;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[] A = new int[N + 1]; // 1-indexed
        var init = Console.ReadLine().Split().Select(int.Parse).ToArray();
        for (int i = 1; i <= N; i++) A[i] = init[i - 1];

        int M = int.Parse(Console.ReadLine());
        for (int t = 0; t < M; t++)
        {
            var parts = Console.ReadLine().Split();
            int gender = int.Parse(parts[0]);
            int k = int.Parse(parts[1]);

            if (gender == 1) // 남학생
            {
                for (int i = k; i <= N; i += k)
                    A[i] ^= 1;
            }
            else // 여학생
            {
                int l = k, r = k;
                while (l - 1 >= 1 && r + 1 <= N && A[l - 1] == A[r + 1])
                {
                    l--; r++;
                }
                for (int i = l; i <= r; i++)
                    A[i] ^= 1;
            }
        }

        var sb = new StringBuilder();
        for (int i = 1; i <= N; i++)
        {
            sb.Append(A[i]);
            if (i % 20 == 0) sb.Append('\n');
            else sb.Append(' ');
        }
        Console.WriteLine(sb.ToString().TrimEnd());
    }
}
