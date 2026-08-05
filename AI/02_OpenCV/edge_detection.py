import cv2
import os

# 获取当前脚本所在文件夹
current_dir = os.path.dirname(__file__)
img_path = os.path.join(current_dir, "part.jpeg")

img = cv2.imread(img_path)
if img is None:
    print(f"读取失败，尝试路径：{img_path}")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# 输出文件也保存到脚本同目录
output_path = os.path.join(current_dir, "part_edges.jpeg")
cv2.imwrite(output_path, edges)
print(f"边缘检测完成！结果已保存为 {output_path}")