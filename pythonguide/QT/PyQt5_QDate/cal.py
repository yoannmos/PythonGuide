from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import (QColor, QFont, QTextCharFormat, QTextLength,
        QTextTableFormat)
from PyQt5.QtWidgets import (QApplication, QComboBox, QDateTimeEdit,
        QHBoxLayout, QLabel, QMainWindow, QSpinBox, QTextBrowser, QVBoxLayout,
        QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.selectedDate = QDate.currentDate()
        self.fontSize = 10

        centralWidget = QWidget()

        dateLabel = QLabel("Date:")
        monthCombo = QComboBox()

        for month in range(1, 13):
            monthCombo.addItem(QDate.longMonthName(month))

        yearEdit = QDateTimeEdit()
        yearEdit.setDisplayFormat('yyyy')
        yearEdit.setDateRange(QDate(1753, 1, 1), QDate(8000, 1, 1))

        monthCombo.setCurrentIndex(self.selectedDate.month() - 1)
        yearEdit.setDate(self.selectedDate)

        self.fontSizeLabel = QLabel("Font size:")
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setRange(1, 64)
        self.fontSizeSpinBox.setValue(10)

        self.editor = QTextBrowser()
        self.insertCalendar()

        monthCombo.activated.connect(self.setMonth)
        yearEdit.dateChanged.connect(self.setYear)
        self.fontSizeSpinBox.valueChanged.connect(self.setfontSize)

        controlsLayout = QHBoxLayout()
        controlsLayout.addWidget(dateLabel)
        controlsLayout.addWidget(monthCombo)
        controlsLayout.addWidget(yearEdit)
        controlsLayout.addSpacing(24)
        controlsLayout.addWidget(self.fontSizeLabel)
        controlsLayout.addWidget(self.fontSizeSpinBox)
        controlsLayout.addStretch(1)

        centralLayout = QVBoxLayout()
        centralLayout.addLayout(controlsLayout)
        centralLayout.addWidget(self.editor, 1)
        centralWidget.setLayout(centralLayout)

        self.setCentralWidget(centralWidget)

    def insertCalendar(self):
        self.editor.clear()
        cursor = self.editor.textCursor()
        cursor.beginEditBlock()

        date = QDate(self.selectedDate.year(), self.selectedDate.month(), 1)

        tableFormat = QTextTableFormat()
        tableFormat.setAlignment(Qt.AlignHCenter)
        tableFormat.setBackground(QColor('#e0e0e0'))
        tableFormat.setCellPadding(2)
        tableFormat.setCellSpacing(4)
        constraints = [QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14),
                       QTextLength(QTextLength.PercentageLength, 14)]

        tableFormat.setColumnWidthConstraints(constraints)

        table = cursor.insertTable(1, 7, tableFormat)

        frame = cursor.currentFrame()
        frameFormat = frame.frameFormat()
        frameFormat.setBorder(1)
        frame.setFrameFormat(frameFormat)

        format = cursor.charFormat()
        format.setFontPointSize(self.fontSize)

        boldFormat = QTextCharFormat(format)
        boldFormat.setFontWeight(QFont.Bold)

        highlightedFormat = QTextCharFormat(boldFormat)
        highlightedFormat.setBackground(Qt.yellow)

        for weekDay in range(1, 8):
            cell = table.cellAt(0, weekDay-1)
            cellCursor = cell.firstCursorPosition()
            cellCursor.insertText(QDate.longDayName(weekDay), boldFormat)

        table.insertRows(table.rows(), 1)

        while date.month() == self.selectedDate.month():
            weekDay = date.dayOfWeek()
            cell = table.cellAt(table.rows()-1, weekDay-1)
            cellCursor = cell.firstCursorPosition()

            if date == QDate.currentDate():
                cellCursor.insertText(str(date.day()), highlightedFormat)
            else:
                cellCursor.insertText(str(date.day()), format)

            date = date.addDays(1)

            if weekDay == 7 and date.month() == self.selectedDate.month():
                table.insertRows(table.rows(), 1)

        cursor.endEditBlock()

        self.setWindowTitle("Calendar for %s %d" % (QDate.longMonthName(self.selectedDate.month()), self.selectedDate.year()))

    def setfontSize(self, size):
        self.fontSize = size
        self.insertCalendar()

    def setMonth(self, month):
        self.selectedDate = QDate(self.selectedDate.year(), month + 1,
                self.selectedDate.day())
        self.insertCalendar()

    def setYear(self, date):
        self.selectedDate = QDate(date.year(), self.selectedDate.month(),
                self.selectedDate.day())
        self.insertCalendar()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(640, 256)
    window.show()
    sys.exit(app.exec_()) 