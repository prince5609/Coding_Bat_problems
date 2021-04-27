'''QUESTON=
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each)
and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks.

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''

def make_bricks(small,big,goal):
    total_big_len=big*5
    if goal == total_big_len:
        return True
    elif goal == small:
        return True
    else:
        if total_big_len+small>=goal:
            big_req=int(goal/5)
            if big_req<=big:
                big_length_used=big_req*5
                small_req=goal-big_length_used
                if small_req<=small:
                    total_length=big_length_used+small_req
                    if total_length==goal:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return True
        else:
            return False
print(make_bricks(3, 1, 8))
print(make_bricks(6, 0, 11))

