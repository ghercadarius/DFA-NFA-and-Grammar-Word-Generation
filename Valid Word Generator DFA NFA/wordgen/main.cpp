#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

const int N = 1e5+10;
map <string, vector<pair<string, string>>> m; /// pair - primul fct tranzitie, doi stare
vector <string> sf;
map <string, bool> st;
string si;
int nr_lit; ///numarul de litere din cuvintele generate
vector <string> dr_fin;
bool afis = false;
string getString(char x)
{
    string s(1, x);
    return s;
}
void parcurgere(string cuvant, string stare){
    if(cuvant.length() == nr_lit){
        if(stare == si){
            afis = true;
            cout<<cuvant<<"\n";
        }
        return;
    }
    for(auto i: m[stare]){
        if(i.first == "lambda"){
            parcurgere(cuvant, i.second);
        }else{
            string aux = i.first + cuvant;
            parcurgere(aux, i.second);
        }
    }

}
int main()
{
    ///exemplu_lambda_afn.in
    ///exemplu2.in
    ///date.in
    ///exemplu3.in
    ///exemplu4.in
    string a, b, c;
    ifstream f("exemplu_lambda_afn.in");
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
        sf.push_back(a);
        n--;
    }
    ///Citire tranzitii modificate
    while(f >> a >> b >> c){
        if(!st[c]){
            m.insert({c, vector<pair<string, string>>()});
            st[c] = true;
        }
        m[c].push_back({b, a}); ///adaugam muchiile invers pentru a genera eficient cuvintele
    }
    f.close();
    cin>>nr_lit; ///citire numarul de litere necesare
    ///Parcurgere generare cuvant
    for(auto i: sf)
        parcurgere("", i);
    if(!afis)
        cout<<"Nu sunt cuvinte valide pentru acest automat!";
    return 0;
}
