from Tests import *


class RotationPocketCubeTests:
    def __init__(self):
        self.cube = PocketCube()
        self.front = self.cube.faces[4]
        self.right = self.cube.faces[1]
        self.down = self.cube.faces[3]
        self.left = self.cube.faces[0]
        self.up = self.cube.faces[2]
        self.back = self.cube.faces[5]


class init_cube_expected:
    def __init__(self):
        self.cubeFaceList = None
        self.init_cube = RotationPocketCubeTests()
        self.init = init_Tests_PocketCube()

        self.front_expected = [Block(0, 0, 0), Block(1, 0, 0),
                               Block(0, 1, 0), Block(1, 1, 0)]

        self.right_expected = [Block(1, 0, 0), Block(1, 0, 1),
                               Block(1, 1, 0), Block(1, 1, 1)]

        self.down_expected = [Block(0, 1, 0), Block(1, 1, 0),
                              Block(0, 1, 1), Block(1, 1, 1)]

        self.left_expected = [Block(0, 0, 1), Block(0, 0, 0),
                              Block(0, 1, 1), Block(0, 1, 0)]

        self.up_expected = [Block(0, 0, 1), Block(1, 0, 1),
                            Block(0, 0, 0), Block(1, 0, 0)]

        self.back_expected = [Block(1, 0, 1), Block(0, 0, 1),
                              Block(1, 1, 1), Block(0, 1, 1)]

    def check_init_cube_creation(self):
        front = self.init.check_face(self.front_expected, self.init_cube.front)
        right = self.init.check_face(self.right_expected, self.init_cube.right)
        down = self.init.check_face(self.down_expected, self.init_cube.down)
        left = self.init.check_face(self.left_expected, self.init_cube.left)
        up = self.init.check_face(self.up_expected, self.init_cube.up)
        back = self.init.check_face(self.back_expected, self.init_cube.back)

        self.cubeFaceList = [front, right, down, left, up, back]
        colorTest = self.init.true_or_falseColorTest(self.cubeFaceList)
        print("[init_cube_expected => front:{} right:{} down:{} left:{} up:{} back:{}]".format(
            colorTest[0], colorTest[1], colorTest[2], colorTest[3], colorTest[4], colorTest[5]))


class horizontalClockwise_oneTurn_lineZero_expected:
    def __init__(self):
        self.cubeFaceList = None
        self.horizontalClockwise_oneTurn_lineZero = RotationPocketCubeTests()
        self.horizontalClockwise_oneTurn_lineZero.cube.horizontal_rotation_clockwise(0)
        self.init = init_Tests_PocketCube()

        self.left_expected = [Block(0, 0, 0), Block(1, 0, 0),
                              Block(0, 1, 1), Block(0, 1, 0)]

        self.front_expected = [Block(1, 0, 0), Block(1, 0, 1),
                               Block(0, 1, 0), Block(1, 1, 0)]

        self.right_expected = [Block(1, 0, 1), Block(0, 0, 1),
                               Block(1, 1, 0), Block(1, 1, 1)]

        self.back_expected = [Block(0, 0, 1), Block(0, 0, 0),
                              Block(1, 1, 1), Block(0, 1, 1)]

        self.up_expected = [Block(0, 0, 0), Block(0, 0, 1),
                            Block(1, 0, 0), Block(1, 0, 1)]

        self.down_expected = [Block(0, 1, 0), Block(1, 1, 0),
                              Block(0, 1, 1), Block(1, 1, 1)]

    def check_horizontalClockwise_oneTurn_lineZero(self):
        front = self.init.check_face(self.front_expected, self.horizontalClockwise_oneTurn_lineZero.front)
        right = self.init.check_face(self.right_expected, self.horizontalClockwise_oneTurn_lineZero.right)
        down = self.init.check_face(self.down_expected, self.horizontalClockwise_oneTurn_lineZero.down)
        left = self.init.check_face(self.left_expected, self.horizontalClockwise_oneTurn_lineZero.left)
        up = self.init.check_face(self.up_expected, self.horizontalClockwise_oneTurn_lineZero.up)
        back = self.init.check_face(self.back_expected, self.horizontalClockwise_oneTurn_lineZero.back)

        self.cubeFaceList = [front, right, down, left, up, back]
        colorTest = self.init.true_or_falseColorTest(self.cubeFaceList)
        print("[horizontalClockwise_oneTurn_lineZero => front:{} right:{} down:{} left:{} up:{} back:{}]".format(
            colorTest[0], colorTest[1], colorTest[2], colorTest[3], colorTest[4], colorTest[5]))


