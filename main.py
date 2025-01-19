import tkinter as tk
from tkinter import font, scrolledtext
import subprocess

def run_script(script_name):
  try:
    result = subprocess.run(
        ["python", script_name],
        text=True,
        capture_output=True,
        check=True
    )
    return result.stdout
  except subprocess.CalledProcessError as e:
    return f"エラー: {e.stdout}\n{e.stderr}"

def on_button_click(script_name, text_area):
  output = run_script(script_name)
  text_area.delete("1.0", tk.END)
  text_area.insert(tk.END, output)

def main():
  root = tk.Tk()
  root.title("ランダムフレーズ作成ソフト")

  # Set window size
  root.geometry("1920x1000")

  # Font setup
  custom_font = font.Font(family='Helvetica', size=24)

  # Title label
  title_label = tk.Label(root, text="ランダムフレーズ作成ソフト", font=custom_font)
  title_label.pack(pady=30)

  # Frame to hold buttons
  button_frame = tk.Frame(root)
  button_frame.pack(pady=20)

  # Backing guitar button
  backing_button = tk.Button(button_frame, text="バッキングギター", font=custom_font, width=18,
                             command=lambda: on_button_click("backing.py", output_area))
  backing_button.grid(row=0, column=0, padx=10)

  # Lead guitar button
  lead_button = tk.Button(button_frame, text="リードギター", font=custom_font, width=18,
                          command=lambda: on_button_click("lead.py", output_area))
  lead_button.grid(row=0, column=1, padx=10)

  # Bass button
  bass_button = tk.Button(button_frame, text="ベース", font=custom_font, width=18,
                          command=lambda: on_button_click("bass.py", output_area))
  bass_button.grid(row=0, column=2, padx=10)

  # Scrolled text area for output
  output_area = scrolledtext.ScrolledText(
      root, wrap=tk.WORD, font=custom_font, width=100, height=10)
  output_area.pack(pady=30)

  # Start the main event loop
  root.mainloop()

if __name__ == "__main__":
  main()
