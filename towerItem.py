import pygame
import globals


class TowerItem(pygame.sprite.Sprite):
    def __init__(self, weight, height, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((weight, height))
        self.image.fill(globals.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.active = False
        self.tower_index = None

    def set_tower_index(self, tower_index):
        self.tower_index = tower_index

    def move(self, move_coordinates):
        x = self.rect.center[0] + move_coordinates[0]
        y = self.rect.center[1] + move_coordinates[1]
        self.rect.center = (x, y)

    def set_coordinates(self, move_coordinates):
        self.rect.center = move_coordinates

    def set_active(self, status=False):
        if status:
            self.image.fill(globals.WHITE)
        else:
            self.image.fill(globals.BLUE)
        self.active = status
