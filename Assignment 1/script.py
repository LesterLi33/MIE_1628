import subprocess

data_file = "data.txt"
centroids_file = "input5.txt"

iterations = 15

for i in range(iterations):
    print(f"Iteration {i + 1}")

    with open('mapper_output.txt', 'w') as mapper_output:
        subprocess.run(['python', 'mapper.py', centroids_file], stdin=open(data_file, 'r'), stdout=mapper_output)

    with open(centroids_file, 'w') as new_centroids:
        subprocess.run(['python', 'reducer.py'], stdin=open('mapper_output.txt', 'r'), stdout=new_centroids)

print("Completed 15 iterations.")

