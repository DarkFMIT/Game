auto read(const string& filename, bool testing = false)
{
    string new_filename;

    //Choose operation
    if(testing)
        new_filename = "./Test_system/test_files/" + filename;
    else
        new_filename = "./files/" + filename;
    
    ifstream file{ new_filename };
    if (!file)
        throw runtime_error{ "Can't open file '" + filename + "'." };
    
    vector<Point> points;
    Point tmp_point;
    string now_string;

    while(!file.eof())
    {
        getline(file, now_string);
        vector<string> values;
        values = Is_correct(now_string);
        if(values.size() == 2)
        {
            tmp_point.x = stod(values[0]);
            tmp_point.y = stod(values[1]);
            points.push_back(tmp_point);
        }
    }
    return points;
}