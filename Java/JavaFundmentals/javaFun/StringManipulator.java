class StringManipulator{
  public String trimAndConcat(String string1, String string2){
    string1 = string1.trim();
    string2 = string2.trim();
    String string3 = string1.concat(string2);
    return string3;
  }
  public String getIndexOrNull(String string, char character){
    int index = string.indexOf(character);
    if(index == -1){
      return "not found";
    }else{
      return "" + index;
    }
  }
  public String getIndexOrNull(String string1, String string2){
    int index = string1.indexOf(string2);
    if(index == -1){
      return "not found";
    }else{
      return "" + index;
    }
  }
  public String concatSubString(String string1, int int1, int int2, String string2){
    String string3 = "";
    for(int x = int1; x < int2; x = x + 1){
      string3 += string1.charAt(x);
    }
    return string3 + string2;
  }
}
