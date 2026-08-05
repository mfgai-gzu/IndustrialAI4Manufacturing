import cv2
import numpy as np
import os

# 自动获取脚本所在目录，解决路径问题
current_dir = os.path.dirname(__file__)
img_path = os.path.join(current_dir, "part.png")

img = cv2.imread(img_path)
if img is None:
    print(f"图片读取失败，路径：{img_path}")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

contour_output = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contour_output) == 3:
    _, contours, _ = contour_output
else:
    contours, _ = contour_output

if len(contours) == 0:
    print("没有找到任何轮廓，请调整Canny阈值或者图片质量")
    exit()

cnt = max(contours, key=cv2.contourArea)

x, y, w_px, h_px = cv2.boundingRect(cnt)

real_width_mm = 76.138
real_height_mm = 42.0
pixels_per_mm = w_px / real_width_mm

measured_w = w_px / pixels_per_mm
measured_h = h_px / pixels_per_mm

print(f"====测量结果====")
print(f"检测尺寸：{measured_w:.2f} mm × {measured_h:.2f} mm")
print(f"图纸要求：{real_width_mm:.2f} mm × {real_height_mm:.2f} mm")
print(f"宽度误差：{measured_w-real_width_mm:.3f} mm")
print(f"高度误差：{measured_h-real_height_mm:.3f} mm")

cv2.rectangle(img, (x, y), (x+w_px, y+h_px), (0, 255, 0), 2)
out_img_path = os.path.join(current_dir, "measure_result.png")
cv2.imwrite(out_img_path, img)
print(f"绘制框结果已保存至：{out_img_path}")