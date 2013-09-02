import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;


public class PowerOutage {

	public int estimateTimeOut(int[] fromJunction, int[] toJunction, int[] ductLength) {
		int totalTime = 0;
		
		for(int x : ductLength) 
			totalTime += x * 2; 
		
		return totalTime - maxHeight(0, fromJunction, toJunction, ductLength);
	}
	
	private int maxHeight(int startNode, int[] from, int[] to, int[] ductLength  ) {
		int length = 0;
		
		for(int i=0; i<from.length; i++) { 
			if(from[i] == startNode){ // spawn a new recursive call forEach matching fromNode. ( >1 calls could be made here!)
				// length of this node + max length of child 
				int recurseLength = ductLength[i] + maxHeight(to[i], from, to, ductLength);
				length = Math.max(length, recurseLength);
			}
		}
		
		return length;
	}
}