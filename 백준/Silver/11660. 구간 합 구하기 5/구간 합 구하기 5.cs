using System;
using System.IO;
using System.Text;

class Program
{
    static void Main()
    {
        var sr = new StreamReader(Console.OpenStandardInput());
        var sb = new StringBuilder();

        string[] first = sr.ReadLine().Split();
        int N = int.Parse(first[0]);
        int M = int.Parse(first[1]);

        int[,] S = new int[N + 1, N + 1];

        for (int i = 1; i <= N; i++)
        {
            string line = sr.ReadLine();
            int col = 1;
            int num = 0;

            for (int k = 0; k < line.Length; k++)
            {
                char c = line[k];

                if (c == ' ')
                {
                    S[i, col] = S[i, col - 1] + S[i - 1, col] - S[i - 1, col - 1] + num;
                    col++;
                    num = 0;
                }
                else
                {
                    num = num * 10 + (c - '0');
                }
            }

            S[i, col] = S[i, col - 1] + S[i - 1, col] - S[i - 1, col - 1] + num;
        }

        for (int q = 0; q < M; q++)
        {
            string line = sr.ReadLine();
            int idx = 0;

            int x1 = NextInt(line, ref idx);
            int y1 = NextInt(line, ref idx);
            int x2 = NextInt(line, ref idx);
            int y2 = NextInt(line, ref idx);

            int result =
                S[x2, y2]
                - S[x1 - 1, y2]
                - S[x2, y1 - 1]
                + S[x1 - 1, y1 - 1];

            sb.Append(result).Append('\n');
        }

        Console.Write(sb.ToString());
    }

    static int NextInt(string s, ref int idx)
    {
        int num = 0;

        while (idx < s.Length && s[idx] == ' ')
            idx++;

        while (idx < s.Length && s[idx] != ' ')
        {
            num = num * 10 + (s[idx] - '0');
            idx++;
        }
        return num;
    }
}
