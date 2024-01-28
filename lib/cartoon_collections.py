def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i + 1}. {dwarves[i]}")    
    pass

def summon_captain_planet(planeteers):
    return [planeteer.capitalize() + '!' for planeteer in planeteers]
    pass

def long_planeteer_calls(words):
    for  n in words:
        if len(n) > 4:
            return True
    return False

def find_the_cheese(cheese_types):
    for cheese in cheese_types:
        if cheese == "gouda" or cheese == "cheddar" or cheese == "camembert":
            return cheese
    pass
