public interface PlayPokemon {
	void attackPokemon(Pokemon pokemon);
	void createPokemon(String name, int health, String type);
	String pokemonInfo(Pokemon pokemon);
}