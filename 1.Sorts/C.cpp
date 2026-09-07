#include <iostream>
#include <vector>

using namespace std;

void BubbleSort(vector<int>& A){
	bool swapped;
	for (int i=0; i < A.size(); i++){
		swapped = false;
		for (int j=0; j < A.size() - i - 1; j++){
			if (A[j] < A[j + 1]){
				swap(A[j], A[j + 1]);
				swapped = true;
			}
		}
		if (!swapped)
			break;
	}
}

main(){
	int x;
	vector <int> A;
	while (cin >> x) {
		A.push_back(x);
	}
	BubbleSort(A);
	for (int i=0; i < A.size(); i++){
		cout << A[i] << " ";
	}
}
