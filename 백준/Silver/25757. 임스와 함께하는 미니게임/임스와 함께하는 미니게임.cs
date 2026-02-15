using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var first = Console.ReadLine().Split();
        int N = int.Parse(first[0]);
        char game = first[1][0];

        int need = (game == 'Y') ? 1 : (game == 'F' ? 2 : 3);

        var set = new HashSet<string>();
        for (int i = 0; i < N; i++)
        {
            string name = Console.ReadLine().Trim();
            set.Add(name);
        }

        Console.WriteLine(set.Count / need);
    }
}
