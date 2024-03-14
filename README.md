# ACQUIRED: A Dataset for Answering Counterfactual Questions In Real Life Videos

This repository releases the curated `ACQUIRED` dataset for counterfactual question answering on real-life videos. For more details, please check out our [EMNLP 2023 paper](https://arxiv.org/abs/2311.01620).

`ACQUIRED` consists of 3.9K annotated videos, encompassing a wide range of event types and incorporating both first and third-person viewpoints, which ensures a focus on real-world diversity.

Each video is annotated with questions that span three distinct dimensions of reasoning, including `physical`, `social`, and `temporal`, which can comprehensively evaluate the model counterfactual abilities along multiple aspects.

## Download The Videos

Please download the zip file from
[this google drive link](https://drive.google.com/file/d/1yFkYeSnXPUxAov7Cudqy8g9lCcbZbIg9/view?usp=sharing)
and directly unzip it here.

The unziped folder structure should look like below:
```
acquired_dataset
├── ego4d
│   ├── 002d2729-df71-438d-8396-5895b349e8fd
│   ├── 01db7c39-a512-4bac-b284-dff8c7360e80
│   └── ... ...
└── oopsqa
```

# Check Out The Data

The main split of the datasets are prepared as `.json` files under the folder `Dataset`, which contains `train.json`, `val.json`, and `test.json`, the official splits used in the above paper.

Please follow the instruction of `Demo.ipynb` to visualize the data samples and check the structure of the datasets more in-depth.

Generally, each `{split}.json` file under the folder `Dataset` will have fields like below:

```
{                                          
    "video_id": ...,                          
    "domain": ...,                              
    "type": "Counterfactual",                            
    "question": ...,               
    "answer1": ...,             
    "answer2": ...,            
    "correct_answer_key": "answer{1/2}",                        
    "video_url": "url_of_the_video.mp4",
    "video_path": "path/to/video.mp4"
  },
```

## Citation

If you find our curated resource useful, please cite our paper using:
```
@inproceedings{wu2023acquired,
  title = {ACQUIRED: A Dataset for Answering Counterfactual Questions In Real-Life Videos},
  author = {Wu*, Te-Lin and Dou*, Zi-Yi and Hu*, Qingyuan and Hou, Yu and Chandra, Nischal Reddy and Freedman, Marjorie and Weischedel, Ralph and Peng, Nanyun},
  booktitle = {The 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year = {2023}
}
```
