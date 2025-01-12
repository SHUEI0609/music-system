import pygame
import sys
from backing import make_code, make_rhythm, gaticode, rhythm
from basstab import generate_bassline, generate_tab_image
import matplotlib.pyplot as plt

# 初期化
pygame.init()

# ウィンドウサイズと色の設定
WIDTH, HEIGHT = 1920, 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# フォントの設定
pygame.font.init()
FONT = pygame.font.SysFont("Arial", 24)

# 画面の作成
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chord and Bassline Generator")

# ボタンの定義
def draw_button(text, x, y, w, h, color):
  pygame.draw.rect(screen, color, (x, y, w, h))
  text_surface = FONT.render(text, True, BLACK)
  screen.blit(text_surface, (x + (w - text_surface.get_width()) //
              2, y + (h - text_surface.get_height()) // 2))

# 楽譜画像生成
def generate_music_score(chords, rhythm, file_name="music_score.png"):
  fig, ax = plt.subplots(figsize=(10, 4))

  # 表示用データの準備
  x_positions = []
  labels = []
  for i, (chord, length) in enumerate(zip(chords, rhythm)):
    x_positions.append(i * 2)
    labels.append(f"{chord}\n({length:.2f}s)")

  ax.set_xlim(-1, len(chords) * 2)
  ax.set_ylim(0, 1)
  ax.set_yticks([])
  ax.set_xticks(x_positions)
  ax.set_xticklabels(labels, rotation=45, ha="right")
  ax.grid(True, linestyle="--", alpha=0.5)

  for x in x_positions:
    ax.plot([x, x], [0.4, 0.6], color="black")

  ax.set_title("Music Score")
  plt.tight_layout()
  plt.savefig(file_name)
  plt.close(fig)

# メインループの準備
running = True
chords_displayed = []
bassline_displayed = []
tab_generated = False
music_score_image = None

while running:
  screen.fill(WHITE)

  # ボタンの描画
  draw_button("Generate Chords", 50, 50, 200, 50, BLUE)
  draw_button("Generate Rhythm", 50, 150, 200, 50, BLUE)
  draw_button("Generate Bassline", 50, 250, 200, 50, BLUE)

  # イベント処理
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = event.pos

      # コード生成ボタンが押された場合
      if 50 <= mouse_x <= 250 and 50 <= mouse_y <= 100:
        make_code()
        chords_displayed = [f"{root}{type_}" for root, type_ in gaticode]
        tab_generated = False

      # リズム生成ボタンが押された場合
      elif 50 <= mouse_x <= 250 and 150 <= mouse_y <= 200:
        make_rhythm()
        tab_generated = False

      # ベースライン生成ボタンが押された場合
      elif 50 <= mouse_x <= 250 and 250 <= mouse_y <= 300:
        bassline = generate_bassline(gaticode, rhythm)
        bassline_displayed = [f"{note} ({r:.2f}s)" for note, r in bassline]
        generate_tab_image(bassline)
        generate_music_score(chords_displayed, rhythm)
        music_score_image = pygame.image.load("music_score.png")
        tab_generated = True

  # テキストの描画
  y_offset = 350
  if chords_displayed:
    chords_text = FONT.render("Chords:", True, BLACK)
    screen.blit(chords_text, (50, y_offset))
    y_offset += 30
    for chord in chords_displayed:
      chord_text = FONT.render(chord, True, BLACK)
      screen.blit(chord_text, (50, y_offset))
      y_offset += 30

  if bassline_displayed:
    bassline_text = FONT.render("Bassline:", True, BLACK)
    screen.blit(bassline_text, (400, 350))
    y_offset = 380
    for bass in bassline_displayed:
      bass_text = FONT.render(bass, True, BLACK)
      screen.blit(bass_text, (400, y_offset))
      y_offset += 30

  if tab_generated and music_score_image:
    screen.blit(music_score_image, (50, HEIGHT - 300))

  # 画面更新
  pygame.display.flip()

# 終了
pygame.quit()
sys.exit()
