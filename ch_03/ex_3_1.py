def find_pay(hours, rate):
    h = float(hours)
    overtime = h - 40
    r = float(rate)
    total = 0

    if h > 40:
        total += r * 40
        total += overtime * r * 1.5
    
    return total
 
print(find_pay(45, 10.50))