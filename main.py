import utils
import canny_edge_detector as ced

# Загрузка изображений из /faces_imgs и приведение их к тонам серого
imgs = utils.load_data()
utils.visualize(imgs, 'gray')

# Запуск детектора Кэнни и сохранение полученных изображенний
detector = ced.cannyEdgeDetector(imgs, sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.17, weak_pixel=100)
imgs_final = detector.detect()

# Вывод полученных изображений с выделенными границами
utils.visualize(imgs_final, 'gray')