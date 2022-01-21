import contextlib
import filecmp
import os
import sys
from unittest.mock import patch

from tests.utils.bench import calculate_duration
from tests.utils.tests import OUTPUT_PATH

from solutions.arrows import main

solution_01_path = f"{os.path.dirname(os.path.abspath(__file__))}/{__name__}.01.expect.txt"
solution_02_path = f"{os.path.dirname(os.path.abspath(__file__))}/{__name__}.02.expect.txt"
solution_03_path = f"{os.path.dirname(os.path.abspath(__file__))}/{__name__}.03.expect.txt"
solution_04_path = f"{os.path.dirname(os.path.abspath(__file__))}/{__name__}.04.expect.txt"
solution_05_path = f"{os.path.dirname(os.path.abspath(__file__))}/{__name__}.05.expect.txt"
output_01_path = f"{OUTPUT_PATH}/{__name__}.01.result.txt"
output_02_path = f"{OUTPUT_PATH}/{__name__}.02.result.txt"
output_03_path = f"{OUTPUT_PATH}/{__name__}.03.result.txt"
output_04_path = f"{OUTPUT_PATH}/{__name__}.04.result.txt"
output_05_path = f"{OUTPUT_PATH}/{__name__}.05.result.txt"

def test_main_arrows_01():
  with open(output_01_path, "w") as f:
    with contextlib.redirect_stdout(f):
      with patch.object(sys, 'argv', [" ", "↔", "↱", "⇔", "⇐", "↗", "⇙", "→", "↗", "⇧", "↙", "↓", "⇑", "←", "↳", "↑", "↲", "⇩", "↗", "⇑", "↰", "⇓", "⥀", "↑", "↱", "↳", "↕", "↕", "⇨", "⇦", "⇑", "↓", "⇙", "⇨", "⇒", "⥁", "⇓", "⇨", "↖", "⇕", "⇗", "⇩", "←", "↰", "⇔", "↰", "⇘", "⇖", "⇧", "↖", "⇩", "⇖", "↖", "⥁", "⇓", "⥁", "↕", "⇐", "⇧", "↘"]):
        calculate_duration(main)

  assert filecmp.cmp(solution_01_path, output_01_path, shallow=True)

def test_main_arrows_02():
  with open(output_02_path, "w") as f:
    with contextlib.redirect_stdout(f):
      with patch.object(sys, 'argv', [" ", "⇗", "⇓", "⇑", "⇘", "↖", "⇙", "↔", "⥀", "⇙", "⥁", "↳", "↘", "←", "⇙", "⇦", "↳", "←", "↰", "↗", "⇗", "↖", "⇒", "↱", "↙", "↰", "⥁", "⇑", "⇔", "↱", "⇨", "⇩", "↔", "↓", "⇑", "→", "↕", "⇧", "↙", "→", "⇒", "⇓", "⇕", "↱", "⇩", "⇦", "⥀", "↑", "↲", "⇐", "⇒", "↘", "↓", "⇓", "⥁", "↕", "⇨", "⇩", "↳", "⇨", "↔", "→", "⇧", "⇐", "↓", "⇖", "⇔", "↕", "⇦", "↙", "⇘"]):
        calculate_duration(main)

  assert filecmp.cmp(solution_02_path, output_02_path, shallow=True)

def test_main_arrows_03():
  with open(output_03_path, "w") as f:
    with contextlib.redirect_stdout(f):
      with patch.object(sys, 'argv', [" ", "⇘", "→", "↕", "⇔", "↘", "↱", "←", "↳", "⇑", "↰", "⥁", "⇩", "↔", "⥀", "⇖", "⥀", "↖", "↗", "↔", "⇒", "↳", "⇧", "↲", "↖", "↳", "⇓", "↓", "⇙", "⇖", "⇨", "⥀", "⇗", "⇩", "⇐", "↓", "⇒", "↓", "⇓", "↱", "⇗", "→", "⇕", "⇨", "↙", "↲", "⇙", "↱", "⇒", "⇐", "⇩", "⥁", "↗", "⇔", "↗", "↰", "⇦", "←", "⥁", "⇦", "⇦", "↑"]):
        calculate_duration(main)

  assert filecmp.cmp(solution_03_path, output_03_path, shallow=True)

def test_main_arrows_04():
  with open(output_04_path, "w") as f:
    with contextlib.redirect_stdout(f):
      with patch.object(sys, 'argv', [" ", "⇩", "⇓", "↳", "↑", "⥀", "⥁", "⇕", "⇔", "→", "↱", "↘", "→", "⇘", "↰", "⥁", "↑", "⇦", "⇒", "⇓", "↖", "←", "↰", "⇨", "⇘", "↰", "⇐", "⇘", "↗", "↳", "↕", "⇩", "⇦", "⇩", "⇧", "↲", "⇙", "←", "↓", "↲", "↕", "⥁", "↗", "⇔", "⇗", "↘", "↗", "⇔", "↙", "⇧", "⇑", "⇓", "↖", "↖", "⇑", "⇗", "↔", "↑", "⇖", "⇗", "⇖", "↓", "↔", "⇖", "↳", "⇕"]):
        calculate_duration(main)

  assert filecmp.cmp(solution_04_path, output_04_path, shallow=True)

def test_main_arrows_05():
  with open(output_05_path, "w") as f:
    with contextlib.redirect_stdout(f):
      with patch.object(sys, 'argv', [" ", "↘", "↲", "↕", "⇒", "⇔", "⇐", "⇒", "⇙", "⇓", "⇨", "↔", "←", "↗", "⇧", "⇑", "⇔", "⇨", "↘", "⇔", "⇐", "⇘", "⇖", "↓", "⥀", "⇧", "↕", "⇗", "⥁", "⇓", "⇕", "⥀", "↳", "⇖", "⇩", "↘", "↗", "↓", "↙", "←", "⇕", "⇙", "⇦", "↰", "⇨", "⇩", "↱", "↔", "→", "↓", "⇓", "↔", "⇙", "↰", "↕", "↗", "⥁", "↑", "⇑", "⇩", "↖", "↑"]):
        calculate_duration(main)

  assert filecmp.cmp(solution_05_path, output_05_path, shallow=True)