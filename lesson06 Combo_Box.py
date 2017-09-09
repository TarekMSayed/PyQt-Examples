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
window.setGeometry(300, 200, 400,300)  # (الطول الرأسى , الطول الأفقى , البعد الرأسى , البعد الأفقى)

# إنشاء متغير صندوق اختيارات
cmb = QComboBox(window)
cmb.setGeometry(80, 80, 150, 30)
cmb.addItem("Windows 7")
cmb.addItem("Windows 8")
cmb.addItem("Windows 10")

cmb1 = QComboBox(window)
cmb1.resize(150, 30)
cmb1.move(80, 120)
cmb1.addItem("Windows 7")  # إضافة العناصر واحد بواحد
cmb1.addItem("Windows 8")
cmb1.addItem("Windows 10")
cmb1.setCurrentIndex(1)  # تحديد الخيار الافتراضى

cmb2 = QComboBox(window)
cmb2.setGeometry(80, 160, 150, 30)
cmb2.addItems(["Windows 7", "Windows 8", "Windows 10"])  # إضافة العناصر كقائمة واحدة
cmb2.setCurrentIndex(2)

window.show()  # إظهار النافذة

app.exec_()  # تنفيذ البرنامج (exec_) دالة تابعة لمكتبة Qt أما exec دالة تابعة للغة بايثون
