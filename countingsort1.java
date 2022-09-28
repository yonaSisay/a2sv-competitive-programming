   public static List<Integer> countingSort(List<Integer> arr) {
    // Write your code here
      List<Integer> output = new ArrayList<>(Collections.nCopies(100, 0));
        for (Integer value : arr) {
            if (output.get(value) != 0) {
                output.set(value, output.get(value)+1);
            } else {
                output.set(value, 1);
            }
        }
    return output;

    }