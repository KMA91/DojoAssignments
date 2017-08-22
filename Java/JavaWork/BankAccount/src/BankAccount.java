import java.util.Random;

public class BankAccount {
	private String accountNumber;
	private long checkingBalance = 0;
	private long savingsBalance = 0;
	private static int totalaccounts = 0;
	private static int totalamount = 0;
	
	public BankAccount(){
		this.accountNumber = createAccount();
		totalaccounts += 1;
	}
	public String createAccount(){
		String string = "";
		for(int x = 0; x <= 10; x++){
			Random r = new Random();
		    int n = 1 + r.nextInt(9);
		    string += n;		
		}
		return string;
	}
	public long getCBalance(){
		System.out.println(this.checkingBalance);
		return this.checkingBalance;
	}
	
	public long getSBalance(){
		System.out.println(this.savingsBalance);
		return this.savingsBalance;
	}
	
	public void deposit(String account, long amount){
		if(account == "checking"){
			this.checkingBalance += amount;
			this.totalamount += amount;
		}else{
			this.savingsBalance += amount;
			this.totalamount += amount;
		}
	}
	
	public void withdraw(String account, long amount){
		if(account == "checking"){
			if(this.checkingBalance < amount){
				System.out.println("You do not have enough in your checking account!");
			}else{
				this.checkingBalance -= amount;
				this.totalamount -= amount;
			}
		}else{
			if(this.savingsBalance < amount){
				System.out.println("You do not have enough in your savings account!");
			}else{
				this.savingsBalance -= amount;
				this.totalamount -= amount;
			}
		}
	}
	public void getTotal(){
		System.out.println("Checking total is: " + this.checkingBalance + ". Savings total is: " + this.savingsBalance + ".");
	}
}