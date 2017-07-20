import sys
sys.path.append("..")
from pandaeditor import *

class Panel(Entity):

    def __init__(self):
        super().__init__()
        self.name = 'panel'
        self.parent = scene.ui.entity.node_path
        self.model = loader.loadModel('models/quad.egg')
        scene.entities.append(self)
        print('created panel')

    def __setattr__(self, name, value):
        if name == 'position':
            value = tuple(x / 2 for x in value)
            print('newpos', value)
        super().__setattr__(name, value)