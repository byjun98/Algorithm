using System;
using System.Collections.Generic;
using System.Text;

class Program
{
    static void Main()
    {
        string[] first = Console.ReadLine().Split();
        int n = int.Parse(first[0]);

        List<long> list = new List<long>(n);

        for (int i = 1; i < first.Length; i++)
        {
            list.Add(ReverseToLong(first[i]));
        }

        while (list.Count < n)
        {
            string line = Console.ReadLine();
            if (string.IsNullOrEmpty(line)) continue;

            string[] parts = line.Split();
            foreach (string s in parts)
            {
                list.Add(ReverseToLong(s));
            }
        }

        list.Sort();

        StringBuilder sb = new StringBuilder();
        foreach (var v in list)
            sb.AppendLine(v.ToString());

        Console.Write(sb.ToString());
    }

    static long ReverseToLong(string s)
    {
        char[] arr = s.ToCharArray();
        Array.Reverse(arr);
        return long.Parse(new string(arr));
    }
}
