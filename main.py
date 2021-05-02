from cs1media import *
def luma(p):
    r, g, b = p
    return int(0.213 * r + 0.715 * g + 0.072 * b)

# 디지털 사진에서 각각의 픽셀의 밝기를 luma함수를 통해 구할 수 있음

white = (255, 255, 255)
black = (0, 0, 0)


def blackwhite(img, threshold):  # 임계점을 인자로 넘겨줌
    w, h = img.size()
    for y in range(h):
        for x in range(w):  # 이미지의 가로, 세로 폭을 받음
            v = luma(img.get(x, y))  # 각각의 픽셀에 대한 빛의 세기를 받음
            if v > threshold:
                img.set(x, y, white)  # 하얀색 입히기
            else:
                img.set(x, y, black)  # 검정색 입히기


pict = load_picture("./data/bus_people.jpg")
blackwhite(pict, 100)
pict.show()