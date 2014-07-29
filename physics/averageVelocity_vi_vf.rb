#!/usr/bin/env ruby

=begin 
finding average velocity based 
off final and initial velocities
v(avg) = (Vi + Vf) / 2
=end

puts "Enter initial velocity(m/s) "
vi = gets.chomp.to_f
puts "Enter final velocity(m/s) "
vf = gets.chomp.to_f

average = (vi + vf) / 2
puts "The average velocity is #{average} m/s"

#end
