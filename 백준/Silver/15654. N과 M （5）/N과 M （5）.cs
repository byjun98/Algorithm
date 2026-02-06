using System;
using System.Linq;
using System.Text;

public class Program
{
    static int N, M;
    static int[] arr;
    static bool[] used;
    static int[] picked;
    static StringBuilder sb = new StringBuilder();

    static void Dfs(int depth)
    {
        if (depth == M)
        {
            for (int i = 0; i < M; i++)
            {
                if (i > 0) sb.Append(' ');
                sb.Append(picked[i]);
            }
            sb.Append('\n');
            return;
        }

        for (int i = 0; i < N; i++)
        {
            if (used[i]) continue;
            used[i] = true;
            picked[depth] = arr[i];
            Dfs(depth + 1);
            used[i] = false;
        }
    }

    public static void Main()
    {
        var nm = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
        N = nm[0];
        M = nm[1];

        arr = Console.ReadLine()!.Split().Select(int.Parse).ToArray();
        Array.Sort(arr);

        used = new bool[N];
        picked = new int[M];

        Dfs(0);
        Console.Write(sb.ToString());
    }
}