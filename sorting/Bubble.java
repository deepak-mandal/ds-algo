import java.util.Arrays;

public class Bubble{

    public void bubbleSort(int arr[]){
        for(int i=arr.length-1; i>=0; i--){
            for(int j=0; j<i; j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;

                }
            }
        }
    }

    public static void main(String args[]){
        System.out.println("Bubble sort");

        int list1[]={7, 3, 23, 2, 43, 7, 7};
        System.out.println(Arrays.toString(list1));
        Bubble bubble=new Bubble();
        bubble.bubbleSort(list1);
        System.out.println(Arrays.toString(list1));
    }
}