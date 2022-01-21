import os
import cProfile
import pstats

# Score : 350 bytes, 350 chars
def main():
  b=" of beer"
  c=" bottle"
  w=f"{b} on the wall"
  m=" more"
  n=f"no{m}"
  s=lambda i:('s','')[i==1]
  p=print
  i=100
  while i!=0:
    i=i-1
    t=i>0
    p(f"{(n.capitalize(),i)[t]}{c}{s(i)}{w}, {(n,i)[t]}{c}{s(i)}{b}.")
    e=(f"{n}{c}s",f"{i-1}{c}{s(i-1)}")[i>1]
    p((f"Go to the store and buy some{m}, 99{c}s{w}.", f"Take one down and pass it around, {e}{w}.\n")[t])


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    main()

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()
