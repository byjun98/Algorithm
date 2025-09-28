using System;

class Program
{
    static void Main()
    {
        int T = int.Parse(Console.ReadLine());

        for (int tc = 0; tc < T; tc++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] votes = new int[n];

            int total = 0;
            int mx = -1;
            int mxIdx = -1;

            for (int i = 0; i < n; i++)
            {
                votes[i] = int.Parse(Console.ReadLine());
                total += votes[i];

                if (votes[i] > mx)
                {
                    mx = votes[i];
                    mxIdx = i;
                }
            }

            int cnt = 0;
            for (int i = 0; i < n; i++)
                if (votes[i] == mx) cnt++;

            if (cnt >= 2)
            {
                Console.WriteLine("no winner");
            }
            else
            {
                int R = mxIdx + 1;
                if (mx * 2 > total)
                    Console.WriteLine($"majority winner {R}");
                else
                    Console.WriteLine($"minority winner {R}");
            }
        }
    }
}