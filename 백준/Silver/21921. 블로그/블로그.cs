using System;
using System.Linq;

class Program
{
    static void Main()
    {
        var nx = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = nx[0];
        int X = nx[1];

        int[] arr = Console.ReadLine().Split().Select(int.Parse).ToArray();

        int windowSum = 0;
        for (int i = 0; i < X; i++)
        {
            windowSum += arr[i];
        }

        int maxSum = windowSum;
        int count = 1;

        for (int i = X; i < N; i++)
        {
            windowSum = windowSum - arr[i - X] + arr[i];

            if (windowSum > maxSum)
            {
                maxSum = windowSum;
                count = 1;
            }
            else if (windowSum == maxSum)
            {
                count++;
            }
        }

        if (maxSum == 0)
        {
            Console.WriteLine("SAD");
        }
        else
        {
            Console.WriteLine(maxSum);
            Console.WriteLine(count);
        }
    }
}