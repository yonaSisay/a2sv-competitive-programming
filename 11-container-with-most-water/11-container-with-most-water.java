class Solution {
    public int maxArea(int[] height) {
        int area = 0;
        int r = 0;
        int l = height.length -1;
        
        while(r<l){
            if(height[r]<height[l]){
                area = Math.max(area, height[r] * (l-r));
                r++;
            }else{
                  area = Math.max(area, height[l] * (l-r));
                l--;
            }
        }
        return area;
    }
}