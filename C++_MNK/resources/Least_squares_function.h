

pair<Coeff, Coeff> least_squares(const vector<Point>&points, bool Dop_information = false, bool testing_system_on = false)
{
    // compute average values
        size_t N = points.size();
    if(N == 0)
        throw overflow_error{ "No points in a file." };
    double x_ave = 0., x2_ave = 0.;
    double y_ave = 0., xy_ave = 0.;
    double y2_ave = 0.;
   
        for (auto& p : points)
        {
        y2_ave += p.y * p.y;
        x_ave += p.x;
        x2_ave += p.x * p.x;
        y_ave += p.y;
        xy_ave += p.x * p.y;
        }
    y2_ave /= N;
    x_ave /= N;
    x2_ave /= N;
    y_ave /= N;
    xy_ave /= N;
           // compute linear coefficient estimate
        double a = (xy_ave - x_ave * y_ave) / (x2_ave - x_ave * x_ave);
        if (x2_ave - x_ave * x_ave == 0)
        throw overflow_error{ "division by zero" };
    if(Dop_information)
    {
        ofstream Dop("./results/Dop_information.txt");
        Dop.clear();
        Dop << "<y> = " << y_ave << endl;
        Dop << "<y * y> = " << y2_ave << endl;
        Dop << "<y> * <y> = " << y_ave * y_ave << endl;
        Dop << "<x> = " << x_ave << endl;
        Dop << "<x * x> = " << x2_ave << endl;
        Dop << "<x> * <x> = " << x_ave * x_ave << endl;
        Dop << "<y * x> = " << xy_ave << endl;
        Dop.close();
    }
    if(testing_system_on)
    {
        ofstream Dop("./Test_system/Results", ios_base::app);
        Dop << "<y> = " << y_ave << endl;
        Dop << "<y * y> = " << y2_ave << endl;
        Dop << "<y> * <y> = " << y_ave * y_ave << endl;
        Dop << "<x> = " << x_ave << endl;
        Dop << "<x * x> = " << x2_ave << endl;
        Dop << "<x> * <x> = " << x_ave * x_ave << endl;
        Dop << "<y * x> = " << xy_ave << endl;
        Dop.close();
    }
   
        // compute constant coefficient estimate
        double b = y_ave - a * x_ave;
        double delta_a, delta_b;
        delta_a = 1 / sqrt(N) * sqrt((y2_ave - y_ave * y_ave) / (x2_ave - x_ave * x_ave) - a * a);
        delta_b = delta_a * sqrt(x2_ave - x_ave * x_ave);
           return make_pair(Coeff{ a, delta_a }, Coeff{ b, delta_b });
    }