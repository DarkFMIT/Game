#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>
#include <iterator>
#include <stdexcept>
#include <cmath>
#include <string>
#include "windows.h"
using namespace std;
#include "./resources/struct_Point.h"
#include "./resources/struct_Coeff.h"
#include "./resources/Is_correct_input.h"
#include "./resources/Least_squares_read_from_file.h"
#include "./resources/Least_squares_function.h"
#include "./resources/Testing_system.h"

int main()
{
    cout << "Please, put file with your points in this folder" << endl;
    Sleep(1000);
    system("explorer \".\\files\"");
    Sleep(3000);
    string filename, dop_inf;
    double slope, free;
    cout << "Please, enter the file name: ";
    cin >> filename;

    // Part for test system
    if(filename == "Start_test_system")
    {
        if(Test_system())
            cout << "The programm is correct" << endl;
        else
            cout << "Mistake! Mistake! Mistake!" << endl;
        system("pause");
        return 0;
    }

    cout << "If you want more information about your points, enter Yes\n";
    cin >> dop_inf;
    try
    {
        auto [a, b] = least_squares(read(filename), dop_inf == "Yes"); // C++17 
        slope = a.value;
        free = b.value;
        ofstream results("./results/Results.txt");
        results << "Slope coefficient = " << a.value << "  Error rate = " << a.delta << endl 
            << "Free member = " << b.value << "  Error rate = " << b.delta << endl;
        cout << "Successfully finished" << endl;
    }
    catch (exception& e)
    {
        ofstream results("./Results.txt");
        results << "error: " << e.what() << endl;
        cerr << "error: " << e.what() << endl;
        system("pause");
        return 1;
    }

    // Сохраняем информацию для построения графика 
    ofstream Help("./python//help_information.txt");
    Help << filename << endl;
    Help << slope << " " << free;
    Help.close();
    system("start ./python/python_script_for_grafics.exe");
    cout << "Graph will be ready in 15 seconds." << endl;
    Sleep(15000);
    system("move Grafic.png ./results");
    system("explorer \".\\results\"");
}