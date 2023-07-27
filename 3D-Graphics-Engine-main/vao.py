from vbo import VBO

class VAO:
    def __init__(self, context):
        self.context = context
        self.vbo = VBO(context)
        self.program = Shaders(context)
        self.vaos = {}
        
        
        def model_vao(model_name, shader_pro='main_shader'):    
            if shader_pro == 'skybox':
                # advanced_skybox vao
                self.vaos['skybox'] = self.get_vao(program=self.program.programs['skybox'],
                                                            vbo=self.vbo.vbos['skybox'])
                
                
            else:
                self.vaos[model_name] = self.get_vao(program=self.program.programs[shader_pro],
                                                     vbo = self.vbo.vbos[model_name])
            
                self.vaos['shadow_' + model_name] = self.get_vao(program=self.program.programs['shadow_map'],
                                                                 vbo = self.vbo.vbos[model_name])

        model_vao('basen')
        model_vao('ground')
        model_vao('tree')
        model_vao('water', 'water')

        model_vao('skybox', 'skybox')
        model_vao('monkey')
        model_vao('fish')
        model_vao('rock')
        
    def get_vao(self, program, vbo):
        vao = self.context.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
        
        
             
class Shaders:
    def __init__(self, context):
        self.context = context
        self.programs = {}
        self.programs['main_shader'] = self.get_program('main_shader')
        self.programs['skybox'] = self.get_program('skybox')
        self.programs['shadow_map'] = self.get_program('shadow_map')
        self.programs['water'] = self.get_program('water')

    def get_program(self, shader_program_name):
        with open(f'shaders/{shader_program_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_program_name}.frag') as file:
            fragment_shader = file.read()

        program = self.context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]