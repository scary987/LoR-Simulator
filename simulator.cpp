

#include <bits/stdc++.h> 
#include <nlohmann/json.hpp>
using namespace std;





typedef struct{
    string name;
    void *effect_ptr;
}Effect;




typedef struct{
    int health;
    string name;
    int attack;
    Effect effect;
}Entity;

typedef struct{
    string name;
    Entity body;
    int cost;
    Effect summon;
    Effect spell;
}Card;

/*typedef struct {
    int health;
    vector<Card> hand;
    vector<Card> deck;
}Player;*/

typedef struct{
    string name;
    void *spell_ptr;
}Spell;



class Player{
    public: int health;
    vector<Card> hand;
    vector<Card> deck;

    public: void draw(int i){
        
        for(;i>0;i--)
        {   
            hand.push_back(deck[deck.size()-1]);
            deck.pop_back();
        }
    }
    public: void draw(){
        draw(1);
    }

    public: Player(){
        health = 20;
        draw(5);

    }
    

};

class simulator{
    int seed;
    string name;
    Player player1;
    Player player2;
    vector<Spell> Burst; //Burstq
    vector<Spell> Fast;  //Fastq
    bool slowspell;
    vector<Entity> board ;


    public: void dd_to(Player p,int n){
        p.health-=n;
    }
    
    public: void dd_to(Entity e,int n){
        e.health-=n;
    }

    public: void frostbyte(Entity e){
        e.attack= 0;
    }

    

    public: simulator(int s)
    {
        slowspell = false;
        player1 = Player();
        player2 = Player();
        seed = s;
        name="list1, list2- simulation";
        srand(seed);
    }
    void execute(){}

};

int main(){

    simulator s =  simulator(5);
   
    return 0;
}

