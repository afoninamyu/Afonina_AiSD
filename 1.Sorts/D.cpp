#include <iostream>
#include <vector>

using namespace std;

int BubbleSort(vector<int>& A){
	int cnt = 0;
	bool swapped;
	for (int i=0; i < A.size(); i++){
		swapped = false;
		for (int j=0; j < A.size() - i - 1; j++){
			if (A[j] > A[j + 1]){
				swap(A[j], A[j + 1]);
				cnt++;
				swapped = true;
			}
		}
		if (!swapped)
			break;
	}
	return cnt;
}

main(){
	int n;
	cin >> n;
	vector <int> A(n);
	for (int i=0; i < n; i++) {
		cin >> A[i];
	}
	cout << BubbleSort(A);
}
