#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;
void error(int code){
    cout << "error code " << to_string(code) << "\n";
    exit(code);
}
string input(string input){
    cout << input;
    string r;
    cin >> r;
    cout << "\n";
    return r;
}
void print(string input){
    cout << input;
}
void abs_to_interval_ineq(){
    //print the syntax of the absolute value 
    print("format : |x-c| =/>/</<=/>= r \n");
    //c=center ; input center as int (to add: check for int no not have errors) ;
    int c;
    c = stoi(input("c = "));
    //opp=opperator ; the input is an int to symplify usage on calculators (to add: check for int from 1 to 5  no not have errors)
    int opp;
    opp = stoi(input("1 : =\n2 : >\n3 : <\n4 : <=\n5 : >=\n:"));
    if (opp <= 0 or opp >= 6){
        error(0);
    }
    // r=radius ; (to add: check for int no not have errors)
    int r;
    r = stoi(input("r = "));
    int cmr_i,cpr_i;
    cmr_i = c - r;
    cpr_i = c + r;
    string cmr, cpr;
    cmr = to_string(cmr_i);
    cpr = to_string(cpr_i);
    //break print to separate input from answer 
    print("=====================\n");
    //exeptions
    if (opp == 2 and r<0){
        print("S = |R = ]-inf;+inf[\n");
    } else if (opp == 5 and r<0) {
        print("S = |R = ]-inf;+inf[\n");
    }else if (opp == 3 and r<0){
        print("S = phi = {}\n");
    }else if (opp == 4 and r == 0){
        print ("x = "+ to_string(c) + "\n");
    }
    // usual opperations 
    else if (opp == 1) {
        print ("x="+cmr+" or x="+cpr+" ; S={"+cmr+" ; "+cpr+"}\n");
    } else if (opp == 2) {
        print("x ]"+cmr+";"+cpr+"[\n");
        print(cmr + " < x < " + cpr + "\n");
    } else if (opp == 3) {
        print("x ]-inf;"+cmr+"[U]"+cpr+";+inf[\n");
        print("x < " + cmr + " et x > " + cpr + "\n");
    } else if (opp == 4) {
        print("x ["+cmr+';'+cpr+"]\n");
        print(cmr + " <= x <= " + cpr + "\n");
    } else if (opp == 5) {
        print("x ]-inf;"+cmr+"]U["+cpr+";+inf[\n");
        print("x <= " + cmr + " et x >= " + cpr + "\n");
    }
}
void ineq_to_abs(){
    //choose a syntax for the ineqation (int check + [1,4])
    int opp;
    opp = stoi(input("1. *1 < x < *2\n2. *1 <= x <= *2\n3. x < *1 et x > *2\n4. x <= *1 et x >= *2\n5. x > *1\n6. x < *1\n7. x >= *1\n8. x <= *1\n"));
    if (opp <= 0 or opp >= 9){
        error(4);
    }
    // *1 represents c - r and *2 represents c + r
    int cmr_i = stoi(input("*1 = "));
    int cpr_i = stoi(input("*2 = "));
    // if cmr > cpr than the inequation is wrong
    if (cmr_i > cpr_i and opp < 5){
        error(7);
    }
    // (c + r) + (c - r) = 2c ; Ans/2 = c ... r = c+r - c 
    string c,r;
    c = to_string((cpr_i + cmr_i)/2);
    r = to_string(cpr_i - stoi(c));
    // redifine cmr and cpr to be used as str after completing calculations 
    string cmr,cpr;
    cmr = to_string(cmr_i);
    cpr = to_string(cpr_i);
    // exeptions 

    if (opp == 1 and cmr==cpr){
        print("S = phi = {}\n");
    } else if ( opp == 3 and cmr==cpr){
        print("S = phi = {}\n");
    } else if ( opp == 2 and cmr==cpr ){
        print("x = " + cmr + "\n");
    } else if ( opp == 4 and cmr==cpr){
        print("x = " + cmr + "\n");
    } 
    //normal execution
    else if ( opp == 1){
        print("x ]"+cmr+";"+cpr+"[\n");
        print("|x - "+ c + "| < " + r + "\n");
    } else if ( opp == 2){
        print("x ["+cmr+';'+ cpr +"]\n");
        print("|x - "+ c + "| <= " + r + "\n");
    } else if ( opp == 3){
        print("x ]-inf;"+cmr+"[U]"+cpr+";+inf[\n");
        print("|x - "+ c + "| > " + r + "\n");
    } else if ( opp == 4 ){ 
        print("x ]-inf;"+cmr+"]U["+cpr+";+inf[\n");
        print("|x - "+ c + "| >= " + r + "\n");
    } else if ( opp == 5 ){
        print("x ]" + cmr + ", +inf[\n");
    } else if ( opp == 6 ){
        print("x ]-inf," + cmr + "[\n");
    } else if ( opp == 7 ){
        print("x [" + cmr + ", +inf[\n");
    } else if ( opp == 8 ){
        print("x ]-inf," + cmr + "]\n");
    }
}
void interval_to_abs(){
    //input opperator (syntax)
    int opp;
    opp = stoi(input("1. x ]*1;*2[\n2. x [*1;*2]\n3. x ]-inf;*1[U]*2;+inf[\n4. x ]-inf;*1]U[*2;+inf[\n5. x ]-inf,*1[\n6. x ]*1,+inf[\n7. x ]-inf,*1]\n8. x [*1,+inf[\n"));
    if (opp <= 0 or opp >= 9){
        error(4);
    }
    // input 
    int cmr_i,cpr_i;
    cmr_i = stoi(input("*1 = "));
    cpr_i = stoi(input("*2 = "));
    //check for errors 
    if (cmr_i > cpr_i and opp <5 ){
        error(7);
    }
    //calculate c and r 
    string c,r ;
    c = to_string((cpr_i + cmr_i)/2);
    r = to_string(cpr_i - stoi(c));
    //convert to str after calculations
    string cmr,cpr;
    cmr = to_string(cmr_i);
    cpr = to_string(cpr_i);
    // ...
    if ( opp == 1){
        print(cmr+" < x < "+cpr + "\n");
        print("|x - "+ c + "| < " + r + "\n");
    } else if ( opp == 2){
        print(cmr+" <= x <= "+cpr + "\n");
        print("|x - "+ c + "| <= " + r + "\n");
    } else if ( opp == 3){
        print("x < "+cmr+" et x > "+cpr + "\n");
        print("|x - "+ c + "| > " + r + "\n");
    } else if ( opp == 4 ){ 
        print("x <= "+cmr+" et x >= "+cpr + "\n");
        print("|x - "+ c + "| >= " + r + "\n");
    } else if (opp == 5 ){
    print("x < " + cmr + "\n");
    } else if (opp == 6 ){
        print("x > " + cmr + "\n");
    } else if (opp == 7 ){
        print("x <= " + cmr + "\n");
    } else if (opp == 8 ){
        print("x >= " + cmr + "\n");
    }
}