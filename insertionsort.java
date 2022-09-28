    public static void print(List<Integer> arr){
        for(int x: arr){
            System.out.print(x+" ");
        }
        System.out.println();
    }
    public static void insertionSort1(int n, List<Integer> arr) {
        int key = arr.get(arr.size()-1);
        int j = arr.size()-2;
        
        while(j>=0 && arr.get(j)>key){
            arr.set(j+1, arr.get(j));
            j--;
            print(arr);
        }
        
        arr.set(j+1, key);
        print(arr);
    }