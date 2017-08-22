class ListTester{
  public static void main(String[] args) {
    SinglyLinkedList s = new SinglyLinkedList();
    Node n = new Node(5);
    Node n1 = new Node(64);
    Node n2 = new Node(34);
    s.add(n);
    // s.printValues();
    s.add(n1);
    // s.printValues();
    s.add(n2);
    s.remove();
    s.printValues();
  }
}
