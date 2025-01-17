from PyQt5 import QtCore, QtGui, QtWidgets


class SeckillUi(object):
    def setupUi(self, quick_buy):
        quick_buy.setObjectName("quick_buy")
        quick_buy.resize(700, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        quick_buy.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(quick_buy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choose_tao = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_tao.sizePolicy().hasHeightForWidth())
        self.choose_tao.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.choose_tao.setFont(font)
        self.choose_tao.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/taobao_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("icons/taobao.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.choose_tao.setIcon(icon1)
        self.choose_tao.setIconSize(QtCore.QSize(200, 100))
        self.choose_tao.setCheckable(True)
        self.choose_tao.setObjectName("choose_tao")
        self.horizontalLayout.addWidget(self.choose_tao)
        self.choose_jing = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_jing.sizePolicy().hasHeightForWidth())
        self.choose_jing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.choose_jing.setFont(font)
        self.choose_jing.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/jdong_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("icons/jdong.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.choose_jing.setIcon(icon2)
        self.choose_jing.setIconSize(QtCore.QSize(200, 100))
        self.choose_jing.setCheckable(True)
        self.choose_jing.setObjectName("choose_jing")
        self.horizontalLayout.addWidget(self.choose_jing)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_now = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_now.setFont(font)
        self.btn_now.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/qiang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_now.setIcon(icon3)
        self.btn_now.setIconSize(QtCore.QSize(150, 150))
        self.btn_now.setObjectName("btn_now")
        self.horizontalLayout_3.addWidget(self.btn_now)
        self.btn_later = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_later.sizePolicy().hasHeightForWidth())
        self.btn_later.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_later.setFont(font)
        self.btn_later.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/later.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_later.setIcon(icon4)
        self.btn_later.setIconSize(QtCore.QSize(150, 150))
        self.btn_later.setCheckable(False)
        self.btn_later.setObjectName("btn_later")
        self.horizontalLayout_3.addWidget(self.btn_later)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/bangzhushouce.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon5)
        self.help.setObjectName("help")
        self.horizontalLayout_2.addWidget(self.help)
        self.about = QtWidgets.QPushButton(self.centralwidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about.setIcon(icon6)
        self.about.setObjectName("about")
        self.horizontalLayout_2.addWidget(self.about)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_mode = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mode.setObjectName("btn_mode")
        self.verticalLayout_5.addWidget(self.btn_mode)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.btn_quit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_quit.setObjectName("btn_quit")
        self.verticalLayout_5.addWidget(self.btn_quit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        quick_buy.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(quick_buy)
        self.statusbar.setObjectName("statusbar")
        quick_buy.setStatusBar(self.statusbar)

        self.retranslateUi(quick_buy)
        QtCore.QMetaObject.connectSlotsByName(quick_buy)

    def retranslateUi(self, quick_buy):
        _translate = QtCore.QCoreApplication.translate
        quick_buy.setWindowTitle(_translate("quick_buy", "SecKill"))
        self.label.setText(_translate("quick_buy", "step1：选择购物平台"))
        self.choose_tao.setStatusTip(_translate("quick_buy", "淘宝"))
        self.choose_jing.setStatusTip(_translate("quick_buy", "京东"))
        self.label_3.setText(_translate("quick_buy", "step2：输入商品链接"))
        self.lineEdit.setStatusTip(_translate("quick_buy", "输入链接"))
        self.label_2.setText(_translate("quick_buy", "step3：选择抢购方式"))
        self.btn_now.setStatusTip(_translate("quick_buy", "立即抢购"))
        self.btn_later.setStatusTip(_translate("quick_buy", "定时抢购"))
        self.help.setStatusTip(_translate("quick_buy", "帮助"))
        self.help.setText(_translate("quick_buy", "帮助"))
        self.about.setStatusTip(_translate("quick_buy", "关于"))
        self.about.setText(_translate("quick_buy", "关于"))
        self.textBrowser.setStatusTip(_translate("quick_buy", "抢单状态"))
        self.btn_mode.setStatusTip(_translate("quick_buy", "切换为浅色模式"))
        self.btn_mode.setText(_translate("quick_buy", "深色模式"))
        self.btn_quit.setStatusTip(_translate("quick_buy", "结束抢单"))
        self.btn_quit.setText(_translate("quick_buy", "结束抢单"))
