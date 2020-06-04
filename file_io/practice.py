# def statistics(file_name):
#     with open(file_name) as file:
#         stat_file = file.readlines()
#     return {
#         "lines": len(stat_file),
#         "words": sum(len(stat.split(" ")) for stat in stat_file),
#         "characters": sum(len(stat) for stat in stat_file)
#     }

def find_and_replace(file_name, word, new_word):
    with open(file_name, "r+") as file:
        read_file = file.read()
        new_text = read_file.replace(word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()