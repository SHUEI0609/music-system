from backing import *
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
