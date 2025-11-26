using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string[] first = Console.ReadLine().Split();
        int n = int.Parse(first[0]);
        int w = int.Parse(first[1]);
        int L = int.Parse(first[2]);

        string[] line = Console.ReadLine().Split();
        int[] trucks = Array.ConvertAll(line, int.Parse);

        Queue<int> bridge = new Queue<int>();
        for (int i = 0; i < w; i++)
            bridge.Enqueue(0);

        int time = 0;
        int currentWeight = 0;
        int idx = 0;

        while (idx < n)
        {
            time++;

            int outTruck = bridge.Dequeue();
            currentWeight -= outTruck;

            if (currentWeight + trucks[idx] <= L)
            {
                bridge.Enqueue(trucks[idx]);
                currentWeight += trucks[idx];
                idx++;
            }
            else
            {
                bridge.Enqueue(0);
            }
        }

        time += w;

        Console.WriteLine(time);
    }
}
