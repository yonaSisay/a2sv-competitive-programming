    public static void countSwaps(List<Integer> a) {
        int n = a.size();
        int temp;
        long swaps = 0;
        boolean swaped;
        
        for(int i=0; i<n; i++){
            swaped = false;
            for(int j =0 ;j<n-1;j++){
               if(a.get(j)>a.get(j+1)){
                  temp = a.get(j);
                  a.set(j,a.get(j+1));
                  a.set(j+1, temp);
                  swaped =true;
                  swaps++;
               }
            }
            if(swaped==false) break; 
        }
        System.out.println("Array is sorted in "+swaps+" swaps.");
        System.out.println("First Element: "+a.get(0));
        System.out.println("Last Element: "+a.get(n-1));
    }

}
