auto Is_correct(string line_from_file)
{
    vector<string> values;
    string tmp_string = "";
    int minuses = 0, dots = 0;
    for(long long s = 0; s < line_from_file.size(); s++)
    {
        if(line_from_file[s] == ' ')
        {
            if(tmp_string == "-")
                throw logic_error{ "Incorrect points. The value without numbers." };
            
            if(tmp_string.size() != 0)
            {
                values.push_back(tmp_string);
            }
            tmp_string = "";
            minuses = 0;
            dots = 0;
        }
        else
        {
            if(line_from_file[s] == '.' || line_from_file[s] == ',')
            {
                dots += 1;
                if(dots > 1 || (tmp_string.size() - minuses) == 0 )
                //More then 1 dot in number or " -. "/" . " situation
                    throw logic_error{ "Incorrect points. Too much dots or dot at the first place." };
                tmp_string += '.';
            }
            else
                if(line_from_file[s] == '-')
                {
                    minuses += 1;
                    if(minuses > 1 || tmp_string.size() > 0)
                    //More then 1 minus or minus in the number "12-23"
                        throw logic_error{ "Incorrect points. Too much minuses or minus in the center." };
                    tmp_string += '-';
                }
                else
                    if(line_from_file[s] >= '0' && line_from_file[s] <= '9')
                    {
                        tmp_string += line_from_file[s];
                    }
                    else
                    //Something that can't be in a number
                        throw logic_error{ "Incorrect points. Unknown sign." };
        }
    }
    
    if(tmp_string.size() != 0)  //Add last number
    {
        if(tmp_string == "-")
        //Only "-"(another situations can't be)
            throw logic_error{ "Incorrect points. The value without numbers." };
        values.push_back(tmp_string);
    }

    if(values.size() != 0 && values.size() != 2)
        //Not 2 points in line
        throw logic_error{ "Incorrect points. Must be 2 values in one line." };
    return values;
}