import cv2


class CalculateDistance:
    def __init__(self, background_path, slide_path, offset_px, offset_py, display):
        self.background_img = cv2.imread(background_path)
        self.offset_px = offset_px
        self.offset_py = offset_py
        self.slide_img = cv2.imread(slide_path, cv2.IMREAD_GRAYSCALE)
        # 计算x轴缩放因子，以50px为基准
        scale_x = 50 / self.slide_img.shape[1]
        self.slide_scale_img = cv2.resize(self.slide_img, (0, 0), fx=scale_x, fy=scale_x)
        self.background_cut_img = None
        self.display = display

    def get_distance(self):
        # 将小图转换为灰色
        slide_grey_img = cv2.merge([self.slide_scale_img, self.slide_scale_img, self.slide_scale_img])
        slide_grey_img = cv2.cvtColor(slide_grey_img, cv2.COLOR_BGR2GRAY)
        # 使用canny算子，提取图片边缘特征
        # 特征值可以调试：100,200，细节特征比较明显，数值增大后特征较为粗略
        slide_edge_img = cv2.Canny(slide_grey_img, 100, 250)
        # self.cv_show('canny', slide_edge_img)
        # 将背景图转换为灰色
        # background_grey_img = cv2.merge([self.background_cut_img, self.background_cut_img, self.background_cut_img])
        background_grey_img = cv2.cvtColor(self.background_cut_img, cv2.COLOR_BGR2GRAY)
        # 使用canny算子，提取图片边缘特征
        background_edge_img = cv2.Canny(background_grey_img, 200, 300)
        # self.cv_show('bg_canny', background_edge_img)
        # 取小图的高和宽
        h, w = background_edge_img.shape

        # 将滑块图与背景进行模板匹配，找到缺口对应的位置
        result = cv2.matchTemplate(background_edge_img, slide_edge_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # 获取缺口左上角位置
        top_left = (max_loc[0], max_loc[1])
        # 右下角位置
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # 在切割后背景图片中画出需要移动的终点位置
        # rectangle(图片源数据, 左上角, 右下角, 颜色, 画笔厚度)
        if self.display:
            after_img = cv2.rectangle(self.background_cut_img, top_left, bottom_right, (0, 0, 255), 2)
            # 画图
            self.cv_show('after', after_img)
        # 计算移动距离
        slide_distance = top_left[0] + w / 2.25 + 10
        return slide_distance

    def cut_background(self):
        # 切割图片的上下边框
        height = self.slide_scale_img.shape[0]
        # 将图片中上下多余部分以及滑块图片部分去掉
        self.background_cut_img = self.background_img[self.offset_py - 10: self.offset_py + height + 10, self.offset_px + height + 10:]

    def cv_show(self, name, img):
        cv2.imshow(name, img)
        cv2.waitKey(1)
        cv2.destroyAllWindows()

    def run(self):
        self.cut_background()
        return self.get_distance()

