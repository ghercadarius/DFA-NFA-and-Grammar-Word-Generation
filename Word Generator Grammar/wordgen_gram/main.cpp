#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;
ofstream g("output.txt");
const int N = 1e5 + 10;
unordered_map <char, vector<string>> gram;
unordered_map <char, bool> verif;

int n;

void bkt(string s){
    int sl = s.length();
    if(sl > n + 1)
        return;
    bool lm = false;
    for(int i = 0; i < sl; i++){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            lm = true;
            //string aux = s.substr(0, i);
            for(auto j: gram[s[i]]){
                string aux = s.substr(0, i);
                if(j != "lambda")
                    aux += j;
                aux += s.substr(i + 1 , sl - i - 1);
                bkt(aux);
            }
        }
    }
    if(!lm && sl == n){
        g << s << "\n";
    }
}

int main()
{
    ifstream f("input.in");
    ifstream fin("word.in");
    fin >> n;
    fin.close();
    string citire;
    while(getline(f, citire)){
        char first = citire[0];
        int fpoz = 5, spoz;
        bool ok = true;
        do{
            spoz = citire.find(" | ", fpoz + 1);
            if(spoz <= 0){
                spoz = citire.length();
                ok = false;
            }
            if(!verif[first]){
                verif[first] = true;
                gram.insert({first, vector<string>()});
            }
            string aux = citire.substr(fpoz, spoz - fpoz);
            //cout << fpoz << " " << spoz << " " << aux << "\n";
            gram[first].push_back(aux);
            fpoz = spoz + 3;
        }while(ok);
    }
    f.close();
    /*for(auto i: gram){
        cout << i.first << ": ";
        for(auto j : i.second)
            cout << j << " ";
        cout << "\n";
    }*/
    bkt("S");
    g.close();
    return 0;
}
