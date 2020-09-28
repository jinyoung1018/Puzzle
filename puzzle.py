from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene = Scene( 'puzzle', 'Images/배경.png')
board = Scene('board','Images/white.png')

img1=Object('Images/1.png')
img1.show( )

img2=Object('Images/2.png')
img2.show( )

img3=Object('Images/3.png')
img3.show( )

img4=Object('Images/4.png')
img4.show( )


img5=Object('Images/5.png')
img5.show( )

img6=Object('Images/6.png')
img6.show( )

img7=Object('Images/7.png')
img7.show( )

img8=Object('Images/8.png')
img8.show( )

img9=Object('Images/balnk.png')
img9.show( )

timer = Timer(5,)
showTimer(timer)


Imags = [img2,img7,img4,img3,img8,img5,img6,img1,img9]
boardinfo = [0,1,2,3,4,5,6,7,8]
startButton = Object('Images/start.png')
startButton.setScale(1.6)
startButton.locate(scene, 560, 240)
startButton.show( )



def startButton_onMouseAction(x,y,action):

    startButton.hide( ) 
    initBoard()
    showMessage('5초 안에 퍼즐을 완성하세요!!!!')
    timer.start( )


def initBoard():
    i=0
    h=460
    w=0
    for n in range(9):
        
        w=340+i
        Imags[n].locate(scene,w,h)
        Imags[n].show( )
        if (n+1)%3==0 :
            i=0
            h=h-200
        else:
            i=i+200


def get_random_move(self, last_move, tile):
        moves = [UP, DOWN, LEFT, RIGHT]
        if last_move:
            moves.remove(last_move)
        for i in range(len(moves) - 1, -1, -1):
            if not self.is_tile(tile, moves[i]):
                moves.remove(moves[i])

        return random.choice(moves)
def tile1_onMouseAction(x,y,action):
    img1.locate(scene,740,60)
    img9.locate(scene,540,60)

def tile2_onMouseAction(x,y,action):
    img5.locate(scene,740,60)
    img9.locate(scene,740,260)    
    
startButton.onMouseAction = startButton_onMouseAction
img1.onMouseAction=tile1_onMouseAction
img5.onMouseAction=tile2_onMouseAction

def timer_onTimeout( ):
    showMessage('헉 실패!!!')

    
timer.onTimeout = timer_onTimeout


startGame(scene)
