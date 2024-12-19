import secret_christmas_song_data
import math 
import wave
import struct


pitches = secret_christmas_song_data.pitches
durations = secret_christmas_song_data.durations
sr = 44100
dur_samples = []
freq = []
audio_buffer =[]
bin_buf = bytearray()
def mtof(p_midi_note):
	return 440 * 2 ** ((p_midi_note - 69) / 12)

for midi_note in pitches:
	freq.append(mtof(midi_note))

for duration in durations:
	dur_samples.append(int(sr * duration))

def make_audio_buffer(p_sr, p_freq, p_len_smps):
	buffer = []
	for i in range(p_len_smps):
		sample = 0
		sample = math.sin(2 * math.pi * i * p_freq / p_sr)
		buffer.append(sample)
	return buffer

for i in range(len(freq)):
	local_audio_buffer = make_audio_buffer(sr, freq[i], dur_samples[i])
	for j in range(len(local_audio_buffer)):
		local_audio_buffer[j] *= 1. - j /len(local_audio_buffer)
	for j in local_audio_buffer:
		audio_buffer.append(j)

#write buffer

for sample in audio_buffer:
	local_sample = sample * ((2**16 - 1)/2**16) 
	bin_buf= bin_buf + struct.pack("h", round(local_sample*2**16/2) - 1)

wav = wave.open("song.wav", "w")
wav.setnchannels(1)
wav.setsampwidth(2)
wav.setframerate(sr)
wav.writeframes(bin_buf)
wav.close()