from pygame.locals import *
import pygame
import time
import random
import os

class Maze:
        maze = dict()
        # maze[i][j] stores the directions you can go in from location (i,j)
        # maze[i][j] = [N,E,S,W]

        for i in range(10):
                maze[i] = dict()
                for j in range(10):
                        maze[i][j] = [1, 1, 1, 1]

        maze[0][0] = [0, 1, 1, 0]
        maze[0][1] = [0, 1, 0, 1]
        maze[0][2] = [0, 0, 1, 1]
        maze[0][3] = [0, 1, 1, 0]
        maze[0][4] = [0, 1, 0, 1]
        maze[0][5] = [0, 1, 0, 1]
        maze[0][6] = [0, 1, 1, 1]
        maze[0][7] = [0, 0, 1, 1]
        maze[0][8] = [0, 1, 1, 0]
        maze[0][9] = [0, 0, 1, 1]

        maze[1][0] = [1, 0, 1, 0]
        maze[1][1] = [0, 1, 1, 0]
        maze[1][2] = [1, 1, 0, 1]
        maze[1][3] = [1, 0, 1, 1]
        maze[1][4] = [0, 1, 1, 0]
        maze[1][5] = [0, 0, 0, 1]
        maze[1][6] = [1, 0, 1, 0]
        maze[1][7] = [1, 0, 1, 0]
        maze[1][8] = [1, 0, 1, 0]
        maze[1][9] = [1, 0, 1, 0]

        maze[2][0] = [1, 0, 0, 0]
        maze[2][1] = [1, 0, 1, 0]
        maze[2][2] = [0, 1, 1, 0]
        maze[2][3] = [1, 0, 0, 1]
        maze[2][4] = [1, 1, 0, 0]
        maze[2][5] = [0, 1, 0, 1]
        maze[2][6] = [1, 0, 0, 1]
        maze[2][7] = [1, 1, 0, 0]
        maze[2][8] = [1, 0, 0, 1]
        maze[2][9] = [1, 0, 1, 0]

        maze[3][0] = [0, 1, 1, 0]
        maze[3][1] = [1, 0, 0, 1]
        maze[3][2] = [1, 0, 1, 0]
        maze[3][3] = [0, 1, 0, 0]
        maze[3][4] = [0, 1, 0, 1]
        maze[3][5] = [0, 1, 0, 1]
        maze[3][6] = [0, 1, 1, 1]
        maze[3][7] = [0, 1, 1, 1]
        maze[3][8] = [0, 1, 0, 1]
        maze[3][9] = [1, 0, 0, 1]

        maze[4][0] = [1, 1, 0, 0]
        maze[4][1] = [0, 0, 1, 1]
        maze[4][2] = [1, 1, 0, 0]
        maze[4][3] = [0, 0, 1, 1]
        maze[4][4] = [0, 0, 0, 0]  # tree
        maze[4][5] = [0, 0, 0, 0]  # tree
        maze[4][6] = [1, 0, 1, 0]
        maze[4][7] = [1, 1, 0, 0]
        maze[4][8] = [0, 1, 0, 1]
        maze[4][9] = [0, 0, 1, 1]

        maze[5][0] = [0, 1, 1, 0]
        maze[5][1] = [1, 0, 0, 1]
        maze[5][2] = [0, 1, 0, 0]
        maze[5][3] = [1, 0, 1, 1]
        maze[5][4] = [0, 0, 0, 0]  # tree
        maze[5][5] = [0, 0, 0, 0]  # tree
        maze[5][6] = [1, 1, 0, 0]
        maze[5][7] = [0, 1, 1, 1]
        maze[5][8] = [0, 0, 0, 1]
        maze[5][9] = [1, 0, 1, 0]

        maze[6][0] = [1, 0, 0, 0]
        maze[6][1] = [0, 1, 1, 0]
        maze[6][2] = [0, 0, 1, 1]
        maze[6][3] = [1, 1, 0, 0]
        maze[6][4] = [0, 1, 1, 1]
        maze[6][5] = [0, 0, 1, 1]
        maze[6][6] = [0, 1, 1, 0]
        maze[6][7] = [1, 0, 0, 1]
        maze[6][8] = [0, 1, 1, 0]
        maze[6][9] = [1, 0, 1, 1]

        maze[7][0] = [0, 1, 1, 0]
        maze[7][1] = [1, 0, 0, 1]
        maze[7][2] = [1, 1, 0, 0]
        maze[7][3] = [0, 0, 1, 1]
        maze[7][4] = [1, 0, 1, 0]
        maze[7][5] = [1, 0, 1, 0]
        maze[7][6] = [1, 1, 0, 0]
        maze[7][7] = [0, 0, 1, 1]
        maze[7][8] = [1, 0, 1, 0]
        maze[7][9] = [1, 0, 0, 0]

        maze[8][0] = [1, 0, 1, 0]
        maze[8][1] = [0, 1, 1, 0]
        maze[8][2] = [0, 0, 1, 1]
        maze[8][3] = [1, 1, 0, 0]
        maze[8][4] = [1, 0, 0, 1]
        maze[8][5] = [1, 1, 0, 0]
        maze[8][6] = [0, 0, 1, 1]
        maze[8][7] = [1, 0, 1, 0]
        maze[8][8] = [1, 1, 0, 0]
        maze[8][9] = [0, 0, 1, 1]

        maze[9][0] = [1, 1, 0, 0]
        maze[9][1] = [1, 0, 0, 1]
        maze[9][2] = [1, 1, 0, 0]
        maze[9][3] = [0, 1, 0, 1]
        maze[9][4] = [0, 1, 0, 1]
        maze[9][5] = [0, 0, 0, 1]
        maze[9][6] = [1, 1, 0, 0]
        maze[9][7] = [1, 0, 0, 1]
        maze[9][8] = [0, 1, 0, 0]
        maze[9][9] = [1, 0, 0, 1]

