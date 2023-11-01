import os

def filter_sequence_files(directory, representative_file):
    # Extract details from the representative file
    rep_basename = os.path.basename(representative_file)
    rep_name, rep_ext = os.path.splitext(rep_basename)
    rep_padding = len(rep_name.split('.')[-2])

    # Step 0: Go to the parent directory
    all_files = os.listdir(directory)

    # Step 1: Filter by extension
    filtered_files = [f for f in all_files if f.endswith(rep_ext)]
    discarded_1 = list(set(all_files) - set(filtered_files))

    # Step 2: Period ahead of the extension must have an integer to its left
    filtered_files = [f for f in filtered_files if f.split('.')[-2].isdigit()]
    discarded_2 = list(set(all_files) - set(filtered_files))

    # Step 3: No period to the left of the second one and only integers separating them
    filtered_files = [f for f in filtered_files if ".." not in f and f.split('.')[-2].isdigit()]
    discarded_3 = list(set(all_files) - set(filtered_files))

    # Step 4: Filter by padding
    filtered_files = [f for f in filtered_files if len(f.split('.')[-2]) == rep_padding]
    discarded_4 = list(set(all_files) - set(filtered_files))

    # Step 5: Filter by filename
    rep_name_start = rep_name.split('.')[0]
    filtered_files = [f for f in filtered_files if f.startswith(rep_name_start) and f[len(rep_name_start)] == '.']
    discarded_5 = list(set(all_files) - set(filtered_files))

    # Combine all discarded files for future use
    all_discarded = discarded_1 + discarded_2 + discarded_3 + discarded_4 + discarded_5

    return filtered_files, all_discarded

# Test
directory = "G:\jobs\IO\IN\vendor\manmath\crvb\CRVB_115_0210_V001"
representative_file = "CRVB_115_0210_V001.1001.exr"
filtered_files, discarded_files = filter_sequence_files(directory, representative_file)
print("Filtered Files:", filtered_files)
print("Discarded Files:", discarded_files)
