#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

void reader(vector<int>& A){
	string line;
	getline(cin, line);
	stringstream ss(line);
	int num;
	while (ss >> num){
		A.push_back(num);
	}
}

main(){
	vector<int> dist;
	vector<int> pay;
	reader(dist);
	reader(pay);
	sort(dist.begin(), dist.end());
	sort(pay.begin(), pay.end(), greater<int>());
	int sum = 0;
	for (int i=0; i < dist.size(); i++){
		sum += dist[i]*pay[i];
	}
	cout << sum;
}
