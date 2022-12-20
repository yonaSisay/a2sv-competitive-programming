import java.util.*;

class HelloWorld {
    public static void word(String word, int n){
        String[] words = word.split("/n",n);
        HashMap <String,Integer> map = new HashMap<>();
        for(String s: words){
            if(map.containsKey(s)){
                map.put(s,map.get(s)+1);
                --n;
            }else{
                map.put(s,1);
            }
        }
        System.out.println(n);
        for(Map.Entry<String,Integer> mapElement: map.entrySet()){
            Integer value = mapElement.getValue();
            System.out.print(" "+value);
        }
    }
    public static void main(String[] args) {
        word("yonas/nsisay/nyonas/nabebe",4);
    }
}
