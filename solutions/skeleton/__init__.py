import os
import cProfile
import pstats


def main():
  p=print
  p("TODO")


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    main()

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()
