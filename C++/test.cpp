#include <iostream>


using namespace std;

string getUserInput()
{
    string x;
    cout << "Write a string of letters without spaces.";
    cin >> x;
    return x;
}

int printUserInput(string butts)
{
	cout << butts << endl;
	return 0;
}

int main()
{
	string thing;
    thing = getUserInput();
    printUserInput(thing);
}