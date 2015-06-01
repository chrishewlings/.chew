//first try at bitwise arithmetic

#include <iostream>
using namespace std;

uint8_t option1 = 0x01;
uint8_t option2 = 0x02;
uint8_t option3 = 0x04;
uint8_t option4 = 0x08;
uint8_t option5 = 0x10;
uint8_t option6 = 0x20;
uint8_t option7 = 0x40;
uint8_t option8 = 0x80;

unsigned char myflags;

int main()
{
	myflags |= option7;
	myflags |= option5;
	
	int bitCounter = 1;
	while (bitCounter < 9)
	{
		if(myflags & 0x01)
		{
			printf("bit %d is 1\n", bitCounter);
		}
		else 
		{
			printf("bit %d is 0\n", bitCounter);	
		}
	bitCounter++;
	myflags = myflags >> 1;
	}

}