class horizontalClockwise_oneTurn_lineOne_expected:
    def __init__(self):
        self.cubeFaceList = None
        self.horizontalClockwise_oneTurn_lineOne = RotationPocketCubeTests()
        self.horizontalClockwise_oneTurn_lineOne.cube.horizontal_rotation_clockwise(1)
        self.init = init_Tests_PocketCube()

        self.left_expected = [Block(0, 0, 1), Block(0, 0, 0),
                              Block(0, 1, 0), Block(1, 1, 0)]

        self.front_expected = [Block(0, 0, 0), Block(1, 0, 0),
                               Block(1, 1, 0), Block(1, 1, 1)]

        self.right_expected = [Block(1, 0, 0), Block(1, 0, 1),
                               Block(1, 1, 1), Block(0, 1, 1)]

        self.back_expected = [Block(1, 0, 1), Block(0, 0, 1),
                              Block(0, 1, 1), Block(0, 1, 0)]

        self.up_expected = [Block(0, 0, 1), Block(1, 0, 1),
                            Block(0, 0, 0), Block(1, 0, 0)]

        self.down_expected = [Block(1, 1, 0), Block(1, 1, 1),
                              Block(0, 1, 0), Block(0, 1, 1)]

    def check_horizontalClockwise_oneTurn_lineOne(self):
        front = self.init.check_face(self.front_expected, self.horizontalClockwise_oneTurn_lineOne.front)
        right = self.init.check_face(self.right_expected, self.horizontalClockwise_oneTurn_lineOne.right)
        down = self.init.check_face(self.down_expected, self.horizontalClockwise_oneTurn_lineOne.down)
        left = self.init.check_face(self.left_expected, self.horizontalClockwise_oneTurn_lineOne.left)
        up = self.init.check_face(self.up_expected, self.horizontalClockwise_oneTurn_lineOne.up)
        back = self.init.check_face(self.back_expected, self.horizontalClockwise_oneTurn_lineOne.back)

        self.cubeFaceList = [front, right, down, left, up, back]
        colorTest = self.init.true_or_falseColorTest(self.cubeFaceList)
        print("[horizontalClockwise_oneTurn_lineOne => front:{} right:{} down:{} left:{} up:{} back:{}]".format(
            colorTest[0], colorTest[1], colorTest[2], colorTest[3], colorTest[4], colorTest[5]))


class horizontalAntiClockwise_oneTurn_lineZero_expected:
    def __init__(self):
        self.cubeFaceList = None
        self.horizontalAntiClockwise_oneTurn_lineZero = RotationPocketCubeTests()
        self.horizontalAntiClockwise_oneTurn_lineZero.cube.horizontal_rotation_anticlockwise(0)
        self.init = init_Tests_PocketCube()

        self.left_expected = [Block(1, 0, 1), Block(0, 0, 1),
                              Block(0, 1, 1), Block(0, 1, 0)]

        self.front_expected = [Block(0, 0, 1), Block(0, 0, 0),
                               Block(0, 1, 0), Block(1, 1, 0)]

        self.right_expected = [Block(0, 0, 0), Block(1, 0, 0),
                               Block(1, 1, 0), Block(1, 1, 1)]

        self.back_expected = [Block(1, 0, 0), Block(1, 0, 1),
                              Block(1, 1, 1), Block(0, 1, 1)]

        self.up_expected = [Block(1, 0, 1), Block(1, 0, 0),
                            Block(0, 0, 1), Block(0, 0, 0)]

        self.down_expected = [Block(0, 1, 0), Block(1, 1, 0),
                              Block(0, 1, 1), Block(1, 1, 1)]

    def check_horizontalAntiClockwise_oneTurn_lineZero(self):
        front = self.init.check_face(self.front_expected, self.horizontalAntiClockwise_oneTurn_lineZero.front)
        right = self.init.check_face(self.right_expected, self.horizontalAntiClockwise_oneTurn_lineZero.right)
        down = self.init.check_face(self.down_expected, self.horizontalAntiClockwise_oneTurn_lineZero.down)
        left = self.init.check_face(self.left_expected, self.horizontalAntiClockwise_oneTurn_lineZero.left)
        up = self.init.check_face(self.up_expected, self.horizontalAntiClockwise_oneTurn_lineZero.up)
        back = self.init.check_face(self.back_expected, self.horizontalAntiClockwise_oneTurn_lineZero.back)

        self.cubeFaceList = [front, right, down, left, up, back]
        colorTest = self.init.true_or_falseColorTest(self.cubeFaceList)
        print("[horizontalAntiClockwise_oneTurn_lineZero => front:{} right:{} down:{} left:{} up:{} back:{}]".format(
            colorTest[0], colorTest[1], colorTest[2], colorTest[3], colorTest[4], colorTest[5]))


