# @title read guitar

# from backing import *
from backing import gaticode  # 必要なものだけをインポート

import random

# リズムの決定
tempo = [1, 2, 4, 8, 16]
read_rhythm = []

total = 0
while total < 64:
  choice = random.choice(tempo)
  if total + choice <= 64:  # 64を超えない場合のみ追加
    read_rhythm.append(choice)
    total += choice


# コード進行のリスト（例: 先のプログラムで生成されたコード進行を使用）
chord_progression = gaticode

# 各コードに対応するスケール（簡易版）
scales = {
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "C#": ["C#", "D#", "F", "F#", "G#", "A#", "C"],
    "D": ["D", "E", "F#", "G", "A", "B", "C#"],
    "D#": ["D#", "F", "G", "G#", "A#", "C", "D"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "F": ["F", "G", "A", "A#", "C", "D", "E"],
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "F"],
    "G": ["G", "A", "B", "C", "D", "E", "F#"],
    "G#": ["G#", "A#", "C", "C#", "D#", "F", "G"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "A#": ["A#", "C", "D", "D#", "F", "G", "A"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
}

# メロディ生成用関数
def generate_melody(chords, note_count=8):
  melody = []
  for chord in chords:
    root = chord[0]  # コードのルート音を取得
    if len(chord) > 1 and chord[1] == "#":  # シャープの場合
      root = chord[:2]
    scale = scales.get(root, [])  # 対応するスケールを取得
    if scale:
      for _ in range(note_count // len(chords)):  # 各コードに対してノートを生成
        note = random.choice(scale)
        melody.append(note)
  return melody

# メロディを生成
melody = generate_melody(chord_progression)
# print("コード進行:", chord_progression)
# print("スケール:", melody)

def extract_melody_by_count(rhythm, melody):
  note_count = len(rhythm)  # read_rhythm の数字の数を取得
  extracted_melody = [random.choice(melody)
                      for _ in range(note_count)]  # 数字の数だけランダムに抽出
  return extracted_melody

# read_rhythm の数字の数だけ melody からランダム抽出
extracted_melody = extract_melody_by_count(read_rhythm, melody)

print("Rhythm:", read_rhythm)

print("メロディ:", extracted_melody)
