
public abstract class AbstractClass implements PlayPokemon{
//	@Override
	public void attackPokemon(Pokemon pokemon){
		pokemon.setHealth(pokemon.getHealth() - 10);
	}
//	@Override
	public String pokemonInfo(Pokemon pokemon){
		return "Name: " + pokemon.getName() + ". Health: " + pokemon.getHealth() + ". Type: " + pokemon.getType() + ".";
	}
//	@Override
	public void createPokemon(String name, int health, String type){
		new Pokemon(name, health, type);
	}
}