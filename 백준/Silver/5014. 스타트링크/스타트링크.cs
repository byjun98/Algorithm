using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var parts = Console.ReadLine().Split();
        int F = int.Parse(parts[0]);
        int S = int.Parse(parts[1]);
        int G = int.Parse(parts[2]);
        int U = int.Parse(parts[3]);
        int D = int.Parse(parts[4]);

        if (S == G)
        {
            Console.WriteLine(0);
            return;
        }

        bool[] visited = new bool[F + 1];
        int[] dist = new int[F + 1];
        for (int i = 0; i <= F; i++) dist[i] = -1;

        Queue<int> q = new Queue<int>();
        q.Enqueue(S);
        visited[S] = true;
        dist[S] = 0;

        while (q.Count > 0)
        {
            int x = q.Dequeue();

            if (x == G)
            {
                Console.WriteLine(dist[x]);
                return;
            }

            int nx = x + U;
            if (U > 0 && nx <= F && !visited[nx])
            {
                visited[nx] = true;
                dist[nx] = dist[x] + 1;
                q.Enqueue(nx);
            }

            nx = x - D;
            if (D > 0 && nx >= 1 && !visited[nx])
            {
                visited[nx] = true;
                dist[nx] = dist[x] + 1;
                q.Enqueue(nx);
            }
        }

        Console.WriteLine("use the stairs");
    }
}