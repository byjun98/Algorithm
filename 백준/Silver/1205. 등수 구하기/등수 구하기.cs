using System;
using System.Linq;

class Program
{
    static void Main()
    {
        var first = Console.ReadLine().Split();
        int N = int.Parse(first[0]);
        int S = int.Parse(first[1]);
        int P = int.Parse(first[2]);

        if (N == 0)
        {
            Console.WriteLine(1);
            return;
        }

        int[] scores = Console.ReadLine().Split().Select(int.Parse).ToArray();

        // 랭킹이 꽉 찼는데 새 점수가 마지막보다 좋지 않으면 진입 불가
        if (N == P && S <= scores[N - 1])
        {
            Console.WriteLine(-1);
            return;
        }

        int rank = 1;
        for (int i = 0; i < N; i++)
        {
            if (scores[i] > S) rank++;
            else break; // 내림차순이라 여기서 종료 가능
        }

        Console.WriteLine(rank);
    }
}
