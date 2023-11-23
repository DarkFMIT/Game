#include "least_squares.h"

std::tuple<Coeff, Coeff> least_squares(const std::vector<Point>&points)
{
    // compute average values
        size_t N = points.size();
    double x_ave = 0., x2_ave = 0.;
    double y_ave = 0., xy_ave = 0.;
    double y2_ave = 0.;
        for (const auto& p : points)
        {
        x_ave += p.x;
        x2_ave += p.x * p.x;
        y2_ave += p.y * p.y;
        y_ave += p.y;
        xy_ave += p.x * p.y;
        }
    x_ave /= N;
    x2_ave /= N;
    y2_ave /= N;
    y_ave /= N;
    xy_ave /= N;
   
        // compute linear coefficient estimate
        double b = (xy_ave - x_ave * y_ave) / (x2_ave - x_ave * x_ave);
        double delta_b, delta_a;
        delta_b = 1 / sqrt(N) * sqrt((y2_ave - y_ave * y_ave) / (x2_ave - x_ave * x_ave) - b * b);
        if (!std::isfinite(b))
        throw std::overflow_error{ "division by zero" };
   
        // compute constant coefficient estimate
        double a = y_ave - b * x_ave;
        delta_a = delta_b * sqrt(x2_ave - x_ave * x_ave);
           return std::make_tuple(Coeff{ a, delta_a }, Coeff{ b, delta_b });
    }