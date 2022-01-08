import readchar
import os
import random

pos_x = 0
pos_y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_MAP_OBJECTS = 15

my_position = [6, 1]
tail_lenght = 0
tail = []
map_objects = []


while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if new_position not in map_objects:
        map_objects.append(new_position)

# print(map_objects)

while True:
    text = " Wizard in the house "
    print(text.center(70, "="))
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None
            for map_object in map_objects:
                if (
                    map_object[pos_x] == coordinate_x
                    and map_object[pos_y] == coordinate_y
                ):
                    char_to_draw = "*"
                    object_in_cell = map_object
            for tail_piece in tail:
                if (
                    tail_piece[pos_x] == coordinate_x
                    and tail_piece[pos_y] == coordinate_y
                ):
                    char_to_draw = "W"
                    tail_in_cell = tail_piece

            if (
                my_position[pos_x] == coordinate_x
                and my_position[pos_y] == coordinate_y
            ):
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1
                if tail_in_cell:
                    print("has muerto!!! ")
                    break
            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("")

    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[pos_y] -= 1
        my_position[pos_y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[pos_y] += 1
        my_position[pos_y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[pos_x] -= 1
        my_position[pos_x] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[pos_x] += 1
        my_position[pos_x] %= MAP_WIDTH
    elif direction == "q":
        break
    os.system("clear")
