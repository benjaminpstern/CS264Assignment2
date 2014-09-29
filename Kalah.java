
public class Kalah {
	public final static int DEPTH = 5;

        public static Integer[] minimax(Board startboard, int depth, Player player) {
	    //	Performs the minimax procedure by initializing alpha and beta and calling
	    //  minimax(startboard, depth, player, alpha, beta)
	    //  For a description of the Player class see Board.java
	}

        public static Integer[] minimax(Board startboard, int depth, Player player, int alpha, int beta) {
	    //  Performs the minimax procedure with cutoff values alpha and beta
	    //  Essentially a translation of the Python function shown in class
	}

	public static void play(int depth) {
	    // Main game play loop
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            // Use this buffered reader to get input from the human player
	    //  br.readLine() produces a String corresponding to a line of input
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
