import random
import tqdm
import numpy

size = 10000000
degrees = [2, 4, 8]
nnz_max = size * degrees[-1]
graph = numpy.empty(shape=nnz_max * 2, dtype=int)

print("generating graph...")

nnz = 0

for i in tqdm.tqdm(range(size)):
    degree = random.choice(degrees)
    left, right = i + 1, size
    edges = random.sample(range(left, right), min(degree, right - left))
    for j in edges:
        graph[2 * nnz + 0] = i
        graph[2 * nnz + 1] = j
        nnz += 1

out_file = f"generated.mtx"

print("writing graph to file...")

with open(out_file, "w") as f:
    f.write("%%MatrixMarket matrix coordinate pattern general\n")
    f.write("%-------------------------------------------------------------------------------\n")
    f.write("%% kind: directed graph\n")
    f.write("%-------------------------------------------------------------------------------\n")
    f.write(f"{size} {size} {nnz * 2}\n")
    for idx in tqdm.tqdm(range(nnz)):
        i = graph[2 * idx + 0] + 1
        j = graph[2 * idx + 1] + 1
        f.write(f"{i} {j}\n")
        f.write(f"{j} {i}\n")

print(f"generated graph to file {out_file} of size {size}x{size} with total {nnz * 2} edges")