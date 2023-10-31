from .base import ImgInfo
from src.whatimg.const.img_ext import ImgExt
from src.whatimg.const.img_type import ImgType


class JPEG(ImgInfo):
    """
    JPEG 类型图片
    包含可用扩展名，如: [.jpg, .jpeg, .jpe, .jfif]
    """

    def __init__(self, raw: bytes):
        self.jpeg = None
        super().__init__(raw)

    def _analyse(self):
        self._parser_header()
        return super()._analyse()

    def _parser_header(self):
        if self.raw[6:10] in (b'JFIF', b'Exif'):
            self.type = ImgType.JPEG
            self.extensions = [ImgExt.JPEG, ImgExt.JPG, ImgExt.JPE, ImgExt.JFIF]
            self.analyse_succeed = True
        elif self.raw[:4] == b'\xff\xd8\xff\xdb':
            self.type = ImgType.JPEG
            self.extensions = [ImgExt.JPEG, ImgExt.JPG, ImgExt.JPE, ImgExt.JFIF]
            self.analyse_succeed = True
