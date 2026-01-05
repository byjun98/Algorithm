using System;
using System.Collections.Generic;
using System.Text;

class Program
{
    static void Main()
    {
        var first = Console.ReadLine()!.Split();
        int N = int.Parse(first[0]);
        int M = int.Parse(first[1]);
        int R = int.Parse(first[2]);

        var adj = new List<int>[N + 1];
        for (int i = 1; i <= N; i++) adj[i] = new List<int>();

        for (int i = 0; i < M; i++)
        {
            var parts = Console.ReadLine()!.Split();
            int u = int.Parse(parts[0]);
            int v = int.Parse(parts[1]);
            adj[u].Add(v);
            adj[v].Add(u);
        }

        // 내림차순 정렬
        for (int i = 1; i <= N; i++)
            adj[i].Sort((a, b) => b.CompareTo(a));

        int[] order = new int[N + 1];
        int cnt = 0;
        var stack = new Stack<int>();
        stack.Push(R);

        while (stack.Count > 0)
        {
            int v = stack.Pop();
            if (order[v] != 0) continue;

            order[v] = ++cnt;

            // 내림차순 방문을 위해 오름차순으로 push
            // adj[v]는 내림차순이므로 뒤에서 앞으로 push
            var list = adj[v];
            for (int idx = list.Count - 1; idx >= 0; idx--)
            {
                int x = list[idx];
                if (order[x] == 0) stack.Push(x);
            }
        }

        var sb = new StringBuilder();
        for (int i = 1; i <= N; i++)
        {
            sb.Append(order[i]).Append('\n');
        }
        Console.Write(sb.ToString());
    }
}
