def scan_sector(sector_id, status):

  return status=="hazard"

grid = [(1, "safe"),
        (2, "hazard"),
        (3, "safe"),
        (4, "hazard"),
        (5, "safe")]

hazard_count= 0
scanned_count= 0
total_sectors= len(grid)

for sector_id, status in grid:

  scanned_count+=1

  if not scan_sector(sector_id, status):
    continue

  print(f"Hazard detected in sector in {sector_id}!")

  hazard_count+=1

  if hazard_count==2:
    print(f"Reached hazard limit (2). Exiting early after sector {sector_id}.")
    break

print("\nFinal Report:")
print(f"Sectors scanned before exit: {scanned_count}")
print(f"Total sectors in grid: {total_sectors}")