using System;
using System.IO;
using System.Text;

class Program
{
    static void Main()
    {
        StreamReader sr = new StreamReader(Console.OpenStandardInput());
        StreamWriter sw = new StreamWriter(Console.OpenStandardOutput());
        StringBuilder sb = new StringBuilder();

        int n = int.Parse(sr.ReadLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++)
        {
            arr[i] = int.Parse(sr.ReadLine());
        }

        Array.Sort(arr);
        Array.Reverse(arr);

        for (int i = 0; i < n; i++)
        {
            sb.AppendLine(arr[i].ToString());
        }

        sw.Write(sb.ToString());
        sw.Flush();
    }
}