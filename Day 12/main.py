def read_input(file_name):
  with open('input.txt', 'r') as f:
    ret = f.readlines()
  return ret


def parse_line(line):
  springs, groups_str = line.split()
  return springs, [int(g) for g in groups_str.split(',')]


def get_clusters(springs):
  return [s for s in springs.split('.') if s]


def count_placements(groups, clusters, cache={}):
  key = "|".join(map(str, groups))
  key += "#" + ":".join(clusters)
  if key in cache:
    return cache[key]

  if not groups:
    for cluster in clusters:
      if "#" in cluster:
        return 0
    return 1
  if not clusters:
    return 0
  ret = 0
  group = groups[0]
  cluster = clusters[0]
  len_cluster = len(cluster)
  if group > len_cluster and "#" in cluster:
    return 0
  for i in range(len_cluster - group + 1):
    left = cluster[:i]
    if "#" in left:
      continue
    right = cluster[i + group:]
    if right.startswith("#"):
      continue
    new_clusters = clusters[1:]
    if len(right) > 1:
      new_clusters.insert(0, right[1:])
    ret += count_placements(groups[1:], new_clusters, cache)

  if "#" not in cluster:
    ret += count_placements(groups, clusters[1:], cache)

  cache[key] = ret

  return ret


def calculate_total(filename, expand):
  total = 0
  for line in read_input(filename):
    springs, groups = parse_line(line)
    if expand:
      springs = "?".join(5 * [springs])
      groups = 5 * groups
    clusters = get_clusters(springs)
    delta = count_placements(groups, clusters)
    total += delta
  return total


def part1():
  print(calculate_total('input.txt', False))


def part2():
  print(calculate_total('input.txt', True))


if __name__ == '__main__':
  part1()
  part2()