class Player:
        scaling = .5
        x = 0
        y = 0
        #N = 0, E = 1, S = 2, W = 3
        direction = 0
        speed = 99
        current = (0,0)
        maze = Maze.maze

        def __init__(self, x, y):
                self.current = (x,y)
                self.x = x*99 + 30
                self.y = y*99 + 30
                self.x *= self.scaling
                self.y *= self.scaling
                self.speed *= self.scaling

        def tryMove(self):
                if self.maze[self.current[1]][self.current[0]][self.direction] == 0:
                        return 0
                else:
                        return 1
        def moveRight(self):
                if self.tryMove():
                        self.x = self.x + self.speed
                        self.current = (self.current[0] + 1, self.current[1])
                        return 1
                return 0

        def moveLeft(self):
                if self.tryMove():
                        self.x = self.x - self.speed
                        self.current = (self.current[0] - 1, self.current[1])
                        return 1
                return 0

        def moveUp(self):
                if self.tryMove():
                        self.y = self.y - self.speed
                        self.current = (self.current[0], self.current[1]-1)
                        return 1
                return 0
        def moveDown(self):
                if self.tryMove():
                        self.y = self.y + self.speed
                        self.current = (self.current[0], self.current[1] + 1)
                        return 1
                return 0


class GUI:
        windowWidth = 1000
        windowHeight = 1000
        player = 0
        finishX = 0
        finishY = 0

        def __init__(self, startX, startY, finishX, finishY):
                self.running = True
                self._display_surf = None
                self._player_image = None
                self._bg = None
                self.player = Player(startX, startY)
                self.finish = (finishX, finishY)
                self.finishX = (finishX*99 + 20) * self.player.scaling
                self.finishY = (finishY*99 + 20) * self.player.scaling
                self._finish_image = None
                self.beachb = None
                self.beachf = None
                self.beachl = None
                self.beachr = None

                self.trainb = None
                self.trainl = None
                self.trainf = None
                self.trainr = None

                self.farmr = None
                self.farmb = None
                self.farmf = None
                self.farml = None

                self.carsf = None
                self.carsb = None
                self.carsl = None
                self.carsr = None

                self.treef = None
                self.treeb = None
                self.treel = None
                self.treer = None
                self.treefr = None
                self.treefl = None
                self.treebr = None
                self.treebl = None

        def on_init(self):
                pygame.mixer.pre_init(44100, -16, 2, 2048)
                pygame.init()
                self._display_surf = pygame.display.set_mode((int(self.windowWidth*self.player.scaling),int(self.windowHeight*self.player.scaling)), pygame.HWSURFACE)

                pygame.display.set_caption('Who turned out the lights!?')
                self._running = True

                self._finish_image = pygame.image.load("finish.png").convert()
                w, h = self._finish_image.get_size()
                self._finish_image = pygame.transform.scale(self._finish_image,(int(w * self.player.scaling), int(h * self.player.scaling)))

                self._bg = pygame.image.load("maze.png").convert()
                w, h = self._bg.get_size()
                self._bg = pygame.transform.scale(self._bg,(int(w * self.player.scaling), int(h * self.player.scaling)))

                self._player_image = pygame.image.load("current.png").convert()
                w, h = self._player_image.get_size()
                self._player_image = pygame.transform.scale(self._player_image,(int(w * self.player.scaling), int(h * self.player.scaling)))


                pygame.mixer.set_num_channels(60)

                forward = 'a0.ogg'
                back = 'a180.ogg'
                left = 'a-90.ogg'
                right = 'a90.ogg'

                self.successSound = pygame.mixer.Sound(os.path.join('Sounds', 'success.wav'))
                self.failSound = pygame.mixer.Sound(os.path.join('Sounds', 'fail.wav'))

                self.beachl = pygame.mixer.Sound(os.path.join('Sounds', 'beach3D', left))
                self.beachr = pygame.mixer.Sound(os.path.join('Sounds', 'beach3D', right))
                self.beachf = pygame.mixer.Sound(os.path.join('Sounds', 'beach3D', forward))
                self.beachb = pygame.mixer.Sound(os.path.join('Sounds', 'beach3D', back))

                self.trainb = pygame.mixer.Sound(os.path.join('Sounds', 'train3D', back))
                self.trainl = pygame.mixer.Sound(os.path.join('Sounds', 'train3D', left))
                self.trainf = pygame.mixer.Sound(os.path.join('Sounds', 'train3D', forward))
                self.trainr = pygame.mixer.Sound(os.path.join('Sounds', 'train3D', right))

                self.farmr = pygame.mixer.Sound(os.path.join('Sounds', 'farm3D', right))
                self.farmb = pygame.mixer.Sound(os.path.join('Sounds', 'farm3D', back))
                self.farmf = pygame.mixer.Sound(os.path.join('Sounds', 'farm3D', forward))
                self.farml = pygame.mixer.Sound(os.path.join('Sounds', 'farm3D', left))

                self.carsf = pygame.mixer.Sound(os.path.join('Sounds', 'cars3D', forward))
                self.carsb = pygame.mixer.Sound(os.path.join('Sounds', 'cars3D', back))
                self.carsl = pygame.mixer.Sound(os.path.join('Sounds', 'cars3D', left))
                self.carsr = pygame.mixer.Sound(os.path.join('Sounds', 'cars3D', right))

                self.treef = pygame.mixer.Sound(os.path.join('Sounds', 'tree3D', forward))
                self.treeb = pygame.mixer.Sound(os.path.join('Sounds', 'tree3D', back))
                self.treel = pygame.mixer.Sound(os.path.join('Sounds', 'tree3D', left))
                self.treer = pygame.mixer.Sound(os.path.join('Sounds', 'tree3D', right))
                self.treefr = pygame.mixer.Sound(os.path.join('Sounds', 'tree3D', 'a45.ogg'))
                self.treefl = pygame.mixer.Sound(os.path.join('Sounds', 'tree3D', 'a-45.ogg'))
                self.treebr = pygame.mixer.Sound(os.path.join('Sounds', 'tree3D', 'a135.ogg'))
                self.treebl = pygame.mixer.Sound(os.path.join('Sounds', 'tree3D', 'a-135.ogg'))

                self.updateSound()

        def on_event(self, event):
                if event.type == QUIT:
                        self.running = False

        def on_loop(self):
                pass
        def on_render(self):
                self._display_surf.fill((0,0,0))
                self._display_surf.blit(self._bg,(0,0))
                self._display_surf.blit(self._finish_image, (self.finishX, self.finishY))
                self._display_surf.blit(self._player_image, (self.player.x, self.player.y))
                pygame.display.flip()

        def on_cleanup(self):
                pygame.quit()

        def updateSound(self):
                beach = None
                farm = None
                cars = None
                train = None
                tree = None
                x,y = self.player.current
                direction = self.player.direction
                if direction == 0:
                        beach = self.beachl
                        train = self.trainb
                        farm = self.farmr
                        cars = self.carsf
                elif direction == 1:
                        beach = self.beachb
                        train = self.trainr
                        farm = self.farmf
                        cars = self.carsl
                elif direction == 2:
                        beach = self.beachr
                        train = self.trainf
                        farm = self.farml
                        cars = self.carsb
                elif direction == 3:
                        beach = self.beachf
                        train = self.trainl
                        farm = self.farmb
                        cars = self.carsr
