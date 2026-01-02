using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine()!.Trim());
        Console.Write(new string('a', n));
    }
}
