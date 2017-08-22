
public class BankAccountTest {

	public static void main(String[] args) {
		BankAccount b = new BankAccount();
		b.getCBalance();
		b.getSBalance();
		b.deposit("checking", 25);
		b.deposit("savings", 45);
		b.withdraw("checking", 75);
		b.withdraw("savings", 10);
		b.getTotal();
//		next line will error. this is to check access to private method
		System.out.println(BankAccount.totalaccounts);
	}

}
