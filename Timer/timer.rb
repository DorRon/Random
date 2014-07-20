def timer    
    seconds = "Enter how many seconds you want to count down from: "
    print seconds
    total = gets.chomp.to_i
    until total <= 0
        puts total
        sleep(1)
        total -= 1
    end
end

timer
