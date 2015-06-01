// enumerated types
//define a new enumerator named color
#include <iostream>
using namespace std;

enum Color
{
	//every possible value is a symbolic constant
	COLOR_BLACK, //0
	COLOR_RED,
	COLOR_BLUE,
	COLOR_GREEN,
	COLOR_WHITE,
	COLOR_CYAN,
	COLOR_YELLOW,
	COLOR_MAGENTA, //7

	// values of constants can be defined here explicitly
	// they're just 0-7 here because nothing else was defined
	// any non defined enumerator is given a value one higher
	// than the one that precedes it
};

Color eColor = COLOR_WHITE;


int main()
{
	cout << eColor;
	return 0;
}