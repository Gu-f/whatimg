from .base import ImgInfo
from src.whatimg.const.img_ext import ImgExt
from src.whatimg.const.img_type import ImgType


class PNG(ImgInfo):
    """
    PNG 类型图片
    包含可用扩展名，如: [.png]
    """

    def __init__(self, raw: bytes):
        self.png = None
        super().__init__(raw)

    def _analyse(self):
        self._parser_header()
        return super()._analyse()

    def _parser_header(self):
        if self.raw.startswith(b'\211PNG\r\n\032\n'):
            self.type = ImgType.PNG
            self.extensions = [ImgExt.PNG]
            self.analyse_succeed = True


