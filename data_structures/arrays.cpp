/* 
ARRAY IN C++ 
Declaration: type arrayName[arraySize]
*/

#include <iostream>

using namespace std;

float getAverage(float param[], int size);
float *getValues();

int main(){
    /*
    Ways of initializing an array:
    float balance[5] = {1.0, 2.0, 3.0, 4.0, 5.0} creates an array 
                    of size 5 and initialize the values, omitted values will be left empty
    float balance[] = {1.0, 2.0, 3.0} creates an array of size 3
    */
    float balance[10] = {23.0, 12.9, 32.9, 23.9}; // uninitialized values left empty
    // to access the value, index the array name
    cout << balance[2] << endl;

    /*
   Returning an array from a function
   Return a pointer to the array, declare the array as a static variable
   in the function so that it persists after function returns
   */
    float *values = getValues();
    for(int i = 0; i < 5; i++){
        cout << *(values + i) << " ";
    }
    cout << endl;
    /*
    Passing an array as an argument to a function
    Method 1 - void myFunc(int param[5]); pass a one dimensional array
    Method 2 - void myFunc(int param[], int size)
    */
   float average = getAverage(values, 5);
   cout << average << endl;
}

float getAverage(float param[], int size){
    float sum, avg;
    
    for(int i = 0; i < size; i++){
        sum += param[i];
    }
    return (avg = sum / size);
}

float *getValues(){
    static float arr[5] = {230, 120, 100, 450, 400};
    return arr;
}