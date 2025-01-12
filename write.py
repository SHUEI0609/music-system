import random
from music21 import stream, note, chord, meter, tempo, converter
import matplotlib.pyplot as plt
from backing import *


# BPMをランダムに設定
bpm = random.randint(50, 250)
quarter_tempo = tempo.MetronomeMark(number=bpm)

# コード進行を作成する
def make_code():
  code = ["C", "D", "E", "F", "G", "A", "B"]
  sharpcode = ["C#", "D#", "F#", "G#", "A#"]
  type1 = ["", "M7", "7", "6", "aug", "m", "mM7", "m7",
           "m6", "m7b5", "add9", "sus4", "7sus4", "dim7"]
  type2 = ["", "M7", "7", "aug", "m", "mM7", "m7",
           "m6", "m7b5", "add9", "sus4", "7sus4", "dim7"]

  code_list = [code, sharpcode]
  gaticode = []

  for i in range(4):
    code0 = random.choice(code_list)
    code1 = random.choice(code0)

    if code0 == code:
      type01 = random.choice(type1)
      gaticode.append((code1, type01))
    elif code0 == sharpcode:
      type02 = random.choice(type2)
      gaticode.append((code1, type02))

  return gaticode

# コード進行から構成音を取得する
def get_chord_notes(root, chord_type):
  intervals = {
      "": [0, 4, 7], "m": [0, 3, 7], "7": [0, 4, 7, 10], "M7": [0, 4, 7, 11],
      "m7": [0, 3, 7, 10], "dim7": [0, 3, 6, 9], "aug": [0, 4, 8], "m7b5": [0, 3, 6, 10],
      "sus4": [0, 5, 7], "7sus4": [0, 5, 7, 10], "6": [0, 4, 7, 9],
      "m6": [0, 3, 7, 9], "add9": [0, 4, 7, 14], "mM7": [0, 3, 5, 7]
  }

  root_value = scale[root]
  if chord_type not in intervals:
    return []

  chord_intervals = intervals[chord_type]
  chord_notes = [(root_value + interval) % 12 for interval in chord_intervals]
  return [reverse_scale[note] for note in chord_notes]

# 楽譜を作成
melody = stream.Part()
melody.insert(0, meter.TimeSignature('4/4'))
melody.append(quarter_tempo)

chord_progression = make_code()

# NoteとChordを追加
for chord_info in chord_progression:
  root, ctype = chord_info
  notes = get_chord_notes(root, ctype)
  # コードを追加
  melody.append(chord.Chord(notes, quarterLength=1.0))

# 楽譜を表示
melody.show('text')

# PNGファイルとして保存
musicxml = converter.parse(melody.write('musicxml'))
fig = musicxml.plot('histogram', 'pitchClass',
                    addLines='middleground', returnFig=True)
fig.savefig("chord_progression.png")
