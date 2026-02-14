using System;
using System.Text;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        var dq = new LinkedList<int>();
        var sb = new StringBuilder();

        for (int i = 0; i < n; i++)
        {
            string line = Console.ReadLine();
            // split 최소화
            if (line.StartsWith("push_front"))
            {
                int x = int.Parse(line.Substring(11));
                dq.AddFirst(x);
            }
            else if (line.StartsWith("push_back"))
            {
                int x = int.Parse(line.Substring(10));
                dq.AddLast(x);
            }
            else if (line == "pop_front")
            {
                if (dq.Count == 0) sb.AppendLine("-1");
                else { sb.AppendLine(dq.First.Value.ToString()); dq.RemoveFirst(); }
            }
            else if (line == "pop_back")
            {
                if (dq.Count == 0) sb.AppendLine("-1");
                else { sb.AppendLine(dq.Last.Value.ToString()); dq.RemoveLast(); }
            }
            else if (line == "size")
            {
                sb.AppendLine(dq.Count.ToString());
            }
            else if (line == "empty")
            {
                sb.AppendLine(dq.Count == 0 ? "1" : "0");
            }
            else if (line == "front")
            {
                sb.AppendLine(dq.Count == 0 ? "-1" : dq.First.Value.ToString());
            }
            else if (line == "back")
            {
                sb.AppendLine(dq.Count == 0 ? "-1" : dq.Last.Value.ToString());
            }
        }

        Console.Write(sb.ToString());
    }
}
