using System;

class Program
{
    static void Main()
    {
        string s = Console.ReadLine();
        if (string.IsNullOrEmpty(s))
        {
            Console.WriteLine(0);
            return;
        }

        int c0 = 0, c1 = 0;
        char prev = '\0';

        for (int i = 0; i < s.Length; i++)
        {
            char ch = s[i];
            if (i == 0 || ch != prev)
            {
                if (ch == '0') c0++;
                else c1++;
                prev = ch;
            }
        }

        Console.WriteLine(Math.Min(c0, c1));
    }
}
