using System;
using System.IO;

class Program
{
    static void Main()
    {
        using var sr = new StreamReader(Console.OpenStandardInput());

        int N = int.Parse(sr.ReadLine());

        var first = sr.ReadLine().Split();
        int r = int.Parse(first[0]);
        int g = int.Parse(first[1]);
        int b = int.Parse(first[2]);

        for (int i = 2; i <= N; i++)
        {
            var s = sr.ReadLine().Split();
            int cr = int.Parse(s[0]);
            int cg = int.Parse(s[1]);
            int cb = int.Parse(s[2]);

            int nr = cr + Math.Min(g, b);
            int ng = cg + Math.Min(r, b);
            int nb = cb + Math.Min(r, g);

            r = nr; g = ng; b = nb;
        }

        Console.WriteLine(Math.Min(r, Math.Min(g, b)));
    }
}
