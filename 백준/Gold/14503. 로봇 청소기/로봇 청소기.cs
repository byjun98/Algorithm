using System;

class Program
{
    static void Main()
    {
        var nm = Console.ReadLine().Split();
        int N = int.Parse(nm[0]);
        int M = int.Parse(nm[1]);

        var input = Console.ReadLine().Split();
        int r = int.Parse(input[0]);
        int c = int.Parse(input[1]);
        int d = int.Parse(input[2]);

        int[,] map = new int[N, M];

        for (int i = 0; i < N; i++)
        {
            var row = Console.ReadLine().Split();
            for (int j = 0; j < M; j++)
                map[i, j] = int.Parse(row[j]);
        }

        int[] dr = { -1, 0, 1, 0 };
        int[] dc = { 0, 1, 0, -1 };

        int cleaned = 0;

        while (true)
        {
            if (map[r, c] == 0)
            {
                map[r, c] = 2;
                cleaned++;
            }

            bool found = false;

            for (int i = 0; i < 4; i++)
            {
                d = (d + 3) % 4;
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (map[nr, nc] == 0)
                {
                    r = nr;
                    c = nc;
                    found = true;
                    break;
                }
            }

            if (!found)
            {
                int backDir = (d + 2) % 4;
                int br = r + dr[backDir];
                int bc = c + dc[backDir];

                if (map[br, bc] == 1)
                    break;

                r = br;
                c = bc;
            }
        }

        Console.WriteLine(cleaned);
    }
}
