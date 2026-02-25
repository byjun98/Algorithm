using System;

class Program
{
    static void Main()
    {
        for (int i = 0; i < 3; i++)
        {
            var parts = Console.ReadLine().Split();
            int h1 = int.Parse(parts[0]);
            int m1 = int.Parse(parts[1]);
            int s1 = int.Parse(parts[2]);
            int h2 = int.Parse(parts[3]);
            int m2 = int.Parse(parts[4]);
            int s2 = int.Parse(parts[5]);

            int start = h1 * 3600 + m1 * 60 + s1;
            int end = h2 * 3600 + m2 * 60 + s2;
            int diff = end - start;

            int h = diff / 3600;
            int m = (diff % 3600) / 60;
            int s = diff % 60;

            Console.WriteLine($"{h} {m} {s}");
        }
    }
}