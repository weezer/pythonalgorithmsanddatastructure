def move(fromPole, tempPole, toPole, platesnum):
    if platesnum == 1:
        print "move from " + fromPole + " to " + toPole
        return

    move(fromPole, toPole, tempPole, platesnum - 1)
    print "move from " + fromPole + " to " + toPole
    move(tempPole, fromPole, toPole, platesnum - 1)

if __name__ == "__main__":
    move("A", "B", "C", 3)