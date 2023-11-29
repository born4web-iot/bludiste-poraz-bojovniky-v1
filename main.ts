namespace SpriteKind {
    export const FinalPrize = SpriteKind.create()
}
function createXBounceEnemy (X: number, Y: number, XSpeed: number) {
    XEnemy = sprites.create(img`
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
        `, SpriteKind.Enemy)
    XEnemy.setPosition(X, Y)
    XEnemy.setBounceOnWall(true)
    XEnemy.setVelocity(XSpeed, 0)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    game.gameOver(false)
})
function showXYPosition (movingSprite: Sprite) {
    scene.cameraFollowSprite(movingSprite)
    console.log("X: " + ("" + movingSprite) + " Y: " + ("" + movingSprite))
}
function createTreasure () {
    finalReward = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . b d b . . . . . . 
        . . . . . . . b d b c . . . . . 
        . . . . b b c 5 5 5 c b b . . . 
        . . . . b 5 5 5 1 5 5 5 b . . . 
        . . . c c 5 5 5 1 5 5 5 c c . . 
        . . b b 5 5 5 1 1 1 5 5 5 b b . 
        . . d d 5 1 1 1 1 1 1 1 5 d d . 
        . . b b 5 5 5 1 1 1 5 5 5 b b . 
        . . . c c 5 5 5 1 5 5 5 c c . . 
        . . . . b 5 5 5 1 5 5 5 b . . . 
        . . . . b b c 5 5 5 c b b . . . 
        . . . . . . c b d b c . . . . . 
        . . . . . . . b d b . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.FinalPrize)
    finalReward.setPosition(335, 277)
    scene.setBackgroundImage(img`
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
        `)
}
function createYBounceEnemy (X2: number, Y2: number, YSpeed: number) {
    XEnemy = sprites.create(img`
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
        `, SpriteKind.Enemy)
    XEnemy.setPosition(X2, Y2)
    XEnemy.setBounceOnWall(true)
    XEnemy.setVelocity(0, YSpeed)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.FinalPrize, function (sprite, otherSprite) {
    game.gameOver(true)
})
let finalReward: Sprite = null
let XEnemy: Sprite = null
tiles.setCurrentTilemap(tilemap`level1`)
let Jedi = sprites.create(img`
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
    `, SpriteKind.Player)
Jedi.setPosition(30, 35)
controller.moveSprite(Jedi, 100, 100)
scene.cameraFollowSprite(Jedi)
let movingSprite2 = Jedi
createXBounceEnemy(50, 80, 50)
createXBounceEnemy(50, 80, 60)
createXBounceEnemy(414, 370, 60)
createXBounceEnemy(380, 229, 70)
createYBounceEnemy(289, 352, 70)
createTreasure()
game.onUpdateInterval(1000, function () {
	
})
