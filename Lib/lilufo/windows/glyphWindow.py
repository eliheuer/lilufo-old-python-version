# Started as a fork from: https://github.com/expectocode/captivox

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from math import sin, cos, radians
from time import sleep
from PyQt5.QtGui import QPainter, QPalette, QPen, QColor, QBrush, QIcon
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QFormLayout,
                             QSizePolicy, QSlider, QLabel,
                             QPushButton, QCheckBox, QFileDialog, QMessageBox,
                             QProgressDialog, QColorDialog)
from PyQt5.QtCore import (QSize, QTimer, QPointF, Qt, QLineF, QByteArray,
                          QBuffer, QIODevice)

# DEFAULT VALUES FOR GLYPH EDITOR #############################
X_MULT_DEF = 1
Y_MULT_DEF = 1
DOT_SIZE_DEF = 32
NUM_DOTS_DEF = 16
ANGLE_FACTOR_DEF = 360
HALFMAX_DEF = 180
SPEED_MULT_DEF = 2
DELAY_DEF = 35
AXES_DEF = True
JOIN_ENDS_DEF = False
DRAW_AXES_DEF = False
COL1_DEF = QColor("#ffff22")
COL2_DEF = QColor("#ff2211")
LINES_DEF = False
CONNECT_LINES_DEF = False

# This value allows "using" floating point values on the slider by
# multiplying the maximum by it, and then dividing whatever value.
SIDE_MULT_PRECISION = 100
SIDE_MULT_FMT = '{:.2f}'

