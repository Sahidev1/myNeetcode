package Easy_problems.meeting_schedule.java;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
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
        Collections.sort(intervals, new Comparator<Interval>() {
            @Override 
            public int compare(Interval i0, Interval i1){
                return i0.start - i1.start;
            }
        });

        
        
        for (int i = 1; i < intervals.size(); i++){
            if(intervals.get(i).start < intervals.get(i - 1).end) return false;
        }
        return true;
    }
}
