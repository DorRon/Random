#!/usr/bin/env ruby

=begin
Physics Helper #1
velocity is equivalent to the
distance divided by the change in time
v = (d/t)
=end

puts "To find the velocity you need to know both the distance traveled over an interval of time\n Do you know both the distance and delta time? [Y/N]"
initialQuery = gets.chomp.upcase!

if initialQuery == "Y"
	puts "Enter the total distance traveled (in meters): "
	d = gets.chomp.to_f
	puts "Enter the amount of time which the object traveled (in seconds)"
	t = gets.chomp.to_f
	v = (d/t)
	puts "The velocity of the object is #{v} m/s"
else
	puts "This script cannot solve your problem, look at a different velocity script, or solve for distance or time first."
end
