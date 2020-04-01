# ICWSM2020

### Citation
If you use our work, please cite our paper [**Top Comment or Flop Comment? Predicting and Explaining User Engagement in Online News Discussions**](https://github.com/julian-risch/ICWSM2020/raw/master/risch2020top.pdf) as follows:

    @inproceedings{risch2020top,
    author = {Risch, Julian and Krestel, Ralf},
    booktitle = {Proceedings of the International Conference on Web and Scoial Media (ICWSM)},
    title = {Top Comment or Flop Comment? Predicting and Explaining User Engagement in Online News Discussions},
    year = {2020}
    }

### Implementation

### Dataset
This repository contains a python script `create_dataset.py` and four files `comment_ids_*` that list comment IDs.
We provide a script to download a dataset of comments. The script accesses the Guardian’s Web API to download a predefined list of comments identified by their IDs.

The script takes comment IDs as input and retrieves the corresponding comments via the Guardian's API. An API key is required to access the API. You can register for a key by filling out this short form: https://bonobo.capi.gutools.co.uk/register/developer

In case the daily number of API calls is limited, the script stops when the limit is reached. If restarted, the script will continue from the point where it stopped.

There are four files (please see the paper for details):
* `comment_ids_replies_top.csv` 3111 IDs, the top 10% comments in the politics section with the largest relative number of replies received
* `comment_ids_replies_flop.csv` 3111 IDs, the flop 10% comments in the politics section with the smallest relative number of replies received
* `comment_ids_upvotes_top.csv` 11081 IDs, the top 10% comments in the politics section with the largest relative number of upvotes received
* `comment_ids_upvotes_flop.csv` 11081 IDs, the flop 10% comments in the politics section with the smallest relative number of upvotes received
