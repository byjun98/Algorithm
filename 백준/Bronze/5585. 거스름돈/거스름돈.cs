using System;

class Program
{
    static void Main()
    {
        int X = int.Parse(Console.ReadLine());
        int change = 1000 - X;

        int[] coins = { 500, 100, 50, 10, 5, 1 };
        int count = 0;

        foreach (int coin in coins)
        {
            count += change / coin;
            change %= coin;
        }

        Console.WriteLine(count);
    }
}