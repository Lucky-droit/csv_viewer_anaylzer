import SimpleGUICS2Pygame.simpleguics2pygame as simplegui 
msg = "" ; 
size = 10
def keydown_handler(key) : 
    global msg 
    msg = chr(key) ; 
def draw(canvas) : 
    global size 
    # canvas.draw_text(msg , (250 ,250) , size , 'blue') 
    canvas.draw_image(img , (img.get_width()/2 , img.get_height()/2) , (img.get_width() , img.get_height())  , (250,250),(100,100))
    # canvas.draw_polygon([(10,10) ,(20,20) ,(30,30) , (50 ,50)]  , 4, 'red')
def incre() : 
    global size 
    size += 10 
def input_handler(text):
    global msg 
    msg  = text 

frame = simplegui.create_frame("Game" , 500 , 500) 
img = simplegui.load_image('Screenshot 2023-09-25 235731.jpg')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.add_button("Increse" , incre)

frame.add_input("Enter the Text : " , input_handler , 100) 
frame.start() 