public class Mammal {
	protected Integer energyLevel = 100;
	
	public Integer displayEnergy(){
		System.out.println(this.energyLevel);
		return this.energyLevel;
	}

	public void setEnergyLevel(Integer energyLevel) {
		this.energyLevel = energyLevel;
	}
}