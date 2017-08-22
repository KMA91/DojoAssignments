import java.util.HashMap;

class TrackList{
  public static void main(String[] args){
    HashMap <String, String> userMap = new HashMap<>();

    userMap.put("titleone", "lyrics1");
    userMap.put("titletwo", "lyrics2");
    userMap.put("titlethree", "lyrics3");
    userMap.put("titlefour", "lyrics4");

    System.out.println(userMap.get("titleone"));
    System.out.println("Track: titleone" + " Lyrics: " + userMap.get("titleone"));
    System.out.println("Track: titletwo" + " Lyrics: " + userMap.get("titletwo"));
    System.out.println("Track: titlethree" + " Lyrics: " + userMap.get("titlethree"));
    System.out.println("Track: titlefour" + " Lyrics: " + userMap.get("titlefour"));
  }
}
