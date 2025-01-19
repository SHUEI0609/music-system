import random

# 元ファイルからインポートされた関数やデータ
from base import bpm, gaticode, get_chord_notes, quarter

def generate_bassline():
  """
  コード進行に基づくベースライン（ルート音を4分音符で演奏）を生成する関数
  """
  bassline = []
  for chord in gaticode:
    root, chord_type = chord
    chord_notes = get_chord_notes(root, chord_type)
    if chord_notes:
      bassline.extend([chord_notes[0]] * 4)  # 4分音符を4回繰り返し
    else:
      bassline.extend(["Rest"] * 4)  # 構成音が取得できない場合は休符

  return bassline

# ベースライン生成
bassline = generate_bassline()

# 出力
print("コード進行:", gaticode)
print("ベースライン:", bassline)
print(f"各音の長さ: {quarter:.2f} 秒 (BPM: {bpm[0]})")
