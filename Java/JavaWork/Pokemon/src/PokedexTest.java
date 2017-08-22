class PokedexTest {

	public static void main(String[] args) {
		Pokemon pokemon = new Pokemon("Kevin", 100, "Grass");
		Pokedex pokedex = new Pokedex();
		pokedex.createPokemon("Kelvin", 50, "Fire");
		System.out.println(pokedex.pokemonInfo(pokemon));
	}
}