class horizontalAntiClockwise_oneTurn_lineOne_expected:
    def __init__(self):
        self.cubeFaceList = None
        self.horizontalAntiClockwise_oneTurn_lineOne = RotationPocketCubeTests()
        self.horizontalAntiClockwise_oneTurn_lineOne.cube.horizontal_rotation_anticlockwise(1)
        self.init = init_Tests_PocketCube()

        self.left_expected = [Block(0, 0, 1), Block(0, 0, 0),
                              Block(1, 1, 1), Block(0, 1, 1)]

        self.front_expected = [Block(0, 0, 0), Block(1, 0, 0),
                               Block(0, 1, 1), Block(0, 1, 0)]

        self.right_expected = [Block(1, 0, 0), Block(1, 0, 1),
                               Block(0, 1, 0), Block(1, 1, 0)]

        self.back_expected = [Block(1, 0, 1), Block(0, 0, 1),
                              Block(1, 1, 0), Block(1, 1, 1)]

        self.up_expected = [Block(0, 0, 1), Block(1, 0, 1),
                            Block(0, 0, 0), Block(1, 0, 0)]

        self.down_expected = [Block(0, 1, 1), Block(0, 1, 0),
                              Block(1, 1, 1), Block(1, 1, 0)]

    def check_horizontalAntiClockwise_oneTurn_lineOne(self):
        front = self.init.check_face(self.front_expected, self.horizontalAntiClockwise_oneTurn_lineOne.front)
        right = self.init.check_face(self.right_expected, self.horizontalAntiClockwise_oneTurn_lineOne.right)
        down = self.init.check_face(self.down_expected, self.horizontalAntiClockwise_oneTurn_lineOne.down)
        left = self.init.check_face(self.left_expected, self.horizontalAntiClockwise_oneTurn_lineOne.left)
        up = self.init.check_face(self.up_expected, self.horizontalAntiClockwise_oneTurn_lineOne.up)
        back = self.init.check_face(self.back_expected, self.horizontalAntiClockwise_oneTurn_lineOne.back)

        self.cubeFaceList = [front, right, down, left, up, back]
        colorTest = self.init.true_or_falseColorTest(self.cubeFaceList)
        print("[horizontalAntiClockwise_oneTurn_lineOne => front:{} right:{} down:{} left:{} up:{} back:{}]".format(
            colorTest[0], colorTest[1], colorTest[2], colorTest[3], colorTest[4], colorTest[5]))


class verticalClockwise_oneTurn_columnZero_expected:
    def __init__(self):
        self.cubeFaceList = None
        self.verticalClockwise_oneTurn_columnZero = RotationPocketCubeTests()
        self.verticalClockwise_oneTurn_columnZero.cube.vertical_rotation_clockwise(0)
        self.init = init_Tests_PocketCube()

        self.up_expected = [Block(0, 1, 1), Block(1, 0, 1),
                            Block(0, 0, 1), Block(1, 0, 0)]

        self.front_expected = [Block(0, 0, 1), Block(1, 0, 0),
                               Block(0, 0, 0), Block(1, 1, 0)]

        self.down_expected = [Block(0, 0, 0), Block(1, 1, 0),
                              Block(0, 1, 0), Block(1, 1, 1)]

        self.back_expected = [Block(1, 0, 1), Block(0, 1, 1),
                              Block(1, 1, 1), Block(0, 1, 0)]

        self.left_expected = [Block(0, 1, 1), Block(0, 0, 1),
                              Block(0, 1, 0), Block(0, 0, 0)]

        self.right_expected = [Block(1, 0, 0), Block(1, 0, 1),
                               Block(1, 1, 0), Block(1, 1, 1)]

    def check_verticalClockwise_oneTurn_columnZero(self):
        front = self.init.check_face(self.front_expected, self.verticalClockwise_oneTurn_columnZero.front)
        right = self.init.check_face(self.right_expected, self.verticalClockwise_oneTurn_columnZero.right)
        down = self.init.check_face(self.down_expected, self.verticalClockwise_oneTurn_columnZero.down)
        left = self.init.check_face(self.left_expected, self.verticalClockwise_oneTurn_columnZero.left)
        up = self.init.check_face(self.up_expected, self.verticalClockwise_oneTurn_columnZero.up)
        back = self.init.check_face(self.back_expected, self.verticalClockwise_oneTurn_columnZero.back)

        self.cubeFaceList = [front, right, down, left, up, back]
        colorTest = self.init.true_or_falseColorTest(self.cubeFaceList)
        print("[verticalClockwise_oneTurn_columnZero => front:{} right:{} down:{} left:{} up:{} back:{}]".format(
            colorTest[0], colorTest[1], colorTest[2], colorTest[3], colorTest[4], colorTest[5]))


