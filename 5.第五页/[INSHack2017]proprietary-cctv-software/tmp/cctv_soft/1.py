# uncompyle6 version 3.7.4
# Python bytecode 3.5 (3351)
# Decompiled from: Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)]
# Embedded file name: src/standalone/cctv_manager_standalone.py
# Compiled at: 2017-03-02 02:01:47
# Size of source mod 2**32: 9817 bytes
import signal, sys
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QSizePolicy
DEBUG = True

def print_dbg(msg):
    if DEBUG:
        print(msg)


class Activator(object):
    CHARSET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self):
        super(Activator, self).__init__()
        self.z = 36
        self.checksum = [30, 24, 18, 12, 6, 0]

    def block(self, b, mod):
        print_dbg('call: block(self, b=<%s>, mod=%d)' % (b, mod))
        if len(b) != 6:
            print_dbg('err: incorrect block length (%d)' % len(b))
            return
        s = 0
        for k in range(0, len(b)):
            l = b[k]
            if l not in Activator.CHARSET:
                print_dbg('err: input not found in charset (%s)' % l)
                return
            v = abs(Activator.CHARSET.index(l) - (k + 1))
            s += v
            print_dbg('current l is: %s' % l)
            print_dbg('current k is: %d' % k)
            print_dbg('current value is: %d' % v)
            print_dbg('current sum is: %d' % s)

        return s % mod

    def activate(self, s):
        print_dbg('call: activate(self, s=<%s>)' % s)
        blocks = s.split('-')
        blocks_sz = len(blocks)
        if blocks_sz != 6:
            print_dbg('err: incorrect number of blocks (%d)' % blocks_sz)
            return False
        for k in range(0, blocks_sz):
            self.z = self.block(blocks[k], self.z)
            print_dbg('dbg: new z is: {}'.format(self.z) )
            if self.z is None:
                print_dbg('err: block function returned error')
                return False
            if self.z != self.checksum[k]:
                print_dbg('err: incorrect checksum (z=%d tested against checksum[%d]=%d)' % (self.z, k, self.checksum[k]))
                return False

        return True


class Communicator(QObject):
    ok = pyqtSignal()
    ko = pyqtSignal()


class ActivationWidget(QWidget):
    __doc__ = 'docstring for ActivationWidget'

    def __init__(self):
        super(ActivationWidget, self).__init__()
        self.activator = Activator()
        self.c = Communicator()
        self.le_parts = []
        self.init_ui()

    def init_ui(self):
        btn_validate = QPushButton('Ok', self)
        btn_cancel = QPushButton('Cancel', self)
        le_code_part_1 = QLineEdit(self)
        le_code_part_2 = QLineEdit(self)
        le_code_part_3 = QLineEdit(self)
        le_code_part_4 = QLineEdit(self)
        le_code_part_5 = QLineEdit(self)
        le_code_part_6 = QLineEdit(self)
        lab_instructions = QLabel('Enter a valid activation key:')
        self.le_parts.append(le_code_part_1)
        self.le_parts.append(le_code_part_2)
        self.le_parts.append(le_code_part_3)
        self.le_parts.append(le_code_part_4)
        self.le_parts.append(le_code_part_5)
        self.le_parts.append(le_code_part_6)
        for le in self.le_parts:
            le.setMaxLength(6)
            le.setPlaceholderText('XXXXXX')

        input_field_layout = QHBoxLayout()
        btns_layout = QHBoxLayout()
        main_layout = QVBoxLayout()
        input_field_layout.addWidget(le_code_part_1)
        input_field_layout.addWidget(QLabel('-'))
        input_field_layout.addWidget(le_code_part_2)
        input_field_layout.addWidget(QLabel('-'))
        input_field_layout.addWidget(le_code_part_3)
        input_field_layout.addWidget(QLabel('-'))
        input_field_layout.addWidget(le_code_part_4)
        input_field_layout.addWidget(QLabel('-'))
        input_field_layout.addWidget(le_code_part_5)
        input_field_layout.addWidget(QLabel('-'))
        input_field_layout.addWidget(le_code_part_6)
        btns_layout.addWidget(btn_validate)
        btns_layout.addWidget(btn_cancel)
        main_layout.addWidget(lab_instructions)
        main_layout.addLayout(input_field_layout)
        main_layout.addLayout(btns_layout)
        self.setWindowTitle('CCTV Manager Activation')
        self.setLayout(main_layout)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        btn_validate.clicked.connect(self.btn_ok_clicked)
        btn_cancel.clicked.connect(self.btn_ko_clicked)

    def btn_ok_clicked(self):
        s = ''
        for le in self.le_parts:
            s += le.text()
            s += '-'

        s = s[:-1]
        if self.activator.activate(s.upper()):
            self.c.ok.emit()
        else:
            self.c.ko.emit()
        self.close()

    def btn_ko_clicked(self):
        self.c.ko.emit()
        self.close()


