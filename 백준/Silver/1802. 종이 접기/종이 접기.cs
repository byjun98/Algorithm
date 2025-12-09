using System;

class Program
{
    static bool Check(string S)
    {
        int n = S.Length;

        if (n == 1) return true;

        int mid = n / 2;

        for (int i = 0; i < mid; i++)
        {
            if (S[mid - 1 - i] == S[mid + 1 + i])
                return false;
        }

        string left = S.Substring(0, mid);
        string right = S.Substring(mid + 1);

        return Check(left) && Check(right);
    }

    static void Main()
    {
        int T = int.Parse(Console.ReadLine());

        while (T-- > 0)
        {
            string S = Console.ReadLine();
            if (Check(S)) Console.WriteLine("YES");
            else Console.WriteLine("NO");
        }
    }
}
