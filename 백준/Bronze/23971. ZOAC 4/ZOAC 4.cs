using System;

class Program
{
    static void Main()
    {
        var s = Console.ReadLine().Split();
        int H = int.Parse(s[0]);
        int W = int.Parse(s[1]);
        int N = int.Parse(s[2]);
        int M = int.Parse(s[3]);

        int row = (H + N) / (N + 1);  // = ceil(H / (N+1))
        int col = (W + M) / (M + 1);  // = ceil(W / (M+1))

        Console.WriteLine(row * col);
    }
}
