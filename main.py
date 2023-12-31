@namespace
class SpriteKind:
    FinalPrize = SpriteKind.create()
def createXBounceEnemy(X: number, Y: number, XSpeed: number):
    global XEnemy
    XEnemy = sprites.create(img("""
            ..............cfff..............
                    ............ccddbf..............
                    ...........cbddbff.........ccc..
                    ..........fccbbcf.........cbbc..
                    ...fffffffccccccff.......cdbc...
                    .ffcbbbbbbbbbbbbbcfff....cdbf...
                    fcbbbbbbbbbcbbbbbbcccff.cdbf....
                    fbcbbbbffbbbcbcbbbcccccffdcf....
                    fbb1111ffbbbcbcbbbccccccbbcf....
                    .fb11111111bbcbbbccccccccbbcf...
                    ..fccc33cb11bbbbcccccccfffbbf...
                    ...fc131c111bbbcccccbdbc..fbbf..
                    ....f33c111cbbccdddddbc....fff..
                    .....ff1111fdbbccddbcc..........
                    .......cccccfdbbbfcc............
                    .............fffff..............
        """),
        SpriteKind.enemy)
    XEnemy.set_position(X, Y)
    XEnemy.set_bounce_on_wall(True)
    XEnemy.set_velocity(XSpeed, 0)

def on_on_overlap(sprite2, otherSprite2):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def showXYPosition(movingSprite: Sprite):
    scene.camera_follow_sprite(movingSprite)
    print("X: " + ("" + str(movingSprite)) + " Y: " + ("" + str(movingSprite)))
def createTreasure():
    global finalReward
    finalReward = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . d . . . . . . . 
                    . . . . . c . b d b . c . . . . 
                    . . . b . . c b d b c . . b . . 
                    . . . . b b c 5 5 5 c b b . . . 
                    . . c . b 5 5 5 1 5 5 5 b . c . 
                    . . . c c 5 5 5 1 5 5 5 c c . . 
                    . . b b 5 5 5 1 1 1 5 5 5 b b . 
                    . d d d 5 1 1 1 5 1 1 1 5 d d d 
                    . . b b 5 5 5 1 1 1 5 5 5 b b . 
                    . . . c c 5 5 5 1 5 5 5 c c . . 
                    . . c . b 5 5 5 1 5 5 5 b . c . 
                    . . . . b b c 5 5 5 c b b . . . 
                    . . . b . . c b d b c . . b . . 
                    . . . . . c . b d b . c . . . . 
                    . . . . . . . . d . . . . . . .
        """),
        SpriteKind.FinalPrize)
    finalReward.set_position(335, 277)
    scene.set_background_image(img("""
        ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
    """))
def createYBounceEnemy(X2: number, Y2: number, YSpeed: number):
    global XEnemy
    XEnemy = sprites.create(img("""
            ..............cfff..............
                    ............ccddbf..............
                    ...........cbddbff.........ccc..
                    ..........fccbbcf.........cbbc..
                    ...fffffffccccccff.......cdbc...
                    .ffcbbbbbbbbbbbbbcfff....cdbf...
                    fcbbbbbbbbbcbbbbbbcccff.cdbf....
                    fbcbbbbffbbbcbcbbbcccccffdcf....
                    fbb1111ffbbbcbcbbbccccccbbcf....
                    .fb11111111bbcbbbccccccccbbcf...
                    ..fccc33cb11bbbbcccccccfffbbf...
                    ...fc131c111bbbcccccbdbc..fbbf..
                    ....f33c111cbbccdddddbc....fff..
                    .....ff1111fdbbccddbcc..........
                    .......cccccfdbbbfcc............
                    .............fffff..............
        """),
        SpriteKind.enemy)
    XEnemy.set_position(X2, Y2)
    XEnemy.set_bounce_on_wall(True)
    XEnemy.set_velocity(0, YSpeed)

def on_on_overlap2(sprite, otherSprite):
    game.game_over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.FinalPrize, on_on_overlap2)

finalReward: Sprite = None
XEnemy: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
"""))
Jedi = sprites.create(img("""
        ........................
            ....ffffff..............
            ..ffeeeef2f.............
            .ffeeeef222f............
            .feeeffeeeef...77.......
            .ffffee2222ef.777.......
            .fe222ffffe2f7777.......
            fffffffeeeff7777........
            ffe44ebf44e7777.........
            fee4d41fdde777..........
            .feee4ddded777..........
            ..ffee44e4dde.7.........
            ...f222244ee...7........
            ...f2222e2f.............
            ...f444455f.............
            ....ffffff..............
            .....fff................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
Jedi.set_position(30, 35)
controller.move_sprite(Jedi, 100, 100)
scene.camera_follow_sprite(Jedi)
movingSprite2 = Jedi
createXBounceEnemy(50, 80, 50)
createXBounceEnemy(50, 80, 60)
createXBounceEnemy(414, 370, 60)
createXBounceEnemy(380, 229, 70)
createYBounceEnemy(289, 352, 70)
createTreasure()

def on_update_interval():
    pass
game.on_update_interval(1000, on_update_interval)
