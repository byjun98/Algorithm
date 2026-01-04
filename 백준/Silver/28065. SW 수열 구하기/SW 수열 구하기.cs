using System;
using System.Text;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine()!.Trim());
        int l = 1, r = N;
        var ans = new List<int>(N);

        while (l <= r)
        {
            ans.Add(l);
            l++;
            if (l <= r)
            {
                ans.Add(r);
                r--;
            }
        }

        var sb = new StringBuilder();
        for (int i = 0; i < ans.Count; i++)
        {
            if (i > 0) sb.Append(' ');
            sb.Append(ans[i]);
        }
        Console.WriteLine(sb.ToString());
    }
}
