using System;
using System.Text;

class Program
{
    static void Main()
    {
        var input = Console.ReadLine().Split();
        int N = int.Parse(input[0]);
        int M = int.Parse(input[1]);

        string s = N.ToString();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N && sb.Length < M; i++)
        {
            sb.Append(s);
        }

        if (sb.Length > M)
        {
            sb.Length = M;
        }

        Console.WriteLine(sb.ToString());
    }
}
