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
# window.resize(300, 100) # إعادة ضبط حجم النافذة (الرأسى ,الأفقى)
# window.move(200, 100) # ضبط إبتعاد النافذة عن الركن اليسار الأعلى للشاشة (البعد الرأسى , البعد الأفقى)
# طريقة أخرى لضبط أبعاد النافذة ومكان ظهورها
window.setGeometry(300, 200, 400,300)  # (الطول الرأسى ,الطول الأفقى ,البعد الرأسى , البعد الأفقى)

# إنشاء متغير زر
btn = QPushButton(QIcon("PyQt.png"), "Close",window)  # (النافذة الأم , اسم الزر , ملف أيقونة الزر(إختيارى))
btn.setGeometry(150, 100, 100, 20)  # ضبط أبعاد الزر ومكانه فى النافذة ويمكن استخدام احدى الطريقتين كالنافذة بالضبط
btn.setToolTip("click to exit")
btn.clicked.connect(exit) # ضبط وظيفة للزر الخروج

window.show()  # إظهار النافذة

app.exec_()  # تنفيذ البرنامج (exec_) دالة تابعة لمكتبة Qt أما exec دالة تابعة للغة بايثون
