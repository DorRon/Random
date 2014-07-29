#!/usr/bin/env ruby

=begin
finding the final velocity of an entity
based off accelaration, initial velocity,
as well as the change in time.
Vf = Vi + (a*t)
=end

puts "Enter initial velocity(m/s) here: "
vi = gets.chomp.to_f
puts "Enter accelaration(m/s^2) here: "
a = gets.chomp.to_f
puts "Enter change in time(in seconds) here: "
t = gets.chomp.to_f

vf = vi + (a*t)
puts "The final velocity of the object is #{vf} meters/second"

#end
