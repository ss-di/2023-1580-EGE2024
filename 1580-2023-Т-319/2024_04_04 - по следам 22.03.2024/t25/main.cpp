#include <iostream>
#include <vector>

using namespace std;

bool check(long long x){

string s = to_string(x);

if (s[0] != '5') return false;
if (s[s.size()-1] != '1') return false;

if (s.find("309") != string::npos) return true;
if (s.find("319") != string::npos) return true;
if (s.find("329") != string::npos) return true;
if (s.find("339") != string::npos) return true;
if (s.find("349") != string::npos) return true;
if (s.find("359") != string::npos) return true;
if (s.find("369") != string::npos) return true;
if (s.find("379") != string::npos) return true;
if (s.find("389") != string::npos) return true;
if (s.find("399") != string::npos) return true;

return false;
}

int main()
{
long long N = 100000000;

vector<int> primes(N+1, 1);

primes[1] = 0;

long long i = 2;
while (i*i <= N) {
    if (primes[i] != 0) {
        cout << i << " ";
        long long j = i * i;
        while (j <= N) {
            primes[j] = 0;
            j = j + i;
        }
    }
    i += 1;
}

long long s = 0;
long long cnt = 0;
for (long long i = 2; i <= N; ++i){
    if (primes[i]) {
       s += i;
       cnt += 1;
       if (check(s))
          cout << i << " " << cnt  << " " << s <<endl;
    }
}
    return 0;
}
