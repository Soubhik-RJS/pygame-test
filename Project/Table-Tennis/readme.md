# pygame-framework (beta)
#### *🚀  This is AquaPHP custom MVC framework.*



## 🧠 Authors

- [@Soubhik1000](https://github.com/Soubhik1000/pygame-framework)

## 📀 Used technology 
<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="bootstrap logo"  />
</div>

## 🛠️ Installation Steps

*Please download this file and save it on your computer.*

__NOTE__: *Python is required in order to run this program.*

### Now run your project:

__Run Commands:__

__1. Install pygame (if not installed)__
```bash
pip install pygame
```

__2. Run main.py__
```bash
python main.py
```

## 📝 Documentation

### Initialization

__The game is initialized in main.py.__

__The game scene is initialized in Scenes folder__

__The game object is initialized in GameObject folder__

### Game Scene
*Basic example of game scene*

```python
import pygame
import sys
from Scenes.Scene import Scene

class Test(Scene):
    def __init__(self, screen, clock, fps):
        super().__init__(screen, clock, fps)

    def start(self):
        return super().start()
    
    def event(self, e):
        return super().event(e)
    
    def update(self):
        return super().update()
    
    def draw(self):
        return super().draw()
```

### Game Object
*Basic example of game object*

```python
import pygame
import sys

class Player(pygame.Rect):

    def __init__(self, screen, WIDTH, HEIGTH, color):
        super().__init__(WIDTH/2, HEIGTH/2, self.size, self.size)
        self.screen = screen
        self.color = color
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
    
    def start(self):
        pass

    def update(self):
        pass

    def darw(self):
        pygame.draw.rect(self.screen, self.color, self)

```