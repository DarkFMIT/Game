struct Point
{
    double x, y;
    Point() = default;
    Point(double _x, double _y) : x{ _x }, y{ _y } {}

};
istream& operator >> (istream& is, Point& p)
{
    is >> p.x >> p.y;
    return is;
}
ostream& operator << (ostream& os, const Point& p)
{
    os << p.x << " " << p.y;
    return os;
}