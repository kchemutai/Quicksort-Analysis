import time
import random
from quick_sort import quicksort
from randomized_quick_sort import randomized_quicksort

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Generate test cases
input_sizes = [10, 100, 1000, 10000]
distributions = {
    "random": lambda size: [random.randint(0, 10000) for _ in range(size)],
    "sorted": lambda size: list(range(size)),
    "reverse_sorted": lambda size: list(range(size, 0, -1))
}

# Run comparisons
results = []
for size in input_sizes:
    for dist_name, generator in distributions.items():
        arr = generator(size)
        deterministic_time = measure_time(quicksort, arr)
        randomized_time = measure_time(randomized_quicksort, arr)
        results.append({
            "Input Size": size,
            "Distribution": dist_name,
            "Deterministic Time (s)": deterministic_time,
            "Randomized Time (s)": randomized_time
        })

# Print results
import pandas as pd
results_df = pd.DataFrame(results)
print(results_df)