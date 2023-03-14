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
string si;
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
        if(i.first[0] == fct && i.first != "lambda"){
            dr_fin.push_back(i.first);
            if(parcurgere(act, i.second))
                return true;
            dr_fin.pop_back();
        }else
        if(i.first == "lambda"){
            dr_fin.push_back(i.first);
            if(parcurgere(test, i.second))
                return true;
            dr_fin.pop_back();
        }
    }
    dr_fin.pop_back();
    return false;
}
int main()
{

    ///exemplu_lambda_afn.in - test: abbaa
    ///exemplu2.in - test: abbabba
    ///date.in - test: 110101002
    string a, b, c;
    ifstream f("date.in");
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
    cout << (parcurgere(test, si) != 0 ? "Acceptat" : "Neacceptat")<<"\n";
    return 0;
}
