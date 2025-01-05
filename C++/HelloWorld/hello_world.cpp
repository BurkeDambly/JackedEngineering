/*
What <iostream> does: includes the input/output stream library in program.
Why its needed: it allows you to use the std::cout object to print output to the console
and std::cin to take input from the user.
How it works: the compiler replaces this line with the entire code for the library (iostream)
at compile time, enabling you to use the libraries features.
*/
#include <iostream>

/*
What 'using namespace std' does: it tells the compiler to use the standard namespace.
Why its needed: Most C++ standard library functions such as cout and cin, are part of the
std namespace. Without tthis line, you would need to prefix them with std::, std::cout. 
*/
using namespace std;

/*
Main is defined as an int because main returns 0. The return of 0 indicates successful execution.
*/
int main(){

    /* 
    Prints "Hello, World" o the console, followed by moving the cursor to the next line.
    The cout or std::cout assigns the print statement to the console. The endl sends a new line character
    to cout 
    */
    std::cout << "Hello, World" << std::endl;
    return 0;
}