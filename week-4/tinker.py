import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 600

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    draw_filled_rect(canvas, 0, 0, 800, 500, "lightblue")
    draw_sun(canvas, 500, 25, 600, 125, "yellow")
    draw_filled_rect(canvas, 0, 350, 800, 600, "lightgreen")
    draw_cloud_group(canvas)
    draw_pine_forest(canvas)
    draw_interstate(canvas)
    draw_flowerbed(canvas)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_flowerbed(canvas):
    for x in range(35):
        if x%3==0:
            draw_flower(canvas, x*25, 592)
        elif x%3==1:
            draw_flower(canvas, x*25, 591)
        elif x%3==2:
            draw_flower(canvas, x*25, 589)

def draw_flower(canvas, x, y):
    canvas.create_line(x, y, x+2, y-10, fill="darkgreen")
    canvas.create_oval(x-4,y-8,x+6,y-16, fill="pink")

def draw_interstate(canvas):
    canvas.create_rectangle(0, 400, 800, 574, fill="gray")
    for x in range(15):
        canvas.create_rectangle(55*x-35,480,55*x,490, fill="yellow")

def draw_filled_rect(canvas, x1, y1, x2, y2, color):
    canvas.create_rectangle(x1,y1,x2,y2,fill=color)

def draw_pine_tree(canvas, bottom_x, bottom_y):
    canvas.create_rectangle(bottom_x,bottom_y, bottom_x+25, bottom_y-35, fill="brown")
    canvas.create_polygon(bottom_x+15, bottom_y-35, bottom_x-25, bottom_y-35, bottom_x, bottom_y-55, bottom_x-25, bottom_y-55, bottom_x, bottom_y-75, bottom_x-25, bottom_y-75, bottom_x+15, bottom_y-110)
    canvas.create_polygon(bottom_x+15, bottom_y-35, bottom_x+50, bottom_y-35, bottom_x+35, bottom_y-55, bottom_x+50, bottom_y-55, bottom_x+35, bottom_y-75, bottom_x+50, bottom_y-75, bottom_x+15, bottom_y-110)

def draw_cloud_group(canvas):
    for x in range(0, 4):
        draw_cloud(canvas, 200*x+75, 100)

def draw_sun(canvas, left_x, left_y, right_x, right_y, color):
    canvas.create_oval(left_x, left_y, right_x, right_y, fill=color)

def draw_pine_forest(canvas):
    for x in range(0, 9):
        draw_pine_tree(canvas, 100*x, 360)

def draw_cloud(canvas, center_x, center_y):
    canvas.create_oval(center_x-25, center_y-25, center_x+25, center_y+25, fill="white", outline="white")
    canvas.create_oval(center_x+10, center_y-15, center_x+50, center_y+30, fill="white", outline="white")
    canvas.create_oval(center_x+10, center_y-40, center_x+50, center_y, fill="white", outline="white")
    canvas.create_oval(center_x+30, center_y-20, center_x+80, center_y+20, fill="white", outline="white")

# this program will start executing.
main()