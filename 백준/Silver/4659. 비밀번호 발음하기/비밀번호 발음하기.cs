using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var vowels = new HashSet<char>{'a','e','i','o','u'};

        while (true)
        {
            string s = Console.ReadLine();
            if (s == "end") break;

            bool ok = true;
            bool hasVowel = false;

            char prev = '\0';
            bool? prevIsVowel = null;
            int run = 0;

            foreach (char ch in s)
            {
                bool isVowel = vowels.Contains(ch);
                if (isVowel) hasVowel = true;

                if (prevIsVowel == null || isVowel != prevIsVowel.Value)
                {
                    run = 1;
                }
                else
                {
                    run++;
                    if (run >= 3) ok = false;
                }

                if (prev != '\0' && ch == prev)
                {
                    if (ch != 'e' && ch != 'o') ok = false;
                }

                prev = ch;
                prevIsVowel = isVowel;
            }

            if (!hasVowel) ok = false;

            Console.WriteLine(ok
                ? $"<{s}> is acceptable."
                : $"<{s}> is not acceptable.");
        }
    }
}
