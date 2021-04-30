#include<iostream>
 #include <bits/stdc++.h>
using namespace std;


int main()
{
    int i;
    fstream fout;
    fout.open("data.csv", ios::out | ios::app); 
   
   double data[]={1200,1300,1400,1260,1260,1230,1300};
   string time[]= {"12:00:01","12:00:02","12:00:00","12:00:04","12:00:05","12:00:06","12:00:07"};
    int size = sizeof(data);
    for(i=0;i<size;i++)
    {
        fout<<data[i]<<","<<time[i]<<endl;
    }

return 0;
}
