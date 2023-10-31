from .base import ImgInfo
from src.whatimg.const.img_ext import ImgExt
from src.whatimg.const.img_type import ImgType


class GIF(ImgInfo):
    """
    GIF 类型图片
    包含可用扩展名，如: [.gif]
    """

    def __init__(self, raw: bytes):
        self.gif = None
        super().__init__(raw)

    def _analyse(self):
        self._parser_header()
        return super()._analyse()

    def _parser_header(self):
        if self.raw[:6] in (b'GIF87a', b'GIF89a'):
            self.type = ImgType.GIF
            self.extensions = [ImgExt.GIF]
            self.analyse_succeed = True


