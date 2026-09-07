#include <iostream>
#include <vector>

using namespace std;

main() {
    int n;
    cin >> n;
    if (n==1)
    	cout << 1;
    else{
	    vector<int> A;
	    A.reserve(n);
	    A.push_back(1);
	    A.push_back(2);
	    for (int i = 3; i <= n; i++) {
	        int mid = (i - 1) / 2;
	        A.push_back(A[mid]);
	        A[mid] = i;
	    }
	    for (int i=0; i < A.size(); i++){
			cout << A[i] << " ";
		}
	}
}
