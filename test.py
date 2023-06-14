import os
import subprocess
import time
import sys

def compare_outputs(expected_output, actual_output):
    return expected_output == actual_output

args = sys.argv
if (len(args) < 3):
	exit(1)

#input_dir = 'tests_a'
program_dir = args[1]
input_dir = args[2]

# Get a sorted list of files in the input directory
files = sorted(os.listdir(input_dir))

# Iterate over the sorted list of files
for filename in files:
    # Check if the file is an input file
    if filename.endswith('.in'):
        print(f"{filename}: \t", end='')
        # Generate the corresponding output file name
        output_filename = os.path.splitext(filename)[0] + '.out'

        # Formulate the file paths
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(input_dir, output_filename)

        # Run naive.py with stdin from the input file
        with open(input_file, 'r') as file:
            start_time = time.time()
            process = subprocess.Popen(['python', program_dir], stdin=file, stdout=subprocess.PIPE)
            output = process.communicate()[0].decode()
            end_time = time.time()
        
		# Read the expected output from the output file
        with open(output_file, 'r') as file:
            expected_output = file.read()

        # Compare the output with the expected output
        if compare_outputs(expected_output, output):
            print(f"[OK]\t{end_time - start_time:.4f} seconds")
        else:
            print(f"[FAIL]\t{end_time - start_time:.4f} seconds")

