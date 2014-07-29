#!/usr/bin/env ruby

=begin
finding the accelaration of an entity
based off final and initial velocity
as well as the change in time.
a = (Vf - Vi) / delta(t)
=end

puts "Enter final velocity (m/s): "
vf = gets.chomp.to_f
puts "Enter initial velocity (m/s): "
vi = gets.chomp.to_f
puts  "Enter the change in time (in seconds): "
t = gets.chomp.to_f

a = (vf-vi)/t
puts "The accelaration of the object is #{a} m/s^2"

#end
