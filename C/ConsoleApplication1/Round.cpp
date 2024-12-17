#include <iostream>
using namespace std;

int round() {
	int list[] = { 1, 2, 3, 4, 5, 6, 7, 69 };
	double result[sizeof(list) - 2] = {};

	for (int i = 1; i < sizeof(list) - 1; i++) {
		double num1 = (double)list[i - 1];
		double num2 = (double)list[i];
		double num3 = (double)list[i + 1];

		result[i - 1] = (num1 + num2 + num3) / 3;
	}

	cout << result;

	return 0;
}