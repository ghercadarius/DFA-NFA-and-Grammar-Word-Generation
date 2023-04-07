#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

const int N = 1e5+10;
map <string, vector<pair<string, string>>> m; /// pair - primul fct tranzitie, doi stare
map <string, bool> sf;
map <string, bool> st;
map <pair<string, string>, bool> marcat;
string si;
vector <string> dr_fin;
bool rez = false;
string getString(char x)
{
    string s(1, x);
    return s;
}
bool parcurgere(string test,string stare, map <pair<string, string>, bool> marcat){
    if(marcat[{test, stare}])
        return false;
    marcat[{test, stare}] = true;
    dr_fin.push_back(stare);
    /*for(auto i:dr_fin){
        cout<<i<<" ";
    }
    cout<<"\n";*/
    if(test == ""){
        if(sf[stare]){
            for(auto i:dr_fin){
                cout<<i<<" ";
            }
            cout<<"\n";
        }
        dr_fin.pop_back();
        return sf[stare];
    }
    string act = test;
    act.erase(act.begin());
    char fct = test[0];
    for(auto i: m[stare]){
        if(i.first[0] == fct && i.first != "lambda"){
            dr_fin.push_back(i.first);
            if(parcurgere(act, i.second, marcat))
                rez = true;
            dr_fin.pop_back();
        }else
        if(i.first == "lambda"){
            dr_fin.push_back(i.first);
            if(parcurgere(test, i.second, marcat))
                rez = true;
            dr_fin.pop_back();
        }
    }
    dr_fin.pop_back();
}
int main()
{

    ///exemplu_lambda_afn.in - test: abbaa
    ///exemplu2.in - test: abbabba
    ///date.in - test: 110101002
    ///exemplu3.in - test: ababbab
    ///exemplu4.in - test: 1001
    ///exemplu5.in - test: 00
    string a, b, c;
    ifstream f("exemplu5.in");
    ///Citire stare initiala
    f >> si;
    /*while(n){
        f >> a;
        si.push_back(a);
        n--;
    }*/
    ///Citire stari finale
    int n = 0;
    f >> n;
    while(n){
        f >> a;
        sf[a] = true;
        n--;
    }
    ///Citire tranzitii
    while(f >> a >> b >> c){
        if(!st[a]){
            m.insert({a, vector<pair<string, string>>()});
            st[a] = true;
        }
        m[a].push_back({b, c});
    }
    f.close();
    ///Citire cuvant
    string test;
    cin >> test;
    parcurgere(test, si, marcat);
    cout << (rez != 0 ? "Acceptat" : "Neacceptat")<<"\n";
    return 0;
}
