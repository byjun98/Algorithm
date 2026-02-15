using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        int T = int.Parse(Console.ReadLine());
        for (int tc = 0; tc < T; tc++)
        {
            int N = int.Parse(Console.ReadLine());
            int[] arr = Console.ReadLine().Split().Select(int.Parse).ToArray();

            // 1) 팀별 출전 인원 카운트
            var cnt = new Dictionary<int, int>();
            foreach (var t in arr)
            {
                if (!cnt.ContainsKey(t)) cnt[t] = 0;
                cnt[t]++;
            }

            var eligible = new HashSet<int>(cnt.Where(kv => kv.Value == 6).Select(kv => kv.Key));

            // 2) 자격 팀만 점수 부여하면서 팀 점수 계산
            var seen = new Dictionary<int, int>();
            var sum4 = new Dictionary<int, int>();
            var fifth = new Dictionary<int, int>();

            foreach (var t in eligible)
            {
                seen[t] = 0;
                sum4[t] = 0;
                fifth[t] = int.MaxValue;
            }

            int score = 0;
            foreach (var t in arr)
            {
                if (!eligible.Contains(t)) continue;

                score++;
                seen[t]++;

                if (seen[t] <= 4) sum4[t] += score;
                else if (seen[t] == 5) fifth[t] = score;
            }

            // 3) 최소 (sum4, fifth) 팀 찾기
            int bestTeam = -1;
            int bestSum = int.MaxValue;
            int bestFifth = int.MaxValue;

            foreach (var t in eligible)
            {
                int s = sum4[t];
                int f = fifth[t];
                if (s < bestSum || (s == bestSum && f < bestFifth))
                {
                    bestSum = s;
                    bestFifth = f;
                    bestTeam = t;
                }
            }

            Console.WriteLine(bestTeam);
        }
    }
}
