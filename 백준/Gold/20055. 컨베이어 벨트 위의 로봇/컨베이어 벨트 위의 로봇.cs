using System;
using System.Linq;

public class Program
{
    public static void Main()
    {
        var first = Console.ReadLine().Split();
        int N = int.Parse(first[0]);
        int K = int.Parse(first[1]);

        int[] A = Console.ReadLine().Split().Select(int.Parse).ToArray(); // length 2N
        bool[] robots = new bool[N]; // only upper positions

        int step = 0;
        int zeroCnt = 0;
        for (int i = 0; i < 2 * N; i++) if (A[i] == 0) zeroCnt++;

        while (true)
        {
            step++;

            // 1) rotate A right by 1
            int last = A[2 * N - 1];
            for (int i = 2 * N - 1; i >= 1; i--) A[i] = A[i - 1];
            A[0] = last;

            // rotate robots right by 1 (within N)
            bool rLast = robots[N - 1];
            for (int i = N - 1; i >= 1; i--) robots[i] = robots[i - 1];
            robots[0] = rLast;

            robots[N - 1] = false; // drop

            // 2) move robots right to left
            for (int i = N - 2; i >= 0; i--)
            {
                if (robots[i] && !robots[i + 1] && A[i + 1] > 0)
                {
                    robots[i] = false;
                    robots[i + 1] = true;
                    A[i + 1]--;
                    if (A[i + 1] == 0) zeroCnt++;
                }
            }

            robots[N - 1] = false; // drop

            // 3) place new robot at 0
            if (!robots[0] && A[0] > 0)
            {
                robots[0] = true;
                A[0]--;
                if (A[0] == 0) zeroCnt++;
            }

            // 4) check
            if (zeroCnt >= K)
            {
                Console.WriteLine(step);
                return;
            }
        }
    }
}
