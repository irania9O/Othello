import os


class Piece:

    def __init__(self, color, texture=None, texture_rect=None) -> None:
        self.color = color
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self):
        self.texture = os.path.join(
            f"assets/images/{self.color}.png"
        )
