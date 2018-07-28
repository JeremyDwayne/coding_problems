import java.util.Arrays;

class DCP {
  public static void main(String[] args){
    TwoSum p1 = new TwoSum();
    int[] vals = {10,15,3,7};
    System.out.println(p1.twoSum(vals, 17));

    ArrayProducts ap = new ArrayProducts();
    int[] apv1 = {1,2,3,4,5};
    System.out.println(Arrays.toString(ap.findProducts(apv1)));
    
  }
}
