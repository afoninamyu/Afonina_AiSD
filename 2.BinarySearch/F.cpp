#include <iostream>
#include <vector>

using namespace std;

bool good(int cnt, int q, int s, int t){
	return t / q + t / s >= cnt;
}

main(){
	int n, quick, slow;
	cin >> n >> quick >> slow;
	if (quick > slow)
		swap(quick, slow);
	
	int l = 0;
	int r = (n - 1) * slow;
	while (r - l > 1) {
		int m = (l + r) / 2;
		if (not good(n - 1, quick, slow, m))
			l = m;
		else
			r = m;
	}
cout << r + quick;
}
