using System.Diagnostics;

internal class PyRwuIniquity
{
    static void Main(string[] args)
    {
        string exePath = System.Reflection.Assembly.GetEntryAssembly().Location;
        String python = Path.Combine(Path.GetDirectoryName(exePath), "python-3.9.10", "python.exe");
        String endpoint = Path.Combine(Path.GetDirectoryName(exePath), "src", "PyRwuIniquity.py");
        Process p = Process.Start(python, endpoint + " " + String.Join(" ", args));
        //Process p = Process.Start(python, "-m cProfile " + endpoint + " " + String.Join(" ", args));
        p.WaitForExit();
    }
}