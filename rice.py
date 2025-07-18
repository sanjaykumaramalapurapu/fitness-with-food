def calories_badmintion(weight_badmintion,minutes_badmintion):
    s= (6*weight_badmintion*3.5)/200
    return (s*minutes_badmintion)
    # (MET x body weight in Kg x 3.5) ÷ 200

def calories_run(weight_run, speed,minutes_run):
    if speed>=6 and speed<8:
        p=(5*weight_run*3.5)/200
        return (p*minutes_run)
    elif speed>=8 and speed<9:
        p = (9 * weight_run * 3.5) / 200
        return (p * minutes_run)
    elif speed>=9 and speed<11:
        p = (10.8 * weight_run * 3.5) / 200
        return (p * minutes_run)
    elif speed>=11 and speed<13:
        p = (11.8 * weight_run * 3.5) / 200
        return (p * minutes_run)
    elif speed>=13 and speed<15:
        p = (13.5 * weight_run * 3.5) / 200
        return (p * minutes_run)
    elif speed>=15 and speed<17:
        p = (15.5 * weight_run * 3.5) / 200
        return (p * minutes_run)
    elif speed>=17 and speed<19:
        p = (16.5 * weight_run * 3.5) / 200
        return (p * minutes_run)
    elif speed>=19 and speed<20:
        p = (19 * weight_run * 3.5) / 200
        return (p * minutes_run)
    elif speed>=20 and speed<21:
        p = (20 * weight_run * 3.5) / 200
        return (p * minutes_run)
    elif speed>=21 and speed<22:
        p = (23 * weight_run * 3.5) / 200
        return (p * minutes_run)
    else:
        return 0
def calories_swim(weight_swim, minutes_swim):
    s = (7 * weight_swim * 3.5) / 200
    return (s * minutes_swim)
    # (MET x body weight in Kg x 3.5) ÷ 200
def calories_cycle(weight_cycle, minutes_cycle):
    s = (7.5 * weight_cycle * 3.5) / 200
    return (s * minutes_cycle)
def calories_boxing(weight_boxing, minutes_boxing):
    s = (5.5 * weight_boxing * 3.5) / 200
    return (s * minutes_boxing)