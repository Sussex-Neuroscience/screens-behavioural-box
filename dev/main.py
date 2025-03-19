import ctypes
from datetime import datetime
from psychopy import visual, core, event

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

platformsNum = 5

print(f"Detected Screen Width: {screen_width}, Screen Height: {screen_height}")

win_width = screen_width
divided_win_width = win_width // platformsNum
win_height = screen_height / 4

def create_windows():
    screens = []
    for i in range(4):
        pos = (i * divided_win_width, 0)
        win = visual.Window(
            size=(divided_win_width, win_height),
            color=(0, 0, 0),
            units="pix",
            fullscr=False,
            pos=pos,
            allowGUI=False,
            winType='pyglet'
        )
        screens.append(win)

    # manager_window = visual.Window(
    #     size=(divided_win_width, win_height),
    #     color=(0.5, 0.5, 0.5),
    #     units="pix",
    #     fullscr=False,
    #     pos=(4 * divided_win_width, 0),
    #     winType='pyglet'
    # )
    # screens.append(manager_window)

    return screens

def create_stimulus(win):
    stimulus = visual.Circle(win, radius=10, fillColor="white", lineColor="black")
    stimulus.pos = (-190,0)
    return stimulus
    

def control_stimulus(stimulus, windows, direction='right'):
    platforms = [windows[0], windows[1], windows[2], windows[3]]
    
    if direction == 'right':
        current_platform_index = 0
    elif direction == 'left':
        current_platform_index = len(platforms) - 1
    else:
        raise ValueError("Invalid direction. Use 'right' or 'left'.")

    speed = 5

    transition_positions_right = [
        (193),  
        (193),  
        (193),  
        (193)   
    ]

    transition_positions_left = [
        (-193),   
        (-193),   
        (-193),   
        (-193)    
    ]

    print(f"Estimated Transition positions (Right): {transition_positions_right}")
    print(f"Estimated Transition positions (Left): {transition_positions_left}")

    while True:
        if direction == 'right':
            stimulus.pos += (speed, 0)
            transition_position = transition_positions_right[current_platform_index]
        elif direction == 'left':
            stimulus.pos -= (speed, 0) 
            transition_position = transition_positions_left[current_platform_index]
        
        # check if reached target
        if (direction == 'right' and stimulus.pos[0] >= transition_position) or \
           (direction == 'left' and stimulus.pos[0] <= transition_position):
            print(f"Transitioning from platform {current_platform_index+1} at x: {stimulus.pos[0]}")

            current_platform_index += 1 if direction == 'right' else -1
            platformSwitchTime = datetime.now()

            if current_platform_index >= len(platforms): 
                direction = 'left' 
                
                current_platform_index = len(platforms) - 1

            elif current_platform_index < 0:
                direction = 'right'
                current_platform_index = 0 

            stimulus = create_stimulus(platforms[current_platform_index])
            if direction == "right":
                stimulus.pos = (-divided_win_width // 2 + 10, 0)
            if direction == "left":                                 #reset pos for next platform
                stimulus.pos = (divided_win_width // 2 + 10, 0)  
        for idx, win in enumerate(platforms):
            if idx == current_platform_index:
                stimulus.draw()

        for win in windows:
            win.flip()

        if 'escape' in event.getKeys():
            break

        core.wait(0.005)

def main():
    windows = create_windows()
    stimulus = create_stimulus(windows[0])
    control_stimulus(stimulus, windows, direction='right') #start moving from right

    for win in windows:
        win.close()
    core.quit()

if __name__ == "__main__":
    main()