using System;
using System.Text;

public class Program
{
    // 빠른 입력
    sealed class FastScanner
    {
        private readonly byte[] _buffer = new byte[1 << 16];
        private int _idx, _size;
        private readonly System.IO.Stream _stream = Console.OpenStandardInput();

        private byte ReadByte()
        {
            if (_idx >= _size)
            {
                _size = _stream.Read(_buffer, 0, _buffer.Length);
                _idx = 0;
                if (_size == 0) return 0;
            }
            return _buffer[_idx++];
        }

        public int NextInt()
        {
            byte c;
            do c = ReadByte(); while (c <= 32);

            int sign = 1;
            if (c == (byte)'-')
            {
                sign = -1;
                c = ReadByte();
            }

            int val = 0;
            while (c > 32)
            {
                val = val * 10 + (c - (byte)'0');
                c = ReadByte();
            }
            return val * sign;
        }
    }

    public static void Main()
    {
        var fs = new FastScanner();
        int T = fs.NextInt();
        var sb = new StringBuilder();

        const long NEG = -1000000000000000000L; // -1e18

        while (T-- > 0)
        {
            int n = fs.NextInt();
            int[] top = new int[n];
            int[] bot = new int[n];

            for (int i = 0; i < n; i++) top[i] = fs.NextInt();
            for (int i = 0; i < n; i++) bot[i] = fs.NextInt();

            long dp0 = 0, dp1 = NEG, dp2 = NEG;

            for (int i = 0; i < n; i++)
            {
                long new0 = Math.Max(dp0, Math.Max(dp1, dp2));
                long new1 = Math.Max(dp0, dp2) + top[i];
                long new2 = Math.Max(dp0, dp1) + bot[i];

                dp0 = new0;
                dp1 = new1;
                dp2 = new2;
            }

            long ans = Math.Max(dp0, Math.Max(dp1, dp2));
            sb.Append(ans).Append('\n');
        }

        Console.Write(sb.ToString());
    }
}