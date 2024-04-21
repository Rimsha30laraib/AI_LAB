def tower_of_hanoi(n,disk1,disk2,disk3):
    if (n==1):
        print("Disk",n,"moved from",disk1,"to",disk3)
        return
    tower_of_hanoi(n-1,disk1,disk3,disk2)
    print("Disk",n,"moved from",disk1,"to",disk3)
    tower_of_hanoi(n-1,disk2,disk1,disk3)

tower_of_hanoi(3,"A","B","C")