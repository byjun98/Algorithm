using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        int T = int.Parse(Console.ReadLine());

        for (int i = 0; i < T; i++)
        {
            var parts = Console.ReadLine().Split();
            double value = double.Parse(parts[0], CultureInfo.InvariantCulture);
            string unit = parts[1];

            double result = 0;
            string newUnit = "";

            if (unit == "kg")
            {
                result = value * 2.2046;
                newUnit = "lb";
            }
            else if (unit == "lb")
            {
                result = value * 0.4536;
                newUnit = "kg";
            }
            else if (unit == "l")
            {
                result = value * 0.2642;
                newUnit = "g";
            }
            else // g
            {
                result = value * 3.7854;
                newUnit = "l";
            }

            Console.WriteLine($"{result:F4} {newUnit}");
        }
    }
}