#left and right sections
                if y == 4 or y == 5:
                        if x < 5:
                                if direction == 0:
                                        tree = self.treer
                                elif direction == 1:
                                        tree = self.treef
                                elif direction == 2:
                                        tree = self.treel
                                elif direction == 3:
                                        tree = self.treeb
                        else:
                                if direction == 0:
                                        tree = self.treel
                                elif direction == 1:
                                        tree = self.treeb
                                elif direction == 2:
                                        tree = self.treer
                                elif direction == 3:
                                        tree = self.treef

                        if x == 3 or x == 6:
                                tree.set_volume(1)
                        elif x == 2 or x == 7:
                                tree.set_volume(.3)
                        elif x == 1 or x == 8:
                                tree.set_volume(.1)
                        else:
                                tree.set_volume(0)
#top and bottom sections
                if x == 4 or x == 5:
                        if y < 5:
                                if direction == 0:
                                        tree = self.treeb
                                elif direction == 1:
                                        tree = self.treer
                                elif direction == 2:
                                        tree = self.treef
                                elif direction == 3:
                                        tree = self.treel
                        else:
                                if direction == 0:
                                        tree = self.treef
                                elif direction == 1:
                                        tree = self.treel
                                elif direction == 2:
                                        tree = self.treeb
                                elif direction == 3:
                                        tree = self.treer

                        if y == 3 or y == 6:
                                tree.set_volume(1)
                        elif y == 2 or y == 7:
                                tree.set_volume(.3)
                        elif y == 1 or y == 8:
                                tree.set_volume(.1)
                        else:
                                tree.set_volume(0)
