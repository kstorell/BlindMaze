from pygame.locals import *
import pygame
import time
import random

class Player:
        scaling = .5
        x = 0
        y = 0
        #N = 0, E = 1, S = 2, W = 3
        direction = 0
        speed = 99
        current = (0,0)

        def __init__(self, x, y):
                self.current = (x,y)
                self.x = x*99 + 30
                self.y = y*99 + 30
                self.x *= self.scaling
                self.y *= self.scaling
                self.speed *= self.scaling

        def moveRight(self):
                self.x = self.x + self.speed
                self.current = (self.current[0] + 1, self.current[1])

        def moveLeft(self):
                self.x = self.x - self.speed
                self.current = (self.current[0] - 1, self.current[1])

        def moveUp(self):
                self.y = self.y - self.speed
                self.current = (self.current[0], self.current[1]-1)

        def moveDown(self):
                self.y = self.y + self.speed
                self.current = (self.current[0], self.current[1] + 1)


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

        def on_init(self):
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

        def turnRight(self):
                self.player.direction += 1
                if self.player.direction == 4:
                        self.player.direction = 0
                self._player_image = pygame.transform.rotate(self._player_image, -90)

        def turnLeft(self):
                self.player.direction -= 1
                if self.player.direction == -1:
                        self.player.direction = 3
                self._player_image = pygame.transform.rotate(self._player_image, 90)

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
                                if self.player.direction == 0:
                                        self.player.moveUp()
                                elif self.player.direction == 1:
                                        self.player.moveRight()
                                elif self.player.direction == 2:
                                        self.player.moveDown()
                                elif self.player.direction == 3:
                                        self.player.moveLeft()
                                wait = 1

                        if (keys[K_DOWN]):
                                #TODO Victory, not victory!


                                print self.player.current
                                print self.finish

                                if self.player.current == self.finish:
                                        self._running = False
                                wait = 1
                        if (keys[K_ESCAPE]):
                                self._running = False

                        self.on_loop()
                        self.on_render()
                        if (wait == 1):
                                time.sleep(.3)
                        #while(wait == 1):
                        #        for event in pygame.event.get():
                        #                if event.type == pygame.KEYUP:
                        #                        wait = 0
                self.on_cleanup()

if __name__ == "__main__" :
        theApp = GUI(0,0, random.randint(0,9), random.randint(0,9))
        theApp.on_execute()
