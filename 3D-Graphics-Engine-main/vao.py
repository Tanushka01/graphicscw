from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, context):
        self.context = context
        self.vbo = VBO(context)
        self.program = ShaderProgram(context)
        self.vaos = {}


        
        self.vaos['water'] = self.get_vao(
            program=self.program.programs['water'],
            vbo = self.vbo.vbos['water'])
        
        self.vaos['shadow_water'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['water'])
        
        self.vaos['basen'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['basen'])
        
        self.vaos['shadow_basen'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['basen'])
        
        self.vaos['shadow_water'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['water'])
        
        # ground vao
        self.vaos['ground'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['ground'])

        # shadow ground vao
        self.vaos['shadow_ground'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['ground'])

        # cat vao
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat'])
        
        self.vaos['tree'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['tree'])

        # shadow cat vao
        self.vaos['shadow_cat'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['cat'])
        
        self.vaos['shadow_tree'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['tree'])

        # skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        # advanced_skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

    def get_vao(self, program, vbo):
        vao = self.context.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()