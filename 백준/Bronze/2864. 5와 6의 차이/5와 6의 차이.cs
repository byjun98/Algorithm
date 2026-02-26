using System;

class Program
{
    static void Main()
    {
        var parts = Console.ReadLine().Split();
        string A = parts[0];
        string B = parts[1];

        int Amin = int.Parse(A.Replace('6', '5'));
        int Bmin = int.Parse(B.Replace('6', '5'));
        int Amax = int.Parse(A.Replace('5', '6'));
        int Bmax = int.Parse(B.Replace('5', '6'));

        Console.WriteLine($"{Amin + Bmin} {Amax + Bmax}");
    }
}