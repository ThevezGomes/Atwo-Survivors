import enemies
enemy_speed = {
    "skeleton" : 4
}

enemy_fov = 400

def get_enemy_sprites(enemy):

    if not isinstance(enemy, enemies.Enemy): raise TypeError("Não é inimigo")

    enemy_sprites = {
        "skeleton" : {
            "walk_down_animations" : [ enemy.game.enemy_skeleton_spritesheet_walk_down.get_sprite(  8, 12, 25, 29),
                                       enemy.game.enemy_skeleton_spritesheet_walk_down.get_sprite( 55, 11, 25, 29),
                                       enemy.game.enemy_skeleton_spritesheet_walk_down.get_sprite(104, 10, 25, 29),
                                       enemy.game.enemy_skeleton_spritesheet_walk_down.get_sprite(152, 11, 25, 29),
                                       enemy.game.enemy_skeleton_spritesheet_walk_down.get_sprite(198, 11, 25, 29),
                                       enemy.game.enemy_skeleton_spritesheet_walk_down.get_sprite(246, 11, 25, 29)],
            
            "walk_up_animations" : [ enemy.game.enemy_skeleton_spritesheet_walk_up.get_sprite( 15, 11, 25, 30),
                                     enemy.game.enemy_skeleton_spritesheet_walk_up.get_sprite( 63, 11, 24, 30),
                                     enemy.game.enemy_skeleton_spritesheet_walk_up.get_sprite(111, 10, 23, 30),
                                     enemy.game.enemy_skeleton_spritesheet_walk_up.get_sprite(159, 11, 25, 30),
                                     enemy.game.enemy_skeleton_spritesheet_walk_up.get_sprite(208, 11, 24, 30),
                                     enemy.game.enemy_skeleton_spritesheet_walk_up.get_sprite(256, 11, 24, 30)],
            
            "walk_right_animations" : [ enemy.game.enemy_skeleton_spritesheet_walk_right.get_sprite( 15, 11, 22, 31),
                                        enemy.game.enemy_skeleton_spritesheet_walk_right.get_sprite( 62, 11, 22, 31),
                                        enemy.game.enemy_skeleton_spritesheet_walk_right.get_sprite(109, 10, 22, 31),
                                        enemy.game.enemy_skeleton_spritesheet_walk_right.get_sprite(159, 11, 22, 31),
                                        enemy.game.enemy_skeleton_spritesheet_walk_right.get_sprite(207, 11, 22, 31),
                                        enemy.game.enemy_skeleton_spritesheet_walk_right.get_sprite(256, 10, 22, 31)],
            
            "walk_left_animations" : [ enemy.game.enemy_skeleton_spritesheet_walk_left.get_sprite(  8, 11, 29, 30),
                                       enemy.game.enemy_skeleton_spritesheet_walk_left.get_sprite( 54, 11, 29, 30),
                                       enemy.game.enemy_skeleton_spritesheet_walk_left.get_sprite(102, 10, 29, 30),
                                       enemy.game.enemy_skeleton_spritesheet_walk_left.get_sprite(152, 11, 29, 30),
                                       enemy.game.enemy_skeleton_spritesheet_walk_left.get_sprite(202, 11, 29, 30),
                                       enemy.game.enemy_skeleton_spritesheet_walk_left.get_sprite(250, 10, 29, 30)]
        }
    }

    return enemy_sprites[enemy.kind].values()

