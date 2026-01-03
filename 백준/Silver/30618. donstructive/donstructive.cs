using System;
using System.Text;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine()!);
        int[] res = new int[N];

        int left = (N - 1) / 2;
        int right = left + 1;
        int val = N;

        while (val > 0)
        {
            if (left >= 0)
            {
                res[left] = val--;
                left--;
            }
            if (val > 0 && right < N)
            {
                res[right] = val--;
                right++;
            }
        }

        var sb = new StringBuilder();
        for (int i = 0; i < N; i++)
        {
            if (i > 0) sb.Append(' ');
            sb.Append(res[i]);
        }
        Console.WriteLine(sb.ToString());
    }
}
