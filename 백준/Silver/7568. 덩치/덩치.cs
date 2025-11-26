using System;
using System.Text;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[,] people = new int[n, 2];

        for (int i = 0; i < n; i++)
        {
            string[] parts = Console.ReadLine().Split();
            people[i, 0] = int.Parse(parts[0]); 
            people[i, 1] = int.Parse(parts[1]);
        }

        int[] rank = new int[n];

        for (int i = 0; i < n; i++)
        {
            int cnt = 0;

            for (int j = 0; j < n; j++)
            {
                if (i == j) continue; 

 
                if (people[j, 0] > people[i, 0] && people[j, 1] > people[i, 1])
                {
                    cnt++;
                }
            }

            rank[i] = cnt + 1;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++)
        {
            sb.Append(rank[i]);
            if (i != n - 1) sb.Append(' ');
        }

        Console.WriteLine(sb.ToString());
    }
}
