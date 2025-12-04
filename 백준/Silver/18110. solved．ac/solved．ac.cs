using System;

class Program
{
    static void Main()
    {
        string inputN = Console.ReadLine();
        if (inputN == null) return; 
        int n = int.Parse(inputN);

        if (n == 0)
        {
            Console.WriteLine(0);
            return;
        }

        int[] scores = new int[n];
        for (int i = 0; i < n; i++)
        {
            scores[i] = int.Parse(Console.ReadLine());
        }

        Array.Sort(scores);

        int cut = (int)Math.Round(n * 0.15, MidpointRounding.AwayFromZero);

        double sum = 0;
        for (int i = cut; i < n - cut; i++)
        {
            sum += scores[i];
        }

        int count = n - (2 * cut);
        double result = sum / count;

        Console.WriteLine((int)Math.Round(result, MidpointRounding.AwayFromZero));
    }
}