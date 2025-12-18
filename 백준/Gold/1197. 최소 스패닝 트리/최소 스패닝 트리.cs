using System;
using System.Collections.Generic;
using System.IO;

public class Program
{
    struct Edge
    {
        public int A, B;
        public int C;
        public Edge(int a, int b, int c) { A = a; B = b; C = c; }
    }

    static int[] parent;
    static byte[] rank;

    static int Find(int x)
    {
        while (parent[x] != x)
        {
            parent[x] = parent[parent[x]]; // path compression (halving)
            x = parent[x];
        }
        return x;
    }

    static bool Union(int a, int b)
    {
        int ra = Find(a), rb = Find(b);
        if (ra == rb) return false;

        if (rank[ra] < rank[rb])
        {
            int tmp = ra; ra = rb; rb = tmp;
        }
        parent[rb] = ra;
        if (rank[ra] == rank[rb]) rank[ra]++;
        return true;
    }

    public static void Main()
    {
        var sr = new StreamReader(Console.OpenStandardInput());
        var first = sr.ReadLine().Split();
        int V = int.Parse(first[0]);
        int E = int.Parse(first[1]);

        var edges = new List<Edge>(E);
        for (int i = 0; i < E; i++)
        {
            var parts = sr.ReadLine().Split();
            int a = int.Parse(parts[0]);
            int b = int.Parse(parts[1]);
            int c = int.Parse(parts[2]);
            edges.Add(new Edge(a, b, c));
        }

        edges.Sort((x, y) => x.C.CompareTo(y.C));

        parent = new int[V + 1];
        rank = new byte[V + 1];
        for (int i = 1; i <= V; i++) parent[i] = i;

        long total = 0; // 합은 long 권장
        int picked = 0;

        foreach (var e in edges)
        {
            if (Union(e.A, e.B))
            {
                total += e.C;
                picked++;
                if (picked == V - 1) break;
            }
        }

        Console.WriteLine(total);
    }
}
