using System;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        char[][] g = new char[N][];
        for (int i = 0; i < N; i++)
            g[i] = Console.ReadLine().ToCharArray();

        // 1) head: first '*'
        int headR = -1, headC = -1;
        for (int r = 0; r < N && headR == -1; r++)
        {
            for (int c = 0; c < N; c++)
            {
                if (g[r][c] == '*')
                {
                    headR = r; headC = c;
                    break;
                }
            }
        }

        // 2) heart
        int hr = headR + 1;
        int hc = headC;

        // 3) left arm
        int left = 0;
        for (int c = hc - 1; c >= 0 && g[hr][c] == '*'; c--) left++;

        // 4) right arm
        int right = 0;
        for (int c = hc + 1; c < N && g[hr][c] == '*'; c++) right++;

        // 5) waist
        int waist = 0;
        for (int r = hr + 1; r < N && g[r][hc] == '*'; r++) waist++;
        int waistEnd = hr + waist;

        // 6) left leg
        int leftLeg = 0;
        for (int r = waistEnd + 1, c = hc - 1; r < N && c >= 0 && g[r][c] == '*'; r++) leftLeg++;

        // 7) right leg
        int rightLeg = 0;
        for (int r = waistEnd + 1, c = hc + 1; r < N && c < N && g[r][c] == '*'; r++) rightLeg++;

        // output (1-indexed)
        Console.WriteLine($"{hr + 1} {hc + 1}");
        Console.WriteLine($"{left} {right} {waist} {leftLeg} {rightLeg}");
    }
}
