class StringManipulatorTesting {
  public static void main(String[] args) {
    StringManipulator newnew = new StringManipulator();
    String result = newnew.trimAndConcat("hello       ", "there");
    System.out.println(result);
    String getindex1 = newnew.getIndexOrNull("hello", 'z');
    System.out.println(getindex1);
    String getindex2 = newnew.getIndexOrNull("hello", "helo");
    System.out.println(getindex2);
    String getindex3 = newnew.concatSubString("hello", 1, 4, "world");
    System.out.println(getindex3);
  }
}
