#include "read.h" 
std::vector<Point> read(const std::string& filename)
{
    std::ifstream ifs{ filename };
    if (!ifs)
        throw std::runtime_error{ "can't open file '" + filename + "'" };
    std::vector<Point> points;
    Point tmp;
    while(!ifs.eof())
    {
        ifs >> tmp;
        points.push_back(tmp);
    }
    return points;    
}