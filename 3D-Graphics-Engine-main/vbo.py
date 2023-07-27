import numpy as np
import moderngl as mgl
import pywavefront


class VBO:
    def __init__(self, context):
        self.vbos = {}
        self.vbos['tree'] = TreeVBO(context)
        self.vbos['ground'] = GroundVBO(context)
        self.vbos['water'] = WaterVBO(context)  
        self.vbos['skybox'] = SkyBoxVBO(context)
        self.vbos['basen'] = BasenVBO(context)
        self.vbos['monkey'] = MonkeyVBO(context)
        self.vbos['fish'] = FishVBO(context)
        self.vbos['rock'] = RockVBO(context)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVBO:
    def __init__(self, context):
        self.context = context
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None

    def get_vertex_data(self):
        pass

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.context.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()

class RockVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

        
    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/rocks/rocks.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class FishVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

        
    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/fish/13007_Blue-Green_Reef_Chromis_v2_l3.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    

class MonkeyVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

        
    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/Monkey/12958_Spider_Monkey_v1_l2.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class WaterVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/water/water.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data   
    
    
class BasenVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/water/water.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

    
class TreeVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

        
    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/10446_Palm_Tree_v1_L3.123c0a37e64c-4659-4136-a23d-059cbcde3ecd/10446_Palm_Tree_v1_max2010_iteration-2.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
   
    
class GroundVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

        
    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/ground/ground.obj', cache=True, parse=True)
        ground_obj = objs.materials.popitem()[1]
        vertex_data = ground_obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class SkyBoxVBO(BaseVBO):
    def __init__(self, context):
        super().__init__(context)
        self.format = '3f'
        self.attribs = ['in_position']

    def get_vertex_data(self):
        # in clip space
        z = 0.9999
        vertices = [(-1, -1, z), (3, -1, z), (-1, 3, z)]
        vertex_data = np.array(vertices, dtype='f4')
        return vertex_data

