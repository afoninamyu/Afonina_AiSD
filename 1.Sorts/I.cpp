#include <iostream>
#include <vector>
#include <string>

using namespace std;

int getIndex(char c){
	if (c >= '0' && c <= '9')
		return c - '0';
	else
		return 10 + (c - 'a');
}

main(){
	string s1, s2;
	cin >> s1 >> s2;
	vector <int> cnt(36,0);
	for (char c: s1){
		int i = getIndex(c);
		cnt[i]++;
	}
	for (char c: s2){
		int i = getIndex(c);
		cnt[i]--;
	}
	for (int x: cnt){
		if (x != 0){
			cout << "NO";
			return 0;
		}
	}
	cout << "YES";
}
