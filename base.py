import random

bpm = [random.randint(50, 250)]
print("BPM:", bpm)

rhythm_set = ["四分音符", "半音符", "八分音符", "全音符", "16分音符"]
code = ["C", "D", "E", "F", "G", "A", "B"]
sharpcode = ["C#", "D#", "F#", "G#", "A#"]
type1 = ["", "M7", "7", "6", "aug", "m", "mM7", "m7",
         "m6", "m7b5", "add9", "sus4", "7sus4", "dim7"]
type2 = ["", "M7", "7", "aug", "m", "mM7", "m7",
         "m6", "m7b5", "add9", "sus4", "7sus4", "dim7"]

# 音階の構成
scale = {
    "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11
}
reverse_scale = {v: k for k, v in scale.items()}

# BPMに基づくリズム長の計算
quarter = (60 / bpm[0])
half = quarter * 2
eighth = quarter / 2
full = quarter * 4
sixteenth = quarter / 4

def make_code():
  gaticode = []
  for i in range(4):
    code0 = random.choice([code, sharpcode])
    code1 = random.choice(code0)

    if code0 == code:
      type01 = random.choice(type1)
      gaticode.append((code1, type01))
    elif code0 == sharpcode:
      type02 = random.choice(type2)
      gaticode.append((code1, type02))
  return gaticode

# コード進行をグローバルに定義
gaticode = make_code()

def get_chord_notes(root, chord_type):
  """
  与えられたルート音とコードタイプから構成音を生成する関数。
  """
  intervals = {
      "": [0, 4, 7],            # メジャー
      "m": [0, 3, 7],           # マイナー
      "7": [0, 4, 7, 10],       # ドミナント7
      "M7": [0, 4, 7, 11],      # メジャー7
      "m7": [0, 3, 7, 10],      # マイナー7
      "dim7": [0, 3, 6, 9],     # ディミニッシュ7
      "aug": [0, 4, 8],         # オーギュメント
      "m7b5": [0, 3, 6, 10],    # ハーフディミニッシュ
      "sus4": [0, 5, 7],        # サスペンド4
      "7sus4": [0, 5, 7, 10],   # サスペンド4 (7)
      "6": [0, 4, 7, 9],        # メジャー6
      "m6": [0, 3, 7, 9],       # マイナー6
      "add9": [0, 4, 7, 14],    # メジャー(add9)
      "mM7": [0, 3, 5, 7]       # マイナーメジャー7
  }

  root_value = scale[root]
  if chord_type not in intervals:
    return []

  chord_intervals = intervals[chord_type]
  chord_notes = [(root_value + interval) % 12 for interval in chord_intervals]
  return [reverse_scale[note] for note in chord_notes]
