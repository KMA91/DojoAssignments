package com.teamroster.models;

import java.util.ArrayList;

public class Team implements java.io.Serializable{
	private String team_name;
	private int playercount = 0;

	private ArrayList<Player> players;
	
	public Team(){
	}
	
	public Team(String team_name){
		this.team_name = team_name;
	}
	
	public void setPlayers(ArrayList<Player> players) {
		this.players = players;
		this.playercount ++;
	}
	
	public String getTeam_name() {
		return team_name;
	}

	public int getPlayercount() {
		return playercount;
	}
	
	public void getIndexof(Team team){
		
		players[] p = players;
		for(int x = 0; x < this.playercount; x++){
			if(p[x] == team){
				
			}
		}
	}
	
}