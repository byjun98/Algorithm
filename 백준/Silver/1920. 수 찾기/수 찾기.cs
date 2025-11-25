using System;
using System.Text;

class Program
{
    static bool BinarySearch(int[] arr, int target)
    {
        int left = 0;
        int right = arr.Length - 1;

        while (left <= right)
        {
            int mid = (left + right) / 2;

            if (arr[mid] == target)
                return true;
            else if (arr[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return false;
    }

    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] A = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        Array.Sort(A);

        int m = int.Parse(Console.ReadLine());
        int[] queries = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++)
        {
            if (BinarySearch(A, queries[i]))
                sb.Append("1\n");
            else
                sb.Append("0\n");
        }

        Console.Write(sb.ToString());
    }
}
