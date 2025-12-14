using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine()); // 전체 사람 수

        string[] ab = Console.ReadLine().Split();
        int start = int.Parse(ab[0]); // 촌수 계산 시작 사람
        int end = int.Parse(ab[1]);   // 촌수 계산 대상 사람

        int m = int.Parse(Console.ReadLine()); // 부모-자식 관계 수

        // 인접 리스트 그래프 생성
        List<int>[] graph = new List<int>[n + 1];
        for (int i = 1; i <= n; i++)
            graph[i] = new List<int>();

        // 관계 입력 (양방향)
        for (int i = 0; i < m; i++)
        {
            string[] input = Console.ReadLine().Split();
            int parent = int.Parse(input[0]);
            int child = int.Parse(input[1]);

            graph[parent].Add(child);
            graph[child].Add(parent);
        }

        // BFS 준비
        bool[] visited = new bool[n + 1];
        Queue<(int person, int dist)> q = new Queue<(int, int)>();

        q.Enqueue((start, 0));
        visited[start] = true;

        while (q.Count > 0)
        {
            var (cur, dist) = q.Dequeue();

            if (cur == end)
            {
                Console.WriteLine(dist); // 촌수 출력
                return;
            }

            foreach (int next in graph[cur])
            {
                if (!visited[next])
                {
                    visited[next] = true;
                    q.Enqueue((next, dist + 1));
                }
            }
        }

        // 끝까지 못 찾은 경우
        Console.WriteLine(-1);
    }
}
