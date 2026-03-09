using System;

class Program
{
    static void Main()
    {
        string s = Console.ReadLine();
        int idx = 0;
        int num = 1;

        while (true)
        {
            string t = num.ToString();

            foreach (char ch in t)
            {
                if (idx < s.Length && ch == s[idx])
                {
                    idx++;
                    if (idx == s.Length)
                    {
                        Console.WriteLine(num);
                        return;
                    }
                }
            }

            num++;
        }
    }
}