#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<int>& A){
	const int MAX_VAL = 100;
	vector<int> cnt(MAX_VAL + 1, 0);
	for (int x: A){
		cnt[x]++;
	}
	A.clear();
	for (int num=0; num < MAX_VAL + 1; num++){
		for (int c=0; c < cnt[num]; c++){
			A.push_back(num);
		}
	}
}

main(){
	int x;
	vector <int> A;
	while (cin >> x) {
		A.push_back(x);
	}
	CountSort(A);
	for (int i=0; i < A.size(); i++){
		cout << A[i] << " ";
	}
}
