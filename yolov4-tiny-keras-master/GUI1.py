# -*- coding: utf-8 -*-
import sys
import re
import os
import cv2
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QAction, QStatusBar, QFileDialog,QMessageBox, QTextBrowser
from PyQt5.QtCore import QTimer, QDateTime, QThread, pyqtSignal, QObject
from timeit import default_timer as timer
from PIL import Image, ImageDraw
from UI_for_demo import *
import yolo
import numpy as np
from threading import Thread



class MySignals(QObject):
    text_print = pyqtSignal(str)


class hello_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):#最后一个参数对应QtDesigner生成的文件第一个class名字.默认是Ui_Form或Ui_MainWindow
    def __init__(self, parent=None, QSS=None):
        super(hello_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ms = MySignals()
        self.ms.text_print.connect(self.info_show)
        #显示时间
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.actionopenPicture.triggered.connect(self.openPicture)#打开图片
        self.actionopenVideo.triggered.connect(self.openVideo)  # 打开视频
        self.menu_2.triggered.connect(self.popWindow1)
        self.menu_3.triggered.connect(self.popWindow)

        self.pushButton.clicked.connect(self.pattern_fun)#图片识别

        # self.pushButton_2.clicked.connect(self.slotStart)  # 视频识别
        # self.pushButton_2.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.camrun) #打开摄像头
        self.pushButton_3.clicked.connect(self.cutRecg)
        self.pushButton_7.clicked.connect(self.slotStop)  # 停止识别

        self.timer_camera = QTimer()
        #yolo部分初始化
        self.YOLO = yolo.YOLO()

        self.thstop = False
        self.i = 1
#以下是信号槽连接的函数

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label_2.setText(timeDisplay)

    def openPicture(self):
        self.picture_info = QFileDialog.getOpenFileName(self, '选择图片', '',
                                                   'Picture files(*.jpg , *.png)')
        self.picture_name = self.picture_info[0]
        print(self.picture_name)
        if self.picture_name == '':
            return
        self.label.setPixmap(QPixmap(self.picture_name))
        self.label_4.setPixmap(QPixmap(self.picture_name))
        self.label_4.setScaledContents(True)
        self.label.setScaledContents(True)

    def openVideo(self):
        self.video_info = QFileDialog.getOpenFileName(self, '选择视频', '',
                                                   'Video files(*.mp4 , *.avi)')
        self.video_name = self.video_info[0]
        print(self.video_name)
        if self.video_name == '':
            print("\n取消选择")
            return
        # 设置视频
        self.label.setPixmap(QPixmap(self.video_name))
        self.label.setScaledContents(True)

    def popWindow(self):
        self.msgbox = QMessageBox(QMessageBox.Information, "反馈", "欢迎加微信交流\n+vx:17376555001", QMessageBox.Ok, self)
        self.msgbox.show()

    def popWindow1(self):
        self.msgbox = QMessageBox(QMessageBox.Information, "帮助", "1.从‘文件’选择图片或视频文件\n2.点击图片识别或者视频识别\n3.识别结束后暂停识别", QMessageBox.Ok, self)
        self.msgbox.show()

    def info_show(self, text):
        self.textBrowser.append(str(text))
        self.textBrowser.ensureCursorVisible()
   #图片识别
    def pattern_fun(self):
        self.textBrowser.clear()
        image = Image.open(self.picture_name)
        image_info = self.YOLO.detect_image(image)
        r_image = image_info[0]
        d1 = os.path.split(self.picture_name)  # 文件名
        print(d1)
        d2 = re.split(r"[.]", d1[1])  # 去除后缀,
        # 把函数移进来
        out = "{0}/{1}_res.png".format(d1[0], d2[0])
        print(out)
        r_image.save(out)
        print(image_info[2])
        out_class_names = ['can','battery','mask','apple','banana','orange','drug']
        big_classes = {'可回收垃圾': [0], '有害垃圾': [1,6], '干垃圾': [2], '湿垃圾': [3,4,5]}
        for k in big_classes:
            if image_info[2] in big_classes[k]:
                out_cls = k
                print(k)
        self.textBrowser.append('Found {} boxes for {}'.format(len(image_info[1]), 'img'))
        for i, c in reversed(list(enumerate(image_info[2]))):
            predicted_class = out_class_names[c]
            box = image_info[1][i]
            score = image_info[3][i]
            label = '{} {:.2f}'.format(predicted_class, score)
            top, left, bottom, right = box
            top = max(0, np.floor(top + 0.5).astype('int32'))
            left = max(0, np.floor(left + 0.5).astype('int32'))
            bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
            right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
            print(label, (left, top), (right, bottom))
            self.ms.text_print.emit(label +'\n'+ out_cls+ '\n' + str((left, top)) + str((right, bottom)))
            time.sleep(0.1)
            # self.textBrowser.append(label + str((left, top)) + str((right, bottom)))
        self.label.setPixmap(QPixmap(out))
        # 拉伸
        self.label.setScaledContents(True)


    #定时器开始
    def slotStart(self):
        # 100毫秒
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)



    def openFrame(self):

        frame = cv2.cvtColor(self.result, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        q_image = QImage(frame.data, width, height, bytesPerLine,
                         QImage.Format_RGB888).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(QPixmap.fromImage(q_image))

        # 刷新摄像头的显示时间，实时显示：

    def startcam(self):
        self.folder_path = r"D:/dianzishangwu2020/yolov4-tiny-keras-master/temp_pic/"
        self.cap = cv2.VideoCapture(0)  # 开启摄像头
        # 使用label的setPixmap方法显示
        while self.cap.isOpened():
            if self.thstop:
                return
            # get a frame
            ret, img = self.cap.read()
            self.copyimg = img
            if ret == False:
                continue
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
            # 转为QImage对象
            self.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(self.image).scaled(self.label.width(), self.label.height()))
    def camrun(self):
        th = Thread(target=self.startcam)
        th.start()

    # 定时器停止
    def slotStop(self):
        self.thstop = True
        self.cap.release()
        self.timer_camera.stop()  # 停止计时器
    #截图识别 显示在label上
    def cutRecg(self):
        cutimgname = self.folder_path + str(self.i) + '.jpg'
        saveimg = cv2.cvtColor(self.copyimg, cv2.COLOR_BGR2RGB)
        cv2.imwrite(cutimgname, saveimg)  # 存储为图像
        self.i = self.i + 1
        # self.thstop = True
        # self.cap.release()
        # self.timer_camera.stop()  # 停止计时器
        self.label.setPixmap(QPixmap(cutimgname))
        self.label_4.setPixmap(QPixmap(cutimgname))
        self.label_4.setScaledContents(True)
        self.label.setScaledContents(True)
        self.textBrowser.clear()
        image = Image.open(cutimgname)
        image_info = self.YOLO.detect_image(image)
        r_image = image_info[0]
        d1 = os.path.split(cutimgname)  # 文件名
        print(d1)
        d2 = re.split(r"[.]", d1[1])  # 去除后缀,
        # 把函数移进来
        out = "{0}/{1}_res.png".format(d1[0], d2[0])
        print(out)
        r_image.save(out)
        out_class_names = ['can', 'battery', 'mask', 'apple', 'banana', 'orange', 'drug']
        big_classes = {'可回收垃圾': [0], '有害垃圾': [1, 6], '干垃圾': [2], '湿垃圾': [3, 4, 5]}
        for k in big_classes:
            if image_info[2] in big_classes[k]:
                out_cls = k
                print(k)
        self.textBrowser.append('Found {} boxes for {}'.format(len(image_info[1]), 'img'))
        for i, c in reversed(list(enumerate(image_info[2]))):
            predicted_class = out_class_names[c]
            box = image_info[1][i]
            score = image_info[3][i]
            label = '{} {:.2f}'.format(predicted_class, score)
            top, left, bottom, right = box
            top = max(0, np.floor(top + 0.5).astype('int32'))
            left = max(0, np.floor(left + 0.5).astype('int32'))
            bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
            right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
            print(label, (left, top), (right, bottom))
            self.ms.text_print.emit(label +'\n'+ out_cls+ '\n'+ str((left, top)) + str((right, bottom)))
            time.sleep(0.1)
            # self.textBrowser.append(label + str((left, top)) + str((right, bottom)))
        # self.label.setPixmap(QPixmap(out))
        # # 拉伸
        # self.label.setScaledContents(True)
        self.label_4.setPixmap(QPixmap(out))
        self.label_4.setScaledContents(True)




    def run(self):
        # videothread = Thread(target=self.video_fun)
        # videothread.start()
        self.video_fun()

    def video_fun(self):

        d1 = os.path.split(self.video_name)  # 文件名
        d2 = re.split(r"[.]", d1[1])  # 去除后缀,
        #把函数移进来
        invideo=self.video_name
        outvideo="{0}/{1}_res.mp4".format(d1[0],d2[0])
        YOLO = yolo.YOLO()
        self.vid = cv2.VideoCapture(invideo)
        if not self.vid.isOpened():
            raise IOError("Couldn't open webcam or video")
        #格式,帧速率\码率(fps), 帧的尺寸
        video_FourCC = int(self.vid.get(cv2.CAP_PROP_FOURCC))
        video_fps = self.vid.get(cv2.CAP_PROP_FPS)
        video_size = (int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                      int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        isOutput = True if outvideo != "" else False
        if isOutput:
            print("!!! TYPE:", type(outvideo), type(video_FourCC), type(video_fps), type(video_size))
            #名字,格式,帧速率\码率(fps), 帧的尺寸
            out = cv2.VideoWriter(outvideo, video_FourCC, video_fps, video_size)
        accum_time = 0
        curr_fps = 0
        fps = "FPS: ??"
        prev_time = timer()
        while True:
            #读取
            return_value, frame = self.vid.read()
            if frame is None:
                break
            #frame原是np,变成img给YOLO处理后再变回np.
            image = Image.fromarray(frame)
            image = YOLO.detect_image(image)[0]
            self.result = np.asarray(image)
            curr_time = timer()
            #执行时间
            exec_time = curr_time - prev_time
            prev_time = curr_time
            #累计用时
            accum_time = accum_time + exec_time
            #累计fps
            curr_fps = curr_fps + 1
            #大于一秒,计算一秒的累计fps
            if accum_time > 1:
                accum_time = accum_time - 1
                fps = "FPS: " + str(curr_fps)
                curr_fps = 0
            #图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细
            cv2.putText(self.result, text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.50, color=(255, 0, 0), thickness=2)
            cv2.namedWindow("result", cv2.WINDOW_NORMAL)
            #显示和图像一样大,第一个是视频标题

            cv2.imshow("result", self.result)
            if isOutput:
                out.write(self.result)
            # 保持窗口.参数表示延迟多少毫秒。默认情况为0。当delay≤0，可以理解为延迟无穷大毫秒，就是暂停了。
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        YOLO.close_session()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("logo.png"))
    mainWindow = hello_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
