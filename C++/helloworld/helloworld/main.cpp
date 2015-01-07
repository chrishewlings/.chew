//
//  main.cpp
//  helloworld
//
//  Created by Chris Hewlings on 2014-07-02.
//  Copyright (c) 2014 Chris Hewlings. All rights reserved.
//

#include <iostream>
using namespace std;

string doPrint(string x)
{
    cout << x << endl;
    return x;
}

int multiply(int z, int w)
{
    return z * w;
}

int main()
{
    doPrint("string");
}