from TensorTransmit_client import run
import numpy as np

latency_record_f = []
latency_record_b = []
runs = 100

for i in range(runs):
    latency_f, latency_b = run(1,3, "int8")
    latency_record_f.append(latency_f)
    latency_record_b.append(latency_b)

print(f"The average latency (numerical data) over {runs} runs is: {np.mean(latency_record_f)}")
print(f"The average latency (raw bytes) over {runs} runs is: {np.mean(latency_record_b)}")