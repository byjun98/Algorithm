using System;
using System.Text;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        var sb = new StringBuilder();

        for (int i = 0; i < n; i++)
        {
            string line = Console.ReadLine();
            string[] words = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);

            for (int j = 2; j < words.Length; j++)
            {
                sb.Append(words[j]).Append(' ');
            }
            sb.Append(words[0]).Append(' ').Append(words[1]);

            if (i != n - 1) sb.Append('\n');
        }

        Console.Write(sb.ToString());
    }
}