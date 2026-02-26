using System;

class Program
{
    static void Main()
    {
        int cnt = 0;

        for (int r = 0; r < 8; r++)
        {
            string line = Console.ReadLine();
            for (int c = 0; c < 8; c++)
            {
                if (((r + c) % 2 == 0) && line[c] == 'F')
                    cnt++;
            }
        }

        Console.WriteLine(cnt);
    }
}