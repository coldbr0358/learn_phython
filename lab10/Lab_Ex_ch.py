event_attendance = {"Seminar": ["S01", "S02", "S03", "S04"], 
                    "AI Workshop": ["S02","S03"], 
                    "Job Fair": ["S01", "S03", "S05"], 
                    "Hackathon": ["S03", "S04", "S06", "S02"]}

print("== Converted to a dictionary with sets ==")
print(event_attendance)
print("")

semi = set(event_attendance["Seminar"])
aiWork = set(event_attendance["AI Workshop"])
jobFair = set(event_attendance["Job Fair"])
hackathon = set(event_attendance["Hackathon"])
all = semi & aiWork & jobFair & hackathon

print("Student who attended All events:",all)
print()

uni = semi | aiWork | jobFair | hackathon

print("Students who attended ANY events:",uni)
print()

attendence_count = {}

for v in event_attendance.values():
    for stu in v:
        if stu in attendence_count:
            attendence_count[stu] += 1
        else:
            attendence_count[stu] = 1
    
print("Attendance count:",attendence_count)
print()

t1_v = 0
t2_v = 0

for k,v in attendence_count.items():
    if v >= t1_v:
        t1_v = v
        t1_k = k 
    elif v >= t2_v:
        t2_v = v
        t2_k = k

top1 = (t1_k,t1_v)
top2 = (t2_k,t2_v)

print(f"Top 2 most active students: [{top1}, {top2}]")
