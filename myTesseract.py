#coding:utf-8
# Pillow+Tesseract组合。图像处理+文字识别
# Pillow图像处理，等价于ps，主要为了处理成更加容易识别的图片
from PIL import Image, ImageFilter

# kitten = Image.open("test.jpg")  #读取图片
# blurryKitten = kitten.filter(ImageFilter.GaussianBlur)  #图片处理——图片高斯模糊
# blurryKitten.save("test1.jpg")  #图片保存
# blurryKitten.show()  #打开图片


# Tesseract可以直接将图片中的文字进行识别（验证码），其最新版本3.0已经支持中文OCR，并提供了一个命令行工具，转换成文本信息
#安装时记得选择要识别的文字类型，现在支持60多种文字，包含中文简体繁体。

# Usage:tesseract imagename outputbase [-l lang] [-psm pagesegmode] [configfile...]
# pagesegmode values are:
# 0 = Orientation and script detection (OSD) only.
# 1 = Automatic page segmentation with OSD.
# 2 = Automatic page segmentation, but no OSD, or OCR
# 3 = Fully automatic page segmentation, but no OSD. (Default)
# 4 = Assume a single column of text of variable sizes.
# 5 = Assume a single uniform block of vertically aligned text.
# 6 = Assume a single uniform block of text.
# 7 = Treat the image as a single text line.
# 8 = Treat the image as a single word.
# 9 = Treat the image as a single word in a circle.
# 10 = Treat the image as a single character.
# -l lang and/or -psm pagesegmode must occur before anyconfigfile.
# tesseract imagename outputbase [-l lang] [-psm pagesegmode] [configfile...]
# tesseract    图片名  输出文件名 -l 字库文件 -psm pagesegmode 配置文件
# 例如：
# tesseract code.jpg result  -l chi_sim -psm 7 nobatch
# -l chi_sim 表示用简体中文字库（需要下载中文字库文件，解压后，存放到tessdata目录下去,字库文件扩展名为  .raineddata 简体中文字库文件名为:  chi_sim.traineddata）
# -psm 7 表示告诉tesseract code.jpg图片是一行文本  这个参数可以减少识别错误率.  默认为 3
# configfile 参数值为tessdata\configs 和  tessdata\tessconfigs 目录下的文件名


import subprocess #用来执行doc命令

#图片清洗
def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    # 对图片进行阈值过滤，然后保存
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)
    # 调用系统的tesseract命令对图片进行OCR识别
    subprocess.call(["tesseract", newFilePath, "output"])
    # 打开文件读取结果
    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()

cleanFile("text1.jpg", "text1_clean.png")