class verticalClockwise_oneTurn_columnOne_expected:
    def __init__(self):
        self.cubeFaceList = None
        self.verticalClockwise_oneTurn_columnOne = RotationPocketCubeTests()
        self.verticalClockwise_oneTurn_columnOne.cube.vertical_rotation_clockwise(1)
        self.init = init_Tests_PocketCube()

        self.up_expected = [Block(0, 0, 1), Block(1, 1, 1),
                            Block(0, 0, 0), Block(1, 0, 1)]

        self.front_expected = [Block(0, 0, 0), Block(1, 0, 1),
                               Block(0, 1, 0), Block(1, 0, 0)]

        self.down_expected = [Block(0, 1, 0), Block(1, 0, 0),
                              Block(0, 1, 1), Block(1, 1, 0)]

        self.back_expected = [Block(1, 1, 1), Block(0, 0, 1),
                              Block(1, 1, 0), Block(0, 1, 1)]

        self.left_expected = [Block(0, 0, 1), Block(0, 0, 0),
                              Block(0, 1, 1), Block(0, 1, 0)]

        self.right_expected = [Block(1, 0, 1), Block(1, 1, 1),
                               Block(1, 0, 0), Block(1, 1, 0)]

    def check_verticalClockwise_oneTurn_columnOne(self):
        front = self.init.check_face(self.front_expected, self.verticalClockwise_oneTurn_columnOne.front)
        right = self.init.check_face(self.right_expected, self.verticalClockwise_oneTurn_columnOne.right)
        down = self.init.check_face(self.down_expected, self.verticalClockwise_oneTurn_columnOne.down)
        left = self.init.check_face(self.left_expected, self.verticalClockwise_oneTurn_columnOne.left)
        up = self.init.check_face(self.up_expected, self.verticalClockwise_oneTurn_columnOne.up)
        back = self.init.check_face(self.back_expected, self.verticalClockwise_oneTurn_columnOne.back)

        self.cubeFaceList = [front, right, down, left, up, back]
        colorTest = self.init.true_or_falseColorTest(self.cubeFaceList)
        print("[verticalClockwise_oneTurn_columnOne => front:{} right:{} down:{} left:{} up:{} back:{}]".format(
            colorTest[0], colorTest[1], colorTest[2], colorTest[3], colorTest[4], colorTest[5]))


class verticalAntiClockwise_oneTurn_columnZero_expected:
    def __init__(self):
        self.cubeFaceList = None
        self.verticalAntiClockwise_oneTurn_columnZero = RotationPocketCubeTests()
        self.verticalAntiClockwise_oneTurn_columnZero.cube.vertical_rotation_anticlockwise(0)
        self.init = init_Tests_PocketCube()

        self.up_expected = [Block(0, 0, 0), Block(1, 0, 1),
                            Block(0, 1, 0), Block(1, 0, 0)]

        self.front_expected = [Block(0, 1, 0), Block(1, 0, 0),
                               Block(0, 1, 1), Block(1, 1, 0)]

        self.down_expected = [Block(0, 1, 1), Block(1, 1, 0),
                              Block(0, 0, 1), Block(1, 1, 1)]

        self.back_expected = [Block(1, 0, 1), Block(0, 0, 0),
                              Block(1, 1, 1), Block(0, 0, 1)]

        self.left_expected = [Block(0, 0, 0), Block(0, 1, 0),
                              Block(0, 0, 1), Block(0, 1, 1)]

        self.right_expected = [Block(1, 0, 0), Block(1, 0, 1),
                               Block(1, 1, 0), Block(1, 1, 1)]

    def check_verticalAntiClockwise_oneTurn_columnZero(self):
        front = self.init.check_face(self.front_expected, self.verticalAntiClockwise_oneTurn_columnZero.front)
        right = self.init.check_face(self.right_expected, self.verticalAntiClockwise_oneTurn_columnZero.right)
        down = self.init.check_face(self.down_expected, self.verticalAntiClockwise_oneTurn_columnZero.down)
        left = self.init.check_face(self.left_expected, self.verticalAntiClockwise_oneTurn_columnZero.left)
        up = self.init.check_face(self.up_expected, self.verticalAntiClockwise_oneTurn_columnZero.up)
        back = self.init.check_face(self.back_expected, self.verticalAntiClockwise_oneTurn_columnZero.back)

        self.cubeFaceList = [front, right, down, left, up, back]
        colorTest = self.init.true_or_falseColorTest(self.cubeFaceList)
        print("[verticalAntiClockwise_oneTurn_columnZero => front:{} right:{} down:{} left:{} up:{} back:{}]".format(
            colorTest[0], colorTest[1], colorTest[2], colorTest[3], colorTest[4], colorTest[5]))


