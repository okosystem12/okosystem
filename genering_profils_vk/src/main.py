from genering_profils_vk.src.func import *
from pprint import pprint

list_token = []
with open(os.path.join("..", "tokens", "tokens.txt"), 'r') as f:
    for line in f:
        list_token.append(str(line).rstrip('\n'))


dt = datetime.now().strftime("%d-%m-%Y_%H-%M")
dir_path_date_and_time = create_dir_current_date_and_time(dt)


start = time()
data_id = collector(list_token, dir_path_date_and_time, dt)
print("Итоговое время", time() - start)
pprint(data_id[0])
print()
pprint(data_id[1])


