# TLB Effective Access Time Calculation

tlb_time = 10
memory_time = 80

hit_ratios = [0.90, 0.75]

for h in hit_ratios:

    eat = (h * (tlb_time + memory_time)) + \
          ((1 - h) * (tlb_time + 2 * memory_time))

    print("TLB Hit Ratio:", h)
    print("TLB Lookup Time:", tlb_time, "ns")
    print("Memory Access Time:", memory_time, "ns")
    print("Effective Access Time:", eat, "ns")
    print("--------------------------")