package com.stopwatch.models;
import java.time.LocalDateTime;

public class Time {
	private LocalDateTime start;
	private LocalDateTime stop;
	private String runningTime;
	
	public Time(LocalDateTime start, LocalDateTime stop, String runningTime){
		this.start = start;
		this.stop = stop;
		this.runningTime = runningTime;
	}
	
	public LocalDateTime getStart() {
		return start;
	}
	public LocalDateTime getStop() {
		return stop;
	}
	public String getRunningTime() {
		return runningTime;
	}
	
}
