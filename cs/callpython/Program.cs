using System;
using System.Diagnostics;
using System.IO;
using System.Threading.Tasks;

namespace callpython
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Console.WriteLine("Hello World!"); */
            int x = 1;
            int y = 2;
            string progToRun = "/home/jianfenz/practiceCode/cs/callpython/hello.py";
            char[] splitter = {'\r'};
 
            Process proc = new Process();
            proc.StartInfo.FileName = "python";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
             
            // call hello.py to concatenate passed parameters
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", x.ToString(), " ", y.ToString());
            proc.Start();
 
            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);
 
            foreach (string s in output)
                Console.WriteLine(s);
 
            proc.WaitForExit();
 
            Console.ReadLine();
        }
    }
}
