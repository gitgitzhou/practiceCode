using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FocusFinderLibrary
{
    public class FocusFinder
    {
        public double focusValue;
        public double motorPosition;

        public void SetFocusVal(double focusVal)
        {
            focusValue = focusVal;
        }
        public void SetMotorPos(double motorPos)
        {
            motorPosition = motorPos;
        }
        public void PrintVal()
        {
            Console.WriteLine($"The current focus value is: {focusValue}");
            Console.WriteLine($"The current motor position is: {motorPosition}");
        }
        public bool MoveMotor()
        {
            return true;
        }
    }
}
