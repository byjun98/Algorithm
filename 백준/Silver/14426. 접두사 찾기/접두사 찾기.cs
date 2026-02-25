using System;
using System.IO;

class Program
{
    static int LowerBound(string[] a, string key)
    {
        int lo = 0, hi = a.Length;
        while (lo < hi)
        {
            int mid = (lo + hi) >> 1;
            if (string.CompareOrdinal(a[mid], key) < 0) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    static void Main()
    {
        var sr = new StreamReader(Console.OpenStandardInput());
        var first = sr.ReadLine().Split();
        int n = int.Parse(first[0]);
        int m = int.Parse(first[1]);

        string[] arr = new string[n];
        for (int i = 0; i < n; i++) arr[i] = sr.ReadLine().Trim();

        Array.Sort(arr, StringComparer.Ordinal);

        int ans = 0;
        for (int i = 0; i < m; i++)
        {
            string q = sr.ReadLine().Trim();
            int idx = LowerBound(arr, q);
            if (idx < n && arr[idx].StartsWith(q, StringComparison.Ordinal))
                ans++;
        }

        Console.Write(ans);
    }
}