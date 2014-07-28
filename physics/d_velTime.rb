#!/usr/bin/env ruby

=begin
Physics Helper #2
distance is equivalent to the
velocity multiplied by the change in time
v = (d/t)
=end

puts "To find the total distance you need to know the velocity and change in time\n Do you know both the velocity and delta time? [Y/N]"
initialQuery = gets.chomp.upcase!

if initialQuery == "Y"
	puts "Enter the velocity (m/s): "
	v = gets.chomp.to_f
	puts "Enter the amount of time which the object traveled (in seconds)"
	t = gets.chomp.to_f
	d = v*t
	puts "The distance traveled is #{d} meters"
else
	puts "This script cannot solve your problem, look at a different velocity script, or solve for distance or time first."
end
