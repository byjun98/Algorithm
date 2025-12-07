using System;
using System.Collections.Generic;

class Program
{
    static int N;
    static int[,] grid;
    static bool[,] visited;
    static int[] dx = { 1, -1, 0, 0 };
    static int[] dy = { 0, 0, 1, -1 };

    static void DFS(int x, int y, int h)
    {
        Stack<(int, int)> stack = new Stack<(int, int)>();
        stack.Push((x, y));
        visited[x, y] = true;

        while (stack.Count > 0)
        {
            var (cx, cy) = stack.Pop();
            for (int k = 0; k < 4; k++)
            {
                int nx = cx + dx[k];
                int ny = cy + dy[k];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N)
                {
                    if (!visited[nx, ny] && grid[nx, ny] > h)
                    {
                        visited[nx, ny] = true;
                        stack.Push((nx, ny));
                    }
                }
            }
        }
    }

    static void Main()
    {
        N = int.Parse(Console.ReadLine());
        grid = new int[N, N];

        int maxHeight = 0;

        for (int i = 0; i < N; i++)
        {
            var row = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            for (int j = 0; j < N; j++)
            {
                grid[i, j] = row[j];
                maxHeight = Math.Max(maxHeight, row[j]);
            }
        }

        int answer = 1;

        for (int h = 0; h <= maxHeight; h++)
        {
            visited = new bool[N, N];
            int count = 0;

            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    if (grid[i, j] > h && !visited[i, j])
                    {
                        DFS(i, j, h);
                        count++;
                    }
                }
            }

            answer = Math.Max(answer, count);
        }

        Console.WriteLine(answer);
    }
}
