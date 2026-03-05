using System;
using System.Collections.Generic;

public class Program
{
    static int N, M;
    static int[,] grid;

    static int CountComponents(List<(int r, int c)> iceCells)
    {
        bool[,] visited = new bool[N, M];
        int comp = 0;

        int[] dr = { 1, -1, 0, 0 };
        int[] dc = { 0, 0, 1, -1 };

        Queue<(int r, int c)> q = new Queue<(int r, int c)>();

        foreach (var (r, c) in iceCells)
        {
            if (grid[r, c] > 0 && !visited[r, c])
            {
                comp++;
                visited[r, c] = true;
                q.Enqueue((r, c));

                while (q.Count > 0)
                {
                    var (x, y) = q.Dequeue();
                    for (int k = 0; k < 4; k++)
                    {
                        int nx = x + dr[k];
                        int ny = y + dc[k];
                        if (0 <= nx && nx < N && 0 <= ny && ny < M)
                        {
                            if (grid[nx, ny] > 0 && !visited[nx, ny])
                            {
                                visited[nx, ny] = true;
                                q.Enqueue((nx, ny));
                            }
                        }
                    }
                }
            }
        }

        return comp;
    }

    public static void Main()
    {
        var first = Console.ReadLine().Split();
        N = int.Parse(first[0]);
        M = int.Parse(first[1]);

        grid = new int[N, M];
        var iceCells = new List<(int r, int c)>();

        for (int i = 0; i < N; i++)
        {
            var parts = Console.ReadLine().Split();
            for (int j = 0; j < M; j++)
            {
                int v = int.Parse(parts[j]);
                grid[i, j] = v;
                if (v > 0) iceCells.Add((i, j));
            }
        }

        int year = 0;
        int[] dr = { 1, -1, 0, 0 };
        int[] dc = { 0, 0, 1, -1 };

        while (true)
        {
            int comp = CountComponents(iceCells);
            if (comp == 0)
            {
                Console.WriteLine(0);
                return;
            }
            if (comp >= 2)
            {
                Console.WriteLine(year);
                return;
            }

            int[,] melt = new int[N, M];
            foreach (var (x, y) in iceCells)
            {
                int sea = 0;
                for (int k = 0; k < 4; k++)
                {
                    int nx = x + dr[k];
                    int ny = y + dc[k];
                    if (0 <= nx && nx < N && 0 <= ny && ny < M)
                    {
                        if (grid[nx, ny] == 0) sea++;
                    }
                }
                melt[x, y] = sea;
            }

            var newIce = new List<(int r, int c)>(iceCells.Count);
            foreach (var (x, y) in iceCells)
            {
                int nv = grid[x, y] - melt[x, y];
                if (nv < 0) nv = 0;
                grid[x, y] = nv;
                if (nv > 0) newIce.Add((x, y));
            }

            iceCells = newIce;
            year++;
        }
    }
}