class ActivatedWidget(QWidget):
    __doc__ = 'docstring for ActivatedWidget'

    def __init__(self):
        super(ActivatedWidget, self).__init__()
        self.lab_result = None
        self.yek = [
         5, 202, 234, 95,
         76, 173, 96, 10,
         232, 7, 146, 79,
         111, 147, 145, 13]
        self.vei = [
         175, 161, 61, 70,
         144, 218, 0, 50,
         73, 173, 240, 202,
         184, 17, 148, 2]
        self.cne = [
         253, 14, 187, 117,
         252, 19, 15, 86,
         196, 138, 67, 165,
         142, 237, 112, 47,
         154, 189, 33, 75,
         195, 205, 10, 56,
         3, 230, 180, 147,
         134, 27, 143, 15,
         250, 19, 235, 96,
         231, 5, 74, 83,
         136, 149, 79, 170,
         136, 252, 113, 112,
         223, 248, 33, 119,
         206, 218, 79, 121,
         9, 225, 253, 156,
         136, 26, 146, 93,
         188, 94, 170, 79,
         184, 87, 102, 61,
         178, 167, 20, 231,
         132, 253, 106, 38,
         141, 224, 112, 98,
         171, 153, 50, 89,
         5, 194, 181, 247,
         137, 23, 139, 31,
         251, 89, 169, 89,
         198, 127, 97, 10,
         170, 246, 105, 197,
         226, 128, 30, 22]
        self.init_ui()

    def init_ui(self):
        btn_validate = QPushButton('Ok', self)
        self.lab_result = QLabel('')
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.lab_result)
        main_layout.addWidget(btn_validate)
        self.setWindowTitle('CCTV Manager Activation Result')
        self.setLayout(main_layout)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        btn_validate.clicked.connect(self.terminate)

    def activation_passed(self):
        self.lab_result.setText('Activation is a success !\n%s' % self.finalize())
        self.show()

    def activation_failed(self):
        print("{}".format(self.finalize())) #直接在失败处输出flag就好了！！
        self.lab_result.setText('Activation failed, please try again...')
        self.show()

    def terminate(self):
        self.close()
        QApplication.quit()

    def finalize(self):
        clear = ''
        buf = self.cne
        key = self.yek
        iv = self.vei
        buf_sz = len(buf)
        bsize = 16
        for i in range(0, int(buf_sz / bsize)):
            for j in range(0, bsize):
                c = buf[(i * bsize + j)] ^ key[j] ^ iv[j]
                iv[j] = buf[(i * bsize + j)]
                buf[i * bsize + j] = c

        i = buf[(buf_sz - 1)]
        for j in range(0, i):
            buf[buf_sz - 1 - j] = 0

        for i in range(0, buf_sz):
            if buf[i] == 0:
                break
            clear += chr(buf[i])

        return clear


class Main(object):
    __doc__ = 'docstring for Main'

    def __init__(self):
        super(Main, self).__init__()
        self.app = QApplication(sys.argv)
        self.icon = QIcon('resources/cctv_logo.png')
        self.activation = ActivationWidget()
        self.activated = ActivatedWidget()
        self.activation.setWindowIcon(self.icon)
        self.activation.setWindowIcon(self.icon)
        self.activation.c.ok.connect(self.activated.activation_passed)
        self.activation.c.ko.connect(self.activated.activation_failed)

    def exec(self):
        self.activation.show()
        return self.app.exec_()


def sigint_handler(*args):
    """Handler for the SIGINT signal."""
    sys.stderr.write('\r')
    if QMessageBox.question(None, '', 'Are you sure you want to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
        QApplication.quit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)
    m = Main()
    exit(m.exec())