class DotsWidget(QWidget):
    """A custom widget for animating dots"""
    def __init__(self):
        super().__init__()
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor("#999999"))
        self.setPalette(pal)
        self.setAutoFillBackground(True)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.frame_no = 1
        self.angle_factor = ANGLE_FACTOR_DEF  # related to degrees offset of each dot
        self.num_dots = NUM_DOTS_DEF
        self.dot_size = DOT_SIZE_DEF
        self.x_multiplier = X_MULT_DEF
        self.y_multiplier = Y_MULT_DEF
        self.halfmax = HALFMAX_DEF
        self.speedmult = SPEED_MULT_DEF
        self.draw_axes = AXES_DEF
        self.join_end_dots = JOIN_ENDS_DEF
        self.col1 = COL1_DEF
        self.col2 = COL2_DEF
        self.draw_lines = LINES_DEF
        self.connect_lines = CONNECT_LINES_DEF

    def minimumSizeHint(self):
        """Must be implemented"""
        return QSize(50, 50)

    def sizeHint(self):
        """Must be implemented"""
        return QSize(400, 400)

    def _try_update_frame(self):
        """Updates to the next animation frame if speedmult is 0"""
        if self.parent().speedmult_slider.value() == 0:
            self.frame_no -= 1
            self.next_animation_frame()

    def change_angle_factor(self, value):
        """Take slider input and reflect the new value in the label"""
        self.parent().a_f_slider_val_label.setText(str(value))
        self.angle_factor = value
        self._try_update_frame()

    def change_halfmax(self, value):
        """Take slider input and reflect the new value in the label"""
        self.parent().halfmax_slider_val_label.setText(str(value))
        self.halfmax = value
        self._try_update_frame()

    def change_speedmult(self, value):
        """Take slider input and reflect the new value in the label"""
        self.parent().speedmult_slider_val_label.setText(str(value))
        if value == 0:
            self.timer.stop()
            self._try_update_frame()
            return
        if not self.timer.isActive():
            # it's going from zero to nonzero
            self.timer.start(self.parent().delay_slider.value())

        self.speedmult = value
        # if self.parent().framerate_slider.value() == 0:

    def change_draw_axes(self, value):
        """Take checkbox input"""
        self.draw_axes = value
        self._try_update_frame()

    def change_join_end_dots(self, value):
        """Take checkbox input"""
        self.join_end_dots = value
        self._try_update_frame()

    def change_num_dots(self, value):
        """Take slider input and reflect the new value in the label"""
        self.parent().num_dots_slider_val_label.setText(str(value))
        self.num_dots = value
        self._try_update_frame()

    def change_dot_size(self, value):
        """Take slider input and reflect the new value in the label"""
        self.parent().dot_size_slider_val_label.setText(str(value))
        self.dot_size = value
        self._try_update_frame()

    def change_x_multiplier(self, value):
        """Take slider input and reflect the new value in the label"""
        value /= SIDE_MULT_PRECISION
        self.parent().x_multiplier_slider_val_label.setText(SIDE_MULT_FMT.format(value))
        self.x_multiplier = value
        self._try_update_frame()

    def change_y_multiplier(self, value):
        """Take slider input and reflect the new value in the label"""
        value /= SIDE_MULT_PRECISION
        self.parent().y_multiplier_slider_val_label.setText(SIDE_MULT_FMT.format(value))
        self.y_multiplier = value
        self._try_update_frame()

    def change_lines_state(self, value):
        """Take checkbox input"""
        self.draw_lines = value
        self.parent().connect_lines_checkbox.setEnabled(value)
        self._try_update_frame()

    def change_connect_lines(self, value):
        """Take checkbox input"""
        self.connect_lines = value
        self._try_update_frame()

    def next_animation_frame(self):
        """Connects to the timer to fire the animation"""
        self.update()
        self.frame_no += 1

    def paintEvent(self, *_):
        """
        [TODO] Fix ugly resizes

        This is called on self.update() and on resize.
        This method draws every frame and forms the core of the program.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.translate(self.width() / 2, self.height() / 2)  # Make (0,0) center

        if self.draw_axes:
            painter.setPen(QPen(QColor(0, 0, 0, 64), 1))
            painter.drawLine(QLineF(0, self.height() / 2, 0, -self.height() / 2))
            painter.drawLine(QLineF(self.width() / 2, 0, -self.width() / 2, 0))

        last = None

        for cur_dot_num in range(self.num_dots):

            # [TODO] I have no idea how angle_off is used
            angle_off = radians(self.angle_factor/self.num_dots) * cur_dot_num

            # Set Frame
            frame_no = self.frame_no + cur_dot_num*(180/self.num_dots)/self.speedmult

            green = (240/self.num_dots) * (self.num_dots - cur_dot_num)
            blue = (240/self.num_dots) * cur_dot_num
            colour = QColor(0, green, blue)
            # colour = next(colours).toRgb()
            painter.setPen(QPen(colour))
            painter.setBrush(QBrush(colour))
            progress = abs((frame_no * self.speedmult) % (2*self.halfmax)-self.halfmax)

            # Progress oscillates every 360/speed_mult frames
            # Progress dictates the range of values of x later fed into cos(x)
            # frame_no multiplier dictates frequency of oscillations
            # Progress ranges between 0 and 180 which later gives us a
            # cos(progress) ranging between # 1 and -1, which combines with
            # sometimes-neg wid * hei to give a full range
            print(self.frame_no,progress)

            height = sin(angle_off) * (self.height() - 100)
            width = cos(angle_off) * (self.width() - 100)
            # (0,0) is the centre
            x = cos(radians(self.x_multiplier * progress)) * width / 2
            y = cos(radians(self.y_multiplier * progress)) * height / 2

            if self.draw_lines:
                painter.setPen(QPen(colour, self.dot_size))
                painter.drawLine(QPointF(x, y), QPointF(0,0))
                if self.connect_lines:
                    if last:
                        painter.drawLine(QPointF(x, y), last)
                    last = QPointF(x,y)
            else:
                painter.drawEllipse(QPointF(x, y), self.dot_size, self.dot_size)

class GlyphWindow(QWidget):
    def __init__(self):
        super().__init__(None)

        self.setWindowTitle("Glyph Editor")
        self.setWindowFlags(Qt.Dialog)  # Make it start as floating on tiling WMs

        layout = QVBoxLayout(self)
        self.dotwid = DotsWidget()
        self.dotwid.timer = QTimer(self)
        self.dotwid.timer.timeout.connect(self.dotwid.next_animation_frame)
        layout.addWidget(self.dotwid)
        controls_box = QFormLayout()

        angle_factor_box = QHBoxLayout()
        self.angle_factor_slider = QSlider(Qt.Horizontal)
        self.angle_factor_slider.setMaximum(1080)
        self.angle_factor_slider.setValue(ANGLE_FACTOR_DEF)
        self.a_f_slider_val_label = QLabel(str(self.angle_factor_slider.value()))
        self.angle_factor_slider.valueChanged.connect(self.dotwid.change_angle_factor)
        angle_factor_box.addWidget(self.angle_factor_slider)
        angle_factor_box.addWidget(self.a_f_slider_val_label)
        controls_box.addRow("Slider One", angle_factor_box)

        dot_size_box = QHBoxLayout()
        self.dot_size_slider = QSlider(Qt.Horizontal)
        self.dot_size_slider.setMinimum(1)
        self.dot_size_slider.setMaximum(40)
        self.dot_size_slider.setValue(DOT_SIZE_DEF)
        self.dot_size_slider.valueChanged.connect(self.dotwid.change_dot_size)
        self.dot_size_slider_val_label = QLabel(str(self.dot_size_slider.value()))
        dot_size_box.addWidget(self.dot_size_slider)
        dot_size_box.addWidget(self.dot_size_slider_val_label)
        controls_box.addRow("Slider Two", dot_size_box)

        x_multiplier_box = QHBoxLayout()
        self.x_multiplier_slider = QSlider(Qt.Horizontal)
        self.x_multiplier_slider.setMaximum(10 * SIDE_MULT_PRECISION)
        self.x_multiplier_slider.setValue(X_MULT_DEF * SIDE_MULT_PRECISION)
        self.x_multiplier_slider.valueChanged.connect(self.dotwid.change_x_multiplier)
        self.x_multiplier_slider_val_label = QLabel(SIDE_MULT_FMT.format(X_MULT_DEF))
        x_multiplier_box.addWidget(self.x_multiplier_slider)
        x_multiplier_box.addWidget(self.x_multiplier_slider_val_label)
        controls_box.addRow("Slider Three", x_multiplier_box)

        speedmult_box = QHBoxLayout()
        self.speedmult_slider = QSlider(Qt.Horizontal)
        # self.speedmult_slider.setMinimum(1)
        self.speedmult_slider.setMaximum(12)
        self.speedmult_slider.setValue(SPEED_MULT_DEF)
        self.speedmult_slider.valueChanged.connect(self.dotwid.change_speedmult)
        self.speedmult_slider_val_label = QLabel(str(self.speedmult_slider.value()))
        speedmult_box.addWidget(self.speedmult_slider)
        speedmult_box.addWidget(self.speedmult_slider_val_label)
        controls_box.addRow("Speed", speedmult_box)

        reset_button = QPushButton("Reset values")
        #reset_button.pressed.connect()
        export_button = QPushButton("Export Images")
        #export_button.pressed.connect()

        last_controls = QHBoxLayout()
        last_controls.addStretch()
        last_controls.addWidget(reset_button)
        last_controls.addStretch()
        last_controls.addWidget(export_button)
        controls_box.addRow(last_controls)

        controls_widget = QWidget(self)
        controls_widget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor("#999999"))
        controls_widget.setPalette(pal)
        controls_widget.setAutoFillBackground(False)
        controls_widget.setLayout(controls_box)

        layout.addWidget(controls_widget)
        self.dotwid.timer.start(DELAY_DEF)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("#999999"))
        self.setPalette(p)

    def reset_controls(self):
        """
        Reset all slider controls to their default value
        Also resets animation frame
        """
        self.delay_slider.setValue(DELAY_DEF)
        self.x_multiplier_slider.setValue(X_MULT_DEF * SIDE_MULT_PRECISION)
        self.y_multiplier_slider.setValue(Y_MULT_DEF * SIDE_MULT_PRECISION)
        self.dot_size_slider.setValue(DOT_SIZE_DEF)
        self.num_dots_slider.setValue(NUM_DOTS_DEF)
        self.angle_factor_slider.setValue(ANGLE_FACTOR_DEF)
        self.speedmult_slider.setValue(SPEED_MULT_DEF)
        self.halfmax_slider.setValue(HALFMAX_DEF)
        self.join_end_dots_checkbox.setChecked(JOIN_ENDS_DEF)
        self.draw_axes_checkbox.setChecked(DRAW_AXES_DEF)
        self.dotwid.col1 = COL1_DEF
        pal = self.change_col1_button.palette()
        pal.setColor(QPalette.Button, COL1_DEF)
        self.change_col1_button.setPalette(pal)
        self.dotwid.col2 = COL2_DEF
        pal = self.change_col2_button.palette()
        pal.setColor(QPalette.Button, COL2_DEF)
        self.change_col2_button.setPalette(pal)
        self.lines_checkbox.setChecked(LINES_DEF)
        self.connect_lines_checkbox.setChecked(LINES_DEF)
        self.connect_lines_checkbox.setEnabled(LINES_DEF)
        self.dotwid.frame_no = 1

def main():
    """Run the app"""
    app = QApplication([])
    win = GlyphWindow()
    win.show()
    return app.exec()

if __name__ == '__main__':
    main()
