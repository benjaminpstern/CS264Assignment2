public class Board {
    // I modeled player as an enum. If you don't know how to use enums, you can used integers 0 and 1 for Min and Max
    // If you use an enum you will also be interested in EnumMap
    public Pot[][] pots;
    public Pot[] kalahs;
    public Board(int n) {
	// Constructs a board with n stones per pot
	kalahs = new Pot[2];
	pots = new Pot[2][6];
	for(int player = 0;player<2;player++){
	    kalahs[player] = 0;
	    for(int pot = 0;pot<6;pot++){
		pots[player][pot] = n;
	    }
	}
    }	

    public Board(Board b) {
	// Constructs a board that is a copy of Board b
	kalahs = new Pot[2];
	pots = new Pot[2][6];
	for(int player = 0;player<2;player++){
	    kalahs[player] = b.kalahs[player];
	    for(int pot = 0;pot<6;pot++){
		pots[player][pot] = b.pots[player][pot];
	    }
	}
    }

    // ...

    public Board move(int player, int pot) {
	//  Returns a new Board whose state is that of the Kalah board after Player player
	//      moves using the given pot	    

    }

    @Override
	public boolean equals(Object o) {
	    //  Board equality is required to properly maintain open and closed lists in minimax.
	    //  Two boards should be equal if they have the same number of stones in all corresponding pots and Kalahs
	}

    public boolean isWin() {
	//  Returns true if this board is a winning (i.e. final) configuration. (false otherwise)
	//  A final configuration is one where all pots on one side are empty.
    }

    public boolean legal(int player, int pot) {
	//  Returns true if the move indicated by the given pot is legal (false otherwise)
	if(pot < 0 || pot > 5)	return false;
	return pots[player][pot] != 0;	
    }

    public boolean moveBoard(int player, int pot) {
	//  Performs the move indicated by the given pot on this Board for Player player. 
	//  Includes any capture or final actions if the resulting configuration is a final configuration.
	//  Returns true if the result is a free turn for the player (false otherwise)
    }

    private boolean winCheck() {
	//  Help function for moveBoard, performing any required final actions if the current state is final
    }

    public int eval() {
	//  Returns the value of the static evaluation function on this Board
    }

    public void show() {
	//  Prints the board's state to resemble an actual Kalah board.
    }

    public static class Pot {
	// I found this class particularly useful to serve as my pot.
	int val = 0;
	public Pot(int n) {val = n;}
	public int get() {return val;}
	public void addone() {val++;}
	public void add(int n) {val += n;}
	public int remove() {int temp = val; val = 0; return temp;}
	@Override
	    public boolean equals(Object other) {
		return (other instanceof Pot && ((Pot)other).val == this.val);
	    }
    }

    public static void main(String[] args) {
	//	 As you're building this class you may want to test it using a main function.
	//   Be sure to either eliminate this or that your jar knows which main to execute.
    }

}
