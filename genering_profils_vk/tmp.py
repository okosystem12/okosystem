import os, json

in_path = r"D:\nd\database"
out_path = r"D:\nd\database_new"
try:
    for filename in os.listdir(in_path):
        print(filename)
        path_in = os.path.join(in_path, filename)
        with open(path_in, "r", encoding="utf-8") as file:
            data = [json.loads(line) for line in file]

        print(len(data))
        data_update = [elem for l in data for elem in l if
                       elem.get("deactivated") not in ("deleted", "banned") and not elem.get("is_closed")]

        print(len(data_update))
        path_out = os.path.join(out_path, filename)
        with open(path_out, "a", encoding="utf-8") as file:
            file.write(json.dumps(data_update) + "\n")
        data_update.clear()

except Exception as e:
    print(e)
