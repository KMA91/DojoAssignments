public class Calculator implements UseCalculator{
	public double operand;
	public int operandcheck = 0;
	public String operation;
	public double operand2;
	public int operandcheck2 = 0;
	public double result;
	
	public void setOperandOne(String operand) {
		this.operand = Double.parseDouble(operand);
		System.out.println("Operand One =>" + operand);
	}
	public void setOperation(String operation) {
		this.operation = operation;
		System.out.println("Operation =>" + operation);
	}
	public void setOperandTwo(String operand2) {
		this.operand2 = Double.parseDouble(operand2);
		System.out.println("Operand Two =>" + operand2);
	}
	
	public void performOperation(String value){
		if(this.isDouble(value)){
			if(operandcheck == 0 && operandcheck2 == 0){
				operand = Double.parseDouble(value);
				operandcheck = 1;
				result = operand;
			}
			else if(operandcheck == 1 && operandcheck2 == 0){
				operand2 = Double.parseDouble(value);
				operandcheck2 = 1;
				result = operand2;
			}
			else if(operandcheck == 1 && operandcheck2 == 1){
				operand = Double.parseDouble(value);
				result = operand;
				operandcheck2 = 0;
			}
			else if(operandcheck == 2 && operandcheck2 == 0){
				this.perform(operand, Double.parseDouble(value));
				operandcheck2 = 2;
			}
			else if(operandcheck == 2 || operandcheck == 1 && operandcheck2 == 2){
				this.perform(operand, operand2);
			}
			else if(operandcheck == 2 && operandcheck2 == 1){
				this.perform(operand, operand2);
			}
		}
		else if(value == "+"){
			if(operandcheck == 1 && operandcheck2 == 0 || operandcheck == 2 && operandcheck2 == 0){
				result = operand;
				operandcheck = 2;
				this.operation = "+";
			}else if(operandcheck == 2 && operandcheck2 == 2){
				operand = result;
				operandcheck = 1;
				operandcheck2 = 0;
			}else{
				result = operand + operand2;
				operandcheck2 = 2;
			}
		}
		else if(value == "-"){
			if(operandcheck == 1 && operandcheck2 == 0 || operandcheck == 2 && operandcheck2 == 0){
				result = operand;
				operandcheck = 2;
				operation = "-";
			}else if(operandcheck == 2 && operandcheck2 == 2){
				operand = result;
				operandcheck = 1;
				operandcheck = 0;
			}else{
				result = operand - operand2;
				operandcheck2 = 2;
			}
		}
		else if(value == "/"){
			if(operandcheck == 1 && operandcheck2 == 0 || operandcheck == 2 && operandcheck2 == 0){
				result = operand;
				operandcheck = 2;
				operation = "/";
			}else if(operandcheck == 2 && operandcheck2 == 2){
				operand = result;
				operandcheck = 1;
				operandcheck = 0;
			}else{
				result = operand / operand2;
				operandcheck2 = 2;
			}
		}
		else if(value == "*"){
			if(operandcheck == 1 && operandcheck2 == 0){
				result = operand;
				operandcheck = 2;
				operation = "*";
			}else if(operandcheck == 2 && operandcheck2 == 2){
				operand = result;
				operandcheck = 1;
				operandcheck = 0;
			}else{
				result = operand * operand2;
				operandcheck2 = 2;
			}
		}
		else if(value == "="){
			if(operandcheck == 2 && operandcheck2 == 1){
				operandcheck = 1;
				operandcheck2 = 0;
				this.perform(operand, operand2);
			}
		}
	}
	
	private boolean isDouble(String value){
		try {
			Double.parseDouble(value);
			return true;
		} catch (NumberFormatException e){
			return false;
		}
	}
	
	private void perform(double operand, double operand2){
		if(operation == "+"){
			result = operand + operand2;
			operand = result;
			operandcheck2 = 0;
		}
		else if(operation == "-"){
			result = operand - operand2;
			operand = result;
			operandcheck2 = 0;
		}
		else if(operation == "/"){
			result = operand/operand2;
			operand = result;
			operandcheck2 = 0;
		}
		else if(operation == "*"){
			result = operand*operand2;
			operand = result;
			operandcheck2 = 0;
		}
	}

	@Override
	public double getResults() {
		return result;
	}
}
