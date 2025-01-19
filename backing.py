import random
from base import *


# コード進行の生成
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

def make_rhythm():
  beat = [random.choice(rhythm_set) for _ in range(4)]
  rhythm = []
  for b in beat:
    if b == "四分音符":
      rhythm.append((quarter))
    elif b == "半音符":
      rhythm.append((half))
    elif b == "八分音符":
      rhythm.append((eighth))
    elif b == "全音符":
      rhythm.append((full))
    elif b == "16分音符":
      rhythm.append((sixteenth))
  rhythm_seconds = [f"{r:.1f}" for r in rhythm]
  return beat, rhythm_seconds

if __name__ == "__main__":
  # 実行部分
  gaticode = make_code()
  print("コード進行:", gaticode)
  for chord in gaticode:
    root, chord_type = chord
    notes = get_chord_notes(root, chord_type)
    print(f"{root}{chord_type}: {notes}")

  beat, rhythm = make_rhythm()
  print("リズム:", beat)
  print("リズム(秒):", rhythm)
