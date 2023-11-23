#ifndef POINT_H
#define POINT_H 1


#include "const.h"

struct Point
{
    double x, y;
    Point() = default;
    Point(double _x, double _y) : x{ _x }, y{ _y } {}

};

std::istream& operator >> (std::istream& is, Point& p);

std::ostream& operator << (std::ostream& os, const Point& p);

#endif //POINT_H