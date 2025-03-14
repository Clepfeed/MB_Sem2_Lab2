#include <iostream>
#include <vector>
#include <fstream>

#define PI 3.14159265358979323846

using namespace std;

double f1(double x)
{
    return cos(2 * x);
}

double f2(double x)
{
    return sin(abs(x)) + 1;
}

vector<vector<double>> equidistantNodes(int n, int a, int b, double (*f)(double))
{
    vector<vector<double>> f_x(2, vector<double>(n, 0)); // [0] -> x | [1] -> f(x)
    double h = double(b - a) / (n - 1);

    for (int i = 0; i < n; i++)
    {
        f_x[0][i] = a + i * h;
        f_x[1][i] = f(f_x[0][i]);
    }

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = n - 1; j > i; j--)
        {
            f_x[1][j] = (f_x[1][j] - f_x[1][j - 1]) / (f_x[0][j] - f_x[0][j - i - 1]);
        }
    }

    return f_x;
}

vector<vector<double>> chebyshevKnots(int n, int a, int b, double (*f)(double))
{
    vector<vector<double>> f_x(2, vector<double>(n, 0)); // [0] -> x | [1] -> f(x)

    for (int i = 0; i < n; i++)
    {
        f_x[0][i] = (a + b) / 2 + ((b - a) / 2) * cos(((2 * i - 1) * PI) / 2 * (n + 1));
        f_x[1][i] = f(f_x[0][i]);
    }

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = n - 1; j > i; j--)
        {
            f_x[1][j] = (f_x[1][j] - f_x[1][j - 1]) / (f_x[0][j] - f_x[0][j - i - 1]);
        }
    }

    return f_x;
}

void valuesOfPoint(vector<vector<double>>& f, vector<double>& x, int& n)
{
    for (int i = 0; i < x.size(); i++)
    {
        double res = f[1][n - 1];
        for (int q = n - 2; q >= 0; q--)
        {
            res = f[1][q] + (x[i] - f[0][q]) * res;
        }
        x[i] = res;
    }
}

void tableOut(vector<double>& x, vector<double>& f_x, string name)
{
    ofstream fout(name);
    for (int i = 0; i < x.size(); i++)
    {
        fout << x[i] << " " << f_x[i] << "\n";
    }
}

int main()
{
    int n;
    double a = -2;
    double b = 2;
    vector<vector<double>> f;
    vector<double> x(100, 0);
    vector<double> f_x(100, 0);

    for (int i = 0; i < 100; i++)
    {
        x[i] = a + (i * (b - a)) / 100;
    }

    // Equidstand:
    // f1:
    n = 3;
    f = equidistantNodes(n, a, b, f1);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "P1_1.txt");

    n = 10;
    f = equidistantNodes(n, a, b, f1);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "P2_1.txt");

    n = 20;
    f = equidistantNodes(n, a, b, f1);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "P3_1.txt");
    
    // f2:
    n = 3;
    f = equidistantNodes(n, a, b, f2);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "P1_2.txt");

    n = 10;
    f = equidistantNodes(n, a, b, f2);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "P2_2.txt");

    n = 20;
    f = equidistantNodes(n, a, b, f2);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "P3_2.txt");

    // Chebyshev:
    // f1:
    n = 3;
    f = chebyshevKnots(n, a, b, f1);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "C1_1.txt");

    n = 10;
    f = chebyshevKnots(n, a, b, f1);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "C2_1.txt");

    n = 20;
    f = chebyshevKnots(n, a, b, f1);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "C3_1.txt");

    // f2:
    n = 3;
    f = chebyshevKnots(n, a, b, f2);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "C1_2.txt");

    n = 10;
    f = chebyshevKnots(n, a, b, f2);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "C2_2.txt");

    n = 20;
    f = chebyshevKnots(n, a, b, f2);
    f_x = x;
    valuesOfPoint(f, f_x, n);
    tableOut(x, f_x, "C3_2.txt");

    return 0;
}