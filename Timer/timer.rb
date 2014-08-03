#!/usr/bin/env ruby

def timer
    print "Enter how many seconds you want to count down from: "
    total = gets.chomp.to_f
    until total <= 0
        puts total
        if total > 0 && total < 1 #in order to insure that decimal places (floats) are accounted for
            sleep(total)
        else
            sleep(1)
        end
        total -= 1
    end
end
    
timer
#end
