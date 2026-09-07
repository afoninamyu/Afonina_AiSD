#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const string& a, const string& b){
	return (a + b) > (b + a);
}

main(){
	vector <string> pts;
	string s;
	while (cin >> s){
		pts.push_back(s);
	}
	sort(pts.begin(), pts.end(), compare);
	for (const string& p: pts){
		cout << p;
	}
}
