def grade(score):
    s = float(score)
    if s < 0.6: return 'F'
    elif s >= 0.6 and s < 0.7: return 'D'
    elif s >= 0.7 and s < 0.8: return 'C'
    elif s >= 0.8 and s < 0.9: return 'B'
    elif s >= 0.9 and s <= 1.00: return 'A'
    else:
        print('not a valid entry')
        exit()

print(grade(0.85))