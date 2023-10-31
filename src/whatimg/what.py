import os
from src.whatimg.img import __cls_tests__
from src.whatimg.img.base import ImgInfo


def what(file: str | bytes, simple: bool = True) -> ImgInfo:
    size: int = 32  # simple模式默认只取前32
    if isinstance(file, (str, os.PathLike)):
        if not os.path.exists(file):
            raise ValueError(f"{file} not exist.")
        with open(file, 'rb') as fp:
            if simple:
                raw = fp.read(size)
            else:
                raw = fp.read()
    else:
        if simple:
            raw = file[:size]
        else:
            raw = file

    for img_cls in __cls_tests__:
        img_obj = img_cls(raw)
        result = img_obj._analyse()
        if result:
            return result


if __name__ == '__main__':
    img_info = what(r'/home/guf/Workspace/python/whatimg/images_hdr/jpeg.jpeg')

    print(type(img_info))
    print(img_info.type)
