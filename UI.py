# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui__form(object):
    def setupUi(self, _form):
        _form.setObjectName("_form")
        _form.resize(1600, 900)
        _form.setMinimumSize(QtCore.QSize(1600, 900))
        _form.setStyleSheet("background: rgb(100, 100, 100)")
        self.gridLayout_4 = QtWidgets.QGridLayout(_form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self._toolBarLayout = QtWidgets.QGridLayout()
        self._toolBarLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self._toolBarLayout.setContentsMargins(-1, 0, 0, -1)
        self._toolBarLayout.setObjectName("_toolBarLayout")
        self._toolBarWidget = QtWidgets.QWidget(_form)
        self._toolBarWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._toolBarWidget.sizePolicy().hasHeightForWidth())
        self._toolBarWidget.setSizePolicy(sizePolicy)
        self._toolBarWidget.setMinimumSize(QtCore.QSize(140, 500))
        self._toolBarWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._toolBarWidget.setBaseSize(QtCore.QSize(0, 250))
        self._toolBarWidget.setStyleSheet("background: rgb(50, 50, 50)")
        self._toolBarWidget.setObjectName("_toolBarWidget")
        self._blackIronLabel = QtWidgets.QLabel(self._toolBarWidget)
        self._blackIronLabel.setGeometry(QtCore.QRect(20, 20, 100, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self._blackIronLabel.setFont(font)
        self._blackIronLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._blackIronLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self._blackIronLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._blackIronLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self._blackIronLabel.setTextFormat(QtCore.Qt.PlainText)
        self._blackIronLabel.setAlignment(QtCore.Qt.AlignCenter)
        self._blackIronLabel.setWordWrap(False)
        self._blackIronLabel.setObjectName("_blackIronLabel")
        self._blackIronPriceTextEdit = QtWidgets.QTextEdit(self._toolBarWidget)
        self._blackIronPriceTextEdit.setGeometry(QtCore.QRect(20, 50, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._blackIronPriceTextEdit.sizePolicy().hasHeightForWidth())
        self._blackIronPriceTextEdit.setSizePolicy(sizePolicy)
        self._blackIronPriceTextEdit.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self._blackIronPriceTextEdit.setFont(font)
        self._blackIronPriceTextEdit.setAcceptDrops(True)
        self._blackIronPriceTextEdit.setStyleSheet("background:rgb(120, 120, 120)")
        self._blackIronPriceTextEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._blackIronPriceTextEdit.setLineWidth(1)
        self._blackIronPriceTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self._blackIronPriceTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self._blackIronPriceTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self._blackIronPriceTextEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self._blackIronPriceTextEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self._blackIronPriceTextEdit.setCursorWidth(1)
        self._blackIronPriceTextEdit.setObjectName("_blackIronPriceTextEdit")
        self._whiteIronPriceTextEdit = QtWidgets.QTextEdit(self._toolBarWidget)
        self._whiteIronPriceTextEdit.setEnabled(True)
        self._whiteIronPriceTextEdit.setGeometry(QtCore.QRect(20, 140, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._whiteIronPriceTextEdit.sizePolicy().hasHeightForWidth())
        self._whiteIronPriceTextEdit.setSizePolicy(sizePolicy)
        self._whiteIronPriceTextEdit.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self._whiteIronPriceTextEdit.setFont(font)
        self._whiteIronPriceTextEdit.setAcceptDrops(True)
        self._whiteIronPriceTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._whiteIronPriceTextEdit.setStyleSheet("background:rgb(120, 120, 120)")
        self._whiteIronPriceTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self._whiteIronPriceTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self._whiteIronPriceTextEdit.setObjectName("_whiteIronPriceTextEdit")
        self._whiteIronLabel = QtWidgets.QLabel(self._toolBarWidget)
        self._whiteIronLabel.setGeometry(QtCore.QRect(20, 110, 100, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self._whiteIronLabel.setFont(font)
        self._whiteIronLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._whiteIronLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self._whiteIronLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._whiteIronLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self._whiteIronLabel.setTextFormat(QtCore.Qt.PlainText)
        self._whiteIronLabel.setAlignment(QtCore.Qt.AlignCenter)
        self._whiteIronLabel.setWordWrap(False)
        self._whiteIronLabel.setObjectName("_whiteIronLabel")
        self._aluminumPriceTextEdit = QtWidgets.QTextEdit(self._toolBarWidget)
        self._aluminumPriceTextEdit.setEnabled(True)
        self._aluminumPriceTextEdit.setGeometry(QtCore.QRect(20, 230, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._aluminumPriceTextEdit.sizePolicy().hasHeightForWidth())
        self._aluminumPriceTextEdit.setSizePolicy(sizePolicy)
        self._aluminumPriceTextEdit.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self._aluminumPriceTextEdit.setFont(font)
        self._aluminumPriceTextEdit.setAcceptDrops(True)
        self._aluminumPriceTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._aluminumPriceTextEdit.setStyleSheet("background:rgb(120, 120, 120)")
        self._aluminumPriceTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self._aluminumPriceTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self._aluminumPriceTextEdit.setObjectName("_aluminumPriceTextEdit")
        self._aluminumLabel_ = QtWidgets.QLabel(self._toolBarWidget)
        self._aluminumLabel_.setGeometry(QtCore.QRect(20, 200, 100, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self._aluminumLabel_.setFont(font)
        self._aluminumLabel_.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._aluminumLabel_.setStyleSheet("color: rgb(255, 255, 255);")
        self._aluminumLabel_.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._aluminumLabel_.setFrameShadow(QtWidgets.QFrame.Plain)
        self._aluminumLabel_.setTextFormat(QtCore.Qt.PlainText)
        self._aluminumLabel_.setAlignment(QtCore.Qt.AlignCenter)
        self._aluminumLabel_.setWordWrap(False)
        self._aluminumLabel_.setObjectName("_aluminumLabel_")
        self._plusButton = QtWidgets.QPushButton(self._toolBarWidget)
        self._plusButton.setGeometry(QtCore.QRect(20, 290, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self._plusButton.setFont(font)
        self._plusButton.setStyleSheet("background: rgb(140, 140, 140);")
        self._plusButton.setObjectName("_plusButton")
        self._minusButton = QtWidgets.QPushButton(self._toolBarWidget)
        self._minusButton.setGeometry(QtCore.QRect(80, 290, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self._minusButton.setFont(font)
        self._minusButton.setStyleSheet("background: rgb(140, 140, 140);")
        self._minusButton.setObjectName("_minusButton")
        self._computeButton = QtWidgets.QPushButton(self._toolBarWidget)
        self._computeButton.setGeometry(QtCore.QRect(20, 355, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(40)
        self._computeButton.setFont(font)
        self._computeButton.setStyleSheet("background: rgb(140, 140, 140);\n"
"padding-bottom: 7px;")
        self._computeButton.setObjectName("_computeButton")
        self._screenshotButton = QtWidgets.QPushButton(self._toolBarWidget)
        self._screenshotButton.setGeometry(QtCore.QRect(20, 420, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self._screenshotButton.setFont(font)
        self._screenshotButton.setStyleSheet("background: rgb(140, 140, 140);")
        self._screenshotButton.setObjectName("_screenshotButton")
        self._toolBarLayout.addWidget(self._toolBarWidget, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self._toolBarLayout, 0, 0, 2, 1)
        self._informationLayout = QtWidgets.QGridLayout()
        self._informationLayout.setObjectName("_informationLayout")
        self._informationWidget = QtWidgets.QWidget(_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._informationWidget.sizePolicy().hasHeightForWidth())
        self._informationWidget.setSizePolicy(sizePolicy)
        self._informationWidget.setMinimumSize(QtCore.QSize(400, 200))
        self._informationWidget.setStyleSheet("background: rgb(255, 255, 255);")
        self._informationWidget.setObjectName("_informationWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self._informationWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._addressLayout = QtWidgets.QHBoxLayout()
        self._addressLayout.setObjectName("_addressLayout")
        self._addressWidget = QtWidgets.QWidget(self._informationWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._addressWidget.sizePolicy().hasHeightForWidth())
        self._addressWidget.setSizePolicy(sizePolicy)
        self._addressWidget.setMinimumSize(QtCore.QSize(400, 0))
        self._addressWidget.setObjectName("_addressWidget")
        self._customerName = QtWidgets.QLineEdit(self._addressWidget)
        self._customerName.setGeometry(QtCore.QRect(100, 110, 400, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self._customerName.setFont(font)
        self._customerName.setFrame(False)
        self._customerName.setObjectName("_customerName")
        self._address = QtWidgets.QLineEdit(self._addressWidget)
        self._address.setGeometry(QtCore.QRect(100, 140, 400, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self._address.setFont(font)
        self._address.setFrame(False)
        self._address.setObjectName("_address")
        self._customerNameLabel = QtWidgets.QLabel(self._addressWidget)
        self._customerNameLabel.setGeometry(QtCore.QRect(10, 110, 90, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._customerNameLabel.setFont(font)
        self._customerNameLabel.setObjectName("_customerNameLabel")
        self._addressLabel = QtWidgets.QLabel(self._addressWidget)
        self._addressLabel.setGeometry(QtCore.QRect(10, 140, 90, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._addressLabel.setFont(font)
        self._addressLabel.setObjectName("_addressLabel")
        self._addressLabel.raise_()
        self._customerNameLabel.raise_()
        self._customerName.raise_()
        self._address.raise_()
        self._addressLayout.addWidget(self._addressWidget)
        self.horizontalLayout_4.addLayout(self._addressLayout)
        self._centerLayout = QtWidgets.QHBoxLayout()
        self._centerLayout.setObjectName("_centerLayout")
        self._centerWidget = QtWidgets.QWidget(self._informationWidget)
        self._centerWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._centerWidget.setAutoFillBackground(False)
        self._centerWidget.setStyleSheet("")
        self._centerWidget.setObjectName("_centerWidget")
        self._billOfSaleLabel = QtWidgets.QLabel(self._centerWidget)
        self._billOfSaleLabel.setGeometry(QtCore.QRect(150, 10, 110, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(26)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self._billOfSaleLabel.setFont(font)
        self._billOfSaleLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._billOfSaleLabel.setObjectName("_billOfSaleLabel")
        self._centerLayout.addWidget(self._centerWidget)
        self.horizontalLayout_4.addLayout(self._centerLayout)
        self._dataLayout = QtWidgets.QHBoxLayout()
        self._dataLayout.setObjectName("_dataLayout")
        self._dataWidget = QtWidgets.QWidget(self._informationWidget)
        self._dataWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._dataWidget.setObjectName("_dataWidget")
        self._phoneLabel = QtWidgets.QLabel(self._dataWidget)
        self._phoneLabel.setGeometry(QtCore.QRect(110, 150, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._phoneLabel.sizePolicy().hasHeightForWidth())
        self._phoneLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._phoneLabel.setFont(font)
        self._phoneLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._phoneLabel.setObjectName("_phoneLabel")
        self._dateLabel = QtWidgets.QLabel(self._dataWidget)
        self._dateLabel.setGeometry(QtCore.QRect(110, 115, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._dateLabel.sizePolicy().hasHeightForWidth())
        self._dateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._dateLabel.setFont(font)
        self._dateLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._dateLabel.setObjectName("_dateLabel")
        self._phone = QtWidgets.QLineEdit(self._dataWidget)
        self._phone.setGeometry(QtCore.QRect(170, 147, 191, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._phone.sizePolicy().hasHeightForWidth())
        self._phone.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self._phone.setFont(font)
        self._phone.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._phone.setFrame(False)
        self._phone.setObjectName("_phone")
        self._serialNumber = QtWidgets.QLineEdit(self._dataWidget)
        self._serialNumber.setGeometry(QtCore.QRect(170, 77, 150, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._serialNumber.sizePolicy().hasHeightForWidth())
        self._serialNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self._serialNumber.setFont(font)
        self._serialNumber.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._serialNumber.setFrame(False)
        self._serialNumber.setObjectName("_serialNumber")
        self._date = QtWidgets.QLineEdit(self._dataWidget)
        self._date.setGeometry(QtCore.QRect(170, 112, 150, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._date.sizePolicy().hasHeightForWidth())
        self._date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self._date.setFont(font)
        self._date.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._date.setFrame(False)
        self._date.setObjectName("_date")
        self._serialNumberLabel = QtWidgets.QLabel(self._dataWidget)
        self._serialNumberLabel.setGeometry(QtCore.QRect(110, 80, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._serialNumberLabel.sizePolicy().hasHeightForWidth())
        self._serialNumberLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._serialNumberLabel.setFont(font)
        self._serialNumberLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._serialNumberLabel.setObjectName("_serialNumberLabel")
        self._dataLayout.addWidget(self._dataWidget)
        self.horizontalLayout_4.addLayout(self._dataLayout)
        self._informationLayout.addWidget(self._informationWidget, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self._informationLayout, 0, 1, 1, 1)
        self._tableLayout = QtWidgets.QGridLayout()
        self._tableLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self._tableLayout.setVerticalSpacing(6)
        self._tableLayout.setObjectName("_tableLayout")
        self._bottomSpaceWidget = QtWidgets.QWidget(_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._bottomSpaceWidget.sizePolicy().hasHeightForWidth())
        self._bottomSpaceWidget.setSizePolicy(sizePolicy)
        self._bottomSpaceWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self._bottomSpaceWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self._bottomSpaceWidget.setObjectName("_bottomSpaceWidget")
        self.gridLayout = QtWidgets.QGridLayout(self._bottomSpaceWidget)
        self.gridLayout.setObjectName("gridLayout")
        self._emptyLayout = QtWidgets.QHBoxLayout()
        self._emptyLayout.setObjectName("_emptyLayout")
        self._emptyWidget = QtWidgets.QWidget(self._bottomSpaceWidget)
        self._emptyWidget.setObjectName("_emptyWidget")
        self._emptyLayout.addWidget(self._emptyWidget)
        self.gridLayout.addLayout(self._emptyLayout, 0, 0, 1, 1)
        self._totalLayout = QtWidgets.QHBoxLayout()
        self._totalLayout.setObjectName("_totalLayout")
        self._totalWidget = QtWidgets.QWidget(self._bottomSpaceWidget)
        self._totalWidget.setObjectName("_totalWidget")
        self._totalLabel = QtWidgets.QLabel(self._totalWidget)
        self._totalLabel.setGeometry(QtCore.QRect(120, 20, 65, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._totalLabel.sizePolicy().hasHeightForWidth())
        self._totalLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self._totalLabel.setFont(font)
        self._totalLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._totalLabel.setTextFormat(QtCore.Qt.PlainText)
        self._totalLabel.setObjectName("_totalLabel")
        self._total = QtWidgets.QLabel(self._totalWidget)
        self._total.setGeometry(QtCore.QRect(210, 20, 250, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._total.sizePolicy().hasHeightForWidth())
        self._total.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self._total.setFont(font)
        self._total.setLayoutDirection(QtCore.Qt.RightToLeft)
        self._total.setTextFormat(QtCore.Qt.PlainText)
        self._total.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self._total.setObjectName("_total")
        self._totalLayout.addWidget(self._totalWidget)
        self.gridLayout.addLayout(self._totalLayout, 0, 2, 1, 1)
        self._emptyLayout2 = QtWidgets.QHBoxLayout()
        self._emptyLayout2.setObjectName("_emptyLayout2")
        self._emptyWidget2 = QtWidgets.QWidget(self._bottomSpaceWidget)
        self._emptyWidget2.setObjectName("_emptyWidget2")
        self._emptyLayout2.addWidget(self._emptyWidget2)
        self.gridLayout.addLayout(self._emptyLayout2, 0, 1, 1, 1)
        self._tableLayout.addWidget(self._bottomSpaceWidget, 3, 1, 1, 1)
        self._table = QtWidgets.QTableWidget(_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._table.sizePolicy().hasHeightForWidth())
        self._table.setSizePolicy(sizePolicy)
        self._table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._table.setSizeIncrement(QtCore.QSize(0, 0))
        self._table.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self._table.setFont(font)
        self._table.setFocusPolicy(QtCore.Qt.NoFocus)
        self._table.setWhatsThis("")
        self._table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self._table.setAutoFillBackground(False)
        self._table.setStyleSheet("QTableWidget {\n"
"    /* 设置表格的背景颜色 */\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background:rgb(154, 154, 154);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);  \n"
"}")
        self._table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._table.setLineWidth(0)
        self._table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self._table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self._table.setAutoScroll(True)
        self._table.setDragEnabled(False)
        self._table.setTextElideMode(QtCore.Qt.ElideRight)
        self._table.setShowGrid(True)
        self._table.setGridStyle(QtCore.Qt.SolidLine)
        self._table.setWordWrap(True)
        self._table.setRowCount(0)
        self._table.setColumnCount(17)
        self._table.setObjectName("_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        item.setFont(font)
        self._table.setHorizontalHeaderItem(16, item)
        self._table.horizontalHeader().setVisible(True)
        self._table.horizontalHeader().setCascadingSectionResizes(False)
        self._table.horizontalHeader().setDefaultSectionSize(110)
        self._table.horizontalHeader().setHighlightSections(True)
        self._table.horizontalHeader().setSortIndicatorShown(False)
        self._table.horizontalHeader().setStretchLastSection(True)
        self._table.verticalHeader().setVisible(True)
        self._table.verticalHeader().setStretchLastSection(False)
        self._tableLayout.addWidget(self._table, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self._tableLayout, 1, 1, 1, 1)

        self.retranslateUi(_form)
        QtCore.QMetaObject.connectSlotsByName(_form)

    def retranslateUi(self, _form):
        _translate = QtCore.QCoreApplication.translate
        _form.setWindowTitle(_translate("_form", "ShimmerLaser"))
        self._blackIronLabel.setText(_translate("_form", "黑鐵價格"))
        self._blackIronPriceTextEdit.setToolTip(_translate("_form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self._blackIronPriceTextEdit.setHtml(_translate("_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lato\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self._whiteIronPriceTextEdit.setToolTip(_translate("_form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self._whiteIronPriceTextEdit.setHtml(_translate("_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lato\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\';\">0</span></p></body></html>"))
        self._whiteIronLabel.setText(_translate("_form", "白鐵價格"))
        self._aluminumPriceTextEdit.setToolTip(_translate("_form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self._aluminumPriceTextEdit.setHtml(_translate("_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lato\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\';\">0</span></p></body></html>"))
        self._aluminumLabel_.setText(_translate("_form", "鋁價格"))
        self._plusButton.setText(_translate("_form", "+"))
        self._minusButton.setText(_translate("_form", "-"))
        self._computeButton.setText(_translate("_form", "🖩"))
        self._screenshotButton.setText(_translate("_form", "📷"))
        self._customerName.setText(_translate("_form", "1111111111111111111111111111111"))
        self._address.setText(_translate("_form", "111111111111111111111111111111111"))
        self._customerNameLabel.setText(_translate("_form", "客戶名稱:"))
        self._addressLabel.setText(_translate("_form", "送貨地址:"))
        self._billOfSaleLabel.setText(_translate("_form", "銷貨單"))
        self._phoneLabel.setText(_translate("_form", "電話:"))
        self._dateLabel.setText(_translate("_form", "日期:"))
        self._phone.setText(_translate("_form", "(06)-3333333"))
        self._serialNumber.setText(_translate("_form", "11111111111111"))
        self._date.setText(_translate("_form", "2023/5/30"))
        self._serialNumberLabel.setText(_translate("_form", "編號:"))
        self._totalLabel.setText(_translate("_form", "合計:"))
        self._total.setText(_translate("_form", "0"))
        self._table.setToolTip(_translate("_form", "<html><head/><body><pre align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\';\"><br/></pre></body></html>"))
        self._table.setSortingEnabled(False)
        item = self._table.horizontalHeaderItem(0)
        item.setText(_translate("_form", "件號/品名規格"))
        item = self._table.horizontalHeaderItem(1)
        item.setText(_translate("_form", "數量"))
        item = self._table.horizontalHeaderItem(2)
        item.setText(_translate("_form", "種類"))
        item = self._table.horizontalHeaderItem(3)
        item.setText(_translate("_form", "面積(mm^2)"))
        item = self._table.horizontalHeaderItem(4)
        item.setText(_translate("_form", "厚度(mm)"))
        item = self._table.horizontalHeaderItem(5)
        item.setText(_translate("_form", "重量(kg)"))
        item = self._table.horizontalHeaderItem(6)
        item.setText(_translate("_form", "單價"))
        item = self._table.horizontalHeaderItem(7)
        item.setText(_translate("_form", "板材費用"))
        item = self._table.horizontalHeaderItem(8)
        item.setText(_translate("_form", "打折(板材費用)"))
        item = self._table.horizontalHeaderItem(9)
        item.setText(_translate("_form", "板材費用(打折後)"))
        item = self._table.horizontalHeaderItem(10)
        item.setText(_translate("_form", "切割長度(m)"))
        item = self._table.horizontalHeaderItem(11)
        item.setText(_translate("_form", "大孔(>14mm)"))
        item = self._table.horizontalHeaderItem(12)
        item.setText(_translate("_form", "小孔(<14mm)"))
        item = self._table.horizontalHeaderItem(13)
        item.setText(_translate("_form", "雷射工資"))
        item = self._table.horizontalHeaderItem(14)
        item.setText(_translate("_form", "打折(雷射工資)"))
        item = self._table.horizontalHeaderItem(15)
        item.setText(_translate("_form", "雷射工資(打折後)"))
        item = self._table.horizontalHeaderItem(16)
        item.setText(_translate("_form", "合計"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    _form = QtWidgets.QWidget()
    ui = Ui__form()
    ui.setupUi(_form)
    _form.show()
    sys.exit(app.exec_())
