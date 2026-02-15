using System;
using System.Text;

class Program
{
    static void Main()
    {
        int P = int.Parse(Console.ReadLine());
        StringBuilder sb = new StringBuilder();

        for (int tc = 0; tc < P; tc++)
        {
            string[] parts = Console.ReadLine().Split();
            int T = int.Parse(parts[0]);

            int[] h = new int[20];
            for (int i = 0; i < 20; i++)
                h[i] = int.Parse(parts[i + 1]);

            int ans = 0;
            for (int i = 0; i < 20; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    if (h[j] > h[i]) ans++;
                }
            }

            sb.Append(T).Append(' ').Append(ans).Append('\n');
        }

        Console.Write(sb.ToString());
    }
}
