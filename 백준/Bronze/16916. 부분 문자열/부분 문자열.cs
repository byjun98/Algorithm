using System;
using System.Text;

class Program
{
    static int[] BuildPi(string p)
    {
        int m = p.Length;
        int[] pi = new int[m];
        int j = 0;

        for (int i = 1; i < m; i++)
        {
            while (j > 0 && p[i] != p[j])
                j = pi[j - 1];

            if (p[i] == p[j])
                pi[i] = ++j;
        }
        return pi;
    }

    static int KmpContains(string s, string p)
    {
        int n = s.Length;
        int m = p.Length;
        int[] pi = BuildPi(p);

        int j = 0;
        for (int i = 0; i < n; i++)
        {
            while (j > 0 && s[i] != p[j])
                j = pi[j - 1];

            if (s[i] == p[j])
            {
                j++;
                if (j == m) return 1;
            }
        }
        return 0;
    }

    static void Main()
    {
        string s = Console.ReadLine();
        string p = Console.ReadLine();

        Console.Write(KmpContains(s, p));
    }
}