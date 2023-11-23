

struct Coeff
{
    double value; // coefficient estimate
    double delta; // confidence band
    Coeff(double v, double d) : value{ v }, delta{ d }
    { /* empty body */
    }
};
istream& operator >> (istream& is, Coeff& c)
{
    is >> c.value >> c.delta;
    return is;
}
ostream& operator << (ostream& os, const Coeff& c)
{
    os << c.value << " " << c.delta;
    return os;
}