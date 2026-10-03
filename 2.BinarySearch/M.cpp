#include <iostream>
#include <vector>

using namespace std;

bool good(vector<int>& a, int x, int k){
	if (x <= 1e-9) return false;
	int cnt = 0;
	for (int i=0; i < a.size(); i++){
		cnt += a[i] / x;
	}
	return cnt >= k;
}

main(){
	int n, k;
	cin >> n >> k;
	vector<int> a(n);
	for (int i=0; i < n; i++){
		cin >> a[i];
	}
	int l = 0;
	int r = 10000001;
	for (int i=0; i < 100; i++){
		int m = (l + r) / 2;
		if (good(a, m, k))
			l = m;
		else
			r = m;
	}
cout << l;
}
