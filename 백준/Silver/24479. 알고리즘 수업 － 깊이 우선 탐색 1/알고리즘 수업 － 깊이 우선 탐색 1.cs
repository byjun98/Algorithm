using System;
using System.Collections.Generic;
using System.Text;

class Program
{
    static List<int>[] graph;
    static int[] order;
    static int cnt = 1;

    static void DFS(int v)
    {
        order[v] = cnt++;
        foreach (int next in graph[v])
        {
            if (order[next] == 0)
                DFS(next);
        }
    }

    static void Main()
    {
        var input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int M = int.Parse(input[1]);
        int R = int.Parse(input[2]);

        graph = new List<int>[N + 1];
        for (int i = 1; i <= N; i++)
            graph[i] = new List<int>();

        for (int i = 0; i < M; i++)
        {
            var edge = Console.ReadLine().Split();
            int u = int.Parse(edge[0]);
            int v = int.Parse(edge[1]);
            graph[u].Add(v);
            graph[v].Add(u);
        }

        for (int i = 1; i <= N; i++)
            graph[i].Sort();

        order = new int[N + 1];

        DFS(R);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++)
            sb.AppendLine(order[i].ToString());

        Console.Write(sb.ToString());
    }
}