class verticalAntiClockwise_oneTurn_columnOne_expected:
    def __init__(self):
        self.cubeFaceList = None
        self.verticalAntiClockwise_oneTurn_columnOne = RotationPocketCubeTests()
        self.verticalAntiClockwise_oneTurn_columnOne.cube.vertical_rotation_anticlockwise(1)
        self.init = init_Tests_PocketCube()

        self.up_expected = [Block(0, 0, 1), Block(1, 0, 0),
                            Block(0, 0, 0), Block(1, 1, 0)]

        self.front_expected = [Block(0, 0, 0), Block(1, 1, 0),
                               Block(0, 1, 0), Block(1, 1, 1)]

        self.down_expected = [Block(0, 1, 0), Block(1, 1, 1),
                              Block(0, 1, 1), Block(1, 0, 1)]

        self.back_expected = [Block(1, 0, 0), Block(0, 0, 1),
                              Block(1, 0, 1), Block(0, 1, 1)]

        self.left_expected = [Block(0, 0, 1), Block(0, 0, 0),
                              Block(0, 1, 1), Block(0, 1, 0)]

        self.right_expected = [Block(1, 1, 0), Block(1, 0, 0),
                               Block(1, 1, 1), Block(1, 0, 1)]

    def check_verticalAntiClockwise_oneTurn_columnOne(self):
        front = self.init.check_face(self.front_expected, self.verticalAntiClockwise_oneTurn_columnOne.front)
        right = self.init.check_face(self.right_expected, self.verticalAntiClockwise_oneTurn_columnOne.right)
        down = self.init.check_face(self.down_expected, self.verticalAntiClockwise_oneTurn_columnOne.down)
        left = self.init.check_face(self.left_expected, self.verticalAntiClockwise_oneTurn_columnOne.left)
        up = self.init.check_face(self.up_expected, self.verticalAntiClockwise_oneTurn_columnOne.up)
        back = self.init.check_face(self.back_expected, self.verticalAntiClockwise_oneTurn_columnOne.back)

        self.cubeFaceList = [front, right, down, left, up, back]
        colorTest = self.init.true_or_falseColorTest(self.cubeFaceList)
        print("[verticalAntiClockwise_oneTurn_columnOne => front:{} right:{} down:{} left:{} up:{} back:{}]".format(
            colorTest[0], colorTest[1], colorTest[2], colorTest[3], colorTest[4], colorTest[5]))


class init_Tests_PocketCube:
    def check_face(self, expected, face):
        return expected == face.blocks

    def true_or_falseColorTest(self, listFace):
        colorTest = []
        for i in listFace:
            if i:
                i = "\033[92m {}\033[00m".format(i)
            else:
                i = "\033[91m {}\033[00m".format(i)
            colorTest.append(i)

        return colorTest

    def display_tests(self):
        print("PocketCubeTest :")
        print("     -> Init RubiksCube :")
        init_cube_expected().check_init_cube_creation()
        print("     -> Horizontal Rotation :")
        horizontalClockwise_oneTurn_lineZero_expected().check_horizontalClockwise_oneTurn_lineZero()
        horizontalClockwise_oneTurn_lineOne_expected().check_horizontalClockwise_oneTurn_lineOne()
        horizontalAntiClockwise_oneTurn_lineZero_expected().check_horizontalAntiClockwise_oneTurn_lineZero()
        horizontalAntiClockwise_oneTurn_lineOne_expected().check_horizontalAntiClockwise_oneTurn_lineOne()
        print("     -> Vertical Rotation :")
        verticalClockwise_oneTurn_columnZero_expected().check_verticalClockwise_oneTurn_columnZero()
        verticalClockwise_oneTurn_columnOne_expected().check_verticalClockwise_oneTurn_columnOne()
        verticalAntiClockwise_oneTurn_columnZero_expected().check_verticalAntiClockwise_oneTurn_columnZero()
        verticalAntiClockwise_oneTurn_columnOne_expected().check_verticalAntiClockwise_oneTurn_columnOne()

        print('\n""""""""\n')
