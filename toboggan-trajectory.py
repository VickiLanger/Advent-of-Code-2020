"""
toboggan-trajectory.py: from day_3.txt find out how many trees the sled would hit when moving right 3 and down 1; solve puzzle at https://adventofcode.com/2020/day/3
3 December 2020
@Vicki_Langer / @VickiLanger
"""


# read text file
tree_map_section = open("inputs/day_3.txt", "r").read().splitlines()

# repeat tree_map_section to the right a bunch of times
tree_map_full = 

move_right = 3
move_down = 1
while move_right and move_down:
    tree = "#"
    hit_tree_count = 0
    if hit tree:
        hit_tree_count += 1
    print("Damn! You hit " + hit_tree_count + " trees! How are you still alive?!")


"""
repeat tree_map_section to the right a bunch of times
tree = "#"
move sled 3 to the right
move sled 1 spot down
count trees when moving right 3 and down 1
print number of trees hit
"""