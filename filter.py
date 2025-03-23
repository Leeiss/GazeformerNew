import json

def filter_json(input_file, output_file, target_task="cup"):
    with open(input_file, 'r') as f:
        data = json.load(f)

    filtered_data = [entry for entry in data if entry.get("task") == target_task]

    with open(output_file, 'w') as f:
        json.dump(filtered_data, f, indent=4)

input_file1 = "./dataset/coco_search18_fixations_TP_test.json"  # Укажите путь к вашему исходному файлу
input_file2 = "./dataset/coco_search18_fixations_TP_train.json"  # Укажите путь к вашему исходному файлу
input_file3 = "./dataset/coco_search18_fixations_TP_validation.json"  # Укажите путь к вашему исходному файлу

output_file1 = "file1.json"  # Укажите путь для сохранения отфильтрованного файла
output_file2 = "file2.json"  # Укажите путь для сохранения отфильтрованного файла
output_file3 = "file3.json"  # Укажите путь для сохранения отфильтрованного файла

filter_json(input_file1, output_file1)
filter_json(input_file2, output_file2)
filter_json(input_file3, output_file3)

