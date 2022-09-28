public static List<Integer> gradingStudents(List<Integer> grades) {
    // Write your code here
for (int i = 0; i < grades.size(); i++ ) {
            int item = grades.get(i);
            if (item >= 38 && item%5 != 0) {
                int targetNumber = ((item/5) +1) * 5;
                int difference = targetNumber - item;
                if ( difference < 3 )
                    grades.set(i, targetNumber); 
            }
        }
        
        return grades;

    }

}