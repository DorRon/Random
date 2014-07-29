#!/usr/bin/env ruby

=begin
finding the initial velocity from the
final velocity, accelaration, and the
change in time.

Vi = Vf - (a*t)
=end

puts "Enter final velocity(m/s) "
vf = gets.chomp.to_f
puts "Enter the accelaration(m/s^2) "
a = gets.chomp.to_f
puts "Enter the change in time(in seconds) "
t = gets.chomp.to_f

vi = vf - (a*t)
puts "The initial velocity of the object is #{vi} m/s"

#end
