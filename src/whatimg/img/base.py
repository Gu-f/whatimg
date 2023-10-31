class ImgInfo(object):
    """
    图片公共属性
    Base class for image
    """

    def __init__(self, raw: bytes):
        self.raw = raw  # 原始数据 (raw data)
        # self.high = None  # 高 todo
        # self.width = None  # 宽 todo
        self.extensions = list  # 可用扩展名 (Available image extension)
        self.type = None  # 类型 (type)
        self.analyse_succeed = False  # 分析状态是否成功 (if it is successful)

    def _analyse(self):
        if self.analyse_succeed is True:
            return self
        else:
            return None
