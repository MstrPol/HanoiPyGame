import pygame
import globals
from tower import Tower
from towerItem import TowerItem


def items_generator(first_tower, num_items=5):
    x = first_tower.rect.midbottom[0]
    y = first_tower.rect.midbottom[1]
    width = 25 * num_items
    height = 30
    offset = 5

    for i in range(1, num_items + 1):
        first_tower.add_item(TowerItem(width, height, (x, y)))
        width -= 25
        y -= height + offset


def get_next_tower(active_tower_index, towers):
    if active_tower_index is None:
        towers[0].set_active(True)
        return 0

    if active_tower_index != len(towers) - 1:
        towers[active_tower_index + 1].set_active(True)
        towers[active_tower_index].set_active(False)
        return active_tower_index + 1
    else:
        return active_tower_index


def get_prev_tower(active_tower_index, towers):
    if active_tower_index is None:
        towers[0].set_active(True)
        return 0

    if active_tower_index != 0:
        towers[active_tower_index - 1].set_active(True)
        towers[active_tower_index].set_active(False)
        return active_tower_index - 1
    else:
        return active_tower_index


def get_active_item(active_tower_index, towers):
    if len(towers[active_tower_index].items) > 0:
        max_index = len(towers[active_tower_index].items) - 1
        active_status = towers[active_tower_index].items[max_index].active
        towers[active_tower_index].items[max_index].set_tower_index(active_tower_index)
        towers[active_tower_index].items[max_index].set_active(not active_status)
        return towers[active_tower_index].items[max_index]
    else:
        return None


def move_active_item(active_item, active_tower_index, towers):
    active_item.set_active(False)
    items_on_dest_tower = len(towers[active_tower_index].items)
    move_flag = False  # флаг для условия перемещения

    # можно перемещать, если на целевой башне нет ничего
    if items_on_dest_tower == 0:
        move_flag = True

    # можно перемещать, если последний элемент целевой башни больше текущего
    if items_on_dest_tower > 0:
        last_item_on_dest_tower = towers[active_tower_index].items[items_on_dest_tower - 1]
        if last_item_on_dest_tower.rect.width > active_item.rect.width:
            move_flag = True

    if move_flag:
        towers[active_item.tower_index].remove_item(active_item)
        active_item.set_tower_index(active_tower_index)
        x = towers[active_tower_index].rect.midbottom[0]
        y = towers[active_tower_index].rect.midbottom[1]
        active_item.set_coordinates((x, y - (items_on_dest_tower * 35)))
        towers[active_tower_index].add_item(active_item)

    return None


def check_won(items_count, towers):
    if len(towers[2].items) == items_count:
        print('WON!!!')


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
    pygame.display.set_caption("Hanoi!")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    towers = [
        Tower(weight=10, height=200, pos=(156, globals.HEIGHT / 2)),
        Tower(weight=10, height=200, pos=(312, globals.HEIGHT / 2)),
        Tower(weight=10, height=200, pos=(468, globals.HEIGHT / 2)),
    ]
    for tower in towers:
        all_sprites.add(tower)

    items_count = 4
    items_generator(towers[0], items_count)
    for item in towers[0].items:
        all_sprites.add(item)

    active_tower_index = None
    active_item = None

    running = True
    while running:
        clock.tick(globals.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("RIGHT")
                    active_tower_index = get_next_tower(active_tower_index, towers)
                if event.key == pygame.K_LEFT:
                    print("LEFT")
                    active_tower_index = get_prev_tower(active_tower_index, towers)
                if event.key == pygame.K_UP:
                    print("UP")
                if event.key == pygame.K_SPACE:
                    print("SPACE")
                    if active_tower_index is not None:
                        if active_item is None:
                            active_item = get_active_item(active_tower_index, towers)
                        else:
                            active_item = move_active_item(active_item, active_tower_index, towers)
                            check_won(items_count, towers)

        all_sprites.update()
        screen.fill(globals.BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
