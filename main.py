from PyQt5 import QtWidgets
from Design import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
import sys
from IPython.display import Audio
import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
import soundfile as sf
import enum
import pygame, pygame.sndarray
import time, random
import scipy.signal
import sys, os

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.SAMPLE_RATE = 48000
        self.length = 500
        self.DAMPING = 0.999
        self.Flag_String1=0
        self.Flag_String2=0
        self.Flag_String3=0
        self.Flag_String4=0
        self.Flag_String5=0
        self.Flag_String6=0
        self.Clear_All()
        self.ui.String1_Button.clicked.connect(lambda: self.pushbutton(0))
        self.ui.String2_Button.clicked.connect(lambda: self.pushbutton(1))
        self.ui.String3_Button.clicked.connect(lambda: self.pushbutton(2))
        self.ui.String4_Button.clicked.connect(lambda: self.pushbutton(3))
        self.ui.String5_Button.clicked.connect(lambda: self.pushbutton(4))
        self.ui.String6_Button.clicked.connect(lambda: self.pushbutton(5))
        self.ui.Major_checkBox.stateChanged.connect(self.Chords)
        self.ui.Minor_checkBox.stateChanged.connect(self.Chords)

        self.ui.A_Button.clicked.connect(self.Chords)
        self.ui.B_Button.clicked.connect(self.Chords)
        self.ui.C_Button.clicked.connect(self.Chords)
        self.ui.D_Button.clicked.connect(self.Chords)
        self.ui.E_Button.clicked.connect(self.Chords)
        self.ui.F_Button.clicked.connect(self.Chords)
        self.ui.G_Button.clicked.connect(self.Chords)

        self.SubSubContra = self.octave(-1)
        self.SubContra = self.octave(0)
        self.Contra = self.octave(1)
        self.Great = self.octave(2)
        self.Small = self.octave(3)
        self.OneLined = self.octave(4)
        self.TwoLined = self.octave(5)
        self.ThreeLined = self.octave(6)
        self.FourLined = self.octave(7)
        self.FiveLined = self.octave(8)
        self.SixLined = self.octave(9)

        self.ui.White_Button_1.clicked.connect(lambda:  self.play_for(self.sine_wave(261.6256), 1))
        self.ui.Black_Button_2.clicked.connect(lambda:  self.play_for(self.sine_wave(277.1826), 2))
        self.ui.White_Button_3.clicked.connect(lambda:  self.play_for(self.sine_wave(293.6648), 3))
        self.ui.Black_Button_4.clicked.connect(lambda:  self.play_for(self.sine_wave(311.1270), 4))
        self.ui.White_Button_5.clicked.connect(lambda:  self.play_for(self.sine_wave(329.6276), 5))
        self.ui.White_Button_6.clicked.connect(lambda:  self.play_for(self.sine_wave(349.2282), 6))
        self.ui.Black_Button_7.clicked.connect(lambda:  self.play_for(self.sine_wave(369.9944), 7))
        self.ui.White_Button_8.clicked.connect(lambda:  self.play_for(self.sine_wave(391.9954), 8))
        self.ui.Black_Button_9.clicked.connect(lambda:  self.play_for(self.sine_wave(415.3047), 9))
        self.ui.White_Button_10.clicked.connect(lambda: self.play_for(self.sine_wave(440.0000), 10))
        self.ui.Black_Button_11.clicked.connect(lambda: self.play_for(self.sine_wave(466.1638), 11))
        self.ui.White_Button_12.clicked.connect(lambda: self.play_for(self.sine_wave(493.8833), 12))
        self.ui.White_Button_13.clicked.connect(lambda: self.play_for(self.sine_wave(523.2511), 13))
        self.ui.Black_Button_14.clicked.connect(lambda: self.play_for(self.sine_wave(554.3653), 14))
        self.ui.White_Button_15.clicked.connect(lambda: self.play_for(self.sine_wave(587.3295), 15))
        self.ui.Black_Button_16.clicked.connect(lambda: self.play_for(self.sine_wave(622.2540), 16))
        self.ui.White_Button_17.clicked.connect(lambda: self.play_for(self.sine_wave(659.2551), 17))
        self.ui.White_Button_18.clicked.connect(lambda: self.play_for(self.sine_wave(698.4565), 18))
        self.ui.Black_Button_19.clicked.connect(lambda: self.play_for(self.sine_wave(739.9888), 19))
        self.ui.White_Button_20.clicked.connect(lambda: self.play_for(self.sine_wave(783.9909), 20))
        self.ui.Black_Button_21.clicked.connect(lambda: self.play_for(self.sine_wave(830.6094), 21))
        self.ui.White_Button_22.clicked.connect(lambda: self.play_for(self.sine_wave(880.0000), 22))
        self.ui.Black_Button_23.clicked.connect(lambda: self.play_for(self.sine_wave(932.3275), 23))
        self.ui.White_Button_24.clicked.connect(lambda: self.play_for(self.sine_wave(987.7666), 24))
        self.ui.White_Button_25.clicked.connect(lambda: self.play_for(self.sine_wave(1046.502), 25))
        self.ui.Black_Button_26.clicked.connect(lambda: self.play_for(self.sine_wave(1108.731), 26))
        self.ui.White_Button_27.clicked.connect(lambda: self.play_for(self.sine_wave(1174.659), 27))
        self.ui.Black_Button_28.clicked.connect(lambda: self.play_for(self.sine_wave(1244.508), 28))
        self.ui.White_Button_29.clicked.connect(lambda: self.play_for(self.sine_wave(1318.510), 29))
        self.ui.White_Button_30.clicked.connect(lambda: self.play_for(self.sine_wave(1396.913), 30))
        self.ui.Black_Button_31.clicked.connect(lambda: self.play_for(self.sine_wave(1479.978), 31))
        self.ui.White_Button_32.clicked.connect(lambda: self.play_for(self.sine_wave(1567.982), 32))
        self.ui.Black_Button_33.clicked.connect(lambda: self.play_for(self.sine_wave(1661.219), 33))
        self.ui.White_Button_34.clicked.connect(lambda: self.play_for(self.sine_wave(1760.000), 34))
        self.ui.White_Button_35.clicked.connect(lambda: self.play_for(self.sine_wave(1864.655), 35))
        self.ui.White_Button_36.clicked.connect(lambda: self.play_for(self.sine_wave(1975.533), 36))
        self.ui.White_Button_37.clicked.connect(lambda: self.play_for(self.sine_wave(2093.005), 37))


    def Clear_All(self):
            self.ui.Fret1_String1.setVisible(0)
            self.ui.Fret1_String2.setVisible(0)
            self.ui.Fret1_String3.setVisible(0)
            self.ui.Fret1_String4.setVisible(0)
            self.ui.Fret1_String5.setVisible(0)
            self.ui.Fret1_String6.setVisible(0)
            self.ui.Fret2_String1.setVisible(0)
            self.ui.Fret2_String2.setVisible(0)
            self.ui.Fret2_String3.setVisible(0)
            self.ui.Fret2_String4.setVisible(0)
            self.ui.Fret2_String5.setVisible(0)
            self.ui.Fret2_String6.setVisible(0)
            self.ui.Fret3_String1.setVisible(0)
            self.ui.Fret3_String2.setVisible(0)
            self.ui.Fret3_String3.setVisible(0)
            self.ui.Fret3_String4.setVisible(0)
            self.ui.Fret3_String5.setVisible(0)
            self.ui.Fret3_String6.setVisible(0)
            self.ui.Fret4_String1.setVisible(0)
            self.ui.Fret4_String2.setVisible(0)
            self.ui.Fret4_String3.setVisible(0)
            self.ui.Fret4_String4.setVisible(0)
            self.ui.Fret4_String5.setVisible(0)
            self.ui.Fret4_String6.setVisible(0)
            self.ui.Fret5_String1.setVisible(0)
            self.ui.Fret5_String2.setVisible(0)
            self.ui.Fret5_String3.setVisible(0)
            self.ui.Fret5_String4.setVisible(0)
            self.ui.Fret5_String5.setVisible(0)
            self.ui.Fret5_String6.setVisible(0)


    def octave(self, order):
        """Create an enum of all the notes in the octave
        of the given order.
        """
        frequency_of_A = 440 * 2 ** (order - 4)

        class Octave(enum.Enum):
            C = -9
            C_sharp = -8
            D_flat = -8
            D = -7
            D_sharp = -6
            E_flat = -6
            E = -5
            F = -4
            F_sharp = -3
            G_flat = -3
            G = -2
            G_sharp = -1
            A_flat = -1
            A = 0
            A_sharp = 1
            B_flat = 1
            B = 2
            C_flat = 2
            def __float__(self):
                return 2 ** (self.value / 12) * frequency_of_A

        return Octave


    def karplusStrong(self, frequency, volume, duration):

        samples_count = duration * self.SAMPLE_RATE
        N = int(self.SAMPLE_RATE / frequency)
        buf = np.random.rand(N) * 2 - 1
        samples = np.empty(samples_count, dtype=float)

        for i in range(samples_count):
            samples[i] = buf[i % N]
            avg = self.DAMPING * 0.5 * (buf[i % N] + buf[(1 + i) % N])
            buf[i % N] = avg

        return samples * volume

    def generate_chord(self, frequencies, duration, volume=0.5):
        notes = map(float, frequencies)
        plucks = (self.karplusStrong(note, volume, duration) for note in notes)
        return np.sum(plucks, axis=0)

    def pushbutton(self, index):
        SAMPLE_RATE = 48000
        if index==0:
           if self.Flag_String1 ==0: #82.41
                A_major = [self.Great.E]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String1_Fret0.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
           elif self.Flag_String1==1: #87.31
               A_major = [self.Great.F]
               strum = self.generate_chord(A_major, duration=2)

               filename = "String1_Fret1.wav"
               write(filename, self.SAMPLE_RATE, strum)
               data, SAMPLERATE = sf.read(filename, dtype='float32')
               sd.play(data, SAMPLERATE)
           elif self.Flag_String1==3: #98
               A_major = [self.Great.G]
               strum = self.generate_chord(A_major, duration=2)

               filename = "String1_Fret3.wav"
               write(filename, self.SAMPLE_RATE, strum)
               data, SAMPLERATE = sf.read(filename, dtype='float32')
               sd.play(data, SAMPLERATE)

        elif index==1:

           if self.Flag_String2==0:
                A_major = [self.Great.A]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String2_Fret0.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
           elif self.Flag_String2==1: #116.54
               A_major = [self.Small.A_sharp]
               strum = self.generate_chord(A_major, duration=2)

               filename = "String2_Fret1.wav"
               write(filename, self.SAMPLE_RATE, strum)
               data, SAMPLERATE = sf.read(filename, dtype='float32')
               sd.play(data, SAMPLERATE)
           elif self.Flag_String2==2: #123.47
               A_major = [self.Small.B]
               strum = self.generate_chord(A_major, duration=2)

               filename = "String2_Fret2.wav"
               write(filename, self.SAMPLE_RATE, strum)
               data, SAMPLERATE = sf.read(filename, dtype='float32')
               sd.play(data, SAMPLERATE)
           elif self.Flag_String2==3: #130.81
               A_major = [self.Small.C]
               strum = self.generate_chord(A_major, duration=2)

               filename = "String2_Fret3.wav"
               write(filename, self.SAMPLE_RATE, strum)
               data, SAMPLERATE = sf.read(filename, dtype='float32')
               sd.play(data, SAMPLERATE)
        elif index==2:
            if self.Flag_String3==0: #146.83
                A_major = [self.Small.D]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String3_Fret0.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
            elif self.Flag_String3==2: #164.81
                A_major = [self.Small.E]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String3_Fret2.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
            elif self.Flag_String3 == 3: #174.61
                A_major = [self.Small.F]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String3_Fret3.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
            elif self.Flag_String3 == 4:#185
                A_major = [self.Small.F_sharp]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String3_Fret4.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
            elif self.Flag_String3 == 5: #196
                A_major = [self.Small.G]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String3_Fret5.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
        elif index==3:
             if self.Flag_String4==0:
                A_major = [self.Small.G]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String4_Fret0.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
             elif self.Flag_String4==1: #207.65
                A_major = [self.Small.G_sharp]
                strum = self.generate_chord(A_major, duration=2)
                filename = "String4_Fret1.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
             elif self.Flag_String4 == 2: #220
                A_major = [self.Small.A]
                strum = self.generate_chord(A_major, duration=2)
                filename = "String4_Fret2.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
             elif self.Flag_String4==4:#246.94
                A_major = [self.Small.B]
                strum = self.generate_chord(A_major, duration=2)
                filename = "String4_Fret4.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
             elif self.Flag_String4==5: #261.63
                A_major = [self.OneLined.C]
                strum = self.generate_chord(A_major, duration=2)
                filename = "String4_Fret5.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)

        elif index==4:
              if self.Flag_String5==0:
                A_major = [self.Small.B]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String5_Fret0.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
              elif self.Flag_String5==1: #261.63
                A_major = [self.OneLined.C]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String5_Fret1.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
              elif self.Flag_String5==2: #277.18
                A_major = [self.OneLined.C_sharp]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String5_Fret2.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
              elif self.Flag_String5==3: #293.66
                A_major = [self.OneLined.D]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String5_Fret3.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
              elif self.Flag_String5==4: #311.13
                A_major = [self.OneLined.D_sharp]
                strum = self.generate_chord(A_major, duration=2)

                filename = "String5_Fret4.wav"
                write(filename, self.SAMPLE_RATE, strum)
                data, SAMPLERATE = sf.read(filename, dtype='float32')
                sd.play(data, SAMPLERATE)
        elif index==5:
               if self.Flag_String6==0: #329.11
                    A_major = [self.OneLined.E]
                    strum = self.generate_chord(A_major, duration=2)

                    filename = "String6_Fret0.wav"
                    write(filename, self.SAMPLE_RATE, strum)
                    data, SAMPLERATE = sf.read(filename, dtype='float32')
                    sd.play(data, SAMPLERATE)
               elif self.Flag_String6 == 1: #349.23
                   A_major = [self.OneLined.F]
                   strum = self.generate_chord(A_major, duration=2)

                   filename = "String6_Fret1.wav"
                   write(filename, self.SAMPLE_RATE, strum)
                   data, SAMPLERATE = sf.read(filename, dtype='float32')
                   sd.play(data, SAMPLERATE)
               elif self.Flag_String6 == 2: #369.99
                   A_major = [self.OneLined.G_flat]
                   strum = self.generate_chord(A_major, duration=2)

                   filename = "String6_Fret2.wav"
                   write(filename, self.SAMPLE_RATE, strum)
                   data, SAMPLERATE = sf.read(filename, dtype='float32')
                   sd.play(data, SAMPLERATE)
               elif self.Flag_String6 == 3: #392
                   A_major = [self.OneLined.G]
                   strum = self.generate_chord(A_major, duration=2)

                   filename = "String6_Fret3.wav"
                   write(filename, self.SAMPLE_RATE, strum)
                   data, SAMPLERATE = sf.read(filename, dtype='float32')
                   sd.play(data, SAMPLERATE)


    def Chords(self):

        if self.ui.Major_checkBox.isChecked():
            self.ui.Minor_checkBox.setChecked(0)
            if self.ui.A_Button.isChecked():
                self.Clear_All()
                self.ui.Fret2_String3.setVisible(1)
                self.ui.Fret2_String4.setVisible(1)
                self.ui.Fret2_String5.setVisible(1)
                self.Flag_String3=2
                self.Flag_String4 = 2
                self.Flag_String5=2
            elif self.ui.B_Button.isChecked():
                self.Clear_All()
                self.ui.Fret2_String2.setVisible(1)
                self.ui.Fret2_String6.setVisible(1)
                self.ui.Fret4_String3.setVisible(1)
                self.ui.Fret4_String4.setVisible(1)
                self.ui.Fret4_String5.setVisible(1)
                self.Flag_String2=2
                self.Flag_String6=2
                self.Flag_String4=4
                self.Flag_String5=4
            elif self.ui.C_Button.isChecked():
                self.Clear_All()
                self.ui.Fret1_String5.setVisible(1)
                self.ui.Fret2_String3.setVisible(1)
                self.ui.Fret3_String1.setVisible(1)
                self.ui.Fret3_String2.setVisible(1)
                self.Flag_String5=1
                self.Flag_String3=2
                self.Flag_String1=3
                self.Flag_String2=3
            elif self.ui.D_Button.isChecked():
                self.Clear_All()
                self.ui.Fret2_String4.setVisible(1)
                self.ui.Fret2_String6.setVisible(1)
                self.ui.Fret3_String5.setVisible(1)
                self.Flag_String4=2
                self.Flag_String6=2
                self.Flag_String5=3
            elif self.ui.E_Button.isChecked():
                self.Clear_All()
                self.ui.Fret1_String4.setVisible(1)
                self.ui.Fret2_String2.setVisible(1)
                self.ui.Fret2_String3.setVisible(1)
                self.Flag_String4=1
                self.Flag_String2=2
                self.Flag_String3=2
            elif self.ui.F_Button.isChecked():
                self.Clear_All()
                self.ui.Fret1_String1.setVisible(1)
                self.ui.Fret1_String5.setVisible(1)
                self.ui.Fret1_String6.setVisible(1)
                self.ui.Fret2_String4.setVisible(1)
                self.ui.Fret3_String2.setVisible(1)
                self.ui.Fret3_String3.setVisible(1)
                self.Flag_String1=1
                self.Flag_String5=1
                self.Flag_String6=1
                self.Flag_String4=2
                self.Flag_String2=3
                self.Flag_String3=3
            elif self.ui.G_Button.isChecked():
                self.Clear_All()
                self.ui.Fret2_String2.setVisible(1)
                self.ui.Fret3_String1.setVisible(1)
                self.ui.Fret3_String6.setVisible(1)
                self.Flag_String2=2
                self.Flag_String1=3
                self.Flag_String6=3
        elif self.ui.Minor_checkBox.isChecked():
            self.ui.Major_checkBox.setChecked(0)
            if self.ui.A_Button.isChecked():
                self.Clear_All()
                self.ui.Fret1_String5.setVisible(1)
                self.ui.Fret2_String3.setVisible(1)
                self.ui.Fret2_String4.setVisible(1)
                self.Flag_String5=1
                self.Flag_String3=2
                self.Flag_String4=2
            elif self.ui.B_Button.isChecked():
                self.Clear_All()
                self.ui.Fret2_String2.setVisible(1)
                self.ui.Fret2_String6.setVisible(1)
                self.ui.Fret3_String5.setVisible(1)
                self.ui.Fret4_String3.setVisible(1)
                self.ui.Fret4_String4.setVisible(1)
                self.Flag_String2=2
                self.Flag_String6=2
                self.Flag_String5=3
                self.Flag_String3=4
                self.Flag_String4=4
            elif self.ui.C_Button.isChecked():
                self.Clear_All()
                self.ui.Fret3_String1.setVisible(1)
                self.ui.Fret3_String2.setVisible(1)
                self.ui.Fret3_String6.setVisible(1)
                self.ui.Fret4_String5.setVisible(1)
                self.ui.Fret5_String3.setVisible(1)
                self.ui.Fret5_String4.setVisible(1)
                self.Flag_String1=3
                self.Flag_String2=3
                self.Flag_String6=3
                self.Flag_String5=4
                self.Flag_String3=5
                self.Flag_String4=5
            elif self.ui.D_Button.isChecked():
                self.Clear_All()
                self.ui.Fret1_String6.setVisible(1)
                self.ui.Fret2_String4.setVisible(1)
                self.ui.Fret3_String5.setVisible(1)
                self.Flag_String6=1
                self.Flag_String4=2
                self.Flag_String5=3
            elif self.ui.E_Button.isChecked():
                self.Clear_All()
                self.ui.Fret2_String2.setVisible(1)
                self.ui.Fret2_String3.setVisible(1)
                self.Flag_String2=2
                self.Flag_String3=2
            elif self.ui.F_Button.isChecked():
                self.Clear_All()
                self.ui.Fret1_String1.setVisible(1)
                self.ui.Fret1_String4.setVisible(1)
                self.ui.Fret1_String5.setVisible(1)
                self.ui.Fret1_String6.setVisible(1)
                self.ui.Fret3_String2.setVisible(1)
                self.ui.Fret3_String3.setVisible(1)
                self.Flag_String1=1
                self.Flag_String4=1
                self.Flag_String5=1
                self.Flag_String6=1
                self.Flag_String2=3
                self.Flag_String3=3
            elif self.ui.G_Button.isChecked():
                self.Clear_All()
                self.ui.Fret3_String1.setVisible(1)
                self.ui.Fret3_String5.setVisible(1)
                self.ui.Fret3_String6.setVisible(1)
                self.ui.Fret1_String2.setVisible(1)
                self.Flag_String1=3
                self.Flag_String5=3
                self.Flag_String6=3
                self.Flag_String2=1
        else:
            self.Clear_All()



######################################################################
############################Piano#####################################
######################################################################

    def sine_wave(self, hz, peak=4096, n_samples=48000):
        """Compute N samples of a sine wave with given frequency and peak amplitude.
           Defaults to one second.
        """
        length = self.SAMPLE_RATE / float(hz)
        omega = np.pi * 2 / length
        xvalues = np.arange(int(length)) * omega
        onecycle = peak * np.sin(xvalues)
        return np.resize(onecycle, (n_samples,)).astype(np.int16)

    def play_for(self, sample_wave, index):
        """Play given samples, as a sound, for ms milliseconds."""

        filename = "Button%d.wav" %index
        write(filename, self.SAMPLE_RATE, sample_wave)
        data, SAMPLERATE = sf.read(filename, dtype='float32')
        sd.play(data, SAMPLERATE)

def main():
     app = QtWidgets.QApplication(sys.argv)
     application = ApplicationWindow()
     application.show()
     app.exec_()

if __name__ == "__main__":
    main()





