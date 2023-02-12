#include <iostream>
#include<fstream>
#include <bits/stdc++.h>
#include <chrono>
using namespace std::chrono;
using namespace std;
int main()
{
    fstream a;
    a.open("2GB.txt",ios::in);
    if(!a)
    cout<<"Error\n";
    char ch;
    auto start = high_resolution_clock::now();
    while(!a.eof())
    {
    a.get(ch);
    ch=toupper(ch);
    }
    auto stop = high_resolution_clock::now();
    double time_taken = chrono::duration_cast<chrono::milliseconds>(stop - start).count();
    cout <<setprecision(3)<<"C++ : "<<time_taken/1000<< endl;
    a.close();
    fstream fout;
    fout.open("cpp.txt",ios::app);
    fout<<setprecision(3)<<time_taken/1000<<endl;
    fout.close();
    return 0;
}