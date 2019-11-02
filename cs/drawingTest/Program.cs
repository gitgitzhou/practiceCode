using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
 
namespace drawingTest
{
    class Program
    {
        static void Main(string[] args)
        {
			Image image = new Bitmap(2000, 1024);

			Graphics graph = Graphics.FromImage(image);

			graph.Clear(Color.Azure);

			Pen pen = new Pen(Brushes.Black);

			graph.DrawLines(pen, new Point[] { new Point(10,10), new Point(800, 900) });

			graph.DrawString("Hello drawing from .NET Core :)", 
			new Font(new FontFamily("DecoType Thuluth"), 20,  FontStyle.Bold), 
			Brushes.Blue, new PointF(150, 90));

			image.Save("graph.jpeg", System.Drawing.Imaging.ImageFormat.Png);

        }
    }
}
