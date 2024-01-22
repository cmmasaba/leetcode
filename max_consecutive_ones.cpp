#include <iostream>

using namespace std;

int count_ones(int param[], int size);

int main(){
    int arr[6] = {1, 1, 0, 1, 1, 1};
    int num_ones = count_ones(arr, 6);
    cout << num_ones << endl;
}

int count_ones(int param[], int size){
    int max = 0, consecutive = 0;
    bool isconsecutive = false;

    for(int i = 0; i < size; i++){
        if(param[i] == 1)
            isconsecutive = true;
        else 
            isconsecutive = false;
        
        if(isconsecutive){
            consecutive += 1;
            if(consecutive > max)
                max = consecutive;
        }
        else {
            consecutive = 0;
        }
    }
    return max;
}