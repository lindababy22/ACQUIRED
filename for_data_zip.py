###############################################
# THIS CODE TO BE DELETED IN ACTUAL RELEASE!! #
###############################################

import os, sys, csv, json
import pprint
import urllib.parse
from tqdm import tqdm
import shutil


def read_json_data(files):
    if type(files) == str:
        files = [files]

    datasets = {}
    for file in files:
        split = file.split("/")[-1].split(".")[0]
        datasets[split] = json.load(open(file))
    return datasets


def check_video_and_transform_url(
    dataset, split,
    url_prefix="https://oops-qa.s3.us-west-1.amazonaws.com/",
    video_root="data",
    target_dir="release",
):
    new_dataset = []
    for d in tqdm(dataset, desc="Preprocessing"):
        video_url = d["video_url"]
        cleansed_url = urllib.parse.unquote_plus(video_url)
        assert url_prefix in cleansed_url
        video_path = cleansed_url.split(url_prefix)[-1]
        if "ego4d" in video_path:
            video_name = "/".join(video_path.split("/")[2:])
        else:
            video_name = "/".join(video_path.split("/")[1:])
        video_path = os.path.join(video_root, video_path)
        assert os.path.exists(video_path)

        video_id = d["video_id"]
        video_resource = video_id.split("-")[0].split(":")[0]
        target_video_folder = os.path.join(video_root, target_dir, video_resource)
        if not os.path.exists(target_video_folder):
            os.makedirs(target_video_folder)

        target_video_path = os.path.join(target_video_folder, video_name)
        if "ego4d" in video_path:
            ego4d_video_folder = "/".join(target_video_path.split("/")[:-1])
            if not os.path.exists(ego4d_video_folder):
                os.makedirs(ego4d_video_folder)

        shutil.copy(
            video_path,
            target_video_path,
        )

        d["video_path"] = os.path.join(video_resource, video_name)
        new_dataset.append(d)

    return new_dataset


if __name__ == "__main__":
    data_files = [
        "Dataset/train.json",
        "Dataset/val.json",
        "Dataset/test.json",
    ]
    datasets = read_json_data(data_files)

    for split in datasets:
        dataset = check_video_and_transform_url(datasets[split], split)
        json.dump(
            dataset,
            open("Dataset_Release/{}.json".format(split), "w"),
            indent=4,
        )

    print("Done!")
