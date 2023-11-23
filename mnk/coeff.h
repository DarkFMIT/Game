#ifndef COEFF_H
#define COEFF_H 1

struct Coeff
{
    double value; // coefficient estimate
    double delta; // confidence band 99                                                           999999  
    Coeff(double v, double d) : value{ v }, delta{ d }
    { /* empty body */
    }
};
#endif