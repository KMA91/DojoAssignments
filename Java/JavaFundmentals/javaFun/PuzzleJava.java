import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Random;

class PuzzleJava{
  public ArrayList<Integer> greaterthan10(int[] array){
    ArrayList<Integer> myArray = new ArrayList<>();
    for(int x = 0; x < array.length; x++){
      System.out.println(array[x]);
      if(array[x] > 10){
        myArray.add(array[x]);
      }
    }
    return myArray;
  }
  public ArrayList<String> names(String[] array){
    ArrayList<String> myArray = new ArrayList<>();
    for(int x = 0; x < array.length; x++){
      myArray.add(array[x]);
    }
    Collections.shuffle(myArray);
    for(int x = 0; x < myArray.size(); x++){
      System.out.println(myArray.get(x));
      if(myArray.get(x).length() <= 5){
        System.out.println("LESS THAN 5");
      }
    }
    return myArray;
  }
  public void letters(char[] array){
    ArrayList<Character> array2 = new ArrayList<>();
    for(int x = 0; x < array.length; x++){
      array2.add(array[x]);
    }
    Collections.shuffle(array2);
    System.out.println(array2);
    System.out.println(array2.get(0) + " is first!");
    System.out.println(array2.get(25) + " is last! ");
    char[] vowelArray = {'a','e','i','o','u','y'};
    for(int x = 0; x < vowelArray.length; x++){
      if(array2.get(0) == vowelArray[x]){
        System.out.println(vowelArray[x] + " is a vowel!");
      }
    }
  }
  public ArrayList<Integer> random10(){
    ArrayList<Integer> myArray = new ArrayList<>();
    while(myArray.size() <= 10){
      Random rand = new Random();
      int n = rand.nextInt(100) + 55;
      myArray.add(n);
    }
    return myArray;
  }
  public void random10again(){
    ArrayList<Integer> myArray = new ArrayList<>();
    while(myArray.size() <= 10){
      Random rand = new Random();
      int n = rand.nextInt(100) + 55;
      myArray.add(n);
    }
    Collections.sort(myArray);
    System.out.println(myArray);
    System.out.println(myArray.get(0) + " is the lowest number!");
    System.out.println(myArray.get(10) + " is the highest number!");
  }
  public void randomstring(){
    String myString = "";
    for(int x = 0; x <= 5; x++){
      Random r = new Random();
      char c = (char)(r.nextInt(26) + 'a');
      myString += c;
    }
    System.out.println(myString);
  }
  public void random10string(){
    ArrayList<String> myArray = new ArrayList<>();
    for(int x = 0; x <= 10; x++){
      String myString = "";
      for(int y = 0; y <= 5; y++){
        Random r = new Random();
        char c = (char)(r.nextInt(26) + 'a');
        myString += c;
      }
      myArray.add(myString);
    }
    System.out.println(myArray);
  }
}
