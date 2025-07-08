# log_error_extractor.py

def extract_errors(log_file, output_file):
    with open(log_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if 'error' in line.lower() or 'fail' in line.lower():
                outfile.write(line)

if __name__ == "__main__":
    input_log = "system.log"
    output_log = "error_output.txt"
    extract_errors(input_log, output_log)
    print(f"Filtered lines written to {output_log}")
