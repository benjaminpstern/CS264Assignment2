import java.util.Scanner;
import java.util.InputMismatchException;
public class Kalah {
    public final static int DEPTH = 5;
    public final static int INFINITY = 100;
    public final static int ILLEGAL = 101;
    //returns the number of the pot that is the best move.
    public static int minimax(Board startboard, int depth, int player) {
	//	Performs the minimax procedure by initializing alpha and beta and calling
	//  minimax(startboard, depth, player, alpha, beta)
	//  For a description of the Player class see Board.java
	int[] moves = new int[6];
	for(int p = 0;p<6;p++){
	    if(startboard.legal(player,p)){
		int alpha = -INFINITY;
		int beta = INFINITY;
		if(player == 1){
		    Board b = new Board(startboard);
		    if(b.moveBoard(player,p)){
			moves[p] = maxi(b, depth, alpha, beta);
		    }
		    else {
			moves[p] = mini(b, depth - 1, alpha, beta);
		    }
		}
		else{
		    Board b = new Board(startboard);
		    if(b.moveBoard(player, p)){
			moves[p] = mini(b, depth, alpha, beta);
		    }
		    else{
			moves[p] = maxi(b, depth - 1, alpha, beta);
		    }
		}
	    }
	    else{
		moves[p] = ILLEGAL;
	    }
	}
	int bestEval = -ILLEGAL;
	if(player == 0) bestEval = ILLEGAL;
	int bestMove = 0;
	for(int p=0;p<6;p++){
	    if(moves[p] == ILLEGAL) continue;
	    if(moves[p] > bestEval && player == 1){
		bestEval = moves[p];
		bestMove = p;
	    }
	    if(moves[p] < bestEval && player == 0){
		bestEval = moves[p];
		bestMove = p;
	    }
	}
	return bestMove;
    }
    //returns the evaluation of the current position as given by the minimax procedure.
    public static int maxi(Board startboard, int depth, int alpha, int beta) {
	//  Performs the minimax procedure with cutoff values alpha and beta
	//  Essentially a translation of the Python function shown in class
	int player = 1;
	if(depth == 0) return startboard.eval();
	int[] moves = new int[6];
	for(int p = 0;p<6;p++){
	    if(startboard.legal(player,p)){
		Board b = new Board(startboard);
		if(b.moveBoard(player,p)){
		    moves[p] = maxi(b, depth, alpha, beta);
		}
		else {
		    moves[p] = mini(b, depth - 1, alpha, beta);
		}
		if(moves[p] > alpha) alpha = moves[p];
		if(moves[p] >= beta) return moves[p];
	    }
	    else{
		moves[p] = ILLEGAL;
	    }
	}
	return alpha;
    }
    //returns the evaluation
    public static int mini(Board startboard, int depth, int alpha, int beta) {
	//  Performs the minimax procedure with cutoff values alpha and beta
	//  Essentially a translation of the Python function shown in class
	int player = 0;
	if(depth == 0) return startboard.eval();
	int[] moves = new int[6];
	for(int p = 0;p<6;p++){
	    if(startboard.legal(player,p)){
		Board b = new Board(startboard);
		if(b.moveBoard(player, p)){
		    moves[p] = mini(b, depth, alpha, beta);
		}
		else{
		    moves[p] = maxi(b, depth - 1, alpha, beta);
		}
		if(moves[p] < beta) beta = moves[p];
		if(moves[p] <= alpha) return moves[p];
	    }
	    else{
		moves[p] = ILLEGAL;
	    }
	}
	return beta;
    }


    public static void play(int depth) {
	// Main game play loop
/*	Board b = new Board(4);
	for(int i = 0;i<10;i++){
	    int p;
	    do{
		p = minimax(b,3,0);
		System.out.println(p+" "+0);
		System.out.println(b);
	    }while(b.moveBoard(0,p));
	    p = minimax(b,3,1);
	    do{
		p = minimax(b,3,1);
		System.out.println(p+" "+1);
		System.out.println(b);
	    }while(b.moveBoard(1,p));
	}
*/  
	System.out.println("CS364 Assignment 2.3\nBen Stern and Cole Peppis\nUsing depth bound "+depth);
	System.out.print("\nLet's play Kalah!\nWho goes first (0) me; (1) you ? ");
	Scanner s = new Scanner(System.in);
	int player = -43;
	while(player!=0 && player!=1){
	    try{
		player = s.nextInt();
	    }
	    catch(InputMismatchException e){
		;
	    }
	    if(player!=0 && player != 1){
		System.out.println("Please type 1 to go first or 0 to go second.");
	    }
	}
	System.out.println(player);
    }

    public static void main(String[] args) {
	int depth = DEPTH;
	if (args.length > 0) {
	    try {
		depth = Integer.parseInt(args[0]);
	    } catch (NumberFormatException ex) {}
	}
	Kalah.play(depth);
    }
}
