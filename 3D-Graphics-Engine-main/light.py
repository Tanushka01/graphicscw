import glm
import numpy as np

class Light:
    def __init__(self, position=(50,50,-10), color=(1, 1, 0.5)):
        
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(1, 1, 1)
        
        
        # intensities
        self.Ia = 0.3 * self.color  # ambient
        self.Id = 0.8 * self.color  # diffuse
        self.Is = 1 * self.color  # specular
        
        # view matrix
        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))
    
    