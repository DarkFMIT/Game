#ifndef LEAST_SQ_H
#define LEAST_SQ_H 1 

#include "const.h"
#include "point.h"
#include "coeff.h"

std::tuple<Coeff, Coeff> least_squares(const std::vector<Point>&points);

#endif 
