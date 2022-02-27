using System.Diagnostics;

internal class PyRwu
{
    static void Main(string[] args)
    {
        //Console.WriteLine(DateTime.Now.Millisecond);
        string exePath = System.Reflection.Assembly.GetEntryAssembly().Location;
        String python = Path.Combine(Path.GetDirectoryName(exePath), "python-3.9.10", "python.exe");
        String endpoint = Path.Combine(Path.GetDirectoryName(exePath), "src", "PyRwu.py");
        //Console.WriteLine(DateTime.Now.Millisecond);
        Process p = Process.Start(python, endpoint + " " + String.Join(" ", args));
        //Console.WriteLine(DateTime.Now.Millisecond);
        //Process p = Process.Start(python, "-m cProfile -s tottime " + endpoint + " " + String.Join(" ", args));
        //Console.WriteLine(DateTime.Now.Millisecond);
        p.WaitForExit();
        //Console.WriteLine(DateTime.Now.Millisecond);
    }
}