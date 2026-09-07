#include <iostream>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& A){
	for (int i=1; i < A.size(); i++){
		int key = A[i];
		int j = i - 1;
		while (j >= 0 && A[j] > key){
			A[j + 1] = A[j];
			--j;
		}
		A[j + 1] = key;
	}
}

main(){
	int x;
	vector <int> A;
	while (cin >> x) {
		A.push_back(x);
	}
	InsertionSort(A);
	for (int i=0; i < A.size(); i++){
		cout << A[i] << " ";
	}
}
