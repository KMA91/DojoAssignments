import java.util.ArrayList;

class BasicJava{
  public void printTo255(){
    for(int x = 1; x < 255; x++){
      System.out.println(x);
    }
  }
  public void printOdd255(){
    for(int x = 1; x < 255; x++){
      if(x % 2 == 1){
        System.out.println(x);
      }
    }
  }
  public void sumOf255(){
    int sum = 0;
    for(int x = 0; x < 255; x++){
      System.out.println("New number: " + x);
      sum += x;
      System.out.println("Sum: " + sum);
    }
  }
  public void iterateArray(int[] array){
    for(int x = 0; x < array.length; x++){
      System.out.println(array[x]);
    }
  }
  public int findMax(int[] array){
    int max = 0;
    for(int x = 0; x < array.length; x++){
      if(max < array[x]){
        max = array[x];
      }
    }
    return max;
  }
  public void findAvg(int[] array){
    int avg = 0;
    for(int x = 0; x < array.length; x++){
      avg += array[x];
    }
    avg = avg / array.length;
    System.out.println(avg);
  }
  public void allOdd(){
    ArrayList<Integer> myArray = new ArrayList<>();
    for(int x = 0; x < 256; x ++){
      if(x % 2 == 1){
        myArray.add(x);
      }
    }
    System.out.println(myArray);
  }
  public void greaterThanY(int[] array, int number){
    int count = 0;
    for(int x = 0; x < array.length; x++){
      if(array[x] > number){
        count += 1;
      }
    }
    System.out.println(count);
  }
  public void squareTheValues(int[] array){
    ArrayList<Integer> myArray = new ArrayList<>();
    for(int x = 0; x < array.length; x++){
      myArray.add(array[x]*array[x]);
    }
    System.out.println(myArray);
  }
  public void eliminateNeg(int[] array){
    ArrayList<Integer> myArray = new ArrayList<>();
    for(int x = 0; x < array.length; x++){
      if(array[x] < 0){
        myArray.add(0);
      }else{
        myArray.add(array[x]);
      }
    }
    System.out.println(myArray);
  }
  public void maxMinAvg(int[] array){
    ArrayList<Integer> myArray = new ArrayList<>();
    int max = array[0];
    int min = array[0];
    int avg = array[0];
    for(int x = 1; x < array.length; x++){
      if(max < array[x]){
        max = array[x];
      }
      if(min > array[x]){
        min = array[x];
      }
      avg += array[x];
    }
    avg = avg/array.length;
    myArray.add(max);
    myArray.add(min);
    myArray.add(avg);
    System.out.println(myArray);
  }
  public void shiftValues(int[] array){
    ArrayList<Integer> myArray = new ArrayList<>();
    myArray.add(array[1]);
    for(int x = 2; x < array.length; x++){
        myArray.add(array[x]);
      }
      myArray.add(0);
    System.out.println(myArray);
  }
}
