

def direction(facing, turn):
    try:
        facings_list = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        index_turn = turn // 45
        index_facing = facings_list.index(facing)
        return(facings_list[(index_facing + index_turn) % 8])
    except:
        print("Error")

print (direction("SE", -45))
