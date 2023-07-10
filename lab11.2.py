import os

def get_directory_tree(path):
    total_size = 0
    files_count = 0
    dirs_count = 0
    tree = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            total_size += size
            files_count += 1
            tree.append("-" * 4 + item + " (" + str(size) + " bytes)")
        elif os.path.isdir(item_path):
            size, sub_files_count, sub_dirs_count, sub_tree = get_directory_tree(item_path)
            total_size += size
            files_count += sub_files_count
            dirs_count += sub_dirs_count + 1
            tree.append(
                "-" * 4 + item + "/(" + str(sub_dirs_count + 1) + " dirs, " + str(sub_files_count) + " files, " + str(
                size) + " bytes)")
            tree.extend(["      " + line for line in sub_tree])
    return total_size, files_count, dirs_count, tree

path = "F:\SteamLibrary\steamapps\common"
size, files_count, dirs_count, tree = get_directory_tree(path)
print("Total size:", size)
print("Files count:", files_count)
print("Dirs count:", dirs_count)
print("\n".join(tree))