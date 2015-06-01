// multidimensional arrays

#include <iostream>

using namespace std;

//int multiDimArray[3][5]; // a multidimensional array. 3 element array of 5 element arrays. 

// defined thusly

int multiDimArray[3][5] = 
{
{ 1, 2, 3, 4, 5}, // row 0
{ 6, 7, 8, 9, 10 }, // row 1
{ 11, 12, 13, 14, 15} // row 2
}; // like a struct, end with ;

int main() // prints out the values of multiDimArray
{
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cout << multiDimArray[i][j] << " ";
			if (j == 4)
			{
				cout << endl;
			}
		}
	}
	
	return 0;
}