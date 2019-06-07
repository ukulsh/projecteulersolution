
def find_cycle_length(n):
    cycle_length = 0
    list_of_remainder = []
    x = 1
    while(True):
        if x%n == 0:
            break
        elif x in list_of_remainder:
            break
        list_of_remainder.append(x)
        x = x*10%n
        cycle_length +=1
    return cycle_length
def main():
    d = 1000
    max_cycle_length = 0
    itha = 0
    for i in range(1,d):
        current_cycle = find_cycle_length(i)
        if current_cycle > max_cycle_length:
            max_cycle_length = current_cycle
            itha = i
            print(i)
main()

        
