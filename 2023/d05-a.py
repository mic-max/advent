import re
import sys

lines = [line for line in sys.stdin]

def s_map_pairs(flg_seed_pairs, dst, src, size):
  new_seed_pairs = []
  src_start = src
  src_stop = src+size-1
  for flg_pair in flg_seed_pairs:
    flag, (start,stop) = flg_pair
    
    if flag == 1:
      new_seed_pairs.append(flg_pair)
      continue
      
    # no mapping
    if (start < src_start and stop < src_start) or (start > src_stop):
      ##print("no overlap for ", (start, stop))
      new_seed_pairs.append((0, (start, stop)))
      continue
      
    # LOWER PART
    if start < src_start and stop >= src_start:
      ##print("lower for ", (start, src_start-1))
      new_seed_pairs.append((0, (start, src_start-1)))
      
    # OVELAP PART
    new_pair = (max(start, src_start), min(stop, src_stop))
    map_pair = tuple(dst+(x-src_start) for x in new_pair)
    ##print(f"mapped {new_pair} to {map_pair}")
    new_seed_pairs.append((1, map_pair))
      
    # UPPER PART
    if stop > src_stop:
      ##print("upper for ", (src_stop+1, stop))
      new_seed_pairs.append((0, (src_stop+1, stop)))
      
  return new_seed_pairs

map_p = False
for line in lines:
  if line.startswith("seeds:"):
    seed_ranges = list(map(int, re.findall(r"\d+", line.split(":")[1])))
    seed_pairs = list(zip(seed_ranges[::2], seed_ranges[1::2]))
    # convert to (start, stop)
    seed_pairs = [ (start, start+size-1) for start,size in seed_pairs]
    ##print("pairs", seed_pairs)
    flg_seed_pairs = [ (0, x) for x in seed_pairs ]
    continue
  if line.find(":") >= 0:
    ##print(); print(line)
    map_p = True
    seed_pairs = [ x for (f, x) in flg_seed_pairs ]
    ##print("pairs", seed_pairs)
    flg_seed_pairs = [ (0, x) for x in seed_pairs ]
    continue
  # map operations
  if len(line) == 0:
    continue
  dst, src, size = map(int, re.findall(r"\d+", line))
  ##print("map", dst, src, size)
  flg_seed_pairs = s_map_pairs(flg_seed_pairs, dst, src, size)
  ##print("flagged pairs", flg_seed_pairs)

print(min(x for x,y in seed_pairs))
