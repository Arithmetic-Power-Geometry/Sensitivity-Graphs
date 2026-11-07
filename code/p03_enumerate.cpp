// Exhaustive n=5 fixed-weight input-coordinate permutation orbits.
// Build: g++ -O3 -std=c++17 enumerate.cpp -o enumerate && ./enumerate
#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
vector<array<int,32>> maps;
U transform(U m,const array<int,32>& p){
 U o=0;while(m){int x=__builtin_ctz(m);m&=m-1;o|=U(1)<<p[x];}return o;
}
string hexmask(U x){char b[12];sprintf(b,"%08x",x);return b;}
int main(){
 array<int,5> perm={0,1,2,3,4};
 do{array<int,32> p;
  for(int x=0;x<32;x++){int y=0;for(int i=0;i<5;i++)if(x>>i&1)y|=1<<perm[i];p[x]=y;}
  maps.push_back(p);
 }while(next_permutation(perm.begin(),perm.end()));
 for(int k:{4,5}){
  unordered_set<U> visited;visited.reserve(220000);
  size_t raw=0,orbits=0;map<int,int> orbit_sizes;vector<U> reps;
  for(int a=0;a<32;a++)for(int b=a+1;b<32;b++)
   for(int c=b+1;c<32;c++)for(int d=c+1;d<32;d++){
    if(k==4){
     U m=(U(1)<<a)|(U(1)<<b)|(U(1)<<c)|(U(1)<<d);
     raw++;if(visited.count(m))continue;
     set<U> orb;for(auto&p:maps)orb.insert(transform(m,p));
     for(auto z:orb)visited.insert(z);
     orbits++;orbit_sizes[orb.size()]++;reps.push_back(*orb.begin());
    }else for(int e=d+1;e<32;e++){
     U m=(U(1)<<a)|(U(1)<<b)|(U(1)<<c)|(U(1)<<d)|(U(1)<<e);
     raw++;if(visited.count(m))continue;
     set<U> orb;for(auto&p:maps)orb.insert(transform(m,p));
     for(auto z:orb)visited.insert(z);
     orbits++;orbit_sizes[orb.size()]++;reps.push_back(*orb.begin());
    }
   }
  cout<<"k="<<k<<" raw="<<raw<<" visited="<<visited.size()
      <<" permutation_orbits="<<orbits<<" orbit_size_distribution=";
  for(auto [sz,n]:orbit_sizes)cout<<sz<<":"<<n<<",";
  cout<<"\n";
  ofstream f("reps_k"+to_string(k)+".txt");
  for(auto z:reps)f<<hexmask(z)<<"\n";
 }
}
