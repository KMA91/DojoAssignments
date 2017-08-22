import java.util.List;
import java.util.ArrayList;

class Exceptions{
  public static void main(String[] args){
    List myList = new ArrayList();
    myList.add("13");
    myList.add("hello world");
    myList.add(48);
    myList.add("Goodbye World");
    for(int i = 0; i < myList.size(); i++){
      try{
                int i2 = (Integer)myList.get(i);
                System.out.println(i2);
      } catch (RuntimeException e){
              System.out.println("ERROR ON INDEX " + i);
      }
    }
  }
}
