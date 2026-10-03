#include <iostream>
#include <vector>

using namespace std;

bool good(long long x, long long w, long long h, long long n){
	return (x / w) * (x / h) >= n;
}

main(){
	long long w, h, n;
	cin >> w >> h >> n;

	long long l = 0;
	long long r = n * max(h, w);
	while (r - l > 1) {
		long long m = (l + r) / 2;
		if (good(m, w, h, n))
			r = m;
		else
			l = m;
	}
cout << r;
}
