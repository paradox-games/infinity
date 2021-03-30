#  INFINITY ENGINE:
# Game scene module with
# GameScene class

# you can find moderngl_window's
# documentation here:
# https://moderngl-window.readthedocs.io/en/latest/
import moderngl_window as mglw

# you can also find moderngl's
# documentation here:
# https://moderngl.readthedocs.io/en/latest/
import moderngl as mgl


class GameScene(mglw.WindowConfig):
	gl_version = (3, 3)
	window_size = (1920, 1080)  # it can be modified

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.prog = self.ctx.program(...)
		self.vao = self.ctx.vertex_array(...)
		self.texture = self.ctx.texture(self.wnd.size, 4)

	def render(self, time, frametime):
		self.vao.render()
