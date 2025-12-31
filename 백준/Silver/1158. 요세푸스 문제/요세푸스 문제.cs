using System;
using System.Collections.Generic;
using System.Text;

class Program
{
    static void Main()
    {
        var parts = Console.ReadLine().Split();
        int N = int.Parse(parts[0]);
        int K = int.Parse(parts[1]);

        List<int> arr = new List<int>();
        for (int i = 1; i <= N; i++)
            arr.Add(i);

        int index = 0;
        StringBuilder sb = new StringBuilder();
        sb.Append("<");

        while (arr.Count > 0)
        {
            index = (index + K - 1) % arr.Count;
            sb.Append(arr[index]);
            arr.RemoveAt(index);

            if (arr.Count > 0)
                sb.Append(", ");
        }

        sb.Append(">");
        Console.WriteLine(sb.ToString());
    }
}
