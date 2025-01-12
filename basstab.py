from backing import *

import random
import matplotlib.pyplot as plt

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

def generate_tab_image(bassline, file_name="bassline_tab.png"):
  """
  ベースラインをタブ譜として画像で表示する関数。

  Parameters:
      bassline (list): [(音, リズム), ...] のリスト。
      file_name (str): 画像ファイル名。
  """
  # 弦の名前
  strings = ["E", "A", "D", "G"]  # E弦が一番下になるように変更

  # 音とそのフレット番号を設定
  fret_positions = {
      "E": {"E": 0, "F": 1, "F#": 2, "G": 3, "G#": 4, "A": 5, "A#": 6, "B": 7, "C": 8, "C#": 9, "D": 10, "D#": 11},
      "A": {"A": 0, "A#": 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7, "F": 8, "F#": 9, "G": 10, "G#": 11},
      "D": {"D": 0, "D#": 1, "E": 2, "F": 3, "F#": 4, "G": 5, "G#": 6, "A": 7, "A#": 8, "B": 9, "C": 10, "C#": 11},
      "G": {"G": 0, "G#": 1, "A": 2, "A#": 3, "B": 4, "C": 5, "C#": 6, "D": 7, "D#": 8, "E": 9, "F": 10, "F#": 11}
  }

  # ベースラインのノートとタイミング
  notes = [note for note, _ in bassline]

  # タブ譜作成用データ
  x = []
  y = []
  labels = []

  for i, note in enumerate(notes):
    # どの弦で弾くかを探索
    string_index = None
    fret = None
    for string, positions in fret_positions.items():
      if note in positions:
        string_index = strings.index(string)
        fret = positions[note]
        break

    if string_index is None or fret is None:
      continue  # ノートが見つからない場合はスキップ

    x.append(i * 2)  # 横位置は音符ごとの間隔
    y.append(string_index)
    labels.append(f"{fret}")

  # 描画開始
  fig, ax = plt.subplots(figsize=(10, 4))
  ax.set_xlim(-1, len(notes) * 2)
  ax.set_ylim(-0.5, 3.5)
  ax.set_yticks(range(len(strings)))
  ax.set_yticklabels(strings)
  ax.set_xticks(range(len(notes) * 2))
  ax.set_xticklabels([])
  ax.grid(True, linestyle="--", alpha=0.5)

  # ノートを配置
  for i in range(len(x)):
    ax.text(x[i], y[i], labels[i], fontsize=10, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="black", boxstyle="circle"))

  ax.set_title("Bassline Tab")
  ax.set_xlabel("Time")
  ax.set_ylabel("Strings")

  # 画像を保存
  plt.savefig(file_name)
  plt.close(fig)

# ベースラインを生成
make_rhythm()  # リズムを生成
bassline = generate_bassline(gaticode, rhythm)

# 結果を表示
print("\n生成されたベースライン:")
for note, note_rhythm in bassline:
  print(f"音: {note}, リズム: {note_rhythm:.2f}秒")

# タブ譜画像を生成
generate_tab_image(bassline)
