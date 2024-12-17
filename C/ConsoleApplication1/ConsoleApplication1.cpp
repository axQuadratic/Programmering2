// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;

int main()
{   
    Round::round();
    return 0;
    while (true) {
        int num1 = 0;
        int num2 = 0;
        char op = ' ';
        double result;

        cout << "Input the first number: ";
        cin >> num1;
        cout << "Input the second number: ";
        cin >> num2;

        cout << "Input an operation: ";
        cin >> op;

        switch (op) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                result = (double)num1 / (double)num2;
                break;
            case '^':
                result = pow((double)num1, (double)num2);
                break;
            default:
                cout << "Invalid operation";
                return 1;
        }

        cout << "The result is: " << result << "\n";

    }
    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
