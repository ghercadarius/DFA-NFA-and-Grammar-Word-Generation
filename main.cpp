#include <bits/stdc++.h>

using namespace std;

const int N = 1e5+10;
map <string, vector<pair<char, string>>> m; /// pair - primul fct tranzitie, doi stare
map <string, bool> sf;
map <string, bool> st;
vector <string> si;
vector <string> dr_fin;
string getString(char x)
{
    string s(1, x);
    return s;
}
bool parcurgere(string test,string stare){
    dr_fin.push_back(stare);
    if(test == ""){
        if(sf[stare]){
            for(auto i:dr_fin){
                cout<<i<<" ";
            }
            cout<<"\n";
        }
        return sf[stare];
    }
    bool rez = false;
    string act = test;
    act.erase(act.begin());
    char fct = test[0];
    for(auto i: m[stare]){
        if(i.first == fct){
            dr_fin.push_back(getString(i.first));
            if(parcurgere(act, i.second))
                return true;
            dr_fin.pop_back();
        }
    }
    dr_fin.pop_back();
    return false;
}
int main()
{
    string a, c;
    char b;
    ifstream f("exemplu2.in");
    ///Citire stare initiala
    int n = 0;
    f >> a;
    si.push_back(a);
    /*while(n){
        f >> a;
        si.push_back(a);
        n--;
    }*/
    ///Citire stari finale
    f >> n;
    while(n){
        f >> a;
        sf[a] = true;
        n--;
    }
    ///Citire tranzitii
    while(f >> a >> b >> c){
        if(!st[a]){
            m.insert({a, vector<pair<char, string>>()});
            st[a] = true;
        }
        m[a].push_back({b, c});
    }
    f.close();
    ///Citire cuvant
    string test;
    cin >> test;
    for(auto i:  si)
        cout << (parcurgere(test, i) != 0 ? "Acceptat" : "Neacceptat")<<"\n";
    return 0;
}
