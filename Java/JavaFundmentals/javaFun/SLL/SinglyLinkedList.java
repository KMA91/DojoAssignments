class SinglyLinkedList{
  private Node head;

  public SinglyLinkedList(){
    this.head = null;
  }

  public void add(Node node){
    if(this.head == null){
      this.head = node;
    }else{
      Node current = this.head;
      while(current.next != null){
        current = current.next;
      }
      current.next = node;
    }
  }

  public void remove(){
    if(this.head == null){
      System.out.println("SLL HAS NO HEAD");
    }else{
      Node current = this.head;
      while(current.next.next != null){
        current = current.next;
      }
      current.next = null;
    }
  }

  public void printValues(){
    if(this.head == null){
      System.out.println("No values!");
    }else{
      Node current = this.head;
      while(current != null){
        Integer x = 1;
        System.out.println("Node # " + x + " is " + current.value);
        x = x + 1;
        current = current.next;
      }
    }
  }
}
