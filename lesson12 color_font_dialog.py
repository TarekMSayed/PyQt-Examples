import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)  # تفعيل النافذة من النظام

window = QWidget()  # إنشاء متغير من الفصيلة ويدجت (كائن رسومي)
window.setWindowTitle("PyQt5 Application Example")  # ضبط عنوان النافذة
window.setToolTip("This is the main window")  # ضبط الرسالة السحابية تظهر عند إشارة الفأرة Tool Tip
window.setWindowIcon(QIcon("PyQt.png"))  # تغيير أيقونة البرنامج بملف صورة يجب وضعها فى مجلد المشروع

# إحدى طرق ضبط أبعاد النافذة ومكان ظهرها على الشاشة
# window.resize(300, 100) # إعادة ضبط حجم النافذة (الرأسى , الأفقى)
# window.move(200, 100) # ضبط إبتعاد النافذة عن الركن اليسار الأعلى للشاشة (البعد الرأسى , البعد الأفقى)
# طريقة أخرى لضبط أبعاد النافذة ومكان ظهورها
window.setGeometry(300, 200, 400, 300)  # (الطول الرأسى , الطول الأفقى , البعد الرأسى , البعد الأفقى)

def show_color():
    c = QColorDialog.getColor()  # إنشاء متغير نافذة ألوان واختيار لون
    print(c)

def show_font():
    f = QFontDialog.getFont()  # إنشاء متغير نافذة خطوط واختيار خط
    print(f)

# إنشاء زر لإظهار نافذة اختيار اللون
c_btn = QPushButton("Color",window)
c_btn.move(80, 80)
c_btn.resize(80, 50)
c_btn.clicked.connect(show_color)

# إنشاء زر لإظهار نافذة اختيار الخط
f_btn = QPushButton("Fonts", window)
f_btn.move(200,80)
f_btn.resize(80,50)
f_btn.clicked.connect(show_font)

window.show()  # إظهار النافذة

app.exec_()  # تنفيذ البرنامج (exec_) دالة تابعة لمكتبة Qt أما exec دالة تابعة للغة بايثون
