import java.util.Random;

public class Board {
    // I modeled player as an enum. If you don't know how to use enums, you can used integers 0 and 1 for Min and Max
    // If you use an enum you will also be interested in EnumMap
    public int[][] pots;
    public int[] kalahs;
    public Board(int n) {
	// Constructs a board with n stones per pot
	kalahs = new int[2];
	pots = new int[2][6];
	for(int player = 0;player<2;player++){
	    kalahs[player] = 0;
	    for(int pot = 0;pot<6;pot++){
		pots[player][pot] = n;
	    }
	}
    }	

    public Board(Board b) {
	// Constructs a board that is a copy of Board b
	kalahs = new int[2];
	pots = new int[2][6];
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
	if (!legal(player, pot)) return null;
	Board b = new Board(this);
	b.moveBoard(player, pot);
	return b;
    }

    @Override
    public boolean equals(Object o) {
	//  Board equality is required to properly maintain open and closed lists in minimax.
	//  Two boards should be equal if they have the same number of stones in all corresponding pots and Kalahs
	if (! ( o instanceof Board ))
	    return false;
	Board b = (Board)o;
	for(int player = 0;player<2;player++){
	    if (kalahs[player] != b.kalahs[player]) return false;
	    for(int pot = 0;pot<6;pot++){
		if (pots[player][pot] != b.pots[player][pot]) return false;
	    }
	}
	return true;
    }

    public boolean isOver() {
	//  Returns true if this board is a winning (i.e. final) configuration. (false otherwise)
	//  A final configuration is one where all pots on one side are empty.
	for(int player = 0;player<2;player++){
	    boolean isEmpty = true;
	    for(int pot = 0;pot<6;pot++){
		if (pots[player][pot] != 0) isEmpty = false;
	    }
	    if (isEmpty) return true;
	}
	return false;
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
	int hand = pots[player][pot];
	pots[player][pot] = 0;
	int side = player;
	int p = pot;
	while (hand > 0) {
	    if (side == 0) p--;
	    else p++;
	    if (p == -1 && player == 1) p--;	//skips the opponent's kalah
	    if (p == 6 && player == 0) p++;	//skips the opponent's kalah
	    if (p <= -2) {
		p = 0;
		side = 1;
	    }
	    if (p >= 7) {
		p = 5;
		side = 0;
	    }
	    if (p == -1) kalahs[0]++;
	    else if (p == 6) kalahs[1]++;
	    else pots[side][p]++;
	    hand--;
	}
	if (side == player && p >=0 && p < 6 && pots[side][p] == 1) {
	    kalahs[player] += pots[0][p];
	    kalahs[player] += pots[1][p];
	    pots[0][p] = 0;
	    pots[1][p] = 0;
	}
	if (winCheck()) return false;
	if (p == -1 || p == 6) return true;
	return false;
    }

    private boolean winCheck() {
	//  Help function for moveBoard, performing any required final actions if the current state is final
	if (!isOver()) return false;
	for(int player = 0;player<2;player++){
	    for(int pot = 0;pot<6;pot++){
		kalahs[player] += pots[player][pot];
		pots[player][pot] = 0;
	    }
	}
	return true;
    }

    public int eval() {
	//  Returns the value of the static evaluation function on this Board
	return kalahs[1]-kalahs[0];
    }

    @Override
    public String toString() {
	//  Prints the board's state to resemble an actual Kalah board.
	String s = "";
	for(int player = 0;player<2;player++){
	    s += "\n     ";
	    for(int pot = 0;pot<6;pot++){
		s += pots[player][pot] + " ";
		if (pots[player][pot] < 10) s += " ";
	    }
	    if (player == 0)
		s += "\n  " + kalahs[0] + "                    "+ kalahs[1];
	}
	s += "\n";
	return s;
    }

//    public static class Pot {
	// I found this class particularly useful to serve as my pot.
//	int val = 0;
//	public Pot(int n) {val = n;}
//	public int get() {return val;}
//	public void addone() {val++;}
//	public void add(int n) {val += n;}
//	public int remove() {int temp = val; val = 0; return temp;}
//	@Override
//	public boolean equals(Object other) {
//	    return (other instanceof Pot && ((Pot)other).val == this.val);
//	}
 //   }

    public static void main(String[] args) {
	//	 As you're building this class you may want to test it using a main function.
	//   Be sure to either eliminate this or that your jar knows which main to execute.
	Board b = new Board(4);
	System.out.println(b);
	int sideToMove = 0;
	Random r = new Random();
	int p = 0;
	boolean goAgain = false;
	while (!b.isOver()) {
	    do { 
		p = r.nextInt(6);
	    } while (b.pots[sideToMove][p] == 0);
	    System.out.println(sideToMove + " " + p);
	    goAgain = b.moveBoard(sideToMove, p);
	    System.out.println(b);
	    if (!goAgain) sideToMove = (sideToMove + 1) % 2;
	}
    }
}
