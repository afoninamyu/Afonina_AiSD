#include <iostream>
#include <vector>

using namespace std;

void SelectionSort(vector<int>& A){
	int n = A.size();
	for (int i=0; i < n - 1; i++){
		int maxi = i;
		for (int j = i + 1; j < n; j++){
			if (A[j] > A[maxi])
			maxi = j;
		}
		swap(A[i], A[maxi]);
	}
}

main(){
	int x;
	vector <int> A;
	while (cin >> x) {
		A.push_back(x);
	}
	SelectionSort(A);
	for (int i=0; i < A.size(); i++){
		cout << A[i] << " ";
	}
}
