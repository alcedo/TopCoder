public class ExerciseMachine {

	public int getPercentages(String time) {
		String[] split = time.split(":");
		int hours = Integer.parseInt(split[0]);
		int mins = Integer.parseInt(split[1]);
		int seconds = Integer.parseInt(split[2]);
		
		int totalSec = hours * 60 * 60 + mins * 60 + seconds; 
		
		int divisor = 1; 
		int ans = 0;
		
		//search for GCD between 100(full percentage pt) and the total Workout time
		for(int i=100; i>0; i--) { 
			if(totalSec % i == 0 && 100 % i ==0) { 
				divisor = i;
				break;
			}
		}
		
		return divisor -1; 
		
	}

}