#diagonal top left
                if (x ==2 and (y==2 or y==3)) or (x == 3 and (y == 2 or y == 3)):
                        if direction == 0:
                                tree = self.treebr
                        elif direction == 1:
                                tree = self.treefr
                        elif direction == 2:
                                tree = self.treefl
                        elif direction == 3:
                                tree = self.treebl

                        if x == 3 and y == 3:
                                tree.set_volume(.8)
                        elif x == 2 and y == 2:
                                tree.set_volume(.05)
                        else:
                                tree.set_volume(.1)

#diagonal bottom left
                if (x == 2 and (y == 6 or y == 7)) or (x == 3 and (y == 6 or y == 7)):
                        if direction == 0:
                                tree = self.treefr
                        elif direction == 1:
                                tree = self.treefl
                        elif direction == 2:
                                tree = self.treebl
                        elif direction == 3:
                                tree = self.treebr

                        if x == 3 and y == 6:
                                tree.set_volume(.8)
                        elif x == 2 and y == 7:
                                tree.set_volume(.05)
                        else:
                                tree.set_volume(.1)



# diagonal bottom right
                if (x == 6 and (y == 6 or y == 7)) or (x == 7 and (y == 6 or y == 7)):
                        if direction == 0:
                                tree = self.treefl
                        elif direction == 1:
                                tree = self.treebl
                        elif direction == 2:
                                tree = self.treebr
                        elif direction == 3:
                                tree = self.treefr

                        if x == 6 and y == 6:
                                tree.set_volume(.8)
                        elif x == 7 and y == 7:
                                tree.set_volume(.05)
                        else:
                                tree.set_volume(.1)


