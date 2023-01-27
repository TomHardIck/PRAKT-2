def getDays(monthNum : int, vis : bool) -> int:
    if(monthNum in (1, 3, 5, 7, 8, 10, 12)):
        return 31
    if(monthNum in (4, 6, 9, 11)):
        return 30
    if(monthNum == 2 and vis): return 29
    if(monthNum == 2 and not vis): return 28

def main():
    year = int(input("Введите год: "))
    visMain = False
    if(year % 4 == 0): visMain = True
    sum = 0
    for i in range(1, 13):
        daysInMonth = getDays(i, visMain)
        for j in range(1, daysInMonth + 1):
            if(len(str(j)) == 1):
                sum += j
            else:
                sum += int(str(j)[0]) + int(str(j)[1])
    print("Сумма: ", sum)

if __name__ == '__main__':
    main()