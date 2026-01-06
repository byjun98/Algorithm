using System;
using System.Text;

class FastScanner
{
    private readonly byte[] _buffer = new byte[1 << 16];
    private int _ptr = 0, _len = 0;

    private int ReadByte()
    {
        if (_ptr >= _len)
        {
            _len = Console.OpenStandardInput().Read(_buffer, 0, _buffer.Length);
            _ptr = 0;
            if (_len <= 0) return -1;
        }
        return _buffer[_ptr++];
    }

    public int NextInt()
    {
        int c;
        do c = ReadByte(); while (c <= 32);
        int sign = 1;
        if (c == '-')
        {
            sign = -1;
            c = ReadByte();
        }
        int val = 0;
        while (c > 32)
        {
            val = val * 10 + (c - '0');
            c = ReadByte();
        }
        return val * sign;
    }
}

class Program
{
    static void Main()
    {
        var fs = new FastScanner();
        int K = fs.NextInt();
        int N = fs.NextInt();

        long[] arr = new long[K];
        long hi = 0;
        for (int i = 0; i < K; i++)
        {
            arr[i] = fs.NextInt();
            if (arr[i] > hi) hi = arr[i];
        }

        long lo = 1;
        long ans = 1;

        while (lo <= hi)
        {
            long mid = (lo + hi) / 2;
            long cnt = 0;
            for (int i = 0; i < K; i++)
                cnt += arr[i] / mid;

            if (cnt >= N)
            {
                ans = mid;
                lo = mid + 1;
            }
            else
            {
                hi = mid - 1;
            }
        }

        Console.WriteLine(ans);
    }
}
