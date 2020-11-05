# ICWSM2020

### Citation
If you use our work, please cite our paper [**Top Comment or Flop Comment? Predicting and Explaining User Engagement in Online News Discussions**](https://hpi.de/fileadmin/user_upload/fachgebiete/naumann/people/risch/risch2020top.pdf) as follows:

    @inproceedings{risch2020top,
    title = {Top Comment or Flop Comment? Predicting and Explaining User Engagement in Online News Discussions},
    author = {Risch, Julian and Krestel, Ralf},
    booktitle = {Proceedings of the International Conference on Web and Social Media (ICWSM)},
    pages = {579-589},
    year = {2020}
    }
    
### Acknowledgments
We would like to thank Johannes Filter, Cornelius Hagmeister and Thomas Kellermeier for their contribution to this project during the seminar [**Text Mining in Practice**](https://hpi.de/naumann/teaching/teaching/ss-18/text-mining-in-practice-ps-master.html).

### Implementation

The Python notebook `train_and_evaluate_model.ipynb` contains the source code for our experiments. 
In order to run the experiments, the following additional files are required:
* `guardian-300.bin` fasttext word embeddings that we trained on 4.4 billion tokens from TheGuardian.com comments. They can be downloaded from here (5.5GB): [Link](https://owncloud.hpi.de/s/8LjQz1nyFI3OZBe/download)
* `amazon-300.bin` fasttext word embeddings that we trained on 7.6 billion tokens from Amazon.com reviews. They can be downloaded from here (4.8GB): [Link](https://owncloud.hpi.de/s/cUCEnFSiR2y47ta/download)
* `comments_top_and_bottom_upvotes_10percent.csv` the top/flop 10% comments in the politics section with the largest/smallest relative number of upvotes received
* `comments_top_and_bottom_replies_10percent.csv` the top/flop 10% comments in the politics section with the largest/smallest relative number of replies received
* `reviews_books_top_10percent.csv` the top 10% book reviews on Amazon.com with the largest relative number of helpfulness upvotes received. The Amazon reviews dataset can be downloaded from here: [Link](https://nijianmo.github.io/amazon/index.html)
* `reviews_books_bottom_10percent.csv` the flop 10% book reviews on Amazon.com with the smallest relative number of helpfulness upvotes received.

### Dataset
This repository contains a python script `create_dataset.py` and four files `comment_ids_*` that list comment IDs.
We provide a script to download a dataset of comments. The script accesses the Guardian’s Web API to download a predefined list of comments identified by their IDs.

The script takes comment IDs as input and retrieves the corresponding comments via the Guardian's API. An API key is required to access the API. You can register for a key by filling out this short form: https://bonobo.capi.gutools.co.uk/register/developer

In case the daily number of API calls is limited, the script stops when the limit is reached. If restarted, the script will continue from the point where it stopped.

The general dataset comprises four files (please see the paper for details):
* `comment_ids_replies_top.csv` 3111 IDs, the top 10% comments in the politics section with the largest relative number of replies received
* `comment_ids_replies_flop.csv` 3111 IDs, the flop 10% comments in the politics section with the smallest relative number of replies received
* `comment_ids_upvotes_top.csv` 11081 IDs, the top 10% comments in the politics section with the largest relative number of upvotes received
* `comment_ids_upvotes_flop.csv` 11081 IDs, the flop 10% comments in the politics section with the smallest relative number of upvotes received

We annotated a subset of the dataset. The subset includes only true positives (top comments correctly classified as such).
The comment ids and labels are split into four files:
* `true_positives_comment_ids_replies_top.csv` 335 IDs 
* `true_positives_comment_upvotes_top.csv` 1128 IDs
* `true_positives_labels_replies_top.csv` 335 labels
* `true_positives_labels_upvotes_top.csv` 1128 labels

Labels (please see the paper for details):
1. Question asking for an **Explanation**
2. Question asking for an **Opinion**
3. Question asking for a **Fact**
4. Information in form of a **Correction**
5. Information in form of a **Personal Story**
6. Information in form of a **Fact**
7. **Consent** referring to an **Article**
8. **Dissent** referring to an **Article**
9. **Consent** referring to a **Comment**
10. **Dissent** referring to a **Comment**
11. **Suggestion**
12. Speculation about the **Future**
13. Speculation about **Reasons**
14. **Joke/Humor**

### Video Presentation
A short video about the paper is on [Youtube](https://www.youtube.com/watch?v=rh--BndimtU).
