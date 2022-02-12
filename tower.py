import pygame
import globals


class Tower(pygame.sprite.Sprite):
    def __init__(self, weight, height, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((weight, height))
        self.image.fill(globals.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.items = []
        self.active_status = False

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def set_active(self, status=False):
        if status:
            self.image.fill(globals.WHITE)
        else:
            self.image.fill(globals.GREEN)
        self.active_status = status
