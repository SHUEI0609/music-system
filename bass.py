from backing import quarter, make_rhythm, gaticode, rhythm

import random

def generate_bassline(gaticode, rhythm):
  """
  コード進行とリズムに基づいてルート弾きのベースラインを生成する関数。

  Parameters:
      gaticode (list): [(ルート音, コードタイプ), ...] のリスト。
      rhythm (list): 音符の長さのリスト。

  Returns:
      bassline (list): [(音, リズム), ...] のリスト。
  """
  bassline = []

  for i, chord in enumerate(gaticode):
    root, _ = chord  # ルート音のみを使用

    # リズムが不足している場合は四分音符をデフォルトに
    note_rhythm = quarter

    # ルート音をベースラインに追加
    bassline.append((root, note_rhythm))

  return bassline

# ベースラインを生成
make_rhythm()  # リズムを生成
bassline = generate_bassline(gaticode, rhythm)

# 結果を表示
print("\n生成されたベースライン:")
for note, note_rhythm in bassline:
  print(f"音: {note}, リズム: {note_rhythm:.2f}秒")
