#include <iostream>
using namespace std;

int main(){

    int arr[5] = {1, 2, 3, 4, 5};

    for(int i = 0; i < 5; i++){
        cout << arr[i] << endl;
    }

    // Array size calculation is the size of the entire array / size of integer.
    cout << "The length of the array is: " << sizeof(arr) / sizeof(arr[0]) << endl;
    return 0;
}