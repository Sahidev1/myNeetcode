package Easy_problems.meeting_schedule.java;

import java.util.List;



public class Solution {
    public class Interval {
        public int start, end;
        public Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
   

    public boolean canAttendMeetings(List<Interval> intervals) {

        boolean[] mem = new boolean[1000001];
        int a,b;
        for (Interval interval : intervals) {
            a = interval.start;
            b = interval.end;
            
            a++;
            while(a < b){
                if (mem[a]) return false;
                mem[a++] = true;
            }
            
        }
        return true;
    }
}
