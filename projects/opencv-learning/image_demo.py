import cv2 #导入Opencv库，程序内所有图像处理功能通过cv2调用
img = cv2.imread("test.jpg") #读取图片
if img is None:
    print("图片读取失败，请检查图片名与路径") #判断图片是否读取成功
else:
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #转为灰度图

    cv2.imshow("Original Image",img) #显示原图
    cv2.imshow("Gray Imge",gray_img) #显示灰度图

    cv2.imwrite("gray_test.jpg",gray_img)
    print("灰度图片保存完成，文件名为 gray_test.jpg") #保存灰度图片

    cv2.waitKey(0)
    cv2.destroyAllWindows() #等待按键关闭窗口，0代表任意按键