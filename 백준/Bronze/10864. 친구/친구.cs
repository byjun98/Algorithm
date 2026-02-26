using System;
using System.Text;

class Program
{
    static void Main()
    {
        var first = Console.ReadLine().Split();
        int N = int.Parse(first[0]);
        int M = int.Parse(first[1]);

        int[] deg = new int[N + 1];

        for (int i = 0; i < M; i++)
        {
            var parts = Console.ReadLine().Split();
            int a = int.Parse(parts[0]);
            int b = int.Parse(parts[1]);

            deg[a]++;
            deg[b]++;
        }

        var sb = new StringBuilder();
        for (int i = 1; i <= N; i++)
        {
            sb.AppendLine(deg[i].ToString());
        }

        Console.Write(sb.ToString());
    }
}