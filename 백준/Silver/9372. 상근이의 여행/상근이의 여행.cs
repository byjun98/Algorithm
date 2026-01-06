using System;
using System.Text;

class Program
{
    static void Main()
    {
        int T = int.Parse(Console.ReadLine());
        var sb = new StringBuilder();

        for (int tc = 0; tc < T; tc++)
        {
            var nm = Console.ReadLine().Split();
            int N = int.Parse(nm[0]);
            int M = int.Parse(nm[1]);

            for (int i = 0; i < M; i++)
                Console.ReadLine();

            sb.AppendLine((N - 1).ToString());
        }

        Console.Write(sb.ToString());
    }
}
