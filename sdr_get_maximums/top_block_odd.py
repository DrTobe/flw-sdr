#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block Odd
# Generated: Wed Jul 25 17:04:54 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from max_receive_power import max_receive_power  # grc-generated hier_block
from max_to_zmq_pub import max_to_zmq_pub  # grc-generated hier_block
from optparse import OptionParser
import sip
import time


class top_block_odd(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block Odd")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block Odd")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block_odd")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.keep_one_in_n = keep_one_in_n = 50
        self.gain = gain = 0
        self.fftlen = fftlen = 1024
        self.f0 = f0 = 2405.1e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0_3 = uhd.usrp_source(
        	"ip_addr=192.168.10.5",
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_3.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_3.set_center_freq(f0, 0)
        self.uhd_usrp_source_0_3.set_gain(gain, 0)
        self.uhd_usrp_source_0_3.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0_1 = uhd.usrp_source(
        	"ip_addr=192.168.10.3",
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_1.set_center_freq(f0, 0)
        self.uhd_usrp_source_0_1.set_gain(gain, 0)
        self.uhd_usrp_source_0_1.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("ip_addr=192.168.10.1", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(f0, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.max_to_zmq_pub_1_3 = max_to_zmq_pub(
            zmq_socket_addr="tcp://*:4445",
        )
        self.max_to_zmq_pub_1_1 = max_to_zmq_pub(
            zmq_socket_addr="tcp://*:4443",
        )
        self.max_to_zmq_pub_1 = max_to_zmq_pub(
            zmq_socket_addr="tcp://*:4441",
        )
        self.max_receive_power_0_3 = max_receive_power(
            fftlen=fftlen,
            keep_one_in_n=keep_one_in_n,
        )
        self.max_receive_power_0_1 = max_receive_power(
            fftlen=fftlen,
            keep_one_in_n=keep_one_in_n,
        )
        self.max_receive_power_0 = max_receive_power(
            fftlen=fftlen,
            keep_one_in_n=keep_one_in_n,
        )

        ##################################################
        # Connections
        ##################################################
<<<<<<< HEAD
        self.connect((self.max_receive_power_0, 0), (self.max_to_zmq_pub_1, 0))
        self.connect((self.max_receive_power_0, 1), (self.max_to_zmq_pub_1, 1))
        self.connect((self.max_receive_power_0_1, 0), (self.max_to_zmq_pub_1_1, 0))
        self.connect((self.max_receive_power_0_1, 1), (self.max_to_zmq_pub_1_1, 1))
        self.connect((self.max_receive_power_0_3, 0), (self.max_to_zmq_pub_1_3, 0))
        self.connect((self.max_receive_power_0_3, 1), (self.max_to_zmq_pub_1_3, 1))
        self.connect((self.uhd_usrp_source_0, 0), (self.max_receive_power_0, 0))
        self.connect((self.uhd_usrp_source_0_1, 0), (self.max_receive_power_0_1, 0))
        self.connect((self.uhd_usrp_source_0_3, 0), (self.max_receive_power_0_3, 0))
=======
        self.connect((self.max_receive_power_0, 0), (self.max_to_zmq_pub_1, 0))    
        self.connect((self.max_receive_power_0, 1), (self.max_to_zmq_pub_1, 1))    
        self.connect((self.max_receive_power_0_1, 0), (self.max_to_zmq_pub_1_1, 0))    
        self.connect((self.max_receive_power_0_1, 1), (self.max_to_zmq_pub_1_1, 1))    
        self.connect((self.max_receive_power_0_3, 0), (self.max_to_zmq_pub_1_3, 0))    
        self.connect((self.max_receive_power_0_3, 1), (self.max_to_zmq_pub_1_3, 1))    
        self.connect((self.uhd_usrp_source_0, 0), (self.max_receive_power_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.uhd_usrp_source_0_1, 0), (self.max_receive_power_0_1, 0))    
        self.connect((self.uhd_usrp_source_0_3, 0), (self.max_receive_power_0_3, 0))    
>>>>>>> 8e08dda... Publish newest state of top_block_odd (used on cardinal).

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block_odd")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_3.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
<<<<<<< HEAD
=======
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
>>>>>>> 8e08dda... Publish newest state of top_block_odd (used on cardinal).

    def get_keep_one_in_n(self):
        return self.keep_one_in_n

    def set_keep_one_in_n(self, keep_one_in_n):
        self.keep_one_in_n = keep_one_in_n
        self.max_receive_power_0.set_keep_one_in_n(self.keep_one_in_n)
        self.max_receive_power_0_1.set_keep_one_in_n(self.keep_one_in_n)
        self.max_receive_power_0_3.set_keep_one_in_n(self.keep_one_in_n)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0_1.set_gain(self.gain, 0)

        self.uhd_usrp_source_0_3.set_gain(self.gain, 0)
<<<<<<< HEAD

        self.uhd_usrp_source_0.set_gain(self.gain, 0)

=======
        	
        self.uhd_usrp_source_0.set_gain(self.gain, 0)
        	
>>>>>>> 8e08dda... Publish newest state of top_block_odd (used on cardinal).

    def get_fftlen(self):
        return self.fftlen

    def set_fftlen(self, fftlen):
        self.fftlen = fftlen
        self.max_receive_power_0.set_fftlen(self.fftlen)
        self.max_receive_power_0_1.set_fftlen(self.fftlen)
        self.max_receive_power_0_3.set_fftlen(self.fftlen)

    def get_f0(self):
        return self.f0

    def set_f0(self, f0):
        self.f0 = f0
        self.uhd_usrp_source_0_1.set_center_freq(self.f0, 0)
        self.uhd_usrp_source_0_3.set_center_freq(self.f0, 0)
        self.uhd_usrp_source_0.set_center_freq(self.f0, 0)


def main(top_block_cls=top_block_odd, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
