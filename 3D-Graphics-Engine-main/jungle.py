from model import *
import moderngl as mgl
import glm
import random

class JungleScene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.place_objects()
        
        # skybox
        self.skybox = SkyBox(app)

    def add_object_list(self, object):
        self.objects.append(object)
        
    def place_trees(self, no_trees):
        place = self.add_object_list
        planted = []
        
        pos_tree = 0
        
        for tree in range(no_trees):
            
            if pos_tree == 0:
                z = random.randint(2, 36)
                pos_tree = 1
            else:
                z = round(random.uniform(-47, -8),2)
                pos_tree = 0
                
            coord = [round(random.randint(-26, 25),2), round(random.randint(-2,-1),2), z]            
            
            if coord not in planted:
                scale_xy = random.uniform(0.02, 0.033)
                scale_z = random.uniform(0.018, 0.035)
                scale_factor = [scale_xy, scale_xy, scale_z]
                
                rot_factor = [-90, random.randint(0,360), random.randint(-10, 10)]
                
                
                place(Tree(self.app, pos=coord, scale=scale_factor, rot=rot_factor))
                planted.append(coord)
    
    def place_objects(self):
        place = self.add_object_list
        
        # trees
        self.place_trees(no_trees=35)
        
        place(Monkey(self.app, pos=(10, -1, -7)))
        place(Fish(self.app, pos=(-10, -2.5, -3)))
        
        
        # floor
        place(Ground(self.app, pos=(0, -2, 0), scale=(0.25, 0.03, 0.28)))
        place(Ground(self.app, pos=(0, -2, -48), scale=(0.25, 0.03, 0.28)))
                
        # river
        place(Basen(self.app, pos=(1,-2.5,-4), scale=(3.8, 1, 0.8)))
                        
        self.app.context.enable(mgl.BLEND)
        self.water = Water(self.app, pos=(1,-1,-4), scale=(3.5, 1, 0.6))
        place(self.water)


    def update(self):
        #self.fish.rot.y = self.app.time
        pass

