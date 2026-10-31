#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
using namespace std;

main() {
    int n, k, p;
    cin >> n >> k >> p;
    
    vector<int> car(p);
    for (int i = 0; i < p; ++i) cin >> car[i];
    
    vector<int> first(n + 1, p);
    vector<int> nxt(p, p);
    for (int i = p - 1; i >= 0; --i) {
        int c = car[i];
        nxt[i] = first[c];
        first[c] = i;
    }
    
    unordered_set<int> flr;
    priority_queue<pair<int, int>> h;
    int ans = 0;
    
    for (int i = 0; i < p; ++i) {
        int c = car[i];
        if (!flr.count(c)) {
            ++ans;
            if ((int)flr.size() == k) {
                while (true) {
                    int car_up = h.top().second;
                    h.pop();
                    if (flr.count(car_up)) {
                        flr.erase(car_up);
                        break;
                    }
                }
            }
            flr.insert(c);
        }
        h.push({nxt[i], c});
    }
    cout << ans << endl;
    return 0;
}
