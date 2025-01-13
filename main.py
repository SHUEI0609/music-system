import pygame
import subprocess
import sys
from backing import *
from lead import *
from bass import *

# 初期化
pygame.init()

# 画面サイズとフォント設定
WIDTH, HEIGHT = 1920, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Component Display")
font_path = "BIZ-UDGOTHICB.TTC"  # ここに使用するフォントファイルのパスを指定
font_size = 25
try:
  font = pygame.font.Font(font_path, font_size)
except FileNotFoundError:
  print("フォントファイルが見つかりません。正しいパスを指定してください。")
  sys.exit()

# ボタン設定
button_width, button_height = 200, 50
buttons = {
    "Backing": pygame.Rect((50, 100, button_width, button_height)),
    "Lead": pygame.Rect((50, 200, button_width, button_height)),
    "Bass": pygame.Rect((50, 300, button_width, button_height))
}

# 色設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# 結果を描画する関数
def draw_text(text, y_offset):
  lines = text.split("\n")
  y = y_offset
  for line in lines:
    rendered_text = font.render(line, True, BLACK)
    screen.blit(rendered_text, (300, y))
    y += 30

# メインループ
running = True
output_text = ""  # 表示する結果
while running:
  screen.fill(WHITE)

  # ボタン描画
  for label, rect in buttons.items():
    pygame.draw.rect(screen, GRAY, rect)
    text = font.render(label, True, BLACK)
    screen.blit(text, (rect.x + 50, rect.y + 10))

  # 出力結果描画
  draw_text(output_text, 100)

  # イベント処理
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      mouse_pos = pygame.mouse.get_pos()
      for label, rect in buttons.items():
        if rect.collidepoint(mouse_pos):
          try:
            if label == "Backing":
              result = subprocess.run(
                  [sys.executable, "backing.py"], capture_output=True, text=True)
            elif label == "Lead":
              result = subprocess.run(
                  [sys.executable, "lead.py"], capture_output=True, text=True)
            elif label == "Bass":
              result = subprocess.run(
                  [sys.executable, "bass.py"], capture_output=True, text=True)

            output_text = result.stdout  # 結果を更新
          except Exception as e:
            output_text = f"Error: {str(e)}"

  pygame.display.flip()

pygame.quit()
