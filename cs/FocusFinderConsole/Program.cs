using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using FocusFinderLibrary;

namespace ConsoleAppFocusFinder
{
    class Program
    {
        static void Main(string[] args)
        {
            bool moveFlag;
            FocusFinder Finder = new FocusFinder();
            Finder.SetFocusVal(100.0);
            Finder.SetMotorPos(1.0);
            Finder.PrintVal();
            moveFlag = Finder.MoveMotor();
            Console.WriteLine($"move motor flag: {moveFlag}");
            Console.ReadKey();
            
        }
    }
}
