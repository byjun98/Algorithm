using System;

class Program
{
    static void Main()
    {
        var parts = Console.ReadLine().Split();
        int E = int.Parse(parts[0]);
        int S = int.Parse(parts[1]);
        int M = int.Parse(parts[2]);

        int year = 1;
        while (true)
        {
            if ((year - 1) % 15 + 1 == E &&
                (year - 1) % 28 + 1 == S &&
                (year - 1) % 19 + 1 == M)
            {
                Console.WriteLine(year);
                break;
            }
            year++;
        }
    }
}
