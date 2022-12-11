#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

vector<int> findLargestHelper(const vector<int>& , vector<int>, int);

vector<int> dataInput(){
    vector<int> data {0};
    string fileName = "input.txt";
    string line;
    fstream file;
    int counter = 0;

    file.open(fileName);
    if(!file.is_open()){
        cout << "Failed to open file" << endl;
        exit(1);
    }
    while(getline(file, line)){
        if (line.empty()){
            data.push_back(0);
            counter++;
        }else{
            data[counter] += stoi(line);
        }
    }

    return data;
}

void findLargest(const vector<int>& v){
    int counter = (int)v.size()-1;
    int total = 0;
    vector<int> max {0, 0, 0};
    max = findLargestHelper(v, max, counter);
    
    for(int x : max){
        cout << "The elf has: " << x << endl;
        total += x;
    }
    cout << max[0] << endl;
    cout << total << endl;
}

vector<int> findLargestHelper(const vector<int>& v, vector<int> max, int counter){
    //Base case
    if(counter == 0){
        return max;
    }

    if(max[0] < v[counter] && max[1] < v[counter] && max[2] < v[counter]){
        max[2] = max[1];
        max[1] = max[0];
        max[0] = v[counter];
    }else if(max[0] >= v[counter] && max[1] < v[counter] && max[2] < v[counter]){
        max[2] = max[1];
        max[1] = v[counter];
    }
    else if(max[0] >= v[counter] && max[1] >= v[counter] && max[2] < v[counter]){
        max[2] = v[counter]; 
    }
    //Tail Recursive call
    return findLargestHelper(v, max, --counter);
}

int main(){

    vector<int> data;

    data = dataInput();
    findLargest(data);


    return 0;
}
