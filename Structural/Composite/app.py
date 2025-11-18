
"""
Composite pattern is used when you have tree like structure and want to treat a single object and composition of objects uniformly.
Here you have component interface which contains common methods for both the leaf and composite ones
leaf and composite classes implement the component interface
"""

from folder import Folder
from file import File

if __name__ == "__main__":
    
    root = Folder("root")
    root.add(File("readme.md"))
    root.add(File("todo.txt"))

    src = Folder("src")
    src.add(File("main.py"))
    src.add(File("utils.py"))

    assets = Folder("assets")
    assets.add(File("logo.png"))
    assets.add(File("background.jpg"))

    root.add(src)
    root.add(assets)

    root.display(0)