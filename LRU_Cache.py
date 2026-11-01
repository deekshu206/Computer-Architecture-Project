# LRU Cache Replacement Algorithm

cache_size = 3
cache = []

access_sequence = [4, 2, 1, 4, 3, 2, 5, 4]

hits = 0
misses = 0

print("LRU CACHE REPLACEMENT")
print("---------------------")

for block in access_sequence:

    if block in cache:
        hits += 1
        cache.remove(block)
        cache.append(block)

        print("Block:", block, "HIT")
        print("Cache:", cache)

    else:
        misses += 1
        removed = None

        if len(cache) == cache_size:
            removed = cache.pop(0)

        cache.append(block)

        print("Block:", block, "MISS")
        print("Removed block:", removed)
        print("Cache:", cache)

print("\nTotal Hits:", hits)
print("Total Misses:", misses)

hit_ratio = hits / len(access_sequence)

print("Hit Ratio:", hit_ratio)
print("Hit Percentage:", hit_ratio * 100, "%")