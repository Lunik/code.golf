import contextlib
import filecmp
import os

from tests.utils.bench import calculate_duration
from tests.utils.tests import OUTPUT_PATH

from solutions.ninety_nine_bottles_of_beer import main

solution_path = f"{os.path.dirname(os.path.abspath(__file__))}/{__name__}.expect.txt"
output_path = f"{OUTPUT_PATH}/{__name__}.result.txt"

def test_main_ninety_nine_bottles_of_beer():
  with open(output_path, "w") as f:
    with contextlib.redirect_stdout(f):
      calculate_duration(main)

  assert filecmp.cmp(solution_path, output_path, shallow=True)