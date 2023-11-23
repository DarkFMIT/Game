bool Test_system()
{
    bool flag = true;
    ofstream Dop("./Test_system/Results");
    Dop.clear();
    Dop.close();
    ifstream names("./Test_system/names_of_files");
    string name_of_now;
    while(!names.eof())
    {
        names >> name_of_now;
        try
        {
            ofstream Dop("./Test_system/Results", ios_base::app);
            auto [a, b] = least_squares(read(name_of_now, true), false, true);
            Dop << "Slope coefficient = " << a.value << "  Error rate = " << a.delta << endl 
                << "Free member = " << b.value << "  Error rate = " << b.delta << endl;
            Dop.close();
        }
        catch (exception& e)
        {
            ofstream Dop("./Test_system/Results", ios_base::app);
            Dop << "error: " << e.what() << endl;
            Dop.close();
        }
    }
    ifstream Results("./Test_system/Results");
    ifstream Correct_results("./Test_system/Correct_results");
    string res, cor_res;
    while(!Results.eof() && !Correct_results.eof())
    {
        getline(Results, res);
        getline(Correct_results, cor_res);
        flag = flag && (res == cor_res);
    }
    flag = flag && Results.eof() && Correct_results.eof();
    return flag;
}