# -*- coding: utf-8 -*-
import os
import glob
import argparse
import librosa
import soundfile as sf

import numpy as np
import matplotlib.pyplot as plt

#https://www.wizard-notes.com/entry/music-analysis/hpss

class Hpss:
	def __init__(self, input_file, anm="./in/anm/", out="./in/sample/", sr=16000, subtype="PCM_16", out_sec=10, start_point=60):
		self._in_file = input_file
		self._anm_dir = anm
		self._out_dir = out
		self._sample_rate = sr
		self._subtype = subtype
		self._start_point = sr * start_point
		self._out_sample_num = sr * out_sec
		
		
	def __call__(self):
		# 入力WAV読み込み
			wav, sr = librosa.load(self._in_file, sr=self._sample_rate)

			if not os.path.isdir(self._out_dir):
				os.makedirs(self._out_dir)
				
			wav_harmonic, wav_percussive = librosa.effects.hpss(wav)
				
			# Get a more isolated percussive component by widening its margin
				#wav_harmonic, wav_percussive = librosa.effects.hpss(y, margin=(1.0,5.0))
				
			# Dump signals
			librosa.output.write_wav('hpss_org.wav', wav, sr)
			librosa.output.write_wav('hpss_harm.wav', wav_harm, sr)
			librosa.output.write_wav('hpss_perc.wav', wav_perc, sr)
				
			# Plot
			plt.subplot(3,1,1)
			plt.plot(y)
			plt.title("Original signal")
			
			plt.subplot(3,1,2)
			plt.plot(y_harm)
			plt.title("Harmonic signal")
			
			plt.subplot(3,1,3)
			plt.plot(y_perc)
			plt.title("Percussive signal")
			
			plt.tight_layout()
			plt.show()
			

def main():
	arg_parser = argparse.ArgumentParser(description='AnomalyMixer')
	arg_parser.add_argument('input_file', type=str)
	arg_parser.add_argument('-a', '--anm_dir', type=str, default="./in/anm/")
	arg_parser.add_argument('-o', '--out_dir', type=str, default="./in/sample/")
	arg_parser.add_argument('-r', '--sample_rate', type=int, default=16000)
	arg_parser.parse_args()
	args = arg_parser.parse_args()

	mixer = Hpss(args.input_file, anm=args.anm_dir, out=args.out_dir, sr=args.sample_rate)
	hpss()
	
