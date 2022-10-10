#include <iostream>
#include "headers.hpp"
using namespace std;
/* cpp; abosute value
Ali Naim; 10/10/2022
*/
int main(){
    // choosing app 
    int opp;
    opp = stoi(input("1. abs input\n2. ineq input\n3. interval input\n:"));
    //test 
    if (opp <= 0 or opp >= 4){
        error(9);
    }
    //menu 
    if (opp == 1) {
        abs_to_interval_ineq();
    } else if (opp == 2) {
        ineq_to_abs();
    } else if ( opp == 3) {
        interval_to_abs();
    }
    // wait before closing window
    string wait = "";
    cin >> wait;
}