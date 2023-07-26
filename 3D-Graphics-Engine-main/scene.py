from model import *
import moderngl as mgl
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)
        
    

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        """
        n, s = 2, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))
                
                
        add(Ground(app, pos=(0, -2, 0), scale=(0.25, 0.03, 0.28)))
        
        add(Ground(app, pos=(0, -2, -50), scale=(0.25, 0.03, 0.28)))
        """
        
        """
        

        add(Tree(app, pos=(0, 0, 0), scale=(0.05, 0.05, 0.03)))
        add(Tree(app, pos=(10, 0, -20)))
        add(Tree(app, pos=(20, 0, 0)))
        add(Tree(app, pos=(50, 0, -30)))
        
        
        add(Ground(app, pos=(0, -2, 0), scale=(0.25, 0.03, 0.28)))
        
        add(Ground(app, pos=(0, -2, -50), scale=(0.25, 0.03, 0.28)))
        
        add(Ground(app, pos=(0, -2, 0), scale=(0.25, 0.03, 0.28)))
        
        add(Ground(app, pos=(0, -2, -48), scale=(0.25, 0.03, 0.28)))
        
        """
        
        add(Ground(app, pos=(0, -2, 0), scale=(0.25, 0.03, 0.28)))
        
        add(Ground(app, pos=(0, -2, -48), scale=(0.25, 0.03, 0.28)))
        
        
                
        add(Tree(app, pos=(10, -1, -20)))
        add(Tree(app, pos=(20, -2, -10)))
        add(Tree(app, pos=(15, -1, 20)))
        
        add(Tree(app, pos=(20, -1, 12)))
        add(Tree(app, pos=(10, -1, -30)))
        add(Tree(app, pos=(-20, -2, -40)))
        add(Tree(app, pos=(15, -1, -40)))
        add(Tree(app, pos=(-25, -1, -12)))
        
        add(Basen(app, pos=(1,-2.5,-4), scale=(3.5, 1, 0.8)))
                
        # add(Cat(app, pos=(0, -1, -10)))
        
        self.app.context.enable(mgl.BLEND)
        self.water = Water(app, pos=(1,-1,-4), scale=(3.5, 1, 0.6))
        add(self.water)
        
    
        
        





        # columns
        """
        for i in range(9):
            add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
            add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))
        """

        # moving cube
        #self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        #add(self.moving_cube)

    def update(self):
        #self.moving_cube.rot.xyz = self.app.time
        # self.water2.rot.y = self.app.time
        
        pass
