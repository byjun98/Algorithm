using System;
using System.Collections.Generic;

class Program
{
    static (int x, int y) ToPos(string s)
    {
        int x = s[0] - 'A'; // A~F -> 0~5
        int y = s[1] - '1'; // 1~6 -> 0~5
        return (x, y);
    }

    static bool IsKnight((int x, int y) a, (int x, int y) b)
    {
        int dx = Math.Abs(a.x - b.x);
        int dy = Math.Abs(a.y - b.y);
        return (dx == 1 && dy == 2) || (dx == 2 && dy == 1);
    }

    static void Main()
    {
        var path = new (int x, int y)[36];
        var visited = new bool[6, 6];

        bool dup = false;
        for (int i = 0; i < 36; i++)
        {
            string s = Console.ReadLine().Trim();
            var p = ToPos(s);
            path[i] = p;

            if (visited[p.x, p.y]) dup = true;
            visited[p.x, p.y] = true;
        }

        if (dup)
        {
            Console.WriteLine("Invalid");
            return;
        }

        for (int i = 0; i < 35; i++)
        {
            if (!IsKnight(path[i], path[i + 1]))
            {
                Console.WriteLine("Invalid");
                return;
            }
        }

        if (!IsKnight(path[35], path[0]))
        {
            Console.WriteLine("Invalid");
            return;
        }

        Console.WriteLine("Valid");
    }
}
