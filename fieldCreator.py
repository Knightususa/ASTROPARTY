import matplotlib.pyplot as plt
import numpy as np
from constants import field_size

field_wall_is=[[0 for i in range(field_size[1]+2)] for j in range(field_size[0]+2)]
field_wall=[[0 for i in range(field_size[1])] for j in range(field_size[0])]

def is_equal(a, b):
    """Checks equality of lists"""
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def input_interface():
    """Interface for field creator"""
    instructions = '''
    Welcome to the Field Creator!\n
    1)You need to draw a picture 20 x 20 pixels (for example in Paint).\n
    2) Use folowing colors to identify blocks:\n
    (255, 255, 255) for empty space\n
    (255, 255, 0) for yellow wall\n
    (0, 255, 0) for green wall\n
    (255, 136, 0) for orange wall\n
    (0, 100, 0) for braking wall\n
    (0, 0, 255) for gravitating wall\n
    (255, 0, 255) and (0, 0, 0) for spawn points\n
    3)Save picture as 'name.bmp' and put it into folder 'graphics'.\n
    4)wright name of the picture without type (example: my_picture.bmp --> my_picture)\n
    5)First list copy to field_typeN where N is number of field\n
    Second list copy to field_wallN\n
    Add field_typeN in list fields\n
    Add field_wallN in list fields_walls\n
    Waiting for picture's name:\n
    '''
    print(instructions)
    name = input()
    image = plt.imread('graphics/' + name + '.bmp')
    if len(image) != field_size[0] or len(image[0]) != field_size[1]:
        print('Your field is not 20 x 20 pixels!')
    return image


def make_field(image):
    """Makes field from the picture"""
    color_keys = [np.array([255, 255, 255]), np.array([255, 255, 0]),
                  np.array([0, 255, 0]), np.array([255, 136, 0]),
                  np.array([0, 100, 0]), np.array([0, 0, 255]),
                  np.array([255, 0, 255]), np.array([0, 0, 0])]
    blocks = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 8, 7: 9}
    field = [[0 for i in range(field_size[1])] for j in range(field_size[0])]
    for i in range(field_size[0]):
        for j in range(field_size[1]):
            for k in range(len(color_keys)):
                curr = []
                if (len(image[i][j]) == 4):
                    curr = image[i][j][:-1]
                else:
                    curr = image[i][j]
                if is_equal(curr, color_keys[k]):
                    field[i][j] = blocks[k]
                    if((field[i][j]==1)or(field[i][j]==2)or(field[i][j]==3)):
                        field_wall_is[i+1][j+1]=1
                    else:
                        field_wall_is[i+1][j+1]=0
    for i in range(field_size[0]):
        for j in range(field_size[1]):
            field_wall[i][j]=field_wall_is[i][j+1]+field_wall_is[i+1][j+2]*2+field_wall_is[i+2][j+1]*4+field_wall_is[i+1][j]*8


    print(field)

    print("\n\n\n\n")

    print(field_wall)


im = input_interface()
make_field(im)
