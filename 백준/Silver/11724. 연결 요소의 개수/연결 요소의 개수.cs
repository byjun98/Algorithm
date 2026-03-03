using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main()
    {
        var sr = new StreamReader(Console.OpenStandardInput());
        var first = sr.ReadLine().Split();
        int N = int.Parse(first[0]);
        int M = int.Parse(first[1]);

        var graph = new List<int>[N + 1];
        for (int i = 1; i <= N; i++) graph[i] = new List<int>();

        for (int i = 0; i < M; i++)
        {
            var parts = sr.ReadLine().Split();
            int u = int.Parse(parts[0]);
            int v = int.Parse(parts[1]);
            graph[u].Add(v);
            graph[v].Add(u);
        }

        bool[] visited = new bool[N + 1];
        int count = 0;

        for (int i = 1; i <= N; i++)
        {
            if (!visited[i])
            {
                count++;
                var stack = new Stack<int>();
                stack.Push(i);
                visited[i] = true;

                while (stack.Count > 0)
                {
                    int x = stack.Pop();
                    foreach (var nx in graph[x])
                    {
                        if (!visited[nx])
                        {
                            visited[nx] = true;
                            stack.Push(nx);
                        }
                    }
                }
            }
        }

        Console.WriteLine(count);
    }
}