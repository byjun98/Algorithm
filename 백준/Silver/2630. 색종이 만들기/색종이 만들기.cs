using System;

class Program
{
    static int N;
    static int[,] paper;
    static int white = 0;
    static int blue = 0;

    static void Divide(int x, int y, int size)
    {
        int first = paper[x, y];
        bool same = true;

        for (int i = x; i < x + size; i++)
        {
            for (int j = y; j < y + size; j++)
            {
                if (paper[i, j] != first)
                {
                    same = false;
                    break;
                }
            }
            if (!same) break;
        }

        if (same)
        {
            if (first == 0) white++;
            else blue++;
            return;
        }

        int half = size / 2;
        Divide(x, y, half);
        Divide(x, y + half, half);
        Divide(x + half, y, half);
        Divide(x + half, y + half, half);
    }

    static void Main(string[] args)
    {
        N = int.Parse(Console.ReadLine());
        paper = new int[N, N];

        for (int i = 0; i < N; i++)
        {
            string[] input = Console.ReadLine().Split();
            for (int j = 0; j < N; j++)
            {
                paper[i, j] = int.Parse(input[j]);
            }
        }

        Divide(0, 0, N);

        Console.WriteLine(white);
        Console.WriteLine(blue);
    }
}
