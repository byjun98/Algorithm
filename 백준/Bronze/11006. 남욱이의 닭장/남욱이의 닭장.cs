using System;
using System.Text;

class Program
{
    static void Main()
    {
        int tc = int.Parse(Console.ReadLine().Trim());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < tc; i++)
        {
            var parts = Console.ReadLine().Split(' ');
            int N = int.Parse(parts[0]);
            int M = int.Parse(parts[1]);

            int good = N - M;
            int injured = 2 * M - N;

            sb.AppendLine($"{injured} {good}");
        }

        Console.Write(sb.ToString());
    }
}