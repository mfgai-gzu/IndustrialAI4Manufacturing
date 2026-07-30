import cv2
import os

# 读取说明书里的零件截图（把截图放到同目录，命名为part.png）
img = cv2.imread('part.jpeg')
if img is None:
    print("请把零件截图放在同目录，命名为 part.pnjpeg")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# 保存结果
cv2.imwrite('part_edges.jpg', edges)
print("边缘检测完成！结果已保存为 part_edges.jpg")