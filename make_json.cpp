#include <nlohmann/json.hpp>
#include <bits/stdc++.h> 
using namespace std;
using json= nlohmann::json;
json j;
ifstream jsonin;
ofstream jsonout;

void add_j(string name,int cost,int attack,int health){
    j[cost+""][name]["attack"]=attack;
    j[cost+""][name]["health"]=health;
}
void add_j(string name,int cost,int attack,int health,string fun){
    j[cost+""][name]["attack"]=attack;
    j[cost+""][name]["health"]=health;
    j[cost+""][name]["effect"]=fun;
}

int main(){

    ifstream jsonin ("lor_database");
    if(jsonin.good()){
        jsonin>>j;
        cout<<j.dump(5)<<endl;
        system("clear");
    }
    j["1"]["Cinthria Cloudfield"]["attack"]=2;
    j["1"]["Cinthria Cloudfield"]["health"]=2;
    add_j("Crackshot Corsair",1,1,1,"CS CORSAIR");
    string nametemp ;
    string attacktemp;
    string defensetemp;
    string costtemp;
    string funtemp;
    while(nametemp!="print"){
    cin>>nametemp>>costtemp>>attacktemp>>defensetemp>>funtemp;    
    } 


    cout<<j.dump(5)<<endl;
    
    jsonout.open("lor_database");
    jsonout<<j.dump(5)<<endl;
    jsonout.close();


    return 0;
}