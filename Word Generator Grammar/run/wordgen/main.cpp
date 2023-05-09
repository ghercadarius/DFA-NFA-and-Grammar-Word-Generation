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
map <pair<string, string>, bool> rez;
string si;
int nr_lit; ///numarul de litere din cuvintele generate
vector <string> dr_fin;
bool afis = false;
ofstream g;
string getString(char x)
{
    string s(1, x);
    return s;
}
///marcat - first cuvant second stare
void parcurgere(string cuvant, string stare, map<pair<string, string>, bool> &marcat){
    if(marcat[{cuvant, stare}])
        return;
    marcat[{cuvant, stare}] = true;
    if(cuvant.length() == nr_lit){
        if(stare == si){
            afis = true;
            g<<cuvant<<"\n";
        }
        for(auto i: m[stare])
            if(i.first == "lambda"){
                parcurgere(cuvant, i.second, marcat);
        }
        return;
    }
    for(auto i: m[stare]){
        if(i.first == "lambda"){
            parcurgere(cuvant, i.second, marcat);
        }else{
            string aux = i.first + cuvant;
            parcurgere(aux, i.second, marcat);
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
    ///exemplu5.in -- afn
    ///exemplu6.in -- ultimul exemplu din word
    ///input.txt
    string a, b, c;
    ifstream f("input.txt");
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
    f.open("word.txt");
    f>>nr_lit; ///citire numarul de litere necesare
    f.close();
    g.open("output.txt");
    ///Parcurgere generare cuvant
    for(auto i: sf)
        parcurgere("", i, rez);
    if(!afis)
        g<<"Nu sunt cuvinte valide pentru acest automat!";
    g.close();
    return 0;
}
