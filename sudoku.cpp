#include<iostream>
#include<vector>
using namespace std;

//Change the values here 
//Leave zeroes where ever you don't have the number
vector<vector<int>> board = {
    {0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0}
};


//Checks whether we can place the number "place" in the location board[x][y]
bool valid_move(int x, int y, int place) {
    for(int i=0; i<9; i++) {
        if(board[i][y] == place) return false;
    }
    for(int j=0; j<9; j++) {
        if(board[x][j] == place) return false;
    }
    int x_block = x/3, y_block = y/3;
    for(int i=3*x_block; i<3*x_block+3; i++) {
        for(int j=3*y_block; j<3*y_block+3; j++) {
            if(board[i][j] == place) return false;
        }
    }
    return true;
}


//Prints the board in a pretty way
void print_board() {
    cout << endl;
    for(int i=0; i<9; i++) {
        cout << "  ";
        for(int j=0; j<9; j++) {
            cout << board[i][j] << " ";
            if(j==2 || j==5) {
                cout << "|" << " ";
            }
        }
        cout << endl;
        if(i==2 || i==5) {
            for(int j=0; j<25; j++) {
                cout << "-" ;
            }
            cout << endl;
        }
    }
    cout << endl;
}


//Actual fun starts here
bool solve_board(int x, int y) {
    if(x == 9) {    //If row number is > 8. Then we have finished whole board so 
        print_board();  //print the board and return true.
        return true;
    }
    if(board[x][y] != 0) {  //If there already exists a number at this location, just move onto next location.
        if(y == 8) return solve_board(x+1, 0);
        return solve_board(x, y+1);
    }
    for(int val=1; val<=9; val++) { //Try out all possible values
        if(valid_move(x, y, val)) {
            board[x][y] = val;  //Place tha value at that location
            if(y == 8) {
                if(solve_board(x+1, 0)) return true;
            }
            else {
                if(solve_board(x, y+1)) return true;
            }
            board[x][y] = 0;    //If we have reached this point, it means solution doesn't have val at this location.
        }
    }
    return false;
}


//Just a auxilary function to make things neat.
void solve() {
    solve_board(0, 0);
    return;
}


int main() {
    solve();
}