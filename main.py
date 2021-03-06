import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.graphics import *
from pyglet.gl import *

window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world',
                        font_name='Times New Roman',
                        font_size=36, 
                        x=window.width//2, y=window.height//2, 
                        anchor_x='center', anchor_y='center')

pyglet.graphics.draw(1, pyglet.gl.GL_QUADS,
    ('v4i', (1, 1, 10, 10)),
    ('c3B', (255, 255, 255))
)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print("The key A was pressed")
    elif symbol == key.LEFT:
        print("The left arrow key was pressed")
    elif symbol == key.ENTER:
        print("The enter key was pressed")

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("The left most button was pressed")

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
