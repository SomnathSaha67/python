log = "ERROR|Database Timeout|2026-06-02"
first_partition_find= log.find("|")
level= log[0:first_partition_find]
second_partition_find= log.find("|", first_partition_find+1)
message= log[first_partition_find+1:second_partition_find]
date= log[second_partition_find+1:]
print(f"Level: {level}\nMessage: {message}\nDate: {date}")