# diagonal top right
                if (x == 6 and (y == 2 or y == 3)) or (x == 7 and (y == 2 or y == 3)):
                        if direction == 0:
                                tree = self.treebl
                        elif direction == 1:
                                tree = self.treebr
                        elif direction == 2:
                                tree = self.treefr
                        elif direction == 3:
                                tree = self.treefl

                        if x == 6 and y == 3:
                                tree.set_volume(.8)
                        elif x == 7 and y == 2:
                                tree.set_volume(.05)
                        else:
                                tree.set_volume(.1)

                if x == 0:
                        beach.set_volume(1)
                elif x == 1:
                        beach.set_volume(.3)
                elif x == 2:
                        beach.set_volume(.1)
                else:
                        beach = None

                if y == 0:
                        cars.set_volume(1)
                elif y == 1:
                        cars.set_volume(.3)
                elif y == 2:
                        cars.set_volume(.1)
                else:
                        cars = None

                if x == 9:
                        farm.set_volume(1)
                elif x == 8:
                        farm.set_volume(.3)
                elif x == 7:
                        farm.set_volume(.1)
                else:
                        farm = None

                if y == 9:
                        train.set_volume(1)
                elif y == 8:
                        train.set_volume(.3)
                elif y == 7:
                        train.set_volume(.1)
                else:
                        train = None

                if beach != None:
                        beach.play(-1)
                if train != None:
                        train.play(-1)
                if farm != None:
                        farm.play(-1)
                if cars != None:
                        cars.play(-1)
                if tree != None:
                        tree.play(-1)

        def moveSuccess(self):
                pygame.mixer.stop()
                channel = self.successSound.play()
                #while channel.get_busy():
                #        pass
                self.updateSound()

        def moveFail(self):
                pygame.mixer.stop()
                channel = self.failSound.play()
                #while channel.get_busy():
                #        pass
                self.updateSound()



        def turnRight(self):
                self.player.direction += 1
                if self.player.direction == 4:
                        self.player.direction = 0
                self._player_image = pygame.transform.rotate(self._player_image, -90)
                pygame.mixer.stop()
                self.updateSound()

        def turnLeft(self):
                self.player.direction -= 1
                if self.player.direction == -1:
                        self.player.direction = 3
                self._player_image = pygame.transform.rotate(self._player_image, 90)
                pygame.mixer.stop()
                self.updateSound()

        def on_execute(self):
                if self.on_init() == False:
                        self._running = False

                while(self._running):
                        pygame.event.pump()
                        keys = pygame.key.get_pressed()
                        wait = 0

                        if(keys[K_RIGHT]):
                                self.turnRight()
                                wait = 1

                        if (keys[K_LEFT]):
                                self.turnLeft()
                                wait = 1

                        if (keys[K_UP]):
                                rtrn = 0
                                if self.player.direction == 0:
                                        rtrn = self.player.moveUp()
                                elif self.player.direction == 1:
                                        rtrn = self.player.moveRight()
                                elif self.player.direction == 2:
                                        rtrn = self.player.moveDown()
                                elif self.player.direction == 3:
                                        rtrn = self.player.moveLeft()
                                wait = 1
                                if rtrn:
                                        self.moveSuccess()
                                else:
                                        self.moveFail()

                        if (keys[K_DOWN]):
                                #TODO Victory, not victory!


                                #print self.player.current
                                #print self.finish

                                if self.player.current == self.finish:
                                        #TODO victory
                                        print "YOU WIN!"
                                        self._running = False
                                wait = 1
                        if (keys[K_ESCAPE]):
                                self._running = False

                        self.on_loop()
                        self.on_render()
                        #if (wait == 1):
                        #        time.sleep(.2)
                        while(wait == 1):
                                for event in pygame.event.get():
                                        if event.type == pygame.KEYUP:
                                                wait = 0
                self.on_cleanup()

if __name__ == "__main__" :
        repeat = 1
        while repeat:
                startX = random.randint(0,9)
                startY = random.randint(0,9)
                if (startX,startY) == (4,4) or (startX,startY) == (5,4) or (startX,startY) == (4,5) or (startX,startY) == (5,5):
                        repeat = 1
                else: repeat = 0
        repeat = 1
        while repeat:
                dist = 5
                xdist = random.randint(0,5)
                ydist = 5-xdist
                finishX = startX+xdist
                if finishX>9:
                        finishX = startX-xdist
                finishY = startY+ydist
                if finishY>9:
                        finishY = startY-ydist
                if (finishX,finishY) == (4,4) or (finishX,finishY) == (5,4) or (finishX,finishY) == (4,5) or (finishX,finishY) == (5,5):
                        repeat = 1
                else: repeat = 0

        theApp = GUI(startX,startY,finishX,finishY)
        theApp.on_execute()
