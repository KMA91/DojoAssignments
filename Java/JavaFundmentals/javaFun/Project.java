class Project{
  private String name;
  private String description;
  private Float initialCost;

  public String elevatorPitch(){
    return (this.name + "(" + this.initialCost + ")" + " : " + this.description);
  }
  // SETTERS
  public void Project() {
  }

  public void Project(String name) {
    this.name = name;
  }
  public void Project(String name, String description, Float initialCost) {
    this.name = name;
    this.description = description;
    this.initialCost = initialCost;
  }
  // GETTERS
  public void getName(){
    System.out.println(this.name);
  }

  public void getDescription(){
    System.out.println(this.description);
  }

  public void getInitialCost(){
    System.out.println(this.initialCost);
  }
}
