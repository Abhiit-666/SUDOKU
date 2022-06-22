import pygame
grid=[  
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0]
]
bcg=(247,240,245)
def main():
    pygame.init()
    win=pygame.display.set_mode((550,550))
    pygame.display.set_caption("SUDOKU")
    win.fill(bcg)
    for i in range(0,10):
        if(i%3==0):
            width=4
        else:
            width=2
        
        pygame.draw.line(win,(0,0,0),(50+50*i,50),(50+50*i,500),width)
        pygame.draw.line(win,(0,0,0),(50,50+50*i),(500,50+50*i),width)  
        pygame.display.update() 




    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                return

main() 
