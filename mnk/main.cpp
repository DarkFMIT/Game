using namespace std;
#include "point.h"
#include "coeff.h"
#include "read.h"
#include "least_squares.h"

int main()
{
    string filename;
    cout << "Give me filename ";
    cin >> filename;
    try
    {
        auto [a, b] = least_squares(read(filename)); 
        cout << "k = " << a.value << " delta_k = " << a.delta << "\nb = "
            << b.value << " delta_b = " << b.delta << endl;
    }
    catch (exception& e)
    {
        cerr << "error: " << e.what() << endl;
        return 1;
    }
}