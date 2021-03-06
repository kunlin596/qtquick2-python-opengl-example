import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

if __name__ == '__main__':
	app = QGuiApplication(sys.argv)

	view = QQuickView()
	view.setSource(QUrl('SimpleRect.qml'))
	view.setResizeMode(QQuickView.SizeRootObjectToView)  # Set for the object to resize correctly

	view.show()

	app.exec()
