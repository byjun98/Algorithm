using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static List<int>[] graph;
    static bool[] visited;
    static int N, M, V;

    static void DFS(int v)
    {
        visited[v] = true;
        Console.Write(v + " ");

        foreach (int next in graph[v])
        {
            if (!visited[next])
                DFS(next);
        }
    }

    static void BFS(int start)
    {
        Queue<int> q = new Queue<int>();
        visited = new bool[N + 1];

        q.Enqueue(start);
        visited[start] = true;

        while (q.Count > 0)
        {
            int v = q.Dequeue();
            Console.Write(v + " ");

            foreach (int next in graph[v])
            {
                if (!visited[next])
                {
                    visited[next] = true;
                    q.Enqueue(next);
                }
            }
        }
    }

    static void Main()
    {
        string[] input = Console.ReadLine().Split();
        N = int.Parse(input[0]);
        M = int.Parse(input[1]);
        V = int.Parse(input[2]);

        graph = new List<int>[N + 1];
        for (int i = 1; i <= N; i++)
            graph[i] = new List<int>();

        for (int i = 0; i < M; i++)
        {
            string[] line = Console.ReadLine().Split();
            int a = int.Parse(line[0]);
            int b = int.Parse(line[1]);

            graph[a].Add(b);
            graph[b].Add(a);
        }

        for (int i = 1; i <= N; i++)
            graph[i].Sort();

        visited = new bool[N + 1];
        DFS(V);
        Console.WriteLine();

        BFS(V);
        Console.WriteLine();
    }
}
