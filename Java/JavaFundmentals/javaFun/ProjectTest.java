class ProjectTest{
  public static void main(String[] args) {
    Project p1 = new Project();
    p1.Project("Kevin", "Likes to eat tacos", 2.5f);
    p1.getName();
    p1.getDescription();
    System.out.println(p1.elevatorPitch());
  }
}
