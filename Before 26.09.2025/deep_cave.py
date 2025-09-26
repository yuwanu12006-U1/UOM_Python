import random, sys, time

WIDTH = 70
PAUSE_AMOUNT = 0.05

time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

diceroll = random.randit(1, 6)
if diceroll == 1 and leftWidth > 1:
    leftWidth = leftWidth - 1
elif diceroll == 2 and leftWidth + gapWidth < WIDTH - 1:
    leftWidth = leftWidth + 1
else:
    pass

