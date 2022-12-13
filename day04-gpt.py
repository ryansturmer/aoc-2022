def contains_range(range1, range2):
  # Check if range1 fully contains range2
  if range1.start <= range2.start and range1.end >= range2.end:
    return True

  # Check if range2 fully contains range1
  if range2.start <= range1.start and range2.end >= range1.end:
    return True

  return False

def find_overlapping_assignments(assignments):
  # Parse the input and convert each assignment into a range object
  ranges = []
  for assignment in assignments:
    start, end = assignment.split('-')
    ranges.append(range(int(start), int(end) + 1))

  # Count the number of pairs where one range fully contains the other
  count = 0
  for i in range(len(ranges)):
    for j in range(i + 1, len(ranges)):
      if contains_range(ranges[i], ranges[j]):
        count += 1

  return count

# Example input
assignments = [
  '2-4,6-8',
  '2-3,4-5',
  '5-7,7-9',
  '2-8,3-7',
  '6-6,4-6',
  '2-6,4-8'
]

# Find the number of overlapping assignments
result = find_overlapping_assignments(assignments)
print(result)  # Expected output: 2