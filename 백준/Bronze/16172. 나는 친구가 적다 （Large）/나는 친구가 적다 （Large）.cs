using System;

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

    static int Exists(string s, string k)
    {
        int[] pi = BuildPi(k);
        int j = 0;
        int m = k.Length;

        for (int i = 0; i < s.Length; i++)
        {
            char ch = s[i];

            if (ch >= '0' && ch <= '9')
                continue;

            while (j > 0 && ch != k[j])
                j = pi[j - 1];

            if (ch == k[j])
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
        string k = Console.ReadLine();
        Console.Write(Exists(s, k));
    }
}