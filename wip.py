

# true_files = []
# fake_files = []
# base_folder_url = "https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data"
# for i in range(1, 27):
#     for j in range(1, 60):
#         true_filename = "{base_folder_url}/P{i:02}_S{j:02}_true.csv".format(
#             base_folder_url=base_folder_url, i=i, j=j)
#         true_files.append(true_filename)
#         fake_filename = "{base_folder_url}/P{i:02}_S{j:02}_false.csv".format(
#             base_folder_url=base_folder_url, i=i, j=j)
#         fake_files.append(fake_filename)
# # print(true_files)
# # print(fake_files)
# print(true_files[0])


# #
# import os
# import pandas as pd
# import requests


# # merging all true csv files
# # true_df = pd.concat(map(pd.read_csv, true_files), ignore_index=True)
# # print(true_df)
# true_files = []
# fake_files = []
# dataset_folder_path = "https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data"
# github_eye_dateset_blob_url="https://api.github.com/repos/rameshdhungana/cs620-project/git/trees/dba8d32958460bfdc8891c8d9a275831cddc0a36"

# response = requests.get(github_eye_dateset_blob_url)
# print(response.json())
# files_tree = response.json()["tree"]
# print(files_tree)
# for file in files_tree:
#   if "true.csv" in file['path'] : true_files.append("{dataset_folder_path}/{path}".format(dataset_folder_path=dataset_folder_path, path=file['path']))
#   if "false.csv" in file['path'] : fake_files.append("{dataset_folder_path}/{path}".format(dataset_folder_path=dataset_folder_path, path=file['path']))

# # print(true_files)
# # print(fake_files)


import seaborn as sns  # Imported Just In Case I Need It
import matplotlib.pyplot as plt  # Imported Just In Case I Need It
import os
from pandas import Series, DataFrame
import numpy as np
import pandas as pd
tree = [
    {
        "path": "P01_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4a2c4a923d2dde54261feeab38586176767f2818",
        "size": 4133,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4a2c4a923d2dde54261feeab38586176767f2818"
    },
    {
        "path": "P01_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "83b694fcb237f9d9e6af1c0a2af69e3db5c66ee7",
        "size": 5375,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/83b694fcb237f9d9e6af1c0a2af69e3db5c66ee7"
    },
    {
        "path": "P01_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b23171feb5e016800b10d74678b1a19192e3de0d",
        "size": 9770,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b23171feb5e016800b10d74678b1a19192e3de0d"
    },
    {
        "path": "P01_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e8452ff9438d9e2256bab3f85f097b3b26eb7dc3",
        "size": 9497,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e8452ff9438d9e2256bab3f85f097b3b26eb7dc3"
    },
    {
        "path": "P01_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "797be402cbd63add1a4d95d0e55cb6ecb027f2ad",
        "size": 11299,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/797be402cbd63add1a4d95d0e55cb6ecb027f2ad"
    },
    {
        "path": "P01_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "78609ca10072d2df30cb96a53c20f7fd0588f8c2",
        "size": 8324,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/78609ca10072d2df30cb96a53c20f7fd0588f8c2"
    },
    {
        "path": "P01_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f263df0973a3437a6146775a86a29963749310cb",
        "size": 4350,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f263df0973a3437a6146775a86a29963749310cb"
    },
    {
        "path": "P01_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "41513bed5183ff604fe0f417fae4cfb566d1c436",
        "size": 6736,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/41513bed5183ff604fe0f417fae4cfb566d1c436"
    },
    {
        "path": "P01_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0340fc4833607021e9963b841aa20140edd40b35",
        "size": 8545,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0340fc4833607021e9963b841aa20140edd40b35"
    },
    {
        "path": "P01_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5935c659984ce93828317b6868da91b94fe5dcfc",
        "size": 7153,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5935c659984ce93828317b6868da91b94fe5dcfc"
    },
    {
        "path": "P01_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "79d6e5c9d2e970af7279352a6e45f6fd6895a886",
        "size": 7223,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/79d6e5c9d2e970af7279352a6e45f6fd6895a886"
    },
    {
        "path": "P01_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d5ed40ffb452eaa61a87b55f5c953d07f9190d54",
        "size": 5164,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d5ed40ffb452eaa61a87b55f5c953d07f9190d54"
    },
    {
        "path": "P01_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "29c25a81e406bf621ab0029c9a2811e974d376a7",
        "size": 6541,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/29c25a81e406bf621ab0029c9a2811e974d376a7"
    },
    {
        "path": "P01_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "df9b89deb4fd08932d714e492acf04f16e769f48",
        "size": 5642,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/df9b89deb4fd08932d714e492acf04f16e769f48"
    },
    {
        "path": "P01_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e4cb9ca69363839ad52323822a14fb9ad74fd7f0",
        "size": 9285,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e4cb9ca69363839ad52323822a14fb9ad74fd7f0"
    },
    {
        "path": "P01_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "436165887200ca1f050ee21b25a6e902e7956804",
        "size": 6423,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/436165887200ca1f050ee21b25a6e902e7956804"
    },
    {
        "path": "P01_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bfd250c09702ce4abdd36e87f6238e63f3789565",
        "size": 3181,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bfd250c09702ce4abdd36e87f6238e63f3789565"
    },
    {
        "path": "P01_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "227c09ee2b1c5895fc4096f15ba5a5441418b6c9",
        "size": 8398,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/227c09ee2b1c5895fc4096f15ba5a5441418b6c9"
    },
    {
        "path": "P01_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6debc8be2b16a6d78aaa3a14d2997a1a92cdfe44",
        "size": 6897,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6debc8be2b16a6d78aaa3a14d2997a1a92cdfe44"
    },
    {
        "path": "P01_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c026fa2c41cc32395fcda8a4bd36cc55bf5ef1ea",
        "size": 14297,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c026fa2c41cc32395fcda8a4bd36cc55bf5ef1ea"
    },
    {
        "path": "P01_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e7b9cc63ae79fdb4187f4866c35b672f95388caf",
        "size": 4426,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e7b9cc63ae79fdb4187f4866c35b672f95388caf"
    },
    {
        "path": "P01_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "99bd30eec15bae516eb620d24caba1217faefa8e",
        "size": 3166,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/99bd30eec15bae516eb620d24caba1217faefa8e"
    },
    {
        "path": "P01_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "865a0cd2cc4c4601582ae7b9eda9b8c9ee2ddd9c",
        "size": 8282,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/865a0cd2cc4c4601582ae7b9eda9b8c9ee2ddd9c"
    },
    {
        "path": "P01_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0827769043503d7c7a5303409ca3942629963973",
        "size": 7832,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0827769043503d7c7a5303409ca3942629963973"
    },
    {
        "path": "P01_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ca17260266bd014cd075819f099406a645d78403",
        "size": 4499,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ca17260266bd014cd075819f099406a645d78403"
    },
    {
        "path": "P01_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4f9d63fa62ccd1b0333ff9ed13eb82d808c070d7",
        "size": 6990,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4f9d63fa62ccd1b0333ff9ed13eb82d808c070d7"
    },
    {
        "path": "P01_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f9765bd939e99f8276381b3e19cca2b6662fb262",
        "size": 6532,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f9765bd939e99f8276381b3e19cca2b6662fb262"
    },
    {
        "path": "P01_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "31beef6b7f1b65c5d1e084f96b168673610d5a37",
        "size": 6109,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/31beef6b7f1b65c5d1e084f96b168673610d5a37"
    },
    {
        "path": "P01_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5cbdcb4cc5c469271fb556d7022fe0b99deac7e4",
        "size": 9057,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5cbdcb4cc5c469271fb556d7022fe0b99deac7e4"
    },
    {
        "path": "P01_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bf6e01f758510c5f186ba89d11816274aab5dd97",
        "size": 9914,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bf6e01f758510c5f186ba89d11816274aab5dd97"
    },
    {
        "path": "P01_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8c6d81ef8bf1fd40c8f0a9d42a1736788b33cdc7",
        "size": 3805,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8c6d81ef8bf1fd40c8f0a9d42a1736788b33cdc7"
    },
    {
        "path": "P01_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "500d4b379450e672f280d916ae668134216cb1c1",
        "size": 10252,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/500d4b379450e672f280d916ae668134216cb1c1"
    },
    {
        "path": "P01_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3a1957d0068cf89759f9b473b314405d6c375dc2",
        "size": 3451,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3a1957d0068cf89759f9b473b314405d6c375dc2"
    },
    {
        "path": "P01_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ad648ba5f64cd3b452570d3678541d38539321ac",
        "size": 8576,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ad648ba5f64cd3b452570d3678541d38539321ac"
    },
    {
        "path": "P01_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a2d5c475a9bb2bcab7077f5005d6e9e7efd5c0fe",
        "size": 3932,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a2d5c475a9bb2bcab7077f5005d6e9e7efd5c0fe"
    },
    {
        "path": "P01_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16aa8b891f6b9b75c530c329d8e2d3282238d69b",
        "size": 5642,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16aa8b891f6b9b75c530c329d8e2d3282238d69b"
    },
    {
        "path": "P01_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f75ca99eacea81ab2cb705470dd6be17711add40",
        "size": 4345,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f75ca99eacea81ab2cb705470dd6be17711add40"
    },
    {
        "path": "P01_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "74ec2da3964f2b8368dd0e6312dd9e640b0a7bab",
        "size": 7405,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/74ec2da3964f2b8368dd0e6312dd9e640b0a7bab"
    },
    {
        "path": "P01_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0172e72442deaa5ec5da98ac51af6a341dfa3701",
        "size": 4754,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0172e72442deaa5ec5da98ac51af6a341dfa3701"
    },
    {
        "path": "P01_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f942d08ca3258315abbe71d7a5b8e42a859e9907",
        "size": 5444,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f942d08ca3258315abbe71d7a5b8e42a859e9907"
    },
    {
        "path": "P01_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8de443f8d397aff15d5a9b579bf4f8ceb3e5c615",
        "size": 6953,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8de443f8d397aff15d5a9b579bf4f8ceb3e5c615"
    },
    {
        "path": "P01_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d9fb2921947af123e0c1b593c1bee55276813967",
        "size": 10419,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d9fb2921947af123e0c1b593c1bee55276813967"
    },
    {
        "path": "P01_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "40b4c3386c192e3337172e1d1864370012fc4880",
        "size": 11202,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/40b4c3386c192e3337172e1d1864370012fc4880"
    },
    {
        "path": "P01_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e6c8c269010d64eeb4770da762daa0f7e6d43f51",
        "size": 8549,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e6c8c269010d64eeb4770da762daa0f7e6d43f51"
    },
    {
        "path": "P01_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "509f7ab330e1b6a49a0a31b8925556ea6b30df45",
        "size": 6417,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/509f7ab330e1b6a49a0a31b8925556ea6b30df45"
    },
    {
        "path": "P01_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a0e9775e5b3ed5e41fcfe03d3985b2bd396248ea",
        "size": 9597,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a0e9775e5b3ed5e41fcfe03d3985b2bd396248ea"
    },
    {
        "path": "P01_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "024deff9a79998cfc5464808ec7a51ca9c1b3a1f",
        "size": 12812,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/024deff9a79998cfc5464808ec7a51ca9c1b3a1f"
    },
    {
        "path": "P01_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6255ec13ce595966d9a99f7f78dba76ea1b4b002",
        "size": 6741,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6255ec13ce595966d9a99f7f78dba76ea1b4b002"
    },
    {
        "path": "P01_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f372d32e78d60c4767e4ba70d29f848b3a31b174",
        "size": 5025,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f372d32e78d60c4767e4ba70d29f848b3a31b174"
    },
    {
        "path": "P01_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5a9a21a44a24bfd124d395d86488b6c65110640a",
        "size": 5106,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5a9a21a44a24bfd124d395d86488b6c65110640a"
    },
    {
        "path": "P01_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9666ad3cf54cc0ea809ca5f0f06e2d5dfff1fc02",
        "size": 5733,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9666ad3cf54cc0ea809ca5f0f06e2d5dfff1fc02"
    },
    {
        "path": "P01_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3107deea472ef2cdb03d682060b137463fb01761",
        "size": 5927,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3107deea472ef2cdb03d682060b137463fb01761"
    },
    {
        "path": "P01_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f9f2850432f40b601c577e3de7216387f4f50bbc",
        "size": 8916,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f9f2850432f40b601c577e3de7216387f4f50bbc"
    },
    {
        "path": "P01_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ee5ebbeb709acac09b646245d800368a6deff52f",
        "size": 6748,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ee5ebbeb709acac09b646245d800368a6deff52f"
    },
    {
        "path": "P01_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d3d43a94d73d04346eb6af547355823bb678e907",
        "size": 4367,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d3d43a94d73d04346eb6af547355823bb678e907"
    },
    {
        "path": "P01_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "48864302eec7118fdf744f62039e058cd72822a6",
        "size": 4692,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/48864302eec7118fdf744f62039e058cd72822a6"
    },
    {
        "path": "P01_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16c0fd5619e5a1c18e8df89599587186dcaf1a76",
        "size": 5160,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16c0fd5619e5a1c18e8df89599587186dcaf1a76"
    },
    {
        "path": "P01_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "242048983e23eed3f6ce47328c2f17c5e74f6d78",
        "size": 3929,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/242048983e23eed3f6ce47328c2f17c5e74f6d78"
    },
    {
        "path": "P01_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "04257e2566283ca2a19b64945fd030a1f88555b7",
        "size": 15670,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/04257e2566283ca2a19b64945fd030a1f88555b7"
    },
    {
        "path": "P01_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7e3b2110a150c38c69e3f5ad1307a593ab6b045f",
        "size": 11637,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7e3b2110a150c38c69e3f5ad1307a593ab6b045f"
    },
    {
        "path": "P02_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4975da9d78d7990be4cfa97cc7dd7a38740762f8",
        "size": 11374,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4975da9d78d7990be4cfa97cc7dd7a38740762f8"
    },
    {
        "path": "P02_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "875f657d45f2f11b842689b643df0ba4744a1d8f",
        "size": 14673,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/875f657d45f2f11b842689b643df0ba4744a1d8f"
    },
    {
        "path": "P02_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a266f02399a1b045784db58918784b013911c687",
        "size": 16462,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a266f02399a1b045784db58918784b013911c687"
    },
    {
        "path": "P02_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dc524ea48ec9bf1c5851dc4fefe27020a971cd36",
        "size": 14681,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dc524ea48ec9bf1c5851dc4fefe27020a971cd36"
    },
    {
        "path": "P02_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ceadfcc15e1be3d0a0263a65f06c86e8dc91d2ff",
        "size": 11596,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ceadfcc15e1be3d0a0263a65f06c86e8dc91d2ff"
    },
    {
        "path": "P02_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2819ac88719103435e20ec03929452553a9b3a2b",
        "size": 9758,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2819ac88719103435e20ec03929452553a9b3a2b"
    },
    {
        "path": "P02_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "76a2ecedba3dfdcd8d8428bc66826cbfc314f20c",
        "size": 7908,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/76a2ecedba3dfdcd8d8428bc66826cbfc314f20c"
    },
    {
        "path": "P02_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3ff95e757748c1bfc9bf9a2a2891584cfaa2c2f1",
        "size": 12646,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3ff95e757748c1bfc9bf9a2a2891584cfaa2c2f1"
    },
    {
        "path": "P02_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "08130616fb886a8243a01fab4cdb3a626cf7acc5",
        "size": 11627,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/08130616fb886a8243a01fab4cdb3a626cf7acc5"
    },
    {
        "path": "P02_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a5937317d71d28fc037d7249a0d2ee238fb539e0",
        "size": 16058,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a5937317d71d28fc037d7249a0d2ee238fb539e0"
    },
    {
        "path": "P02_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "332fe865095cfacd86c786309d67aeed383e3a25",
        "size": 9555,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/332fe865095cfacd86c786309d67aeed383e3a25"
    },
    {
        "path": "P02_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7d564379109f1d5eebeaace86d35148cbce0c715",
        "size": 9814,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7d564379109f1d5eebeaace86d35148cbce0c715"
    },
    {
        "path": "P02_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5f5c27e1d10e5350ff85e8736e7c11c6e6dd0e17",
        "size": 10399,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5f5c27e1d10e5350ff85e8736e7c11c6e6dd0e17"
    },
    {
        "path": "P02_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3664ce10c4b5f0755c9fbf04c18a297318faea5e",
        "size": 8369,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3664ce10c4b5f0755c9fbf04c18a297318faea5e"
    },
    {
        "path": "P02_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "38f43db079c1455a966f140f34c64ef284af43ef",
        "size": 10846,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/38f43db079c1455a966f140f34c64ef284af43ef"
    },
    {
        "path": "P02_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "162e40ed6edc7acf9af7ade2c7f187bfc3727f58",
        "size": 12170,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/162e40ed6edc7acf9af7ade2c7f187bfc3727f58"
    },
    {
        "path": "P02_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7cb2e55472a1c7204321ef65687b567561e6421a",
        "size": 8253,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7cb2e55472a1c7204321ef65687b567561e6421a"
    },
    {
        "path": "P02_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6a4bf34fe0cbc362cbf55d40fc9344c045ee0974",
        "size": 12365,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6a4bf34fe0cbc362cbf55d40fc9344c045ee0974"
    },
    {
        "path": "P02_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "05fcc3574579532577202c6972a3bfaf6f4ee60e",
        "size": 12650,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/05fcc3574579532577202c6972a3bfaf6f4ee60e"
    },
    {
        "path": "P02_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1064e244d87733e3f6493ee87e9045e574990d7a",
        "size": 12555,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1064e244d87733e3f6493ee87e9045e574990d7a"
    },
    {
        "path": "P02_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f9d8584455f3af65ac0690703f4732db07fc04e3",
        "size": 9907,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f9d8584455f3af65ac0690703f4732db07fc04e3"
    },
    {
        "path": "P02_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5f14191a72faae6fd02e0435c78db3a4100c56de",
        "size": 5020,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5f14191a72faae6fd02e0435c78db3a4100c56de"
    },
    {
        "path": "P02_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "42641126062c88ad5272b499b5c5612a1e1d67b0",
        "size": 12642,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/42641126062c88ad5272b499b5c5612a1e1d67b0"
    },
    {
        "path": "P02_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9eb62108daa5744bc757a5d7be622da8959b1f3d",
        "size": 10896,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9eb62108daa5744bc757a5d7be622da8959b1f3d"
    },
    {
        "path": "P02_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "166c727972a14c8f177acab9e80ea3cc734fd849",
        "size": 9337,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/166c727972a14c8f177acab9e80ea3cc734fd849"
    },
    {
        "path": "P02_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "580243e42d33fdd75a5b053ac26673a7dc41cbbb",
        "size": 11064,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/580243e42d33fdd75a5b053ac26673a7dc41cbbb"
    },
    {
        "path": "P02_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d48523e996e02d81762052e0f564bed5d3e7c5e4",
        "size": 7668,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d48523e996e02d81762052e0f564bed5d3e7c5e4"
    },
    {
        "path": "P02_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0758dc4fe182eca35e42ee807b343351f3af28d5",
        "size": 10173,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0758dc4fe182eca35e42ee807b343351f3af28d5"
    },
    {
        "path": "P02_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "95f13348a2ee5a01950ef23419c7f77e13e9345c",
        "size": 14274,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/95f13348a2ee5a01950ef23419c7f77e13e9345c"
    },
    {
        "path": "P02_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2d449d6c45f5e756b53601ccd12d483a3e02f5ab",
        "size": 8884,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2d449d6c45f5e756b53601ccd12d483a3e02f5ab"
    },
    {
        "path": "P02_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b9b924ca26b42ab0da9d3ba07ccb1a929e95447f",
        "size": 6330,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b9b924ca26b42ab0da9d3ba07ccb1a929e95447f"
    },
    {
        "path": "P02_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a7c4fdc3a3652e207ae6d6959bbb44c93e834d89",
        "size": 8443,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a7c4fdc3a3652e207ae6d6959bbb44c93e834d89"
    },
    {
        "path": "P02_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "650ba0964ce37c4e0b7a3e91174537228b4721fb",
        "size": 6098,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/650ba0964ce37c4e0b7a3e91174537228b4721fb"
    },
    {
        "path": "P02_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "26ede144dbbebea91aa894afa0035f6a7f45b91d",
        "size": 8166,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/26ede144dbbebea91aa894afa0035f6a7f45b91d"
    },
    {
        "path": "P02_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "737ccfa9c17b91ae775c0b60d6c798fe668a8a34",
        "size": 5644,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/737ccfa9c17b91ae775c0b60d6c798fe668a8a34"
    },
    {
        "path": "P02_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6196ee67ba2d7e385a7e806b1805f64b7bee7c64",
        "size": 10500,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6196ee67ba2d7e385a7e806b1805f64b7bee7c64"
    },
    {
        "path": "P02_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "210d702747fc11f5467238faf2d49b7ff3006613",
        "size": 10031,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/210d702747fc11f5467238faf2d49b7ff3006613"
    },
    {
        "path": "P02_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c3f9e1823c017ef919d0ea85f34e75a7367a2193",
        "size": 14827,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c3f9e1823c017ef919d0ea85f34e75a7367a2193"
    },
    {
        "path": "P02_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c7533f1f8f43e86e3b2cb031e40e5b649edb8eec",
        "size": 8412,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c7533f1f8f43e86e3b2cb031e40e5b649edb8eec"
    },
    {
        "path": "P02_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "026ab61bd2e826a84673fedbff9ec64e57afc02b",
        "size": 12999,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/026ab61bd2e826a84673fedbff9ec64e57afc02b"
    },
    {
        "path": "P02_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "60afa918c468338214b1bb04e4b356122ed77d59",
        "size": 7767,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/60afa918c468338214b1bb04e4b356122ed77d59"
    },
    {
        "path": "P02_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "766c89147331846318b52311925c8486497d8b98",
        "size": 9264,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/766c89147331846318b52311925c8486497d8b98"
    },
    {
        "path": "P02_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8f1016fc75df8b04c6da905a4a8f6e7d9f408561",
        "size": 10045,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8f1016fc75df8b04c6da905a4a8f6e7d9f408561"
    },
    {
        "path": "P02_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0a694688b4b0cf826c75dea843789eb04688a208",
        "size": 12791,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0a694688b4b0cf826c75dea843789eb04688a208"
    },
    {
        "path": "P02_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "faa1db7da41f603dd4ce47dfd586dfa308dacee2",
        "size": 8442,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/faa1db7da41f603dd4ce47dfd586dfa308dacee2"
    },
    {
        "path": "P02_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1be0aec1263596434c02dfefc0695084151bc237",
        "size": 9038,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1be0aec1263596434c02dfefc0695084151bc237"
    },
    {
        "path": "P02_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "942e00be006bf524e7e882458892a787e112b676",
        "size": 21256,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/942e00be006bf524e7e882458892a787e112b676"
    },
    {
        "path": "P02_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "12ea2e7e0c83ac9b64f21913e3dd53f4cbc390dc",
        "size": 8110,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/12ea2e7e0c83ac9b64f21913e3dd53f4cbc390dc"
    },
    {
        "path": "P02_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ca6683615f275acbb4e64394d38f31bf9d846dc5",
        "size": 6633,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ca6683615f275acbb4e64394d38f31bf9d846dc5"
    },
    {
        "path": "P02_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bb153d544f009e90c5720c78911849ceb39ea805",
        "size": 11922,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bb153d544f009e90c5720c78911849ceb39ea805"
    },
    {
        "path": "P02_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ca3572e97ea4d410058a6d27500762fa08fd67e7",
        "size": 10647,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ca3572e97ea4d410058a6d27500762fa08fd67e7"
    },
    {
        "path": "P02_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4e51d7a0377903bb64a4948c2a2872ee868c0292",
        "size": 9520,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4e51d7a0377903bb64a4948c2a2872ee868c0292"
    },
    {
        "path": "P02_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f8b928181dc38b0b0421f9567f464ac5c18384cb",
        "size": 9339,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f8b928181dc38b0b0421f9567f464ac5c18384cb"
    },
    {
        "path": "P02_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "aeddc89dbfec7d89649893a1356cc25b48883c49",
        "size": 17452,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/aeddc89dbfec7d89649893a1356cc25b48883c49"
    },
    {
        "path": "P02_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "42ec56f45734d192cc0b4ad4b2e37a93628e6418",
        "size": 12582,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/42ec56f45734d192cc0b4ad4b2e37a93628e6418"
    },
    {
        "path": "P02_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1ffaf52532ddd5165dc1c8ac27e5fbd13ecf2a01",
        "size": 11138,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1ffaf52532ddd5165dc1c8ac27e5fbd13ecf2a01"
    },
    {
        "path": "P02_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "84bc77ed2da1b1ddbf554428138171fc499db27b",
        "size": 10382,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/84bc77ed2da1b1ddbf554428138171fc499db27b"
    },
    {
        "path": "P02_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b4a3b35e079355340f38821f5360ba7884590051",
        "size": 8221,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b4a3b35e079355340f38821f5360ba7884590051"
    },
    {
        "path": "P02_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fcbbb1c9f462d1cee5f87959bf2a661443ebc1f3",
        "size": 12932,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fcbbb1c9f462d1cee5f87959bf2a661443ebc1f3"
    },
    {
        "path": "P02_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f9a7de64a708248b2bfaf205879056e21f1eb6af",
        "size": 15766,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f9a7de64a708248b2bfaf205879056e21f1eb6af"
    },
    {
        "path": "P03_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4c9d83155b31087dbffbe786b201be6564db5240",
        "size": 9020,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4c9d83155b31087dbffbe786b201be6564db5240"
    },
    {
        "path": "P03_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3bb351e55c6db00da7efa28b3fc49afc0511b02d",
        "size": 9175,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3bb351e55c6db00da7efa28b3fc49afc0511b02d"
    },
    {
        "path": "P03_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "02ed824cd73e911aae6bc7bd570dc94a5becc2f6",
        "size": 14152,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/02ed824cd73e911aae6bc7bd570dc94a5becc2f6"
    },
    {
        "path": "P03_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3e020d105e0f32bb37826b3fab76afc733f9d67e",
        "size": 16040,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3e020d105e0f32bb37826b3fab76afc733f9d67e"
    },
    {
        "path": "P03_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "83b117d6ce219e4fdb80ea7b31cf03eb42d3ccd9",
        "size": 10203,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/83b117d6ce219e4fdb80ea7b31cf03eb42d3ccd9"
    },
    {
        "path": "P03_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "656f2f536342b6677d345191cede17c18b519201",
        "size": 5892,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/656f2f536342b6677d345191cede17c18b519201"
    },
    {
        "path": "P03_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a1be0a05604ecc85fcece4f99d322a9df73c4c96",
        "size": 13518,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a1be0a05604ecc85fcece4f99d322a9df73c4c96"
    },
    {
        "path": "P03_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "82415bc59ef5811446800bc0934ebf9ce18e1ac7",
        "size": 10728,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/82415bc59ef5811446800bc0934ebf9ce18e1ac7"
    },
    {
        "path": "P03_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a37cb491e8b317ecd6bf858b5fb3392fb76f4881",
        "size": 9836,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a37cb491e8b317ecd6bf858b5fb3392fb76f4881"
    },
    {
        "path": "P03_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7ebf9fccb6db4f80a9bb1e1e0a8a215a38b811d4",
        "size": 9146,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7ebf9fccb6db4f80a9bb1e1e0a8a215a38b811d4"
    },
    {
        "path": "P03_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f5118153b5d01b2050fe244d7119eb2cfa53d123",
        "size": 12911,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f5118153b5d01b2050fe244d7119eb2cfa53d123"
    },
    {
        "path": "P03_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b496bfe9de95545867ad89b44c4ba4582742086c",
        "size": 17676,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b496bfe9de95545867ad89b44c4ba4582742086c"
    },
    {
        "path": "P03_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "806450f6fcc409ade567971079e7566d1beca18a",
        "size": 10097,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/806450f6fcc409ade567971079e7566d1beca18a"
    },
    {
        "path": "P03_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3f0712e57fd94b7c2e1e120c9a1b2e091c23ae91",
        "size": 18777,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3f0712e57fd94b7c2e1e120c9a1b2e091c23ae91"
    },
    {
        "path": "P03_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cded90cd39d46ed62707b50558d1cb61043fbb6d",
        "size": 13152,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cded90cd39d46ed62707b50558d1cb61043fbb6d"
    },
    {
        "path": "P03_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8518f79348861f46e14ed2abed33d56b74dfebcb",
        "size": 6990,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8518f79348861f46e14ed2abed33d56b74dfebcb"
    },
    {
        "path": "P03_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6d89c3458b806cda1bb63056897b9bbef9d9581d",
        "size": 14324,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6d89c3458b806cda1bb63056897b9bbef9d9581d"
    },
    {
        "path": "P03_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c637e8c76df3c10c7d3afce2e8c1916a97c7a856",
        "size": 15087,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c637e8c76df3c10c7d3afce2e8c1916a97c7a856"
    },
    {
        "path": "P03_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2d31ee7f961809f2720c406f186dce28600aba12",
        "size": 11516,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2d31ee7f961809f2720c406f186dce28600aba12"
    },
    {
        "path": "P03_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "858f4fa8ab821e8fa3514d8e4e08197a588a2076",
        "size": 5956,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/858f4fa8ab821e8fa3514d8e4e08197a588a2076"
    },
    {
        "path": "P03_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "068b73263a47aba6b97533f2f540607fa28160ca",
        "size": 7288,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/068b73263a47aba6b97533f2f540607fa28160ca"
    },
    {
        "path": "P03_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3091a35a56b416b8a2233114dee7bff81ad1534c",
        "size": 18255,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3091a35a56b416b8a2233114dee7bff81ad1534c"
    },
    {
        "path": "P03_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cccd59026c40d87b4ea32582a3b601dc9fca0eb6",
        "size": 13974,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cccd59026c40d87b4ea32582a3b601dc9fca0eb6"
    },
    {
        "path": "P03_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b9339dd3e58e47b85a4d37b64932376193224a42",
        "size": 12089,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b9339dd3e58e47b85a4d37b64932376193224a42"
    },
    {
        "path": "P03_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c2ffedaf23bef085c62ebe1982dc1d808d2ee30e",
        "size": 7420,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c2ffedaf23bef085c62ebe1982dc1d808d2ee30e"
    },
    {
        "path": "P03_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7b08262f8b61896b58999fbfc640f6a2d30d3261",
        "size": 8985,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7b08262f8b61896b58999fbfc640f6a2d30d3261"
    },
    {
        "path": "P03_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "546dfc45bd5d3629a3508ff822b30d9b0b663e9d",
        "size": 14924,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/546dfc45bd5d3629a3508ff822b30d9b0b663e9d"
    },
    {
        "path": "P03_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b4c6170b7f19903fb03903439d1baa8ce3cfc95d",
        "size": 18934,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b4c6170b7f19903fb03903439d1baa8ce3cfc95d"
    },
    {
        "path": "P03_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5c5db67e2c443efd8164eb13a405dfd797c842dc",
        "size": 7134,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5c5db67e2c443efd8164eb13a405dfd797c842dc"
    },
    {
        "path": "P03_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "67ce275765e4df047c177c40bdc7e66078f9024a",
        "size": 9152,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/67ce275765e4df047c177c40bdc7e66078f9024a"
    },
    {
        "path": "P03_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3a3486641fa331d127a0d92b03f55ac6c92ca960",
        "size": 16618,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3a3486641fa331d127a0d92b03f55ac6c92ca960"
    },
    {
        "path": "P03_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "86685adb94b62f4fda7288eee64d1900f87cbdd8",
        "size": 11917,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/86685adb94b62f4fda7288eee64d1900f87cbdd8"
    },
    {
        "path": "P03_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5be976584a0d5ec7f8f497cee9b9cfb715525a9f",
        "size": 16094,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5be976584a0d5ec7f8f497cee9b9cfb715525a9f"
    },
    {
        "path": "P03_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e4a822c3ae251725c03a69368221dc556b5ad6b2",
        "size": 15064,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e4a822c3ae251725c03a69368221dc556b5ad6b2"
    },
    {
        "path": "P03_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c52147516f14771f76cda03c406998e9397e2a93",
        "size": 11736,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c52147516f14771f76cda03c406998e9397e2a93"
    },
    {
        "path": "P03_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d5508106fbc03cb63be75e581c5527a58ce7d84b",
        "size": 15092,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d5508106fbc03cb63be75e581c5527a58ce7d84b"
    },
    {
        "path": "P03_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "94441ee7b9f764e8589e0d0139c20a327c59a138",
        "size": 14178,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/94441ee7b9f764e8589e0d0139c20a327c59a138"
    },
    {
        "path": "P03_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "550c41f2309285ec1fa858a9b19d787729677b9c",
        "size": 10341,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/550c41f2309285ec1fa858a9b19d787729677b9c"
    },
    {
        "path": "P03_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4a587ddb5e929a41a8c02c6fc8fbc8fb381bb63f",
        "size": 8470,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4a587ddb5e929a41a8c02c6fc8fbc8fb381bb63f"
    },
    {
        "path": "P03_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "47fe95f233b0cc9d0ece287f4aea6019336c0c29",
        "size": 8885,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/47fe95f233b0cc9d0ece287f4aea6019336c0c29"
    },
    {
        "path": "P03_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2b6214f4fdf10d727f708aa9046591547f26bdfb",
        "size": 11321,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2b6214f4fdf10d727f708aa9046591547f26bdfb"
    },
    {
        "path": "P03_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a85faa44e66911330910f1099d3bce8e9619785e",
        "size": 9302,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a85faa44e66911330910f1099d3bce8e9619785e"
    },
    {
        "path": "P03_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0459e020cbcbda86a044156d2452563e7572362d",
        "size": 4757,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0459e020cbcbda86a044156d2452563e7572362d"
    },
    {
        "path": "P03_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9992ee0c555db9427f2459aae0bf3a6d0a06eb23",
        "size": 11957,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9992ee0c555db9427f2459aae0bf3a6d0a06eb23"
    },
    {
        "path": "P03_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "024c2d985fe7e329215d5135bd0f68ba430e12f7",
        "size": 13588,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/024c2d985fe7e329215d5135bd0f68ba430e12f7"
    },
    {
        "path": "P03_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c33abe4b478b58ad685a7a45ddea16da16fb189e",
        "size": 6027,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c33abe4b478b58ad685a7a45ddea16da16fb189e"
    },
    {
        "path": "P03_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "570c4115702b9e954401946f5fb48d2f21cc4e1d",
        "size": 6695,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/570c4115702b9e954401946f5fb48d2f21cc4e1d"
    },
    {
        "path": "P03_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dfa4c8c741e83db1a27f0ee9625d498fabfddba2",
        "size": 12242,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dfa4c8c741e83db1a27f0ee9625d498fabfddba2"
    },
    {
        "path": "P03_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "542a4ab57ffd6a85450fabd4cd3102277675892a",
        "size": 9897,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/542a4ab57ffd6a85450fabd4cd3102277675892a"
    },
    {
        "path": "P03_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "637d3fb5affb85f2568ba49b633a221ef46b68d0",
        "size": 5258,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/637d3fb5affb85f2568ba49b633a221ef46b68d0"
    },
    {
        "path": "P03_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ee7586414a87176cd0f98ebacb517a524675432b",
        "size": 7242,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ee7586414a87176cd0f98ebacb517a524675432b"
    },
    {
        "path": "P03_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5a4cfcb8420e9a5e2a3a277d3f2b53781e9cfcc1",
        "size": 9590,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5a4cfcb8420e9a5e2a3a277d3f2b53781e9cfcc1"
    },
    {
        "path": "P03_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "931d6135901ee1465c4a652711dec84c89ffe841",
        "size": 13088,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/931d6135901ee1465c4a652711dec84c89ffe841"
    },
    {
        "path": "P03_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3674059c359550037c51f0b281d3f9f3f140fdd1",
        "size": 7782,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3674059c359550037c51f0b281d3f9f3f140fdd1"
    },
    {
        "path": "P03_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "80bdd4ebe7902e6b8dd2cbc175f5be117fd3251e",
        "size": 13369,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/80bdd4ebe7902e6b8dd2cbc175f5be117fd3251e"
    },
    {
        "path": "P03_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "137bf18c101cf984876845a3dab812b7e0f837b0",
        "size": 11507,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/137bf18c101cf984876845a3dab812b7e0f837b0"
    },
    {
        "path": "P03_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6e24608b896d336b794cf3d83e1c357d889fe459",
        "size": 22410,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6e24608b896d336b794cf3d83e1c357d889fe459"
    },
    {
        "path": "P03_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f3d2b22bfcb66503fe9bc4837972cab5f73841cb",
        "size": 14529,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f3d2b22bfcb66503fe9bc4837972cab5f73841cb"
    },
    {
        "path": "P04_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f191d7edae1b850996a12d23746696886db12a44",
        "size": 12684,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f191d7edae1b850996a12d23746696886db12a44"
    },
    {
        "path": "P04_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "47f4522e5a1e50388e1b58e268fd9bab8f902e47",
        "size": 12815,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/47f4522e5a1e50388e1b58e268fd9bab8f902e47"
    },
    {
        "path": "P04_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e79f0466350fb078dd69e6ab0908ed0e4b3189d0",
        "size": 9287,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e79f0466350fb078dd69e6ab0908ed0e4b3189d0"
    },
    {
        "path": "P04_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "eb83b9c4e39ddc781548ae70113aeac3c1f2ee0a",
        "size": 10131,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/eb83b9c4e39ddc781548ae70113aeac3c1f2ee0a"
    },
    {
        "path": "P04_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "99c2df83f71cdccd35ad359242127552c393c72d",
        "size": 10123,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/99c2df83f71cdccd35ad359242127552c393c72d"
    },
    {
        "path": "P04_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "30587aaa45d611ff8000fc61ee8c983b3d3aedbc",
        "size": 8800,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/30587aaa45d611ff8000fc61ee8c983b3d3aedbc"
    },
    {
        "path": "P04_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5e83a12967070dc3befabe8ebf8d75542fbcca3f",
        "size": 9264,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5e83a12967070dc3befabe8ebf8d75542fbcca3f"
    },
    {
        "path": "P04_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3c136d99169214421d0fe3ea4541c8ff5b5fca4d",
        "size": 9098,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3c136d99169214421d0fe3ea4541c8ff5b5fca4d"
    },
    {
        "path": "P04_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e26d59dbe5c48c0fe5e862a8fcb88e36fbc5944d",
        "size": 10228,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e26d59dbe5c48c0fe5e862a8fcb88e36fbc5944d"
    },
    {
        "path": "P04_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "710e5dc2a2a5b5fbd2474c6e9ffc7aa394d8e818",
        "size": 14175,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/710e5dc2a2a5b5fbd2474c6e9ffc7aa394d8e818"
    },
    {
        "path": "P04_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f2de7bdf794909abf999fe913f0033eb90c77743",
        "size": 8604,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f2de7bdf794909abf999fe913f0033eb90c77743"
    },
    {
        "path": "P04_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c1a584cb0235b29a6d307be1afaa068cc101fd27",
        "size": 11132,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c1a584cb0235b29a6d307be1afaa068cc101fd27"
    },
    {
        "path": "P04_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d39762a9e397c85ab99e624935434935bff7684c",
        "size": 10178,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d39762a9e397c85ab99e624935434935bff7684c"
    },
    {
        "path": "P04_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16d0577b60338facfdd36cc61da01b53f1ddf2fe",
        "size": 9425,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16d0577b60338facfdd36cc61da01b53f1ddf2fe"
    },
    {
        "path": "P04_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "26aec2268a813fc4202824d420ec710d9e2dc526",
        "size": 11162,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/26aec2268a813fc4202824d420ec710d9e2dc526"
    },
    {
        "path": "P04_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2308e83b1379502080362e8c410fb856554af15c",
        "size": 9433,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2308e83b1379502080362e8c410fb856554af15c"
    },
    {
        "path": "P04_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7545aaf3ddae60ecfe500068c1a29f55bcca0052",
        "size": 12397,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7545aaf3ddae60ecfe500068c1a29f55bcca0052"
    },
    {
        "path": "P04_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "67340cf316ce0a5beccf7db769ae01db5e357fd3",
        "size": 13213,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/67340cf316ce0a5beccf7db769ae01db5e357fd3"
    },
    {
        "path": "P04_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "54dae9a0547b07330d0da9ee0e385aa00fd2880d",
        "size": 13000,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/54dae9a0547b07330d0da9ee0e385aa00fd2880d"
    },
    {
        "path": "P04_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f90e5e25fd99a26b42a8022291f24541cb26ebc9",
        "size": 9015,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f90e5e25fd99a26b42a8022291f24541cb26ebc9"
    },
    {
        "path": "P04_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6faa081524ea4c01b0914a07206a305f3c8d9f97",
        "size": 10526,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6faa081524ea4c01b0914a07206a305f3c8d9f97"
    },
    {
        "path": "P04_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "94377fdbb7ac327971b9dcf621cc42fd15451b36",
        "size": 9100,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/94377fdbb7ac327971b9dcf621cc42fd15451b36"
    },
    {
        "path": "P04_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d413fb60d06364738c8b5bf8e9b063be569eba00",
        "size": 9029,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d413fb60d06364738c8b5bf8e9b063be569eba00"
    },
    {
        "path": "P04_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8b7b66c28257cb8a36dc225718422d6a6eb6fe4f",
        "size": 10147,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8b7b66c28257cb8a36dc225718422d6a6eb6fe4f"
    },
    {
        "path": "P04_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "be2d41f75291a8d8c745ec14caa78e8af56b28c1",
        "size": 5737,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/be2d41f75291a8d8c745ec14caa78e8af56b28c1"
    },
    {
        "path": "P04_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d1232e2cfacfa1dd19024e06585c754b6d663f43",
        "size": 11143,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d1232e2cfacfa1dd19024e06585c754b6d663f43"
    },
    {
        "path": "P04_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0d96d8b6759dc46e0af732be895a964967c0da09",
        "size": 15098,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0d96d8b6759dc46e0af732be895a964967c0da09"
    },
    {
        "path": "P04_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "012486c30ea04320f7d5608fbf91a6a19cf3cf93",
        "size": 15392,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/012486c30ea04320f7d5608fbf91a6a19cf3cf93"
    },
    {
        "path": "P04_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8032a7e452e0d2090cdd33fd00b4ef6153ac230b",
        "size": 15439,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8032a7e452e0d2090cdd33fd00b4ef6153ac230b"
    },
    {
        "path": "P04_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e50d9b3030bfd06c7d01e77d81f94a20fe4dd778",
        "size": 5240,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e50d9b3030bfd06c7d01e77d81f94a20fe4dd778"
    },
    {
        "path": "P04_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b5ec9daa358558d8386d6b9435e9aa756735840d",
        "size": 7369,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b5ec9daa358558d8386d6b9435e9aa756735840d"
    },
    {
        "path": "P04_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5399e8f294eb55d486fc9a74cf50f1d25cb08349",
        "size": 7144,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5399e8f294eb55d486fc9a74cf50f1d25cb08349"
    },
    {
        "path": "P04_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "27d7b0bf5012eab745cc1a3273edd0291ead1a3d",
        "size": 7420,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/27d7b0bf5012eab745cc1a3273edd0291ead1a3d"
    },
    {
        "path": "P04_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e9d83d45a1501ce826a17f94dc676f2bad3fd10d",
        "size": 10543,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e9d83d45a1501ce826a17f94dc676f2bad3fd10d"
    },
    {
        "path": "P04_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d63fe2469c46208c003943d290b1c285ee3474d8",
        "size": 5225,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d63fe2469c46208c003943d290b1c285ee3474d8"
    },
    {
        "path": "P04_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2147e3b51ab503bfbc83a405c7ee650ae9d48910",
        "size": 6797,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2147e3b51ab503bfbc83a405c7ee650ae9d48910"
    },
    {
        "path": "P04_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2698aca4af199ffd23d95c48c9f8e73092a75b67",
        "size": 6143,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2698aca4af199ffd23d95c48c9f8e73092a75b67"
    },
    {
        "path": "P04_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7b78d5d5852c95b50c7308b73dd5f25f6622e63e",
        "size": 4290,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7b78d5d5852c95b50c7308b73dd5f25f6622e63e"
    },
    {
        "path": "P04_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "14969f207c6aa6906bc2114966278a55f6b2b3b2",
        "size": 12081,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/14969f207c6aa6906bc2114966278a55f6b2b3b2"
    },
    {
        "path": "P04_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a3921a510cfe34ea8eba22b246d91ccf2855e3c4",
        "size": 9197,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a3921a510cfe34ea8eba22b246d91ccf2855e3c4"
    },
    {
        "path": "P04_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "12de1ca033e21e03b45a4fc5fd71e253650cc857",
        "size": 8937,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/12de1ca033e21e03b45a4fc5fd71e253650cc857"
    },
    {
        "path": "P04_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0047b370fe3984a3c2141883cf977c06c71f94f2",
        "size": 9676,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0047b370fe3984a3c2141883cf977c06c71f94f2"
    },
    {
        "path": "P04_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dd25e6317b27b2cc9ed5522cdcb8b5b8de03a508",
        "size": 12488,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dd25e6317b27b2cc9ed5522cdcb8b5b8de03a508"
    },
    {
        "path": "P04_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "457dfe34a988998b20535c0e4e130a089af36fd6",
        "size": 7858,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/457dfe34a988998b20535c0e4e130a089af36fd6"
    },
    {
        "path": "P04_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e99c5322571dc707b3c5200502c14e2d5e3da5fc",
        "size": 9222,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e99c5322571dc707b3c5200502c14e2d5e3da5fc"
    },
    {
        "path": "P04_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c3a427a0d9cc02c0283802c94b00db721bd22145",
        "size": 7730,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c3a427a0d9cc02c0283802c94b00db721bd22145"
    },
    {
        "path": "P04_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "53bf7b36d2ef4bc7e03e2efac63872c562dfb390",
        "size": 12446,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/53bf7b36d2ef4bc7e03e2efac63872c562dfb390"
    },
    {
        "path": "P04_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0a9d7db0c04bb874e23acc06389a6064e2531023",
        "size": 6543,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0a9d7db0c04bb874e23acc06389a6064e2531023"
    },
    {
        "path": "P04_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6e034cbe271e0f548396f1f7b2c76d083638f3f2",
        "size": 5370,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6e034cbe271e0f548396f1f7b2c76d083638f3f2"
    },
    {
        "path": "P04_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "379efe9a234a6fbd3c91870d42cec1fba2694381",
        "size": 10125,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/379efe9a234a6fbd3c91870d42cec1fba2694381"
    },
    {
        "path": "P04_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "591fd42003674f0a91e9724eef56a40ca5f89627",
        "size": 7977,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/591fd42003674f0a91e9724eef56a40ca5f89627"
    },
    {
        "path": "P04_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "402f0ae5b8ef66104cd929ef875cca3e79b74028",
        "size": 6431,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/402f0ae5b8ef66104cd929ef875cca3e79b74028"
    },
    {
        "path": "P04_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2248df1b96cd85f25b759ad1d6268d95756360dc",
        "size": 11934,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2248df1b96cd85f25b759ad1d6268d95756360dc"
    },
    {
        "path": "P04_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2b0699a531814f72a04c3a021d895eefcaf5197e",
        "size": 6686,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2b0699a531814f72a04c3a021d895eefcaf5197e"
    },
    {
        "path": "P04_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5ca35e5845f191d846f25672039db1cd5e9dacb9",
        "size": 23434,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5ca35e5845f191d846f25672039db1cd5e9dacb9"
    },
    {
        "path": "P04_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "413bdae0251054c3bd2ba12e328d458fd6576a99",
        "size": 9970,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/413bdae0251054c3bd2ba12e328d458fd6576a99"
    },
    {
        "path": "P04_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a659f1833c373fa6b7b5c3b2947ddf10c197a83b",
        "size": 10531,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a659f1833c373fa6b7b5c3b2947ddf10c197a83b"
    },
    {
        "path": "P04_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "629745ebb751079c9194c55436e5919ff73f36a7",
        "size": 7620,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/629745ebb751079c9194c55436e5919ff73f36a7"
    },
    {
        "path": "P04_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8884153d83a1d9b96489d2b5f2dea8713ad05f24",
        "size": 13626,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8884153d83a1d9b96489d2b5f2dea8713ad05f24"
    },
    {
        "path": "P04_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6f291cd806406182fece03fa7a2c0c142327bac5",
        "size": 18152,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6f291cd806406182fece03fa7a2c0c142327bac5"
    },
    {
        "path": "P05_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7114b28661647021dba9400c546c86d88f29bfd4",
        "size": 9310,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7114b28661647021dba9400c546c86d88f29bfd4"
    },
    {
        "path": "P05_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "25fd213b165a972a07c243c2ecc7c9fb78980dc3",
        "size": 7029,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/25fd213b165a972a07c243c2ecc7c9fb78980dc3"
    },
    {
        "path": "P05_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "569eaf1cbdbbe6a0f6fa14ea391c17e8a93d98be",
        "size": 10075,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/569eaf1cbdbbe6a0f6fa14ea391c17e8a93d98be"
    },
    {
        "path": "P05_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a89ffd864c6b68480539600b9107c968cd66f344",
        "size": 9593,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a89ffd864c6b68480539600b9107c968cd66f344"
    },
    {
        "path": "P05_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "87432b77330ed8abf2ef13be4c76d8d3529d55b3",
        "size": 6369,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/87432b77330ed8abf2ef13be4c76d8d3529d55b3"
    },
    {
        "path": "P05_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4958d4e03b9e6c6eee57b15b0e00621e70aae381",
        "size": 5594,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4958d4e03b9e6c6eee57b15b0e00621e70aae381"
    },
    {
        "path": "P05_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "84a97c98860633c8e169c00486b5871fa6d78ee4",
        "size": 7782,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/84a97c98860633c8e169c00486b5871fa6d78ee4"
    },
    {
        "path": "P05_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "faec5d52bdc985e78f92fe31d8cf1a7d6cb9c6a0",
        "size": 7950,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/faec5d52bdc985e78f92fe31d8cf1a7d6cb9c6a0"
    },
    {
        "path": "P05_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "44b808008d87b0da0d073625454879dd8e60e6cd",
        "size": 8758,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/44b808008d87b0da0d073625454879dd8e60e6cd"
    },
    {
        "path": "P05_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "770cd2258462894f4fe432feb46d0f224172a959",
        "size": 10070,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/770cd2258462894f4fe432feb46d0f224172a959"
    },
    {
        "path": "P05_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4b82fa951a0ce7febefbe76c222d8dd7f4a1d4ed",
        "size": 5304,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4b82fa951a0ce7febefbe76c222d8dd7f4a1d4ed"
    },
    {
        "path": "P05_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "59e868c3d923100ffc580726f9d267eb03a78407",
        "size": 5042,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/59e868c3d923100ffc580726f9d267eb03a78407"
    },
    {
        "path": "P05_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b0512890edc054ef1de1893c4a988f98eb22ebb4",
        "size": 5865,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b0512890edc054ef1de1893c4a988f98eb22ebb4"
    },
    {
        "path": "P05_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "235d0c1297dd54651e99289a01527f316a5b8fc9",
        "size": 7009,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/235d0c1297dd54651e99289a01527f316a5b8fc9"
    },
    {
        "path": "P05_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "61362146c0f9bc2f73f1966be673690c6c796629",
        "size": 6152,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/61362146c0f9bc2f73f1966be673690c6c796629"
    },
    {
        "path": "P05_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "41312c444265391daabfc7eb9059a9b78c381d3d",
        "size": 8791,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/41312c444265391daabfc7eb9059a9b78c381d3d"
    },
    {
        "path": "P05_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f28324878819c59d5df4f19b3dd9d6b4e5af6585",
        "size": 7756,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f28324878819c59d5df4f19b3dd9d6b4e5af6585"
    },
    {
        "path": "P05_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2b7827922bd9899492c24910bc068b155c7196d2",
        "size": 8216,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2b7827922bd9899492c24910bc068b155c7196d2"
    },
    {
        "path": "P05_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e84ef308f6c5fa3974d27ac8bf6b6be6ed4e2500",
        "size": 7396,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e84ef308f6c5fa3974d27ac8bf6b6be6ed4e2500"
    },
    {
        "path": "P05_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "90d66179e023704967fc8d6891e90d53f5867abb",
        "size": 8491,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/90d66179e023704967fc8d6891e90d53f5867abb"
    },
    {
        "path": "P05_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8855ae3c19515f290dbf8d5f78822adfe2cd7ba1",
        "size": 5041,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8855ae3c19515f290dbf8d5f78822adfe2cd7ba1"
    },
    {
        "path": "P05_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e04aafa9fdf02c5c85063cf2e6b88b11a248e9a8",
        "size": 9104,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e04aafa9fdf02c5c85063cf2e6b88b11a248e9a8"
    },
    {
        "path": "P05_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "56970a2aecdfca460169863252ba924a5f832f66",
        "size": 9081,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/56970a2aecdfca460169863252ba924a5f832f66"
    },
    {
        "path": "P05_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "35064a0270174576a73713665ea3a9943e2b6d09",
        "size": 7512,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/35064a0270174576a73713665ea3a9943e2b6d09"
    },
    {
        "path": "P05_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3fd57b5d611ddfb9282506578f30bdc4e5b9fa3d",
        "size": 7653,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3fd57b5d611ddfb9282506578f30bdc4e5b9fa3d"
    },
    {
        "path": "P05_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0bcd0ee9ae23bdd06db59918e74320d8613cb880",
        "size": 6011,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0bcd0ee9ae23bdd06db59918e74320d8613cb880"
    },
    {
        "path": "P05_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1fb9df6ca5249efca1f2d77cf1d95d4c17cf0dd4",
        "size": 10256,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1fb9df6ca5249efca1f2d77cf1d95d4c17cf0dd4"
    },
    {
        "path": "P05_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "78832ab6d3077e7befb83b08a7d37f40ef8fc1f6",
        "size": 7494,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/78832ab6d3077e7befb83b08a7d37f40ef8fc1f6"
    },
    {
        "path": "P05_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5c170b01061242d1ebd3c25c1d9b8d99e1f47501",
        "size": 7154,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5c170b01061242d1ebd3c25c1d9b8d99e1f47501"
    },
    {
        "path": "P05_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "adc6072eaa9cfcec4f992c8a04ad2c8823e377b3",
        "size": 7401,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/adc6072eaa9cfcec4f992c8a04ad2c8823e377b3"
    },
    {
        "path": "P05_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "88778522e8c12baf1b1a2b7ab293dd02719f1185",
        "size": 8664,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/88778522e8c12baf1b1a2b7ab293dd02719f1185"
    },
    {
        "path": "P05_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "309f34821f3a45e90a3a413107f13b5c7e7b51f8",
        "size": 5376,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/309f34821f3a45e90a3a413107f13b5c7e7b51f8"
    },
    {
        "path": "P05_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d45a0a76b12ea3d30941bdd0e05106a29bfecd3c",
        "size": 5243,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d45a0a76b12ea3d30941bdd0e05106a29bfecd3c"
    },
    {
        "path": "P05_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5b799bdb4a684a0d8361c5acaafea2026772ef09",
        "size": 5716,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5b799bdb4a684a0d8361c5acaafea2026772ef09"
    },
    {
        "path": "P05_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "80879ed6a1dcce64985d870ac90985295cde7b6e",
        "size": 9544,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/80879ed6a1dcce64985d870ac90985295cde7b6e"
    },
    {
        "path": "P05_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "40d87766a22631cf18ba778a96c89e6251e6b26a",
        "size": 7783,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/40d87766a22631cf18ba778a96c89e6251e6b26a"
    },
    {
        "path": "P05_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8c64516750d50fc87855475f7148f7bdd9b283c8",
        "size": 6626,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8c64516750d50fc87855475f7148f7bdd9b283c8"
    },
    {
        "path": "P05_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b3cf9872fb8d12e1197b9e91e6f0ed0aa166708c",
        "size": 6943,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b3cf9872fb8d12e1197b9e91e6f0ed0aa166708c"
    },
    {
        "path": "P05_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d71b3a4ce1233832d682f0039878e74a330ea154",
        "size": 10931,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d71b3a4ce1233832d682f0039878e74a330ea154"
    },
    {
        "path": "P05_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b2eb7cc2a97222606c4808c42eef62b716789e18",
        "size": 8828,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b2eb7cc2a97222606c4808c42eef62b716789e18"
    },
    {
        "path": "P05_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "eb5d098f9c63b857811d13dfa902f67ab7d6ace3",
        "size": 6478,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/eb5d098f9c63b857811d13dfa902f67ab7d6ace3"
    },
    {
        "path": "P05_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b9eb5c167d109870edaa228aee75e519e35dd842",
        "size": 7781,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b9eb5c167d109870edaa228aee75e519e35dd842"
    },
    {
        "path": "P05_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b267ebe8391cb2b7efb79ee2bed10c79fa713691",
        "size": 9156,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b267ebe8391cb2b7efb79ee2bed10c79fa713691"
    },
    {
        "path": "P05_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5279d209931897c0cf3a7ce14fc464090eb5dcba",
        "size": 9240,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5279d209931897c0cf3a7ce14fc464090eb5dcba"
    },
    {
        "path": "P05_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "358d99f608f3be4aaaab5b056a626319f8dc7a69",
        "size": 7591,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/358d99f608f3be4aaaab5b056a626319f8dc7a69"
    },
    {
        "path": "P05_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "97b5ed85757347b200878d8eb55c7c738e352695",
        "size": 10195,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/97b5ed85757347b200878d8eb55c7c738e352695"
    },
    {
        "path": "P05_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0945e2f47bf621cfcf1cfdcee48beab323afd217",
        "size": 5111,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0945e2f47bf621cfcf1cfdcee48beab323afd217"
    },
    {
        "path": "P05_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "79961efb49285a096abacb0e267b4896da75eca8",
        "size": 5161,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/79961efb49285a096abacb0e267b4896da75eca8"
    },
    {
        "path": "P05_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bab81f242961cfc65949f898049974094ec760e7",
        "size": 8486,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bab81f242961cfc65949f898049974094ec760e7"
    },
    {
        "path": "P05_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "46adcf16c9e67a3433f5c3675eca3df07ab92781",
        "size": 6071,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/46adcf16c9e67a3433f5c3675eca3df07ab92781"
    },
    {
        "path": "P05_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16c4d272c6e5c897f8cb72c60a649acbf3841a7d",
        "size": 4088,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16c4d272c6e5c897f8cb72c60a649acbf3841a7d"
    },
    {
        "path": "P05_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "875964cf427c557399be23b27e803887b58450c8",
        "size": 7496,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/875964cf427c557399be23b27e803887b58450c8"
    },
    {
        "path": "P05_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e6429c320d0b533b2b1a16153f1170384e910206",
        "size": 8754,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e6429c320d0b533b2b1a16153f1170384e910206"
    },
    {
        "path": "P05_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0da33df115bc79273c492fb77efc2187763856f4",
        "size": 9369,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0da33df115bc79273c492fb77efc2187763856f4"
    },
    {
        "path": "P05_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0ee4a688e3f2e1d1c0021b50369f5a9181d2771d",
        "size": 7397,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0ee4a688e3f2e1d1c0021b50369f5a9181d2771d"
    },
    {
        "path": "P05_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7d2a16a902b74386052ad805afa0680795ac0bc7",
        "size": 7703,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7d2a16a902b74386052ad805afa0680795ac0bc7"
    },
    {
        "path": "P05_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5d495cc30e4e0dfd7ee77298d4c32b5020287135",
        "size": 5526,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5d495cc30e4e0dfd7ee77298d4c32b5020287135"
    },
    {
        "path": "P05_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16dbeb95a691b437c99fa12c53b1233c6c8a8193",
        "size": 8971,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16dbeb95a691b437c99fa12c53b1233c6c8a8193"
    },
    {
        "path": "P05_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d33576c2ab374278a67b7f3f0323cbaa6d82ea9b",
        "size": 18548,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d33576c2ab374278a67b7f3f0323cbaa6d82ea9b"
    },
    {
        "path": "P06_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e45f6c14a10b5b29471729d98f2c319ba5924e2a",
        "size": 9018,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e45f6c14a10b5b29471729d98f2c319ba5924e2a"
    },
    {
        "path": "P06_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "29f160517d07d5ecafbb9f6ffdf6cf253cfd28fa",
        "size": 7099,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/29f160517d07d5ecafbb9f6ffdf6cf253cfd28fa"
    },
    {
        "path": "P06_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "af0acf0453b2dee489c8443786d3067b10a7e425",
        "size": 9639,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/af0acf0453b2dee489c8443786d3067b10a7e425"
    },
    {
        "path": "P06_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5ca2b0902cc8ba0b877a25fa75e03051b7b087cc",
        "size": 12350,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5ca2b0902cc8ba0b877a25fa75e03051b7b087cc"
    },
    {
        "path": "P06_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3ba4a7e97af463bcfd8713fec1b9e90c0c22ab6f",
        "size": 9922,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3ba4a7e97af463bcfd8713fec1b9e90c0c22ab6f"
    },
    {
        "path": "P06_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f5170418264304ceaf4d6c9fe30fa1c940233680",
        "size": 12053,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f5170418264304ceaf4d6c9fe30fa1c940233680"
    },
    {
        "path": "P06_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4fb06bb4ad6a9fc3f3d3bf83c6bb8e6c83cbdb22",
        "size": 7696,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4fb06bb4ad6a9fc3f3d3bf83c6bb8e6c83cbdb22"
    },
    {
        "path": "P06_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f3db7ba4163f778882125fd78c1f749e5e599f83",
        "size": 14489,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f3db7ba4163f778882125fd78c1f749e5e599f83"
    },
    {
        "path": "P06_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "94c89984e7536b3161485ceabb8756495add39a8",
        "size": 11625,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/94c89984e7536b3161485ceabb8756495add39a8"
    },
    {
        "path": "P06_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1a129fc63e80d2f8dc639a7806f8fffcc71a3327",
        "size": 8462,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1a129fc63e80d2f8dc639a7806f8fffcc71a3327"
    },
    {
        "path": "P06_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ccb0ff9b59cc3da9846ad92b243a2c0bf5741c0f",
        "size": 8328,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ccb0ff9b59cc3da9846ad92b243a2c0bf5741c0f"
    },
    {
        "path": "P06_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b91fa4c0d6678345343063d4d607eb744a713e33",
        "size": 7503,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b91fa4c0d6678345343063d4d607eb744a713e33"
    },
    {
        "path": "P06_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "61dc105416a97869b71895e88e9ec4ee575b6f02",
        "size": 9296,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/61dc105416a97869b71895e88e9ec4ee575b6f02"
    },
    {
        "path": "P06_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "606f13223153b2cb4484d07e0984b2f6cde6e7bc",
        "size": 9776,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/606f13223153b2cb4484d07e0984b2f6cde6e7bc"
    },
    {
        "path": "P06_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "62c125cc29dc1f4cc467735464fa248e606b1892",
        "size": 7734,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/62c125cc29dc1f4cc467735464fa248e606b1892"
    },
    {
        "path": "P06_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6724d22655ddfaa8c2f563041fe20e5c523894eb",
        "size": 9295,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6724d22655ddfaa8c2f563041fe20e5c523894eb"
    },
    {
        "path": "P06_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "707f1cfb8b974836224bfc5961377ecb8c4d59c1",
        "size": 7174,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/707f1cfb8b974836224bfc5961377ecb8c4d59c1"
    },
    {
        "path": "P06_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dba017e63d3900cbd6324d41094b20e54c1b9ed8",
        "size": 8936,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dba017e63d3900cbd6324d41094b20e54c1b9ed8"
    },
    {
        "path": "P06_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "27362abc4ad6eee652d3faacf68958b2f420139d",
        "size": 10666,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/27362abc4ad6eee652d3faacf68958b2f420139d"
    },
    {
        "path": "P06_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0db6374dc6ef11ebaed366ce617b8719be068a63",
        "size": 11292,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0db6374dc6ef11ebaed366ce617b8719be068a63"
    },
    {
        "path": "P06_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "631bf1b69ba4976497231a513a3af04c1d7f3146",
        "size": 5926,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/631bf1b69ba4976497231a513a3af04c1d7f3146"
    },
    {
        "path": "P06_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bb1707c0fedb3c7cd5284b3db6d24ab40937c424",
        "size": 5585,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bb1707c0fedb3c7cd5284b3db6d24ab40937c424"
    },
    {
        "path": "P06_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cee12d5140f9f47526ff5d84712c1f14681c6bf8",
        "size": 13923,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cee12d5140f9f47526ff5d84712c1f14681c6bf8"
    },
    {
        "path": "P06_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "461158df2abbd91fa72275514a6f4e4b4996bfa8",
        "size": 9411,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/461158df2abbd91fa72275514a6f4e4b4996bfa8"
    },
    {
        "path": "P06_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "017617656643eae411f5eec6cc4f8de829175505",
        "size": 7918,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/017617656643eae411f5eec6cc4f8de829175505"
    },
    {
        "path": "P06_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0c610ffb7aaf97c47957aa3d028c50ee77436797",
        "size": 8684,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0c610ffb7aaf97c47957aa3d028c50ee77436797"
    },
    {
        "path": "P06_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b0de2df9ec74ea40be2f8107f646456bf560ed6d",
        "size": 7371,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b0de2df9ec74ea40be2f8107f646456bf560ed6d"
    },
    {
        "path": "P06_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "18ebea38129f914ac4c3091616e858f88e8d683c",
        "size": 11441,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/18ebea38129f914ac4c3091616e858f88e8d683c"
    },
    {
        "path": "P06_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16e36810ade6437cc4b3c425fc5fbfee647fcf4c",
        "size": 9474,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16e36810ade6437cc4b3c425fc5fbfee647fcf4c"
    },
    {
        "path": "P06_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "acb3ba37a7d944dd6877312a0f113fd568c906ad",
        "size": 7489,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/acb3ba37a7d944dd6877312a0f113fd568c906ad"
    },
    {
        "path": "P06_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6c2d80f5ec5a404abce757b506e101301ec86f74",
        "size": 6077,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6c2d80f5ec5a404abce757b506e101301ec86f74"
    },
    {
        "path": "P06_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "67372d43411bf475451c881a5f321c925756369d",
        "size": 7267,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/67372d43411bf475451c881a5f321c925756369d"
    },
    {
        "path": "P06_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "99d710c95df1ef8cba769861c670f9d884e65205",
        "size": 6673,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/99d710c95df1ef8cba769861c670f9d884e65205"
    },
    {
        "path": "P06_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "08bfca3b7f6af30dc4afe5ca30d6a79e6db4ef03",
        "size": 8110,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/08bfca3b7f6af30dc4afe5ca30d6a79e6db4ef03"
    },
    {
        "path": "P06_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5177cc95e06313d48f49da1cb52145635e9ee9d3",
        "size": 4624,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5177cc95e06313d48f49da1cb52145635e9ee9d3"
    },
    {
        "path": "P06_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cb18990930d9e4c8d95298e57ca78b34f315d97c",
        "size": 7777,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cb18990930d9e4c8d95298e57ca78b34f315d97c"
    },
    {
        "path": "P06_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0a3830d9d95683ecd6ff546ed5a4f16b31cc4950",
        "size": 9212,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0a3830d9d95683ecd6ff546ed5a4f16b31cc4950"
    },
    {
        "path": "P06_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7aa1c638daa39735d12c4e8da3680f3cfd591c2d",
        "size": 7567,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7aa1c638daa39735d12c4e8da3680f3cfd591c2d"
    },
    {
        "path": "P06_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e19a3195e03df7132abb31ad9d134a5deb2af71a",
        "size": 5653,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e19a3195e03df7132abb31ad9d134a5deb2af71a"
    },
    {
        "path": "P06_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4358e41f1678835fc572806ebacb0cd245d7dd99",
        "size": 9781,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4358e41f1678835fc572806ebacb0cd245d7dd99"
    },
    {
        "path": "P06_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "17532f5d244e08f7055bb23df4b0469afb2cef2b",
        "size": 6281,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/17532f5d244e08f7055bb23df4b0469afb2cef2b"
    },
    {
        "path": "P06_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "db689de4f165a53e1400231f222d7e5d8c0c68e0",
        "size": 8388,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/db689de4f165a53e1400231f222d7e5d8c0c68e0"
    },
    {
        "path": "P06_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1fdce4c15d5d11524498368b6fb16d302a852d76",
        "size": 8255,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1fdce4c15d5d11524498368b6fb16d302a852d76"
    },
    {
        "path": "P06_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fb2f5fdc05ac1f5c637d2c2595e85569b5f4e5ba",
        "size": 10874,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fb2f5fdc05ac1f5c637d2c2595e85569b5f4e5ba"
    },
    {
        "path": "P06_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "45eba1bf047c0334fecdd8b72dfd59394c27c631",
        "size": 8059,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/45eba1bf047c0334fecdd8b72dfd59394c27c631"
    },
    {
        "path": "P06_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "76531636d80d87fc4c7247bd6e4df118b9c49b16",
        "size": 6265,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/76531636d80d87fc4c7247bd6e4df118b9c49b16"
    },
    {
        "path": "P06_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "730f35665a35a94b82f39736fc63c0abd02139b9",
        "size": 9852,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/730f35665a35a94b82f39736fc63c0abd02139b9"
    },
    {
        "path": "P06_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2409dce8d3557a712fdd2d3c63afdb229ecd40fd",
        "size": 8948,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2409dce8d3557a712fdd2d3c63afdb229ecd40fd"
    },
    {
        "path": "P06_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "60b569f97ad514495d97f29b69f662a35ae12c6b",
        "size": 6051,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/60b569f97ad514495d97f29b69f662a35ae12c6b"
    },
    {
        "path": "P06_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cb34f8ef7d78d082859a56308496a56d736fac1a",
        "size": 8396,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cb34f8ef7d78d082859a56308496a56d736fac1a"
    },
    {
        "path": "P06_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "da9bba1c2812037726a6a4bf64dbe8ec2e76a4e9",
        "size": 10517,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/da9bba1c2812037726a6a4bf64dbe8ec2e76a4e9"
    },
    {
        "path": "P06_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e8fc75dcf35484ab0f74e4f67269e8655b1ce676",
        "size": 4636,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e8fc75dcf35484ab0f74e4f67269e8655b1ce676"
    },
    {
        "path": "P06_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9631af426a1332447e4d01d338b12c648f99f3d4",
        "size": 10112,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9631af426a1332447e4d01d338b12c648f99f3d4"
    },
    {
        "path": "P06_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "56c1e160110fe45b8b6f021af18b6f474ce5a7ad",
        "size": 9438,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/56c1e160110fe45b8b6f021af18b6f474ce5a7ad"
    },
    {
        "path": "P06_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "93224b597e355065ca002f174fcd19ded834cc17",
        "size": 11430,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/93224b597e355065ca002f174fcd19ded834cc17"
    },
    {
        "path": "P06_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3e733de026166c5b9fbc58548048600c20e28c64",
        "size": 7954,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3e733de026166c5b9fbc58548048600c20e28c64"
    },
    {
        "path": "P06_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7de7cd5818305dd919200e9a07ff9127ea77e371",
        "size": 9559,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7de7cd5818305dd919200e9a07ff9127ea77e371"
    },
    {
        "path": "P06_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a998b4b0015103d4ebfae92454b274a9a9488aa2",
        "size": 6365,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a998b4b0015103d4ebfae92454b274a9a9488aa2"
    },
    {
        "path": "P06_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e332902c6a48e2df9bb179b636aae3b942c5cec4",
        "size": 9563,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e332902c6a48e2df9bb179b636aae3b942c5cec4"
    },
    {
        "path": "P06_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "37a56c969138f66072ced3a9bcbb589f7bda73f6",
        "size": 16212,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/37a56c969138f66072ced3a9bcbb589f7bda73f6"
    },
    {
        "path": "P07_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c48ceb80258a00d2be799d0d40d9f6a7e311654c",
        "size": 4343,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c48ceb80258a00d2be799d0d40d9f6a7e311654c"
    },
    {
        "path": "P07_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b1e9f0dcf991a7129bfbd7aedaa1d82765d7dc38",
        "size": 7183,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b1e9f0dcf991a7129bfbd7aedaa1d82765d7dc38"
    },
    {
        "path": "P07_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9ff71641750b641e4619a406748d053e7e4e1b6f",
        "size": 8821,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9ff71641750b641e4619a406748d053e7e4e1b6f"
    },
    {
        "path": "P07_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "60ebeae6fd70d2cbefd728e9c31fee2f8c336d78",
        "size": 10762,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/60ebeae6fd70d2cbefd728e9c31fee2f8c336d78"
    },
    {
        "path": "P07_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "41a994e00769c33742f0ebb49e6634970f35e238",
        "size": 7632,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/41a994e00769c33742f0ebb49e6634970f35e238"
    },
    {
        "path": "P07_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9a5aa4778fc3b248d2d2865e8165ef15f001498d",
        "size": 9002,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9a5aa4778fc3b248d2d2865e8165ef15f001498d"
    },
    {
        "path": "P07_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3bd899f35480cb550f07305817eda19d0f3ccc40",
        "size": 13679,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3bd899f35480cb550f07305817eda19d0f3ccc40"
    },
    {
        "path": "P07_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d8e06f062434111dbc97693cb202a9ad20ad790a",
        "size": 10665,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d8e06f062434111dbc97693cb202a9ad20ad790a"
    },
    {
        "path": "P07_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f792929e3a118a71de7df65863d0bd941d9257a0",
        "size": 9450,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f792929e3a118a71de7df65863d0bd941d9257a0"
    },
    {
        "path": "P07_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "49de194deaa0d8314cdd47ed9852c81a422af4b5",
        "size": 8454,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/49de194deaa0d8314cdd47ed9852c81a422af4b5"
    },
    {
        "path": "P07_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "36c2d4c980718cfcbff4f09afe42fa5f750b0be3",
        "size": 5793,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/36c2d4c980718cfcbff4f09afe42fa5f750b0be3"
    },
    {
        "path": "P07_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c7ebafa289bcb819e1b04a43e0f48b849f4ea445",
        "size": 5310,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c7ebafa289bcb819e1b04a43e0f48b849f4ea445"
    },
    {
        "path": "P07_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f599b89e695f80eb87378e0bfb71a702ee1810d4",
        "size": 6677,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f599b89e695f80eb87378e0bfb71a702ee1810d4"
    },
    {
        "path": "P07_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ad98cb2f8c794966f2b9747f2eec0d839c4a1cf0",
        "size": 7111,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ad98cb2f8c794966f2b9747f2eec0d839c4a1cf0"
    },
    {
        "path": "P07_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "09b91a99268f186549cdaf3d75d7226cfcce9e2d",
        "size": 9514,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/09b91a99268f186549cdaf3d75d7226cfcce9e2d"
    },
    {
        "path": "P07_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d7ccf8770724b2ea53b48b4ff8c69b080c4aa6dd",
        "size": 9968,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d7ccf8770724b2ea53b48b4ff8c69b080c4aa6dd"
    },
    {
        "path": "P07_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "af065224914c3adebdc3f5a36ae4498b27ac8182",
        "size": 7095,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/af065224914c3adebdc3f5a36ae4498b27ac8182"
    },
    {
        "path": "P07_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b28f4a8ed4e28dce5f338806473fad92726d95cd",
        "size": 9380,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b28f4a8ed4e28dce5f338806473fad92726d95cd"
    },
    {
        "path": "P07_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6a910ec08fc2b506556f382691768f8bf5efb67b",
        "size": 9122,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6a910ec08fc2b506556f382691768f8bf5efb67b"
    },
    {
        "path": "P07_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "398c6200620eade9ff4fd1b482492b21c476b91e",
        "size": 8198,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/398c6200620eade9ff4fd1b482492b21c476b91e"
    },
    {
        "path": "P07_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "36c66ddc439e39e4f089f98b0b028a69a6cecf9b",
        "size": 7487,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/36c66ddc439e39e4f089f98b0b028a69a6cecf9b"
    },
    {
        "path": "P07_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "22ec8b86ae17f283311c76296bc942a8c4e9bd14",
        "size": 4357,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/22ec8b86ae17f283311c76296bc942a8c4e9bd14"
    },
    {
        "path": "P07_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8a093d2f2eb91836bfc2fe24d9dcad48fdc23182",
        "size": 11723,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8a093d2f2eb91836bfc2fe24d9dcad48fdc23182"
    },
    {
        "path": "P07_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5900c54e1633ff05d0c6bcb19c4586f8d85534b1",
        "size": 10220,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5900c54e1633ff05d0c6bcb19c4586f8d85534b1"
    },
    {
        "path": "P07_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d25b381fa02c58574e6d385cfe50d062b08b0279",
        "size": 6671,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d25b381fa02c58574e6d385cfe50d062b08b0279"
    },
    {
        "path": "P07_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0bb189cc97375591acf717cf217d4f36961dac00",
        "size": 6430,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0bb189cc97375591acf717cf217d4f36961dac00"
    },
    {
        "path": "P07_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1e1bc896440803ed1a03afd57965fa4c6d2ad1d5",
        "size": 6751,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1e1bc896440803ed1a03afd57965fa4c6d2ad1d5"
    },
    {
        "path": "P07_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4f624c3eb61b03469415609f133c437a3cae97c8",
        "size": 11895,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4f624c3eb61b03469415609f133c437a3cae97c8"
    },
    {
        "path": "P07_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f991da41d78609d299cc4a76a9817cd51f6933f0",
        "size": 8254,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f991da41d78609d299cc4a76a9817cd51f6933f0"
    },
    {
        "path": "P07_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9d22b9e6511efc10e39013955af30051cd98c517",
        "size": 6897,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9d22b9e6511efc10e39013955af30051cd98c517"
    },
    {
        "path": "P07_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ec7aebcebf13fadf3252b843f09ac43c5e625ab2",
        "size": 4417,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ec7aebcebf13fadf3252b843f09ac43c5e625ab2"
    },
    {
        "path": "P07_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c974dc0078437fa71d2fda8401239fd95fb3310a",
        "size": 8746,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c974dc0078437fa71d2fda8401239fd95fb3310a"
    },
    {
        "path": "P07_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6238d2f2c5ae505c398ce5cd1f068b418587f72e",
        "size": 5035,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6238d2f2c5ae505c398ce5cd1f068b418587f72e"
    },
    {
        "path": "P07_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a15740ddd1588f08f5253689f42be8c911d03c22",
        "size": 6619,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a15740ddd1588f08f5253689f42be8c911d03c22"
    },
    {
        "path": "P07_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2a5df264cf974a318290a1d56134b83e469f9645",
        "size": 4338,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2a5df264cf974a318290a1d56134b83e469f9645"
    },
    {
        "path": "P07_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dca06b52ad53770ed5bc322ae0b2b7a7aa4fb8ba",
        "size": 7603,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dca06b52ad53770ed5bc322ae0b2b7a7aa4fb8ba"
    },
    {
        "path": "P07_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3b1d72530a60e397a0e2afe9de7bc2f127fb8c64",
        "size": 6895,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3b1d72530a60e397a0e2afe9de7bc2f127fb8c64"
    },
    {
        "path": "P07_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "effe017dc98ab4e15b19a052d36de4d7dae38092",
        "size": 5501,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/effe017dc98ab4e15b19a052d36de4d7dae38092"
    },
    {
        "path": "P07_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4c6674c5b6eb5235c272eff6a75bc5ed75cf040e",
        "size": 7871,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4c6674c5b6eb5235c272eff6a75bc5ed75cf040e"
    },
    {
        "path": "P07_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5494602ed0b6a867b6796b443270e16e29f99f94",
        "size": 8695,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5494602ed0b6a867b6796b443270e16e29f99f94"
    },
    {
        "path": "P07_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "023d6aebe04cc0910923881d9939a47498d368a9",
        "size": 5806,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/023d6aebe04cc0910923881d9939a47498d368a9"
    },
    {
        "path": "P07_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "277241ffe9e6bb52f1a7f07dd0e22858180085d4",
        "size": 10658,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/277241ffe9e6bb52f1a7f07dd0e22858180085d4"
    },
    {
        "path": "P07_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1258c54e4d7281e7fc70c31308f28ab2fb5cf1d1",
        "size": 12591,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1258c54e4d7281e7fc70c31308f28ab2fb5cf1d1"
    },
    {
        "path": "P07_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ae979a5322344eebb040e8e7234ccde15b995e7d",
        "size": 10200,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ae979a5322344eebb040e8e7234ccde15b995e7d"
    },
    {
        "path": "P07_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fa4d2f924c9e05a227a49ea0554e92c4284f55ff",
        "size": 6685,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fa4d2f924c9e05a227a49ea0554e92c4284f55ff"
    },
    {
        "path": "P07_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8f7ac34d7f89de2594609ee4613e69bca3a4dd42",
        "size": 6748,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8f7ac34d7f89de2594609ee4613e69bca3a4dd42"
    },
    {
        "path": "P07_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "da83195d5d94e274bd22387845a30206a188de5b",
        "size": 12214,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/da83195d5d94e274bd22387845a30206a188de5b"
    },
    {
        "path": "P07_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a133964f26b77287b370ad01d477b7576391f152",
        "size": 5653,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a133964f26b77287b370ad01d477b7576391f152"
    },
    {
        "path": "P07_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3ab7e0f0650732fd61bbcd32dd0c25c020e6b91c",
        "size": 6470,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3ab7e0f0650732fd61bbcd32dd0c25c020e6b91c"
    },
    {
        "path": "P07_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cd24a4187fae09e70e99a5b233f906f5a58e00e7",
        "size": 7792,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cd24a4187fae09e70e99a5b233f906f5a58e00e7"
    },
    {
        "path": "P07_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4416e49d66982ef7e255e3752868b11d4a58e3ee",
        "size": 5602,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4416e49d66982ef7e255e3752868b11d4a58e3ee"
    },
    {
        "path": "P07_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "05151bd76e90b387004af737865722ab77c976cb",
        "size": 7795,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/05151bd76e90b387004af737865722ab77c976cb"
    },
    {
        "path": "P07_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f864932639189fa97ba3eb2270132a3230f0a671",
        "size": 9212,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f864932639189fa97ba3eb2270132a3230f0a671"
    },
    {
        "path": "P07_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2dc18c5ea221c5b552cb9de2575118f75caa07e3",
        "size": 12950,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2dc18c5ea221c5b552cb9de2575118f75caa07e3"
    },
    {
        "path": "P07_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6036c56bd93557769f56584ba9ae3eb43b9e4d93",
        "size": 9098,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6036c56bd93557769f56584ba9ae3eb43b9e4d93"
    },
    {
        "path": "P07_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6cdfa0dd45d824f7d8a3eaed53c0fdf1fdd055ce",
        "size": 7850,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6cdfa0dd45d824f7d8a3eaed53c0fdf1fdd055ce"
    },
    {
        "path": "P07_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f67b799407daec44023dcf8f933b02c2d13ca030",
        "size": 8351,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f67b799407daec44023dcf8f933b02c2d13ca030"
    },
    {
        "path": "P07_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "677f75de2c5c67b3e072fc031bac2bfdb5d9e44b",
        "size": 7426,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/677f75de2c5c67b3e072fc031bac2bfdb5d9e44b"
    },
    {
        "path": "P07_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d9a5f5fd6977b25d0ee010c30950b3ed91f57d8e",
        "size": 9551,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d9a5f5fd6977b25d0ee010c30950b3ed91f57d8e"
    },
    {
        "path": "P07_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f4a81684475b87c04b12037d44598c2701c513f8",
        "size": 18252,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f4a81684475b87c04b12037d44598c2701c513f8"
    },
    {
        "path": "P08_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "69cd642be5b34a6cf73f34927eeaf2520178dbae",
        "size": 11829,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/69cd642be5b34a6cf73f34927eeaf2520178dbae"
    },
    {
        "path": "P08_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9a813492d6745a6d60053cf5c0fe24af2c00002c",
        "size": 7092,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9a813492d6745a6d60053cf5c0fe24af2c00002c"
    },
    {
        "path": "P08_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "72d9aa3fcf5b489a7c2ac552dd3a592cb4dd681c",
        "size": 18208,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/72d9aa3fcf5b489a7c2ac552dd3a592cb4dd681c"
    },
    {
        "path": "P08_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "becef47311f1de34981f315d8a0c1e7e7e6f0328",
        "size": 15724,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/becef47311f1de34981f315d8a0c1e7e7e6f0328"
    },
    {
        "path": "P08_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "36a197e5d1c5fae240ef2e8432d4114bacadddab",
        "size": 17505,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/36a197e5d1c5fae240ef2e8432d4114bacadddab"
    },
    {
        "path": "P08_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c09e0f851d1b6712ede9ca6a6fafc5e4d0fa3527",
        "size": 11994,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c09e0f851d1b6712ede9ca6a6fafc5e4d0fa3527"
    },
    {
        "path": "P08_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e48d69ab74dd2277ef3f0ebdc662df9a1c7fad1b",
        "size": 7820,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e48d69ab74dd2277ef3f0ebdc662df9a1c7fad1b"
    },
    {
        "path": "P08_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fd2c505b2d8ba65cb6825cdaf32fae2f0fdcc017",
        "size": 14749,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fd2c505b2d8ba65cb6825cdaf32fae2f0fdcc017"
    },
    {
        "path": "P08_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fbf1e3827335103ac1a3d2a87c985ef520a91cc4",
        "size": 11469,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fbf1e3827335103ac1a3d2a87c985ef520a91cc4"
    },
    {
        "path": "P08_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "13c8dba602a81579e8f343baecfcb4b6c3db3ec6",
        "size": 15224,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/13c8dba602a81579e8f343baecfcb4b6c3db3ec6"
    },
    {
        "path": "P08_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5b80b3f3b5c7868b23751a002a8957935ce44e00",
        "size": 11139,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5b80b3f3b5c7868b23751a002a8957935ce44e00"
    },
    {
        "path": "P08_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c4defd47d49ea068fe40cef12afaf49f507c2839",
        "size": 11475,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c4defd47d49ea068fe40cef12afaf49f507c2839"
    },
    {
        "path": "P08_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7f2d56ae61156ef5d6028c1bd8a5122a2776245c",
        "size": 11210,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7f2d56ae61156ef5d6028c1bd8a5122a2776245c"
    },
    {
        "path": "P08_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dbbc19b196e8220e359be6909b0b9bb28d830ca1",
        "size": 10069,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dbbc19b196e8220e359be6909b0b9bb28d830ca1"
    },
    {
        "path": "P08_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "14f574242b47e47305a6e6854cbd7fa0bc9d29d6",
        "size": 9095,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/14f574242b47e47305a6e6854cbd7fa0bc9d29d6"
    },
    {
        "path": "P08_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "444d999485994439e8cb68942fa6894310c00fe1",
        "size": 9653,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/444d999485994439e8cb68942fa6894310c00fe1"
    },
    {
        "path": "P08_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2e643f31387bb4b46cbfa32c5d17b58a4152d36d",
        "size": 7488,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2e643f31387bb4b46cbfa32c5d17b58a4152d36d"
    },
    {
        "path": "P08_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f399c2fae6596c32acb592b2bcc41755db0d1378",
        "size": 8880,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f399c2fae6596c32acb592b2bcc41755db0d1378"
    },
    {
        "path": "P08_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cde7cb7c8d537491cea36fc68b0632aa0b8b319a",
        "size": 11617,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cde7cb7c8d537491cea36fc68b0632aa0b8b319a"
    },
    {
        "path": "P08_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d8ca9989f58f7dd648f06d54278865f55594b7d1",
        "size": 10677,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d8ca9989f58f7dd648f06d54278865f55594b7d1"
    },
    {
        "path": "P08_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b852940f88b234e856a92e7c131a96709e08bf83",
        "size": 10608,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b852940f88b234e856a92e7c131a96709e08bf83"
    },
    {
        "path": "P08_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ea01ef40cf6ac771161dfa8acde535319b954c94",
        "size": 7147,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ea01ef40cf6ac771161dfa8acde535319b954c94"
    },
    {
        "path": "P08_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f860f694a1379d1fe6127b6b11634ca53df88323",
        "size": 10686,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f860f694a1379d1fe6127b6b11634ca53df88323"
    },
    {
        "path": "P08_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c2348703fd04a49d0bf522e755a268495f28e57f",
        "size": 13434,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c2348703fd04a49d0bf522e755a268495f28e57f"
    },
    {
        "path": "P08_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "524e445f294a5266ca4362c168185120ee4601d8",
        "size": 9836,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/524e445f294a5266ca4362c168185120ee4601d8"
    },
    {
        "path": "P08_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "594cf6f88fe12d66acaa20941fc698c6725269f7",
        "size": 10165,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/594cf6f88fe12d66acaa20941fc698c6725269f7"
    },
    {
        "path": "P08_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dba180aace7e50a3b3b2973faa7f7e340161e559",
        "size": 7487,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dba180aace7e50a3b3b2973faa7f7e340161e559"
    },
    {
        "path": "P08_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "535a7a72177b00bd22f0ea0990b7ea518f41fc95",
        "size": 11465,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/535a7a72177b00bd22f0ea0990b7ea518f41fc95"
    },
    {
        "path": "P08_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9158a1f356973f383857e0049a4ce6fbc4996960",
        "size": 9535,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9158a1f356973f383857e0049a4ce6fbc4996960"
    },
    {
        "path": "P08_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6b1730fff4016bfd6fc4befe5d881b2d8ee174d7",
        "size": 10189,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6b1730fff4016bfd6fc4befe5d881b2d8ee174d7"
    },
    {
        "path": "P08_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "38712ce79bcc1df3c92f172cbcfae125059eb5a5",
        "size": 7154,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/38712ce79bcc1df3c92f172cbcfae125059eb5a5"
    },
    {
        "path": "P08_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b432b36c849fde7ba9f6c1c7ed13b90c3c60dfbe",
        "size": 8941,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b432b36c849fde7ba9f6c1c7ed13b90c3c60dfbe"
    },
    {
        "path": "P08_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c2d598321e84e8780edc55ee831b178b97a881aa",
        "size": 7960,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c2d598321e84e8780edc55ee831b178b97a881aa"
    },
    {
        "path": "P08_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a03806ce1c736a749b00de29fcb312841cafbb48",
        "size": 9660,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a03806ce1c736a749b00de29fcb312841cafbb48"
    },
    {
        "path": "P08_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d84783a75ddd66e1c907d18e6e409713fb510e93",
        "size": 5449,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d84783a75ddd66e1c907d18e6e409713fb510e93"
    },
    {
        "path": "P08_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6c2dd9c615494befe22410a795357bc9e155ebe6",
        "size": 7013,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6c2dd9c615494befe22410a795357bc9e155ebe6"
    },
    {
        "path": "P08_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b8b2bfe8338f86b275c6bf8c403aa686b356b20d",
        "size": 8383,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b8b2bfe8338f86b275c6bf8c403aa686b356b20d"
    },
    {
        "path": "P08_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "575a8c920a1066d690c1ab8a549e1d157f98e16a",
        "size": 7246,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/575a8c920a1066d690c1ab8a549e1d157f98e16a"
    },
    {
        "path": "P08_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9516495091d6a428174b5e1caf5f9100eed6f21f",
        "size": 7310,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9516495091d6a428174b5e1caf5f9100eed6f21f"
    },
    {
        "path": "P08_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "847d53fd47e914a20bd6cb407246618dbdc9e71a",
        "size": 8044,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/847d53fd47e914a20bd6cb407246618dbdc9e71a"
    },
    {
        "path": "P08_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b66f1f4c655549f8459bc82f1b2d9f4a3792b74c",
        "size": 11752,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b66f1f4c655549f8459bc82f1b2d9f4a3792b74c"
    },
    {
        "path": "P08_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "15a2aa5329f93c42d3530e3a5ee5434fcb6ece84",
        "size": 8982,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/15a2aa5329f93c42d3530e3a5ee5434fcb6ece84"
    },
    {
        "path": "P08_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6ac73f0fc70b2d17c7c5218f914a91cc9f18e777",
        "size": 10254,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6ac73f0fc70b2d17c7c5218f914a91cc9f18e777"
    },
    {
        "path": "P08_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "742341e37354cb92b6352cf458a440e16e9e9562",
        "size": 14675,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/742341e37354cb92b6352cf458a440e16e9e9562"
    },
    {
        "path": "P08_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2afbbc36fc04a81ca92e445a654bc85db500d70b",
        "size": 13663,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2afbbc36fc04a81ca92e445a654bc85db500d70b"
    },
    {
        "path": "P08_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8ffbb754e90341cbc00f229dde6a1fb36d89af67",
        "size": 10232,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8ffbb754e90341cbc00f229dde6a1fb36d89af67"
    },
    {
        "path": "P08_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "88028599d813a0e5de2c65346f5b72d9e7cb252f",
        "size": 10984,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/88028599d813a0e5de2c65346f5b72d9e7cb252f"
    },
    {
        "path": "P08_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1b9dcddaf7f085b8417dd3e1667aaf169c874175",
        "size": 12612,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1b9dcddaf7f085b8417dd3e1667aaf169c874175"
    },
    {
        "path": "P08_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "584bc4d7f63246a16e29f8426b732f9bb6a7de0b",
        "size": 7511,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/584bc4d7f63246a16e29f8426b732f9bb6a7de0b"
    },
    {
        "path": "P08_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c710574308048715d783613acfe4f56a6f8e0636",
        "size": 9225,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c710574308048715d783613acfe4f56a6f8e0636"
    },
    {
        "path": "P08_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6234ba3f1e399f76f7d8a69c4ea702b8eeed970c",
        "size": 10521,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6234ba3f1e399f76f7d8a69c4ea702b8eeed970c"
    },
    {
        "path": "P08_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d7ac46bb729c45423b582f96474321f85d14dd55",
        "size": 8740,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d7ac46bb729c45423b582f96474321f85d14dd55"
    },
    {
        "path": "P08_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1cb04abff2a20417a3de2f2a30ad9ea8e727ef08",
        "size": 9959,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1cb04abff2a20417a3de2f2a30ad9ea8e727ef08"
    },
    {
        "path": "P08_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2d3b37a63a395ad9c39e2a2e0f8fee6968d3dac4",
        "size": 9231,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2d3b37a63a395ad9c39e2a2e0f8fee6968d3dac4"
    },
    {
        "path": "P08_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "acc0f06415972121f0435373ce113ee6328faa12",
        "size": 9297,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/acc0f06415972121f0435373ce113ee6328faa12"
    },
    {
        "path": "P08_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fac3760c6a6ffd1ae68be812e576dc2291474713",
        "size": 9365,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fac3760c6a6ffd1ae68be812e576dc2291474713"
    },
    {
        "path": "P08_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "215203065f44f1d7ca57596fa2d9f477d817485f",
        "size": 11238,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/215203065f44f1d7ca57596fa2d9f477d817485f"
    },
    {
        "path": "P08_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f6635de97b4f989d15542192d5e3f55db66b89b6",
        "size": 7252,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f6635de97b4f989d15542192d5e3f55db66b89b6"
    },
    {
        "path": "P08_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "29ec38fb89e943757f759060ffbfa58301707947",
        "size": 11019,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/29ec38fb89e943757f759060ffbfa58301707947"
    },
    {
        "path": "P08_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "afa129aa6a988f32a0fb35a28164829b56e0e1b5",
        "size": 15795,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/afa129aa6a988f32a0fb35a28164829b56e0e1b5"
    },
    {
        "path": "P09_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9ac13adee29737b61cbbae38475974e0a292e282",
        "size": 14869,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9ac13adee29737b61cbbae38475974e0a292e282"
    },
    {
        "path": "P09_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8c884893b710edb8a7b35e7f95e619410d9290c0",
        "size": 10253,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8c884893b710edb8a7b35e7f95e619410d9290c0"
    },
    {
        "path": "P09_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "20835b70a16c1355ea3eee722e8c549f9ebbae6d",
        "size": 16279,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/20835b70a16c1355ea3eee722e8c549f9ebbae6d"
    },
    {
        "path": "P09_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fa039f3b77a9cb72dbac3cf9bed73a6a4babed39",
        "size": 29915,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fa039f3b77a9cb72dbac3cf9bed73a6a4babed39"
    },
    {
        "path": "P09_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a3c1ac9894fa50633b69b74b699e78e3c8977163",
        "size": 18403,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a3c1ac9894fa50633b69b74b699e78e3c8977163"
    },
    {
        "path": "P09_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e867408ae1de47ca71dd693e4f1aa278ffa73816",
        "size": 16112,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e867408ae1de47ca71dd693e4f1aa278ffa73816"
    },
    {
        "path": "P09_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "06228b60d9d526a8f57f865c17af0ef3f4323805",
        "size": 13675,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/06228b60d9d526a8f57f865c17af0ef3f4323805"
    },
    {
        "path": "P09_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6b5ebe27c2f70b7dd17664f4c37308a5b7c457c1",
        "size": 25338,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6b5ebe27c2f70b7dd17664f4c37308a5b7c457c1"
    },
    {
        "path": "P09_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "580233aeefe5f67f78f7ecd4d51d83dfa58f6e7c",
        "size": 23212,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/580233aeefe5f67f78f7ecd4d51d83dfa58f6e7c"
    },
    {
        "path": "P09_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8f2e90f713bbcbbed3d45c8620dd48b8246419f7",
        "size": 14295,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8f2e90f713bbcbbed3d45c8620dd48b8246419f7"
    },
    {
        "path": "P09_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bd0ae6319cc5d66d5c3e3d9561896b29ffeff9a5",
        "size": 10096,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bd0ae6319cc5d66d5c3e3d9561896b29ffeff9a5"
    },
    {
        "path": "P09_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4efaea81a22d22108eacd4052383c837196639ff",
        "size": 10339,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4efaea81a22d22108eacd4052383c837196639ff"
    },
    {
        "path": "P09_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fe8f49acc14fd3605cba1cd96b86747bc07e2b56",
        "size": 13925,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fe8f49acc14fd3605cba1cd96b86747bc07e2b56"
    },
    {
        "path": "P09_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fc995c60dbffb9a1903b8a4139b23ec4ea3087bb",
        "size": 15053,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fc995c60dbffb9a1903b8a4139b23ec4ea3087bb"
    },
    {
        "path": "P09_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cd3de56046381d4fb1eb0d750bf6a70463e4e277",
        "size": 17517,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cd3de56046381d4fb1eb0d750bf6a70463e4e277"
    },
    {
        "path": "P09_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "37e73ddc0836d29d7409c31e8f0e81fb68f82067",
        "size": 16245,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/37e73ddc0836d29d7409c31e8f0e81fb68f82067"
    },
    {
        "path": "P09_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a8da005c36ee08cc95fee8bf4a71beabf5aa0314",
        "size": 8997,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a8da005c36ee08cc95fee8bf4a71beabf5aa0314"
    },
    {
        "path": "P09_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2fb46b2848a177c5f548d61b24875e35f6e2d33c",
        "size": 17861,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2fb46b2848a177c5f548d61b24875e35f6e2d33c"
    },
    {
        "path": "P09_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1810493347229ebf5c48fd01bde32d5ee655b2a0",
        "size": 23210,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1810493347229ebf5c48fd01bde32d5ee655b2a0"
    },
    {
        "path": "P09_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3857ac928e45ee87fe399121196e8c07a7100066",
        "size": 11420,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3857ac928e45ee87fe399121196e8c07a7100066"
    },
    {
        "path": "P09_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "935ab73a54c4715f62f3d28b14e9583106190c31",
        "size": 13981,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/935ab73a54c4715f62f3d28b14e9583106190c31"
    },
    {
        "path": "P09_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "945cd0107a421f6e3039d2bb0982bf90ed8cfd25",
        "size": 13741,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/945cd0107a421f6e3039d2bb0982bf90ed8cfd25"
    },
    {
        "path": "P09_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "94e2272ec33b55b79b28c014c5421ab46000bd16",
        "size": 24855,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/94e2272ec33b55b79b28c014c5421ab46000bd16"
    },
    {
        "path": "P09_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9c6957e950f8e8494b24dbbed80286de7f325629",
        "size": 13735,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9c6957e950f8e8494b24dbbed80286de7f325629"
    },
    {
        "path": "P09_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f4f79412bddb5c42591506cb701b1d9a8f409621",
        "size": 14275,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f4f79412bddb5c42591506cb701b1d9a8f409621"
    },
    {
        "path": "P09_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7666e489041b13cab44c6a8653ad9d905ef48dfc",
        "size": 17022,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7666e489041b13cab44c6a8653ad9d905ef48dfc"
    },
    {
        "path": "P09_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3d3d6122d20199361439da0da33301a2f445e748",
        "size": 10491,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3d3d6122d20199361439da0da33301a2f445e748"
    },
    {
        "path": "P09_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0587c0d0948e25fbeece3c0e578aaf7b8d6620e7",
        "size": 16016,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0587c0d0948e25fbeece3c0e578aaf7b8d6620e7"
    },
    {
        "path": "P09_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2fe7f0a07857b1838923d7176aba4238be42b382",
        "size": 11557,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2fe7f0a07857b1838923d7176aba4238be42b382"
    },
    {
        "path": "P09_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "502617f493ea19ee9f0ae135eead926ef690ee66",
        "size": 11322,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/502617f493ea19ee9f0ae135eead926ef690ee66"
    },
    {
        "path": "P09_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1803c53d450d8ea1e6e5782610c0f3fed657515e",
        "size": 9050,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1803c53d450d8ea1e6e5782610c0f3fed657515e"
    },
    {
        "path": "P09_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9f21982158e32f7d45d2ddbbb84d0cf794d95bb2",
        "size": 18044,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9f21982158e32f7d45d2ddbbb84d0cf794d95bb2"
    },
    {
        "path": "P09_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "58af38c34c5dd9624afb190025aa0502fef9f2d6",
        "size": 7488,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/58af38c34c5dd9624afb190025aa0502fef9f2d6"
    },
    {
        "path": "P09_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "85bc098c90509795be10d38eea8cdafcc30f3b76",
        "size": 10076,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/85bc098c90509795be10d38eea8cdafcc30f3b76"
    },
    {
        "path": "P09_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "71e2f252981632227da78986cd31b98188f8f61a",
        "size": 7172,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/71e2f252981632227da78986cd31b98188f8f61a"
    },
    {
        "path": "P09_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7c480b734fd6ca5eb9854759589c94dd3c9e0442",
        "size": 9880,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7c480b734fd6ca5eb9854759589c94dd3c9e0442"
    },
    {
        "path": "P09_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "245b116aa2c2d8a77c73ee937baee7188a311cbb",
        "size": 15436,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/245b116aa2c2d8a77c73ee937baee7188a311cbb"
    },
    {
        "path": "P09_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dd0b5d322d6869363dd0e9eee87ba1ff68949c0d",
        "size": 9678,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dd0b5d322d6869363dd0e9eee87ba1ff68949c0d"
    },
    {
        "path": "P09_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ae2108547f896546d23f3fad2a6a0554fa4cbfe4",
        "size": 12704,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ae2108547f896546d23f3fad2a6a0554fa4cbfe4"
    },
    {
        "path": "P09_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ae13a0a90bb840fad18a38d5b4fa0a466daf20e9",
        "size": 14116,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ae13a0a90bb840fad18a38d5b4fa0a466daf20e9"
    },
    {
        "path": "P09_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "875584cde4afb1e62d367d75e18ce15cc88b5aa8",
        "size": 10354,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/875584cde4afb1e62d367d75e18ce15cc88b5aa8"
    },
    {
        "path": "P09_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bb7cf1a0a99637b3ca0253c3b669f35df6ac4140",
        "size": 11779,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bb7cf1a0a99637b3ca0253c3b669f35df6ac4140"
    },
    {
        "path": "P09_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "07de01a8539a07e4e6cb6baa3deb4862fd9c317f",
        "size": 13096,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/07de01a8539a07e4e6cb6baa3deb4862fd9c317f"
    },
    {
        "path": "P09_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c32a47e7e41dcf70162a6a96a1f2c3e506b4cb39",
        "size": 20964,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c32a47e7e41dcf70162a6a96a1f2c3e506b4cb39"
    },
    {
        "path": "P09_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "758309f39deaa2d54e4b347a722ef22dbc943a3f",
        "size": 17744,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/758309f39deaa2d54e4b347a722ef22dbc943a3f"
    },
    {
        "path": "P09_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d65c0c138539db3dbad3c12d2473bf823ffc25c9",
        "size": 16646,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d65c0c138539db3dbad3c12d2473bf823ffc25c9"
    },
    {
        "path": "P09_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8ca4a7134831dd2717a6c8da8517183d4e495ceb",
        "size": 14012,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8ca4a7134831dd2717a6c8da8517183d4e495ceb"
    },
    {
        "path": "P09_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1f428cf5706eb73577f7de15adca4e10943103e5",
        "size": 9003,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1f428cf5706eb73577f7de15adca4e10943103e5"
    },
    {
        "path": "P09_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0a1bae2d397be8d3729cf52eea16fc730fff7894",
        "size": 9328,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0a1bae2d397be8d3729cf52eea16fc730fff7894"
    },
    {
        "path": "P09_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "73e8c9673c4e2b98f80b55923267bccb0cca7f41",
        "size": 16913,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/73e8c9673c4e2b98f80b55923267bccb0cca7f41"
    },
    {
        "path": "P09_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "afdfc940e0b81bca3c60d975b11eea90c3590719",
        "size": 11775,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/afdfc940e0b81bca3c60d975b11eea90c3590719"
    },
    {
        "path": "P09_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16400bacba73e74eed74591c0cec092ee92800c3",
        "size": 8123,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16400bacba73e74eed74591c0cec092ee92800c3"
    },
    {
        "path": "P09_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5c625811021e78456ef6c1e555857bc0d5b78103",
        "size": 9919,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5c625811021e78456ef6c1e555857bc0d5b78103"
    },
    {
        "path": "P09_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "132af5e81b89a577b690cd386a9087e3265f4dcc",
        "size": 11022,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/132af5e81b89a577b690cd386a9087e3265f4dcc"
    },
    {
        "path": "P09_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ba2704a534c47e45e87f57dbbc718dad4aaf96dc",
        "size": 19321,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ba2704a534c47e45e87f57dbbc718dad4aaf96dc"
    },
    {
        "path": "P09_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "35221b42ab0ab0e8226fd68bfbf89b1cc3425d78",
        "size": 8388,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/35221b42ab0ab0e8226fd68bfbf89b1cc3425d78"
    },
    {
        "path": "P09_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0a2e426e06728b76c239cb528d750b4d2715621d",
        "size": 10391,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0a2e426e06728b76c239cb528d750b4d2715621d"
    },
    {
        "path": "P09_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "faf8e9c2c5f7b0466164696f11fe638f849974fa",
        "size": 12082,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/faf8e9c2c5f7b0466164696f11fe638f849974fa"
    },
    {
        "path": "P09_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "789930e496172eefc0b038cf60e453a89813bee7",
        "size": 16687,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/789930e496172eefc0b038cf60e453a89813bee7"
    },
    {
        "path": "P09_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "18efad31978be3f2c9c0d26b71a6de4d67524785",
        "size": 23923,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/18efad31978be3f2c9c0d26b71a6de4d67524785"
    },
    {
        "path": "P10_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4b6d01dc1bb85ac7f78b62e58f72d039d4380f4f",
        "size": 7072,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4b6d01dc1bb85ac7f78b62e58f72d039d4380f4f"
    },
    {
        "path": "P10_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "44cbfa0ffdc01b25210d3463a8bdf06dcb1833a5",
        "size": 12570,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/44cbfa0ffdc01b25210d3463a8bdf06dcb1833a5"
    },
    {
        "path": "P10_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "743b3a6069507fae73bcbf9c41cd412dae7ffbe8",
        "size": 8249,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/743b3a6069507fae73bcbf9c41cd412dae7ffbe8"
    },
    {
        "path": "P10_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "834025e8cd0f49bceb740dec6803b7cab924fccf",
        "size": 6412,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/834025e8cd0f49bceb740dec6803b7cab924fccf"
    },
    {
        "path": "P10_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e66e5fdf76cd6700c57e7b79c36ca8ae2f0e086a",
        "size": 10958,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e66e5fdf76cd6700c57e7b79c36ca8ae2f0e086a"
    },
    {
        "path": "P10_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e11842c040aa2469571440536a9abe5da387bf20",
        "size": 11881,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e11842c040aa2469571440536a9abe5da387bf20"
    },
    {
        "path": "P10_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a5a300a16efe04acc14644922b824c7c9a77775e",
        "size": 7708,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a5a300a16efe04acc14644922b824c7c9a77775e"
    },
    {
        "path": "P10_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3dab4dcf292b9b1863f6283722f28efb4c98bfd1",
        "size": 14362,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3dab4dcf292b9b1863f6283722f28efb4c98bfd1"
    },
    {
        "path": "P10_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cbf7563e99fa711b0c311ba015c462ac15970a82",
        "size": 8166,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cbf7563e99fa711b0c311ba015c462ac15970a82"
    },
    {
        "path": "P10_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f55440f31d7e601ee91a405ba20c92f0c58bf962",
        "size": 8720,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f55440f31d7e601ee91a405ba20c92f0c58bf962"
    },
    {
        "path": "P10_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "daaf4df6329660bd3b0600293c13684dfed1947e",
        "size": 8872,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/daaf4df6329660bd3b0600293c13684dfed1947e"
    },
    {
        "path": "P10_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a8c9f26939bef8512e5740067674b952b9bd0a31",
        "size": 11988,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a8c9f26939bef8512e5740067674b952b9bd0a31"
    },
    {
        "path": "P10_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "67cc0169f64b98781010f8c350e44eba42bc6273",
        "size": 6672,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/67cc0169f64b98781010f8c350e44eba42bc6273"
    },
    {
        "path": "P10_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b402b66242c38c5fd09cc9a935f3a4f0726b38b2",
        "size": 7423,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b402b66242c38c5fd09cc9a935f3a4f0726b38b2"
    },
    {
        "path": "P10_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ac524e1d439cfd73ed7d3c8aec899e804d6a4f54",
        "size": 7642,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ac524e1d439cfd73ed7d3c8aec899e804d6a4f54"
    },
    {
        "path": "P10_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "091c3fb1138f7297defce937229da9618d8799ab",
        "size": 7489,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/091c3fb1138f7297defce937229da9618d8799ab"
    },
    {
        "path": "P10_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0c3f356161f6f145d99d451878b1751e21050476",
        "size": 5647,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0c3f356161f6f145d99d451878b1751e21050476"
    },
    {
        "path": "P10_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3fd20897b978fc83115e93a910f999203ddd01cf",
        "size": 7208,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3fd20897b978fc83115e93a910f999203ddd01cf"
    },
    {
        "path": "P10_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bc8b1fe17693394f557aac70ef4712409a66dac3",
        "size": 7293,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bc8b1fe17693394f557aac70ef4712409a66dac3"
    },
    {
        "path": "P10_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "22e5536e2cb0e0963bae13e6821ec564afd539fc",
        "size": 7011,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/22e5536e2cb0e0963bae13e6821ec564afd539fc"
    },
    {
        "path": "P10_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "218b8841ebc40d80fd0104b8ff4bce787051692d",
        "size": 9086,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/218b8841ebc40d80fd0104b8ff4bce787051692d"
    },
    {
        "path": "P10_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fcbfd3195ab3419a852d1c5a14a335bfc7578f7f",
        "size": 6125,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fcbfd3195ab3419a852d1c5a14a335bfc7578f7f"
    },
    {
        "path": "P10_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "50dcfcd63562bc648b5e5a4d4166d80ecc3e32bb",
        "size": 6088,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/50dcfcd63562bc648b5e5a4d4166d80ecc3e32bb"
    },
    {
        "path": "P10_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4e89652b27acf9e8934bbca45f98958d89c3ba52",
        "size": 8733,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4e89652b27acf9e8934bbca45f98958d89c3ba52"
    },
    {
        "path": "P10_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "84e9b748350c880da44749d61f627bd10b4e20c0",
        "size": 3715,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/84e9b748350c880da44749d61f627bd10b4e20c0"
    },
    {
        "path": "P10_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ad3411a89139cfd1684056871a3ea1a6e34c94fb",
        "size": 8238,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ad3411a89139cfd1684056871a3ea1a6e34c94fb"
    },
    {
        "path": "P10_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "91cef0079c25cfd3c76127aa8b62360e72f0c5f0",
        "size": 12863,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/91cef0079c25cfd3c76127aa8b62360e72f0c5f0"
    },
    {
        "path": "P10_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "255766cf1637542c71289ee88b1dac1c803d3b0d",
        "size": 7564,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/255766cf1637542c71289ee88b1dac1c803d3b0d"
    },
    {
        "path": "P10_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "31cc45c5d9b5ac1fb68ef9266cbd8d21e22eee8d",
        "size": 5434,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/31cc45c5d9b5ac1fb68ef9266cbd8d21e22eee8d"
    },
    {
        "path": "P10_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7e0ff45ee1d60c2659a34e82f55157975d197da2",
        "size": 7158,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7e0ff45ee1d60c2659a34e82f55157975d197da2"
    },
    {
        "path": "P10_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4fc3b328365056ad0499be08c1207a53efe0fcb0",
        "size": 8439,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4fc3b328365056ad0499be08c1207a53efe0fcb0"
    },
    {
        "path": "P10_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e0dd5c8b3abc99013f5216bf86aa3ba9d506ee6e",
        "size": 9478,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e0dd5c8b3abc99013f5216bf86aa3ba9d506ee6e"
    },
    {
        "path": "P10_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d1fb92d053a0fed582c8e531dec9406a539acf27",
        "size": 6971,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d1fb92d053a0fed582c8e531dec9406a539acf27"
    },
    {
        "path": "P10_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6734da955879d662fc8f7b5ca159b0d2437d5a05",
        "size": 13876,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6734da955879d662fc8f7b5ca159b0d2437d5a05"
    },
    {
        "path": "P10_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ae0a230cf1ea2a053e4276982aae87e4572f78f7",
        "size": 8039,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ae0a230cf1ea2a053e4276982aae87e4572f78f7"
    },
    {
        "path": "P10_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "53cb91763d6a65537bf5a51760d18564e7416517",
        "size": 4549,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/53cb91763d6a65537bf5a51760d18564e7416517"
    },
    {
        "path": "P10_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9c14d9b5c60a99889e1b08f95578490860afab44",
        "size": 7763,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9c14d9b5c60a99889e1b08f95578490860afab44"
    },
    {
        "path": "P10_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "34464b60c91cd4fa85d32550ccb8ceeb9c02a976",
        "size": 5513,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/34464b60c91cd4fa85d32550ccb8ceeb9c02a976"
    },
    {
        "path": "P10_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "56d4e95e0c7f5c113c06e82db1e0030822baec68",
        "size": 5320,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/56d4e95e0c7f5c113c06e82db1e0030822baec68"
    },
    {
        "path": "P10_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "def68803b3dc867c17b2c5af6ea058849043a469",
        "size": 7054,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/def68803b3dc867c17b2c5af6ea058849043a469"
    },
    {
        "path": "P10_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "17bdc32dc399a5b5a13b9155e52fe92380c93c9a",
        "size": 4553,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/17bdc32dc399a5b5a13b9155e52fe92380c93c9a"
    },
    {
        "path": "P10_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9ba53c99fcedc126ff4ade5d356c4f155d0f5994",
        "size": 9072,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9ba53c99fcedc126ff4ade5d356c4f155d0f5994"
    },
    {
        "path": "P10_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5bd1c4751adee696e529484ff41baacba5531b19",
        "size": 6168,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5bd1c4751adee696e529484ff41baacba5531b19"
    },
    {
        "path": "P10_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "28adeec7603a214dd881c890cf94f82132793a82",
        "size": 6624,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/28adeec7603a214dd881c890cf94f82132793a82"
    },
    {
        "path": "P10_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f6014159b3cf7eff479173776de634e065fcda01",
        "size": 9857,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f6014159b3cf7eff479173776de634e065fcda01"
    },
    {
        "path": "P10_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0b71f632560a859f4608399ad9437da351e42fc7",
        "size": 4481,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0b71f632560a859f4608399ad9437da351e42fc7"
    },
    {
        "path": "P10_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0649da732f7fe747ebd7f757aa1e0edba7cf18a5",
        "size": 10326,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0649da732f7fe747ebd7f757aa1e0edba7cf18a5"
    },
    {
        "path": "P10_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8993a07c213afbd0cceac3ff3b5f9cfb0a4ef373",
        "size": 11896,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8993a07c213afbd0cceac3ff3b5f9cfb0a4ef373"
    },
    {
        "path": "P11_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "72062eb3fae06fd50fa7b1a53e15eefd70381494",
        "size": 8620,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/72062eb3fae06fd50fa7b1a53e15eefd70381494"
    },
    {
        "path": "P11_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0a6986b30d100267cae0ed845781b22499f316a5",
        "size": 7686,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0a6986b30d100267cae0ed845781b22499f316a5"
    },
    {
        "path": "P11_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "43e0711c84f02ecbabcc3579d6d716d80f2ccab0",
        "size": 7859,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/43e0711c84f02ecbabcc3579d6d716d80f2ccab0"
    },
    {
        "path": "P11_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9d9d3958e8a8a603f48cedb44e76390e0f54f604",
        "size": 11219,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9d9d3958e8a8a603f48cedb44e76390e0f54f604"
    },
    {
        "path": "P11_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "adc378a42832b8d833fcba6a976385746eb4f2d9",
        "size": 10453,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/adc378a42832b8d833fcba6a976385746eb4f2d9"
    },
    {
        "path": "P11_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6450f93fc1733d63f060d6b5623b1730a26df979",
        "size": 8878,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6450f93fc1733d63f060d6b5623b1730a26df979"
    },
    {
        "path": "P11_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "256fe7801546c77d70c93e1ddc814ffe9687d7e8",
        "size": 7115,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/256fe7801546c77d70c93e1ddc814ffe9687d7e8"
    },
    {
        "path": "P11_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bc697952cb05f094a9e972705894ea831d14f517",
        "size": 12289,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bc697952cb05f094a9e972705894ea831d14f517"
    },
    {
        "path": "P11_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "99d48e324b50aa013d7887a2a3105e173b6c8cb2",
        "size": 10498,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/99d48e324b50aa013d7887a2a3105e173b6c8cb2"
    },
    {
        "path": "P11_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1ae45acaa722e301e4146120935fed7bb27f2543",
        "size": 7866,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1ae45acaa722e301e4146120935fed7bb27f2543"
    },
    {
        "path": "P11_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f98ba98646639225fcf366b19fdec559c1f73198",
        "size": 7573,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f98ba98646639225fcf366b19fdec559c1f73198"
    },
    {
        "path": "P11_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dc4c643a2940267747e0a3c1475f34b651b67873",
        "size": 5638,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dc4c643a2940267747e0a3c1475f34b651b67873"
    },
    {
        "path": "P11_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ef7363cc53eb0096922e414ab9581435c0bc1c54",
        "size": 5990,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ef7363cc53eb0096922e414ab9581435c0bc1c54"
    },
    {
        "path": "P11_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9f9683126e0ea4184fa8093ac545a0d0414ab163",
        "size": 8151,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9f9683126e0ea4184fa8093ac545a0d0414ab163"
    },
    {
        "path": "P11_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "61c4cc5dd38c8b1340a29a25436b0b875233367d",
        "size": 8827,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/61c4cc5dd38c8b1340a29a25436b0b875233367d"
    },
    {
        "path": "P11_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dcac5b2115dc970a73694e84cc0af786df44cd92",
        "size": 8453,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dcac5b2115dc970a73694e84cc0af786df44cd92"
    },
    {
        "path": "P11_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7bc1a6ed75b3bc89c6536b0f1f9e742b62249757",
        "size": 5537,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7bc1a6ed75b3bc89c6536b0f1f9e742b62249757"
    },
    {
        "path": "P11_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f7dde15be53ab57f6e69e0d93537da3e0faf4324",
        "size": 4979,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f7dde15be53ab57f6e69e0d93537da3e0faf4324"
    },
    {
        "path": "P11_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dac35d81bbeaabcd8c722f5325e97236849fce4b",
        "size": 10313,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dac35d81bbeaabcd8c722f5325e97236849fce4b"
    },
    {
        "path": "P11_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a01be7535fd8e4ead52013caa88e35cebabbf066",
        "size": 7028,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a01be7535fd8e4ead52013caa88e35cebabbf066"
    },
    {
        "path": "P11_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5eed5e3674c682c683b5ede4250e3d1ab49b8350",
        "size": 8800,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5eed5e3674c682c683b5ede4250e3d1ab49b8350"
    },
    {
        "path": "P11_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d55302074b4f84868a96b03e23b7ebd55a1b82fe",
        "size": 6411,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d55302074b4f84868a96b03e23b7ebd55a1b82fe"
    },
    {
        "path": "P11_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "85644b17ad2a77d332658cec5873f514cbf29b36",
        "size": 10238,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/85644b17ad2a77d332658cec5873f514cbf29b36"
    },
    {
        "path": "P11_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1c7a76c5ac37724f691664fa138f2b6f0736847c",
        "size": 12928,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1c7a76c5ac37724f691664fa138f2b6f0736847c"
    },
    {
        "path": "P11_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "887fc3929577a7d3aa28d4572dd5e1e88d7332ff",
        "size": 5108,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/887fc3929577a7d3aa28d4572dd5e1e88d7332ff"
    },
    {
        "path": "P11_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d674d282a9324468a02b2c2a97a6b0c8efd9bf96",
        "size": 8462,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d674d282a9324468a02b2c2a97a6b0c8efd9bf96"
    },
    {
        "path": "P11_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d2b93849d97bf9592adb998b54888068a53c5bb4",
        "size": 6672,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d2b93849d97bf9592adb998b54888068a53c5bb4"
    },
    {
        "path": "P11_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "de73778ffe686476a2fc35171d043522cae9a9fc",
        "size": 10567,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/de73778ffe686476a2fc35171d043522cae9a9fc"
    },
    {
        "path": "P11_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1a812e8d38eeac3a7d0c4b07c7bfb6dfaf9579a6",
        "size": 9338,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1a812e8d38eeac3a7d0c4b07c7bfb6dfaf9579a6"
    },
    {
        "path": "P11_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "336758084fdb8b5e846e9b1716c19188f18da501",
        "size": 5732,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/336758084fdb8b5e846e9b1716c19188f18da501"
    },
    {
        "path": "P11_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "253ee9899d701ce79e391daf78d109cb8cde9a14",
        "size": 6387,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/253ee9899d701ce79e391daf78d109cb8cde9a14"
    },
    {
        "path": "P11_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dc52d70e0c66bd15c684fe15faf76fda326bc41e",
        "size": 9486,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dc52d70e0c66bd15c684fe15faf76fda326bc41e"
    },
    {
        "path": "P11_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "17b164c049e08170c3a347efe11dedd18e9b3d32",
        "size": 4408,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/17b164c049e08170c3a347efe11dedd18e9b3d32"
    },
    {
        "path": "P11_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "95a014aab017f25bc985ca4b2a7178cdabb23e45",
        "size": 4345,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/95a014aab017f25bc985ca4b2a7178cdabb23e45"
    },
    {
        "path": "P11_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4e0317d03b1dfa269df71feb1ecb45c3ddb97b1e",
        "size": 5602,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4e0317d03b1dfa269df71feb1ecb45c3ddb97b1e"
    },
    {
        "path": "P11_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "15447c7c7c9aacc81c9a02a2fbdefc5ec77bf33d",
        "size": 10566,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/15447c7c7c9aacc81c9a02a2fbdefc5ec77bf33d"
    },
    {
        "path": "P11_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b46be5eeb575176e28968a324171c27530d5dd8d",
        "size": 4955,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b46be5eeb575176e28968a324171c27530d5dd8d"
    },
    {
        "path": "P11_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "75c5c0aeb1b5f49ae34f852aa8916eea80540854",
        "size": 7901,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/75c5c0aeb1b5f49ae34f852aa8916eea80540854"
    },
    {
        "path": "P11_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bc0c311b7b84f43716d4821f8a6d462b99fd2093",
        "size": 6874,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bc0c311b7b84f43716d4821f8a6d462b99fd2093"
    },
    {
        "path": "P11_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "49b80182ec68391f724ac21de3db12666cc233da",
        "size": 9017,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/49b80182ec68391f724ac21de3db12666cc233da"
    },
    {
        "path": "P11_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1b9872562fd9ac2dff960dd89cb2d40051daeb26",
        "size": 3991,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1b9872562fd9ac2dff960dd89cb2d40051daeb26"
    },
    {
        "path": "P11_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f35a8f7e9f55d6373dd8dfa887b821de6c404ed9",
        "size": 8523,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f35a8f7e9f55d6373dd8dfa887b821de6c404ed9"
    },
    {
        "path": "P11_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2404a17a03fd0f8ef90142536b34694ddb547a64",
        "size": 12538,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2404a17a03fd0f8ef90142536b34694ddb547a64"
    },
    {
        "path": "P11_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "54fd6d32d343d65cc8ce6f867fb0293e9f710bb3",
        "size": 7749,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/54fd6d32d343d65cc8ce6f867fb0293e9f710bb3"
    },
    {
        "path": "P11_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "275740cb7b853e9e74236d385c32fa035383ca7f",
        "size": 4686,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/275740cb7b853e9e74236d385c32fa035383ca7f"
    },
    {
        "path": "P11_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "95f5189aea40e640278fc945ecbccdb83e145734",
        "size": 10548,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/95f5189aea40e640278fc945ecbccdb83e145734"
    },
    {
        "path": "P11_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f5815bfa43e36cfa9d3d749f712e62e86c474101",
        "size": 7236,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f5815bfa43e36cfa9d3d749f712e62e86c474101"
    },
    {
        "path": "P11_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "aedf09ca781a52092efb939c1809dc5e10bf7ff3",
        "size": 6389,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/aedf09ca781a52092efb939c1809dc5e10bf7ff3"
    },
    {
        "path": "P11_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6121089a381acc5578af44e8adc6f27740604960",
        "size": 6208,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6121089a381acc5578af44e8adc6f27740604960"
    },
    {
        "path": "P11_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6f0e87635946a0a4960a93c883afdab985fdcfc2",
        "size": 6089,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6f0e87635946a0a4960a93c883afdab985fdcfc2"
    },
    {
        "path": "P11_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2ccbb0425b80ca94049f612ecd43d77ef46a2279",
        "size": 5529,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2ccbb0425b80ca94049f612ecd43d77ef46a2279"
    },
    {
        "path": "P11_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "93bd1babd6fba0f4c030cc393532281fffd42c0f",
        "size": 9342,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/93bd1babd6fba0f4c030cc393532281fffd42c0f"
    },
    {
        "path": "P11_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6e39f9b9eefccbff2504652cff8cc1b043963ddd",
        "size": 8486,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6e39f9b9eefccbff2504652cff8cc1b043963ddd"
    },
    {
        "path": "P11_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0852016fad1dd06e069635a5784bea3ff4052621",
        "size": 12145,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0852016fad1dd06e069635a5784bea3ff4052621"
    },
    {
        "path": "P11_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "78b7f28ac21133132bdfd57551439440f438cc92",
        "size": 8303,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/78b7f28ac21133132bdfd57551439440f438cc92"
    },
    {
        "path": "P11_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a886a04d0d9f76bfd053dc733d5b2021a2bc66fe",
        "size": 9201,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a886a04d0d9f76bfd053dc733d5b2021a2bc66fe"
    },
    {
        "path": "P11_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "016179d45fa823cff617324fbf8522ab83440abe",
        "size": 7551,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/016179d45fa823cff617324fbf8522ab83440abe"
    },
    {
        "path": "P11_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "65bf6ae747bd37422ce4b67bcb4719b07f930fa1",
        "size": 11503,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/65bf6ae747bd37422ce4b67bcb4719b07f930fa1"
    },
    {
        "path": "P11_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f62766b9c8a4b5baa884aa0c947a71d2dde84ff5",
        "size": 14747,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f62766b9c8a4b5baa884aa0c947a71d2dde84ff5"
    },
    {
        "path": "P12_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "86c4c606b540623325db78c65af9307ad0a314d6",
        "size": 5110,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/86c4c606b540623325db78c65af9307ad0a314d6"
    },
    {
        "path": "P12_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d38e64fff40591b933d9ecabd1246642933a9730",
        "size": 4210,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d38e64fff40591b933d9ecabd1246642933a9730"
    },
    {
        "path": "P12_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ca42f575224cb35190e08d64082fe038147a4bdd",
        "size": 11290,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ca42f575224cb35190e08d64082fe038147a4bdd"
    },
    {
        "path": "P12_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e4aeaaa2f6b327cc016b2f345eebd7a0ff91a275",
        "size": 10321,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e4aeaaa2f6b327cc016b2f345eebd7a0ff91a275"
    },
    {
        "path": "P12_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5e5d3198adc4d41794e15327473e5e3b289beb0d",
        "size": 9414,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5e5d3198adc4d41794e15327473e5e3b289beb0d"
    },
    {
        "path": "P12_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fedbf50b52d0f324796cd3a3f0421ef251525992",
        "size": 14730,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fedbf50b52d0f324796cd3a3f0421ef251525992"
    },
    {
        "path": "P12_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c800718dc3c84a6517ed93aba397a37553d0cbf8",
        "size": 10153,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c800718dc3c84a6517ed93aba397a37553d0cbf8"
    },
    {
        "path": "P12_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "afc6de36d3c2f951a0601e45bc976b5a54aadd46",
        "size": 9843,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/afc6de36d3c2f951a0601e45bc976b5a54aadd46"
    },
    {
        "path": "P12_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2102088321886e3b787c6f89d1828c992fc6ae76",
        "size": 12353,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2102088321886e3b787c6f89d1828c992fc6ae76"
    },
    {
        "path": "P12_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a842bd2880189e90ae8483ce11401b422a4677d7",
        "size": 7217,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a842bd2880189e90ae8483ce11401b422a4677d7"
    },
    {
        "path": "P12_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "05d68f7c950717dd1009e70749537aaafd219e96",
        "size": 8253,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/05d68f7c950717dd1009e70749537aaafd219e96"
    },
    {
        "path": "P12_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "544a457c73a4edbd5a61389bfe9e3f2199f3616c",
        "size": 12667,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/544a457c73a4edbd5a61389bfe9e3f2199f3616c"
    },
    {
        "path": "P12_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9e40a05fa7cb7b9faa6485c253f021b2df26399c",
        "size": 14258,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9e40a05fa7cb7b9faa6485c253f021b2df26399c"
    },
    {
        "path": "P12_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "99d6d6277ddacd3d94ff97c0e412e46df6dbea6d",
        "size": 5795,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/99d6d6277ddacd3d94ff97c0e412e46df6dbea6d"
    },
    {
        "path": "P12_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "132a9e1a7161f602bccb13229fe1e883fb7328a2",
        "size": 10865,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/132a9e1a7161f602bccb13229fe1e883fb7328a2"
    },
    {
        "path": "P12_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bee935a99095ae6ad4ba33eec1d6601324df5158",
        "size": 9643,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bee935a99095ae6ad4ba33eec1d6601324df5158"
    },
    {
        "path": "P12_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3cc7d89087b5a23a7c2865d1af38b95905b5ae14",
        "size": 5737,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3cc7d89087b5a23a7c2865d1af38b95905b5ae14"
    },
    {
        "path": "P12_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "39d25bccef1a3d24972734ff97c96d7b53829571",
        "size": 12786,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/39d25bccef1a3d24972734ff97c96d7b53829571"
    },
    {
        "path": "P12_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "855e2d81dd9abd1f3e2c12083e62f7f1e8da7394",
        "size": 8522,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/855e2d81dd9abd1f3e2c12083e62f7f1e8da7394"
    },
    {
        "path": "P12_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "57c6782fa4fb7b762322738676ffafab01cf4967",
        "size": 11425,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/57c6782fa4fb7b762322738676ffafab01cf4967"
    },
    {
        "path": "P12_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "10d47d981eddbdd985703b98d0e87181e86e236d",
        "size": 9289,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/10d47d981eddbdd985703b98d0e87181e86e236d"
    },
    {
        "path": "P12_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "225e3e513c506542b220f4cd7b580fa8fbb3740f",
        "size": 9793,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/225e3e513c506542b220f4cd7b580fa8fbb3740f"
    },
    {
        "path": "P12_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2b0dcccd55f556961a64fdb9cb22ee7679c2da65",
        "size": 8351,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2b0dcccd55f556961a64fdb9cb22ee7679c2da65"
    },
    {
        "path": "P12_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "58c442f309001da96b1012542b1a4868916b4f9d",
        "size": 5633,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/58c442f309001da96b1012542b1a4868916b4f9d"
    },
    {
        "path": "P12_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "69b4ec18f5062ef635ae7d69847000b0004fca94",
        "size": 7094,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/69b4ec18f5062ef635ae7d69847000b0004fca94"
    },
    {
        "path": "P12_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a711fd4ca2eb1bec119e48d75a952751a75b83e9",
        "size": 6423,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a711fd4ca2eb1bec119e48d75a952751a75b83e9"
    },
    {
        "path": "P12_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5fdae69631f490a6aaab0641c94cf7640b5bb496",
        "size": 7072,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5fdae69631f490a6aaab0641c94cf7640b5bb496"
    },
    {
        "path": "P12_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "12c8aced781c570974d3195fa5c0f48e16c940cb",
        "size": 10934,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/12c8aced781c570974d3195fa5c0f48e16c940cb"
    },
    {
        "path": "P12_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4ef9523e91921ebb8ab397330965075c401b0803",
        "size": 7250,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4ef9523e91921ebb8ab397330965075c401b0803"
    },
    {
        "path": "P12_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4d7c64e80b7fe521b04681afa0fb36ff3937044f",
        "size": 8449,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4d7c64e80b7fe521b04681afa0fb36ff3937044f"
    },
    {
        "path": "P12_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8b6f6acb156e9779c20ebee455816bd666903d9b",
        "size": 8312,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8b6f6acb156e9779c20ebee455816bd666903d9b"
    },
    {
        "path": "P12_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "06c1bf7e0191220e757952a264664d10b5b08787",
        "size": 11214,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/06c1bf7e0191220e757952a264664d10b5b08787"
    },
    {
        "path": "P12_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7be51581a46877c9483c1f23d86465f465c6bd46",
        "size": 11011,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7be51581a46877c9483c1f23d86465f465c6bd46"
    },
    {
        "path": "P12_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1b64ebdd8bf989099a47689f8575e07bc26ddacb",
        "size": 7768,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1b64ebdd8bf989099a47689f8575e07bc26ddacb"
    },
    {
        "path": "P12_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4c8fa4b46cac71c0be3b8b63a3c7c000dfaa4890",
        "size": 11655,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4c8fa4b46cac71c0be3b8b63a3c7c000dfaa4890"
    },
    {
        "path": "P12_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7c6aea6fd9dd90d467168373c74a0a7814c14024",
        "size": 9507,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7c6aea6fd9dd90d467168373c74a0a7814c14024"
    },
    {
        "path": "P12_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f706d57bdab5363abc11fa6b07eaa6e606ada290",
        "size": 6453,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f706d57bdab5363abc11fa6b07eaa6e606ada290"
    },
    {
        "path": "P12_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0af7a28c095f100b7f242538b0eb9f4843c1410e",
        "size": 5033,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0af7a28c095f100b7f242538b0eb9f4843c1410e"
    },
    {
        "path": "P12_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0f05549229398d328d7b38dc2e6e8b3797a059f8",
        "size": 5863,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0f05549229398d328d7b38dc2e6e8b3797a059f8"
    },
    {
        "path": "P12_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7545ac7fd2021345fe78be1eb712ba9a4bbbd13b",
        "size": 8624,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7545ac7fd2021345fe78be1eb712ba9a4bbbd13b"
    },
    {
        "path": "P12_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0c3b80e2df162effc2b9c7f2124c549dedba6dc2",
        "size": 7692,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0c3b80e2df162effc2b9c7f2124c549dedba6dc2"
    },
    {
        "path": "P12_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e5f4e7fecb198b4ca36989dced9a67af6b391d9e",
        "size": 11550,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e5f4e7fecb198b4ca36989dced9a67af6b391d9e"
    },
    {
        "path": "P12_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "44fa1ae4a81c8eefa332964f64367e0cf1ddc75f",
        "size": 9999,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/44fa1ae4a81c8eefa332964f64367e0cf1ddc75f"
    },
    {
        "path": "P13_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3b7d7a7437e6ccab470401d5aa09eabe02613885",
        "size": 5452,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3b7d7a7437e6ccab470401d5aa09eabe02613885"
    },
    {
        "path": "P13_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2301f0844d04ec23e88f0a1cda502466b615e940",
        "size": 7924,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2301f0844d04ec23e88f0a1cda502466b615e940"
    },
    {
        "path": "P13_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c29fd4667bde0707288062473b4fa3daf707730a",
        "size": 7865,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c29fd4667bde0707288062473b4fa3daf707730a"
    },
    {
        "path": "P13_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7748fc9165a02347bf7f8f117dfea58d7517ff45",
        "size": 12473,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7748fc9165a02347bf7f8f117dfea58d7517ff45"
    },
    {
        "path": "P13_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "01d6ea6cd5df5e3cc0bbeb1004747fade41ce524",
        "size": 8590,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/01d6ea6cd5df5e3cc0bbeb1004747fade41ce524"
    },
    {
        "path": "P13_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "38dc3518d0118624d4ac7824a2140596ff4591b4",
        "size": 8813,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/38dc3518d0118624d4ac7824a2140596ff4591b4"
    },
    {
        "path": "P13_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "094eb3da1478ecc6cc2aa2aa3179de7df72c498c",
        "size": 8131,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/094eb3da1478ecc6cc2aa2aa3179de7df72c498c"
    },
    {
        "path": "P13_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5c78cea8355de132e742bedf35a8fba109a9fa7b",
        "size": 11729,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5c78cea8355de132e742bedf35a8fba109a9fa7b"
    },
    {
        "path": "P13_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b474a70852b5ae1bcc6366ca8ed67d214af1421c",
        "size": 9231,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b474a70852b5ae1bcc6366ca8ed67d214af1421c"
    },
    {
        "path": "P13_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "67a800ce6b94679e45ba7286d26d9c80df51292d",
        "size": 15588,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/67a800ce6b94679e45ba7286d26d9c80df51292d"
    },
    {
        "path": "P13_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "332f1a54e96dbf36b6bc2befe03d2ab4ecef1fe6",
        "size": 4963,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/332f1a54e96dbf36b6bc2befe03d2ab4ecef1fe6"
    },
    {
        "path": "P13_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1d701066a92246034e73ccd0f70b75b34ddafa34",
        "size": 5726,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1d701066a92246034e73ccd0f70b75b34ddafa34"
    },
    {
        "path": "P13_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d811d5f0b4ed3f3ca9699fe09180fff5766a2d75",
        "size": 8608,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d811d5f0b4ed3f3ca9699fe09180fff5766a2d75"
    },
    {
        "path": "P13_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a2e9a75b87e90915c847f3a7b6e4524248b59748",
        "size": 6396,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a2e9a75b87e90915c847f3a7b6e4524248b59748"
    },
    {
        "path": "P13_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9d25e640e894bfaf368b503cfbb9e8a9df7a1d64",
        "size": 9717,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9d25e640e894bfaf368b503cfbb9e8a9df7a1d64"
    },
    {
        "path": "P13_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6f908a8dfcb0e2abe6ee329cca8aa8592e649b4b",
        "size": 10290,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6f908a8dfcb0e2abe6ee329cca8aa8592e649b4b"
    },
    {
        "path": "P13_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "40c3a8460ab207601c64eecd911a0eca4319e08e",
        "size": 6916,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/40c3a8460ab207601c64eecd911a0eca4319e08e"
    },
    {
        "path": "P13_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "83eb29410e90ee802366f153b90ee6d075922cb7",
        "size": 7275,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/83eb29410e90ee802366f153b90ee6d075922cb7"
    },
    {
        "path": "P13_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0bee20a52ce6b7182b0f25571883fe0dcda8e2f3",
        "size": 11860,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0bee20a52ce6b7182b0f25571883fe0dcda8e2f3"
    },
    {
        "path": "P13_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "53a307587a21fc03be71684d758f85c6b37d712b",
        "size": 11410,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/53a307587a21fc03be71684d758f85c6b37d712b"
    },
    {
        "path": "P13_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "abfee42d49446580db080e7cdf301b4432c84818",
        "size": 4486,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/abfee42d49446580db080e7cdf301b4432c84818"
    },
    {
        "path": "P13_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b232a18cc07ce2961a962a9f94b7fa46869c309c",
        "size": 4214,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b232a18cc07ce2961a962a9f94b7fa46869c309c"
    },
    {
        "path": "P13_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ec2bcd48600f6fba60a56edb615b801558bba7b0",
        "size": 11775,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ec2bcd48600f6fba60a56edb615b801558bba7b0"
    },
    {
        "path": "P13_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8c158569adb6aa4f116d36d724ca0ef3ba8c08d9",
        "size": 8865,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8c158569adb6aa4f116d36d724ca0ef3ba8c08d9"
    },
    {
        "path": "P13_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d7546f155d108587f720a91543bed297a413df98",
        "size": 8767,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d7546f155d108587f720a91543bed297a413df98"
    },
    {
        "path": "P13_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3241444f730d61925192c18e6f0e9f18fd9bb01e",
        "size": 7685,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3241444f730d61925192c18e6f0e9f18fd9bb01e"
    },
    {
        "path": "P13_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0b0cefeb4eaa11a95036e52577edf7807e42ba82",
        "size": 7590,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0b0cefeb4eaa11a95036e52577edf7807e42ba82"
    },
    {
        "path": "P13_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0833c8968cf1dd3ea7f1360042ce8f5dd70f81d8",
        "size": 8139,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0833c8968cf1dd3ea7f1360042ce8f5dd70f81d8"
    },
    {
        "path": "P13_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7d2a71dcc333580dd4925c6413db0e40f2003650",
        "size": 7246,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7d2a71dcc333580dd4925c6413db0e40f2003650"
    },
    {
        "path": "P13_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9987d7f2dd3547ecbb756545dfdd71073737b5fc",
        "size": 10202,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9987d7f2dd3547ecbb756545dfdd71073737b5fc"
    },
    {
        "path": "P13_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2e36d5db426ed288d3ea635572788e75cceea8c6",
        "size": 6531,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2e36d5db426ed288d3ea635572788e75cceea8c6"
    },
    {
        "path": "P13_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "66a1e90c86251ab0d4b62dd7af0f6212df0d4cf1",
        "size": 8598,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/66a1e90c86251ab0d4b62dd7af0f6212df0d4cf1"
    },
    {
        "path": "P13_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cb2da04c281d1f2e58d65d80ea79a22b781e7745",
        "size": 6287,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cb2da04c281d1f2e58d65d80ea79a22b781e7745"
    },
    {
        "path": "P13_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1dc3141198e1af28074ba780f3433b5433e749d7",
        "size": 6194,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1dc3141198e1af28074ba780f3433b5433e749d7"
    },
    {
        "path": "P13_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "35be3d23f3d9d4ed782721a7d4d0c2b3a9444dea",
        "size": 4823,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/35be3d23f3d9d4ed782721a7d4d0c2b3a9444dea"
    },
    {
        "path": "P13_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ca586d7b8c0dd991ca36b42af7427cf54626d220",
        "size": 7012,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ca586d7b8c0dd991ca36b42af7427cf54626d220"
    },
    {
        "path": "P13_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2f9d7a089a6d4b10f1cdac065f6a5d25ae5065d3",
        "size": 6017,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2f9d7a089a6d4b10f1cdac065f6a5d25ae5065d3"
    },
    {
        "path": "P13_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1346f2db84997c084479c2b976e56ae69da4b938",
        "size": 8691,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1346f2db84997c084479c2b976e56ae69da4b938"
    },
    {
        "path": "P13_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a0f82254fc24fb50bca4cc0b88f3c70f7d5bfabd",
        "size": 6077,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a0f82254fc24fb50bca4cc0b88f3c70f7d5bfabd"
    },
    {
        "path": "P13_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5e9d49c89b73a53069d1f54d8e46e42d98cd303a",
        "size": 6971,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5e9d49c89b73a53069d1f54d8e46e42d98cd303a"
    },
    {
        "path": "P13_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c7383889aeed9ab8962ae26ecead39bf1160c000",
        "size": 8186,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c7383889aeed9ab8962ae26ecead39bf1160c000"
    },
    {
        "path": "P13_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "314a2f8892d1e6cc6383a984931d6375438c6b49",
        "size": 9343,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/314a2f8892d1e6cc6383a984931d6375438c6b49"
    },
    {
        "path": "P13_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c6473043f4e91a6faa37f90973c33467b7a334d6",
        "size": 8551,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c6473043f4e91a6faa37f90973c33467b7a334d6"
    },
    {
        "path": "P13_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3da7f52bce9bd57c42d579dc8c746bb2653ebe93",
        "size": 9918,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3da7f52bce9bd57c42d579dc8c746bb2653ebe93"
    },
    {
        "path": "P13_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "88ca58dd114444e71634920212394f7b35a63ba0",
        "size": 9275,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/88ca58dd114444e71634920212394f7b35a63ba0"
    },
    {
        "path": "P13_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c6548f2756864366db899863e2f1b84a06a1df95",
        "size": 7974,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c6548f2756864366db899863e2f1b84a06a1df95"
    },
    {
        "path": "P13_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "17f41072e75c98d5f4ab2aa6f3160ea5b0bb029e",
        "size": 13537,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/17f41072e75c98d5f4ab2aa6f3160ea5b0bb029e"
    },
    {
        "path": "P13_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "375c29ac29174382a7ab6edfc5078e72492dd25e",
        "size": 5243,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/375c29ac29174382a7ab6edfc5078e72492dd25e"
    },
    {
        "path": "P13_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c53ef6e6c388df11fb7980cb612d3e8bc9a82cfa",
        "size": 5360,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c53ef6e6c388df11fb7980cb612d3e8bc9a82cfa"
    },
    {
        "path": "P13_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f13c32049649e4d1f5ab265384dd6700571d9ca0",
        "size": 10269,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f13c32049649e4d1f5ab265384dd6700571d9ca0"
    },
    {
        "path": "P13_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7f735864997af8546e049f56dc9581f23f8327f0",
        "size": 7270,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7f735864997af8546e049f56dc9581f23f8327f0"
    },
    {
        "path": "P13_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "29da3245eaeb21ac0aa271c9e7dade024008ee13",
        "size": 7050,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/29da3245eaeb21ac0aa271c9e7dade024008ee13"
    },
    {
        "path": "P13_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ba8ae9800c3e3deb1bd16b157d3936da5ed118d0",
        "size": 9277,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ba8ae9800c3e3deb1bd16b157d3936da5ed118d0"
    },
    {
        "path": "P13_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "886ae346c4fee5adb02af4ebb029fb6f4973862d",
        "size": 6909,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/886ae346c4fee5adb02af4ebb029fb6f4973862d"
    },
    {
        "path": "P13_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7ab158b31873b738df0eb9c3d8d275e3fa0a9aae",
        "size": 11228,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7ab158b31873b738df0eb9c3d8d275e3fa0a9aae"
    },
    {
        "path": "P13_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a5d914f60374ad2f9e379142aae6f98d2fb294f1",
        "size": 7290,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a5d914f60374ad2f9e379142aae6f98d2fb294f1"
    },
    {
        "path": "P13_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f4d53f01a56ae09ea7ebb89aaa5745f2f0b1a5fd",
        "size": 11372,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f4d53f01a56ae09ea7ebb89aaa5745f2f0b1a5fd"
    },
    {
        "path": "P13_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0121033061e6419e19e12f57b9c82a119e41d019",
        "size": 4501,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0121033061e6419e19e12f57b9c82a119e41d019"
    },
    {
        "path": "P13_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "30b841d71239d3994c71d001e2f0622cf4c6a3bd",
        "size": 9911,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/30b841d71239d3994c71d001e2f0622cf4c6a3bd"
    },
    {
        "path": "P13_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "92bcb5c23b8d8a411a6926f53ff63a53d6e41405",
        "size": 18424,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/92bcb5c23b8d8a411a6926f53ff63a53d6e41405"
    },
    {
        "path": "P14_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "833ee16d9310474adf8949dc41fc901045711573",
        "size": 12273,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/833ee16d9310474adf8949dc41fc901045711573"
    },
    {
        "path": "P14_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6be72324c061bb67be507361cf97c4d38668896c",
        "size": 6657,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6be72324c061bb67be507361cf97c4d38668896c"
    },
    {
        "path": "P14_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d7655881edfbc81311ddd3d1cfde66c8169bbdca",
        "size": 13774,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d7655881edfbc81311ddd3d1cfde66c8169bbdca"
    },
    {
        "path": "P14_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3950be8622735d1a7d68d37a6c2edc76015295bc",
        "size": 13279,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3950be8622735d1a7d68d37a6c2edc76015295bc"
    },
    {
        "path": "P14_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "596da4bb352abcea450c9f6c4c840ad2ec549e77",
        "size": 11902,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/596da4bb352abcea450c9f6c4c840ad2ec549e77"
    },
    {
        "path": "P14_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8ac09685fa55d81a1e8862f797f63e3d8b5f5159",
        "size": 11459,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8ac09685fa55d81a1e8862f797f63e3d8b5f5159"
    },
    {
        "path": "P14_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c038c6f50415bdea915f2694185d25276b636387",
        "size": 4329,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c038c6f50415bdea915f2694185d25276b636387"
    },
    {
        "path": "P14_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7a0d5b2106b2a87f732b2361cbb3d547f53486d9",
        "size": 8464,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7a0d5b2106b2a87f732b2361cbb3d547f53486d9"
    },
    {
        "path": "P14_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f004f79152bea35061a83dfc42a82dde67903e8b",
        "size": 9204,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f004f79152bea35061a83dfc42a82dde67903e8b"
    },
    {
        "path": "P14_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "221c64aed17756a6454fc0472f81ecf9e08af213",
        "size": 12248,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/221c64aed17756a6454fc0472f81ecf9e08af213"
    },
    {
        "path": "P14_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6ef55ead85182282db45e45fbc8b35c04deff970",
        "size": 7225,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6ef55ead85182282db45e45fbc8b35c04deff970"
    },
    {
        "path": "P14_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b627debf71aca6510c7a0762beb66e32f44a6659",
        "size": 6735,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b627debf71aca6510c7a0762beb66e32f44a6659"
    },
    {
        "path": "P14_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7be38bc23c5f437087fe7d298fe544bf17104bf5",
        "size": 8168,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7be38bc23c5f437087fe7d298fe544bf17104bf5"
    },
    {
        "path": "P14_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "30d123cff0cb148b43f97cfdd7d8798220bdfc1d",
        "size": 8022,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/30d123cff0cb148b43f97cfdd7d8798220bdfc1d"
    },
    {
        "path": "P14_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d2e02b3b67628c397c4ff125e320168ae18f57be",
        "size": 10035,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d2e02b3b67628c397c4ff125e320168ae18f57be"
    },
    {
        "path": "P14_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "14ce91476ba26b3e30135478a1b866312e6549bf",
        "size": 12574,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/14ce91476ba26b3e30135478a1b866312e6549bf"
    },
    {
        "path": "P14_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "01f2dc58f19aac3cdd9f980f1a2f671e1e46a8fd",
        "size": 8728,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/01f2dc58f19aac3cdd9f980f1a2f671e1e46a8fd"
    },
    {
        "path": "P14_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9bcc9901b39f0399e11008c7e1fb2652b13792b8",
        "size": 8791,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9bcc9901b39f0399e11008c7e1fb2652b13792b8"
    },
    {
        "path": "P14_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "40e522c88683395f530429638a9f47b93521a049",
        "size": 12163,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/40e522c88683395f530429638a9f47b93521a049"
    },
    {
        "path": "P14_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4a2ad76b128a201e19399252654117d0c5b7298d",
        "size": 9543,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4a2ad76b128a201e19399252654117d0c5b7298d"
    },
    {
        "path": "P14_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b4ba74fac079afbcae41a1e2ff57ae637bbd5c70",
        "size": 7585,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b4ba74fac079afbcae41a1e2ff57ae637bbd5c70"
    },
    {
        "path": "P14_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "774e4a04e7c1e47ca3cbbbf7e5f11e3416578a1f",
        "size": 6045,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/774e4a04e7c1e47ca3cbbbf7e5f11e3416578a1f"
    },
    {
        "path": "P14_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a4424bd219feab8450e2c3750125f55c2a8a5a9a",
        "size": 11417,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a4424bd219feab8450e2c3750125f55c2a8a5a9a"
    },
    {
        "path": "P14_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f1044f9efab5b117e67bfa6362d93a78ea23b142",
        "size": 11521,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f1044f9efab5b117e67bfa6362d93a78ea23b142"
    },
    {
        "path": "P14_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3a67cee4579c10f5a0fb7b83914947f1f06ed4ec",
        "size": 5448,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3a67cee4579c10f5a0fb7b83914947f1f06ed4ec"
    },
    {
        "path": "P14_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "09e21421286c28de5d3576db9948495465123140",
        "size": 10254,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/09e21421286c28de5d3576db9948495465123140"
    },
    {
        "path": "P14_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "14420d45cfd14291cd94c5f4f36278529e194d33",
        "size": 6126,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/14420d45cfd14291cd94c5f4f36278529e194d33"
    },
    {
        "path": "P14_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0ee1a9ffe95808168386e333d0c69196cba4fc72",
        "size": 9067,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0ee1a9ffe95808168386e333d0c69196cba4fc72"
    },
    {
        "path": "P14_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ae36ed5c2bb6738f9f93aaf97db178323e9e72fe",
        "size": 13275,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ae36ed5c2bb6738f9f93aaf97db178323e9e72fe"
    },
    {
        "path": "P14_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1ee2ae086a04f89bc947ac86c6e931d3e998b621",
        "size": 9842,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1ee2ae086a04f89bc947ac86c6e931d3e998b621"
    },
    {
        "path": "P14_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8b92af2ed5f3851ed77740f1501f7b28512de8bf",
        "size": 6262,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8b92af2ed5f3851ed77740f1501f7b28512de8bf"
    },
    {
        "path": "P14_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "90a1374b6906022406713acad342f1359bc16417",
        "size": 6347,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/90a1374b6906022406713acad342f1359bc16417"
    },
    {
        "path": "P14_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "48d16046bb94f2b8e7a0c5d265ffce0cf3125aa7",
        "size": 7611,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/48d16046bb94f2b8e7a0c5d265ffce0cf3125aa7"
    },
    {
        "path": "P14_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e2e110b64701c4ffb82a5afd4e95631de8145bf9",
        "size": 12081,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e2e110b64701c4ffb82a5afd4e95631de8145bf9"
    },
    {
        "path": "P14_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2bd5ab073e1a53592ce63a8db35cd202651a6d23",
        "size": 6447,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2bd5ab073e1a53592ce63a8db35cd202651a6d23"
    },
    {
        "path": "P14_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "11cf835b575c042a827d3d55779b24deafbcb943",
        "size": 4815,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/11cf835b575c042a827d3d55779b24deafbcb943"
    },
    {
        "path": "P14_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cefd8249e0c46978e2562d9ebd61cfe707beeb33",
        "size": 9210,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cefd8249e0c46978e2562d9ebd61cfe707beeb33"
    },
    {
        "path": "P14_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "069601ada27e66fa2870692b0946a7e7840c47d6",
        "size": 6906,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/069601ada27e66fa2870692b0946a7e7840c47d6"
    },
    {
        "path": "P14_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9002578168b7fb6eb1ce1af0b42c6e6ac920595a",
        "size": 6689,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9002578168b7fb6eb1ce1af0b42c6e6ac920595a"
    },
    {
        "path": "P14_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e156c0c18de9e757046295b70b11f8365f808b0c",
        "size": 11349,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e156c0c18de9e757046295b70b11f8365f808b0c"
    },
    {
        "path": "P14_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e8355ef392b3b084809dcdc3f89a86bd09ec62ce",
        "size": 9046,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e8355ef392b3b084809dcdc3f89a86bd09ec62ce"
    },
    {
        "path": "P14_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "212f739c134c3c4edcc2c9ec22a4a7b2f8226091",
        "size": 10857,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/212f739c134c3c4edcc2c9ec22a4a7b2f8226091"
    },
    {
        "path": "P14_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "be9c9e9053ee4be4ecff64f2fe5989ad480500a6",
        "size": 15591,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/be9c9e9053ee4be4ecff64f2fe5989ad480500a6"
    },
    {
        "path": "P14_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2fa33b483ff212e87b327b7451ae1ce188c32d48",
        "size": 14112,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2fa33b483ff212e87b327b7451ae1ce188c32d48"
    },
    {
        "path": "P14_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e2e65b62f849529972a6adffd34bd9440736d243",
        "size": 7499,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e2e65b62f849529972a6adffd34bd9440736d243"
    },
    {
        "path": "P14_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6ffa400cfa43b9bbcccd5afaf4df15ed97e4b79d",
        "size": 13388,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6ffa400cfa43b9bbcccd5afaf4df15ed97e4b79d"
    },
    {
        "path": "P14_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "55341929a03166af15b44a82871107c28d4389a6",
        "size": 17555,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/55341929a03166af15b44a82871107c28d4389a6"
    },
    {
        "path": "P14_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0f5592001016fd764ea0f76cbce753b1777cc6ea",
        "size": 7913,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0f5592001016fd764ea0f76cbce753b1777cc6ea"
    },
    {
        "path": "P14_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "36c9ed95889d83372495e9d07654dc0f28f25f16",
        "size": 8430,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/36c9ed95889d83372495e9d07654dc0f28f25f16"
    },
    {
        "path": "P14_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "47602c9a93008d0dea41056344a5d86201fa9195",
        "size": 6895,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/47602c9a93008d0dea41056344a5d86201fa9195"
    },
    {
        "path": "P14_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "80d54fc7f3dc7b8c29d4102abae29816248f9462",
        "size": 5033,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/80d54fc7f3dc7b8c29d4102abae29816248f9462"
    },
    {
        "path": "P14_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3ddd2437e2f3ce84b04c444b1c52a0de609a2a56",
        "size": 3666,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3ddd2437e2f3ce84b04c444b1c52a0de609a2a56"
    },
    {
        "path": "P14_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "861d7256a1f6c3d8dd4dd6eb73110d2a69d7f06d",
        "size": 9458,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/861d7256a1f6c3d8dd4dd6eb73110d2a69d7f06d"
    },
    {
        "path": "P14_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "596407e04b8f237b5522989338090ccf1e5f5206",
        "size": 6736,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/596407e04b8f237b5522989338090ccf1e5f5206"
    },
    {
        "path": "P14_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fcd64b8b7c2b7d198681474629480721fb364e7e",
        "size": 11140,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fcd64b8b7c2b7d198681474629480721fb364e7e"
    },
    {
        "path": "P14_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0416dda9e34b2de89f48618d8c8d18620e40b72e",
        "size": 9544,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0416dda9e34b2de89f48618d8c8d18620e40b72e"
    },
    {
        "path": "P14_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "34fa564995fe07cb021d43ab474a73356c25d913",
        "size": 9427,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/34fa564995fe07cb021d43ab474a73356c25d913"
    },
    {
        "path": "P14_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d96c2402ea82bf4305b8d5e113b460f05d71547e",
        "size": 6331,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d96c2402ea82bf4305b8d5e113b460f05d71547e"
    },
    {
        "path": "P14_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b417f33a6739dbf809db5e689453aac81c7791ff",
        "size": 11538,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b417f33a6739dbf809db5e689453aac81c7791ff"
    },
    {
        "path": "P14_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dfd5e490cf59069fa4de8682d6a9cf122b7363c6",
        "size": 17449,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dfd5e490cf59069fa4de8682d6a9cf122b7363c6"
    },
    {
        "path": "P15_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "57fc86089a96eab0e34662b83d1eed24adf7351e",
        "size": 3604,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/57fc86089a96eab0e34662b83d1eed24adf7351e"
    },
    {
        "path": "P15_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0037af557401dfaf486579598fe82045ffc470b6",
        "size": 2982,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0037af557401dfaf486579598fe82045ffc470b6"
    },
    {
        "path": "P15_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fcb937d19d9088d6268acef66e001ae4abe30550",
        "size": 4428,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fcb937d19d9088d6268acef66e001ae4abe30550"
    },
    {
        "path": "P15_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "05212b8ae7694fa26e3581dda2601294aaa4927f",
        "size": 2996,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/05212b8ae7694fa26e3581dda2601294aaa4927f"
    },
    {
        "path": "P15_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e0098f5f881edad3825321b201b3e1b74ec176f8",
        "size": 3744,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e0098f5f881edad3825321b201b3e1b74ec176f8"
    },
    {
        "path": "P15_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7c6440905df17ad152780a105845a8ae62a4a4a7",
        "size": 2856,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7c6440905df17ad152780a105845a8ae62a4a4a7"
    },
    {
        "path": "P15_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "17705b06ade94b1536950fe2cd84963b2ac54ecd",
        "size": 4001,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/17705b06ade94b1536950fe2cd84963b2ac54ecd"
    },
    {
        "path": "P15_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16f1565b1b751fadb8c6d82c6bc93ffceff87906",
        "size": 4559,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16f1565b1b751fadb8c6d82c6bc93ffceff87906"
    },
    {
        "path": "P15_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a7763f85612f6a84c0251349f7d6e7fe99cdb7e8",
        "size": 3192,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a7763f85612f6a84c0251349f7d6e7fe99cdb7e8"
    },
    {
        "path": "P15_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ac96271deb850b3ea3db8e6970861d4efd6551eb",
        "size": 5331,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ac96271deb850b3ea3db8e6970861d4efd6551eb"
    },
    {
        "path": "P15_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "01b7197dfcb1a9ee591b96ab8e48e8f7872568d0",
        "size": 1902,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/01b7197dfcb1a9ee591b96ab8e48e8f7872568d0"
    },
    {
        "path": "P15_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "997146aa8210e899e1ef8c3d7c8ef2fe0125a2c3",
        "size": 2839,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/997146aa8210e899e1ef8c3d7c8ef2fe0125a2c3"
    },
    {
        "path": "P15_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a44f1f12e3c7d7c5e450347631f272c30a3d3d98",
        "size": 2017,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a44f1f12e3c7d7c5e450347631f272c30a3d3d98"
    },
    {
        "path": "P15_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "02a9af44a0b8091310384327b65a365218ca19cf",
        "size": 2028,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/02a9af44a0b8091310384327b65a365218ca19cf"
    },
    {
        "path": "P15_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fab17a099b139e95ad73edca906a3c4122c3dac8",
        "size": 4015,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fab17a099b139e95ad73edca906a3c4122c3dac8"
    },
    {
        "path": "P15_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fbdf215687a016e1f819b33a84c52532aa0fd687",
        "size": 2109,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fbdf215687a016e1f819b33a84c52532aa0fd687"
    },
    {
        "path": "P15_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "995f813982d83e458e3a97b102e850ff43d21cb3",
        "size": 2304,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/995f813982d83e458e3a97b102e850ff43d21cb3"
    },
    {
        "path": "P15_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "23a68c6e4e5656f9b8528fcb133d67be25fa6db5",
        "size": 4148,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/23a68c6e4e5656f9b8528fcb133d67be25fa6db5"
    },
    {
        "path": "P15_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f42eb59673e2b2b9434967fc9fd8a68f5adc1093",
        "size": 2375,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f42eb59673e2b2b9434967fc9fd8a68f5adc1093"
    },
    {
        "path": "P15_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "182d6520c92bb89b2616fd7fbf30ba0b002285da",
        "size": 6010,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/182d6520c92bb89b2616fd7fbf30ba0b002285da"
    },
    {
        "path": "P15_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6eebe221aab5537648a95293f1474089bb37fae1",
        "size": 1268,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6eebe221aab5537648a95293f1474089bb37fae1"
    },
    {
        "path": "P15_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "84af7fe643803841a1813d2daf070a7f2660b1c0",
        "size": 2642,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/84af7fe643803841a1813d2daf070a7f2660b1c0"
    },
    {
        "path": "P15_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a0b9390072cbb09caff66161ff4edace3545b281",
        "size": 3619,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a0b9390072cbb09caff66161ff4edace3545b281"
    },
    {
        "path": "P15_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1a0432eebd84160e591691f2f24566f10d8fcb9e",
        "size": 3193,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1a0432eebd84160e591691f2f24566f10d8fcb9e"
    },
    {
        "path": "P15_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "662e6833c7825bc8308e6b36895c6652180d8b2b",
        "size": 3687,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/662e6833c7825bc8308e6b36895c6652180d8b2b"
    },
    {
        "path": "P15_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0846c511254c8cd97a8d95f44c1ac96d8a122d05",
        "size": 4201,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0846c511254c8cd97a8d95f44c1ac96d8a122d05"
    },
    {
        "path": "P15_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "83db52ad1a9d2b9de76088c457c576adf12f9640",
        "size": 3451,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/83db52ad1a9d2b9de76088c457c576adf12f9640"
    },
    {
        "path": "P15_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fd40757bc3b0293061d478ff20ebfffe85d7583f",
        "size": 2708,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fd40757bc3b0293061d478ff20ebfffe85d7583f"
    },
    {
        "path": "P15_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d4e19e88b29950de7b8d4b43eb4e6eb16762edf2",
        "size": 3106,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d4e19e88b29950de7b8d4b43eb4e6eb16762edf2"
    },
    {
        "path": "P15_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e811c7ed8b64787de84724bc1550ade53f06f6d4",
        "size": 4446,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e811c7ed8b64787de84724bc1550ade53f06f6d4"
    },
    {
        "path": "P15_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c96eae3ad3950c41b461ad2c2bdb15697dc05a9e",
        "size": 2566,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c96eae3ad3950c41b461ad2c2bdb15697dc05a9e"
    },
    {
        "path": "P15_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3f2c5ae95f6e7e5eb40e8750cf49042c87e87cc2",
        "size": 4155,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3f2c5ae95f6e7e5eb40e8750cf49042c87e87cc2"
    },
    {
        "path": "P15_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "19a6f593b2ca424ec1a30ed095d7ea11ed996aaa",
        "size": 1067,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/19a6f593b2ca424ec1a30ed095d7ea11ed996aaa"
    },
    {
        "path": "P15_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "60859200564f0a39886b8182418fa3ee6a211488",
        "size": 1275,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/60859200564f0a39886b8182418fa3ee6a211488"
    },
    {
        "path": "P15_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f33d3c6d592a020880b4f7bb94e5bb4f9e3e0774",
        "size": 1333,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f33d3c6d592a020880b4f7bb94e5bb4f9e3e0774"
    },
    {
        "path": "P15_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1c3d8d9b10a25290096864f1d994964770b6ca41",
        "size": 1197,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1c3d8d9b10a25290096864f1d994964770b6ca41"
    },
    {
        "path": "P15_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fa79ca6594b168e523ab72221a55c39b5a811335",
        "size": 1471,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fa79ca6594b168e523ab72221a55c39b5a811335"
    },
    {
        "path": "P15_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e2f8a698179ed65e79ce279bfb7015f5a5572b25",
        "size": 5573,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e2f8a698179ed65e79ce279bfb7015f5a5572b25"
    },
    {
        "path": "P15_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "98c64b748ca15d29fc1e11c047910ebc43946150",
        "size": 2495,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/98c64b748ca15d29fc1e11c047910ebc43946150"
    },
    {
        "path": "P15_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b06a0e220f546388c149eb2f5c4e98856d41eb0b",
        "size": 3402,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b06a0e220f546388c149eb2f5c4e98856d41eb0b"
    },
    {
        "path": "P15_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "007761adc4ff474345f2fe7345f070827ac75709",
        "size": 3051,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/007761adc4ff474345f2fe7345f070827ac75709"
    },
    {
        "path": "P15_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4e80fda92f965fde8e250f2abcf0a313e05c2b00",
        "size": 4615,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4e80fda92f965fde8e250f2abcf0a313e05c2b00"
    },
    {
        "path": "P15_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5448edcc0a8388be908307b5f7a1a135cd006cca",
        "size": 4289,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5448edcc0a8388be908307b5f7a1a135cd006cca"
    },
    {
        "path": "P15_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "89b23f3363fb1f27489996a672b33cf2a5acfb0c",
        "size": 5389,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/89b23f3363fb1f27489996a672b33cf2a5acfb0c"
    },
    {
        "path": "P15_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "53f9cc454bc299375623d0556bb808512cfcc793",
        "size": 3537,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/53f9cc454bc299375623d0556bb808512cfcc793"
    },
    {
        "path": "P15_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d0fe709f2e393f2b73c7a09546311352660dad57",
        "size": 4709,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d0fe709f2e393f2b73c7a09546311352660dad57"
    },
    {
        "path": "P15_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "519ea8715d6835f219d7c5e04eb58be90ba9b2ef",
        "size": 3055,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/519ea8715d6835f219d7c5e04eb58be90ba9b2ef"
    },
    {
        "path": "P15_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2be2d706bddc8b08f4720bbadf11d1e9cf1a3bcd",
        "size": 2776,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2be2d706bddc8b08f4720bbadf11d1e9cf1a3bcd"
    },
    {
        "path": "P15_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "272b1907df3250bd5e280b8b11281b4897234d83",
        "size": 2973,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/272b1907df3250bd5e280b8b11281b4897234d83"
    },
    {
        "path": "P15_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b83852e5b51894b516957ab2713fca70bca5f7fc",
        "size": 3951,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b83852e5b51894b516957ab2713fca70bca5f7fc"
    },
    {
        "path": "P15_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1b7e13c896b86ca4248316f90ee2bff4d9ec3430",
        "size": 3667,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1b7e13c896b86ca4248316f90ee2bff4d9ec3430"
    },
    {
        "path": "P15_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8037148b2a9a7a839bce270588b45296466dc961",
        "size": 1407,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8037148b2a9a7a839bce270588b45296466dc961"
    },
    {
        "path": "P15_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e08232a07fd2f0554b978075869cf8ae8858e2df",
        "size": 3524,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e08232a07fd2f0554b978075869cf8ae8858e2df"
    },
    {
        "path": "P15_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ddef4f27fab2fa9db58a0e83eb2d83fec7783081",
        "size": 3815,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ddef4f27fab2fa9db58a0e83eb2d83fec7783081"
    },
    {
        "path": "P15_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "79b364e98f62e89fc9c1f268ac010e461a3f603f",
        "size": 4368,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/79b364e98f62e89fc9c1f268ac010e461a3f603f"
    },
    {
        "path": "P15_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a5c31fce58f17e7cc100645e4766ea1946854f53",
        "size": 2639,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a5c31fce58f17e7cc100645e4766ea1946854f53"
    },
    {
        "path": "P15_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c136bc80980db2f67c37a95382f6eb483c00882a",
        "size": 2090,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c136bc80980db2f67c37a95382f6eb483c00882a"
    },
    {
        "path": "P15_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0beca7f39420e5fa5c387dd6640146924def3658",
        "size": 2160,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0beca7f39420e5fa5c387dd6640146924def3658"
    },
    {
        "path": "P15_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "055da4b7a3f5a6584d5f6bf3f60094bc6b7eb821",
        "size": 4776,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/055da4b7a3f5a6584d5f6bf3f60094bc6b7eb821"
    },
    {
        "path": "P15_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "75d31b885bff55d70358a146687bbb1296dbbc39",
        "size": 7121,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/75d31b885bff55d70358a146687bbb1296dbbc39"
    },
    {
        "path": "P16_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "774282f8d018cccf531c137164e4f4325207fe39",
        "size": 7209,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/774282f8d018cccf531c137164e4f4325207fe39"
    },
    {
        "path": "P16_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6459e05016a1ab3d89b35ea2c4b091ee825c56f0",
        "size": 8037,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6459e05016a1ab3d89b35ea2c4b091ee825c56f0"
    },
    {
        "path": "P16_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "73ae53b8f9df83f1efbd949c493ef17a4e88c84d",
        "size": 11161,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/73ae53b8f9df83f1efbd949c493ef17a4e88c84d"
    },
    {
        "path": "P16_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8504d695dcff034c4b5f443901030c7dc1a6029c",
        "size": 13963,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8504d695dcff034c4b5f443901030c7dc1a6029c"
    },
    {
        "path": "P16_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a21a631aebf4e9eb82e50ccbd4ddca1dc7370222",
        "size": 11751,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a21a631aebf4e9eb82e50ccbd4ddca1dc7370222"
    },
    {
        "path": "P16_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "516d2e2943773f0eab0221888a9f5776de9a76ec",
        "size": 9621,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/516d2e2943773f0eab0221888a9f5776de9a76ec"
    },
    {
        "path": "P16_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c89017fb64aebc40d90dcf03a438044cc60c44bb",
        "size": 7102,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c89017fb64aebc40d90dcf03a438044cc60c44bb"
    },
    {
        "path": "P16_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "457552abaa932384326ee99076ac0da8ed3a18ae",
        "size": 11986,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/457552abaa932384326ee99076ac0da8ed3a18ae"
    },
    {
        "path": "P16_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16ea6d51523d94a0083bf008ea3018c60987cc57",
        "size": 9376,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16ea6d51523d94a0083bf008ea3018c60987cc57"
    },
    {
        "path": "P16_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "51659c3bcde8e9f78778bb752ab5f5fccf0725b4",
        "size": 10187,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/51659c3bcde8e9f78778bb752ab5f5fccf0725b4"
    },
    {
        "path": "P16_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e2342a46628145bf1bd3fb42e3d87f13641364dd",
        "size": 8442,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e2342a46628145bf1bd3fb42e3d87f13641364dd"
    },
    {
        "path": "P16_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ec5192467b06d040e11078e10dfb9a26398de7e2",
        "size": 9128,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ec5192467b06d040e11078e10dfb9a26398de7e2"
    },
    {
        "path": "P16_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c1ca434b9c6b8a88e954242d8997801785b9074d",
        "size": 9488,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c1ca434b9c6b8a88e954242d8997801785b9074d"
    },
    {
        "path": "P16_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "88d7f99d9433d17d880aa5249bbe91f9f4bfb68b",
        "size": 7626,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/88d7f99d9433d17d880aa5249bbe91f9f4bfb68b"
    },
    {
        "path": "P16_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3d183be45d27c8256f921c1ef888018b15fb7226",
        "size": 11445,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3d183be45d27c8256f921c1ef888018b15fb7226"
    },
    {
        "path": "P16_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8d7e0a131274ed3b449e02052eed95fd19071f0e",
        "size": 9286,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8d7e0a131274ed3b449e02052eed95fd19071f0e"
    },
    {
        "path": "P16_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fce211b97a0537de9b7400dd6729d772df7290a0",
        "size": 9624,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fce211b97a0537de9b7400dd6729d772df7290a0"
    },
    {
        "path": "P16_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6cd33334608b541c9e43e9e26ce115ac5d5212bd",
        "size": 11825,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6cd33334608b541c9e43e9e26ce115ac5d5212bd"
    },
    {
        "path": "P16_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "68c2a1062f5e865147548de6267a9e104ac545c6",
        "size": 13693,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/68c2a1062f5e865147548de6267a9e104ac545c6"
    },
    {
        "path": "P16_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d40614fccdb46fc1c67210c78e0dca086f82e4b9",
        "size": 9412,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d40614fccdb46fc1c67210c78e0dca086f82e4b9"
    },
    {
        "path": "P16_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c08f0226065b3245d34ebefad7df417246c5796d",
        "size": 6360,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c08f0226065b3245d34ebefad7df417246c5796d"
    },
    {
        "path": "P16_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "98552c76ecc6b33dd87c004212e4d1f26a87311f",
        "size": 5711,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/98552c76ecc6b33dd87c004212e4d1f26a87311f"
    },
    {
        "path": "P16_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "650308c501f22ede4f716925d0e429c8bd74b22b",
        "size": 13321,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/650308c501f22ede4f716925d0e429c8bd74b22b"
    },
    {
        "path": "P16_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f1e3afb5dfa2a4b96cd6bf281547d02c9fd72eea",
        "size": 13501,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f1e3afb5dfa2a4b96cd6bf281547d02c9fd72eea"
    },
    {
        "path": "P16_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "62346b5450c2eb7d9aa87a09fcc308eed6a66d51",
        "size": 10369,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/62346b5450c2eb7d9aa87a09fcc308eed6a66d51"
    },
    {
        "path": "P16_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "68b7a696d377d6e701a6f5c4ff04dc63eb4ed1ac",
        "size": 12448,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/68b7a696d377d6e701a6f5c4ff04dc63eb4ed1ac"
    },
    {
        "path": "P16_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "810e4e39a3863dc4d89d1028840f7b93ccd90c07",
        "size": 7080,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/810e4e39a3863dc4d89d1028840f7b93ccd90c07"
    },
    {
        "path": "P16_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "21093c9ee5cc2eaa27b6ee0001ba0d12d595b39f",
        "size": 11049,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/21093c9ee5cc2eaa27b6ee0001ba0d12d595b39f"
    },
    {
        "path": "P16_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fe054fe66e731002ef8641ece0e58b598ba01eaf",
        "size": 10998,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fe054fe66e731002ef8641ece0e58b598ba01eaf"
    },
    {
        "path": "P16_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1666718073f6eb4f9d847a763f315b75413f4781",
        "size": 7062,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1666718073f6eb4f9d847a763f315b75413f4781"
    },
    {
        "path": "P16_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9cbd13ddce9859f2cadd104ecd4d632d1d44b25c",
        "size": 5713,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9cbd13ddce9859f2cadd104ecd4d632d1d44b25c"
    },
    {
        "path": "P16_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7910a8eb3718715237ebd3521ff8463a70db8090",
        "size": 8610,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7910a8eb3718715237ebd3521ff8463a70db8090"
    },
    {
        "path": "P16_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f35c2eb3de0a8f6dfd79d2644118d262f0e147a0",
        "size": 6341,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f35c2eb3de0a8f6dfd79d2644118d262f0e147a0"
    },
    {
        "path": "P16_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d2e3c3ac5b10244c5962b91be96c98327dc9889f",
        "size": 10524,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d2e3c3ac5b10244c5962b91be96c98327dc9889f"
    },
    {
        "path": "P16_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "43a4671783b2495504302535376302567ba4ee81",
        "size": 5840,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/43a4671783b2495504302535376302567ba4ee81"
    },
    {
        "path": "P16_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "59d950ba4896981db8d594027e784ae729eff68f",
        "size": 8769,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/59d950ba4896981db8d594027e784ae729eff68f"
    },
    {
        "path": "P16_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2ebf6541c082fade03ab312da58c05f078f60c6f",
        "size": 11344,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2ebf6541c082fade03ab312da58c05f078f60c6f"
    },
    {
        "path": "P16_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e72060c19783792863dc0f2e34ad41a26f39f3b0",
        "size": 6765,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e72060c19783792863dc0f2e34ad41a26f39f3b0"
    },
    {
        "path": "P16_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c284bfd08f7c588338707f6c058f150b204a9779",
        "size": 9257,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c284bfd08f7c588338707f6c058f150b204a9779"
    },
    {
        "path": "P16_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b423ffffefb0c90b96eee10f33c5f9dc153fb072",
        "size": 10319,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b423ffffefb0c90b96eee10f33c5f9dc153fb072"
    },
    {
        "path": "P16_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c9e30d88f40c4d3150cfd297f759376c728242b8",
        "size": 9695,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c9e30d88f40c4d3150cfd297f759376c728242b8"
    },
    {
        "path": "P16_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f8e7c4cf51836cba703f9f80b7b0f6404e142e6a",
        "size": 9680,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f8e7c4cf51836cba703f9f80b7b0f6404e142e6a"
    },
    {
        "path": "P16_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "733607b84bf0a70c426341ad7b42db5d8dd722c2",
        "size": 8715,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/733607b84bf0a70c426341ad7b42db5d8dd722c2"
    },
    {
        "path": "P16_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "82cd32dddcdb6797c8c565a6ef81d965a54c4d74",
        "size": 12511,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/82cd32dddcdb6797c8c565a6ef81d965a54c4d74"
    },
    {
        "path": "P16_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "63fe9c6de37ba650cebcdfcc309f3d661ecd20c8",
        "size": 12769,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/63fe9c6de37ba650cebcdfcc309f3d661ecd20c8"
    },
    {
        "path": "P16_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "97b45dadc02d4e28d90e460caa26c1f7dcdd3577",
        "size": 11411,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/97b45dadc02d4e28d90e460caa26c1f7dcdd3577"
    },
    {
        "path": "P16_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6733b9491099524b4253467297c0762ef5456a08",
        "size": 9848,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6733b9491099524b4253467297c0762ef5456a08"
    },
    {
        "path": "P16_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "491684cb3429cf99cf0f34f3d917878e5b7ee611",
        "size": 8732,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/491684cb3429cf99cf0f34f3d917878e5b7ee611"
    },
    {
        "path": "P16_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "97428b768050f940818327e8e97885811dc7d8aa",
        "size": 7839,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/97428b768050f940818327e8e97885811dc7d8aa"
    },
    {
        "path": "P16_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d80e8242d0559bd01bbffef3b9e79c1468102412",
        "size": 12136,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d80e8242d0559bd01bbffef3b9e79c1468102412"
    },
    {
        "path": "P16_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e7f812f81e1531a0ec5b861fa87832bd1e2787aa",
        "size": 8053,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e7f812f81e1531a0ec5b861fa87832bd1e2787aa"
    },
    {
        "path": "P16_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "94bfab8a7eae97b7aae0ea19c3c2df089b4be193",
        "size": 5734,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/94bfab8a7eae97b7aae0ea19c3c2df089b4be193"
    },
    {
        "path": "P16_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7ac9b67ad5180450709544069e79c9ba92c66149",
        "size": 9198,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7ac9b67ad5180450709544069e79c9ba92c66149"
    },
    {
        "path": "P16_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e2fb397dfa65d03d484db178bfa7b37cb711969d",
        "size": 8520,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e2fb397dfa65d03d484db178bfa7b37cb711969d"
    },
    {
        "path": "P16_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f2c04e4980369f533eccc6b7b9129c10f01b2de7",
        "size": 12373,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f2c04e4980369f533eccc6b7b9129c10f01b2de7"
    },
    {
        "path": "P16_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "58133726442628ccf2ee691981d839e9e46ecfd5",
        "size": 7425,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/58133726442628ccf2ee691981d839e9e46ecfd5"
    },
    {
        "path": "P16_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3fc3a4b41f68d774c5078f3a8bb65682468caea3",
        "size": 9998,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3fc3a4b41f68d774c5078f3a8bb65682468caea3"
    },
    {
        "path": "P16_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "265d824546d8062b36fa7b03569482efd50c4f0e",
        "size": 5498,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/265d824546d8062b36fa7b03569482efd50c4f0e"
    },
    {
        "path": "P16_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "44555c148c43f3b0e7083dfbe46a98e1961fb164",
        "size": 13941,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/44555c148c43f3b0e7083dfbe46a98e1961fb164"
    },
    {
        "path": "P16_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0facc69caaef6aa85851d5599b5c641cee2ed39c",
        "size": 21599,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0facc69caaef6aa85851d5599b5c641cee2ed39c"
    },
    {
        "path": "P18_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0e29176f557725177661d5d4b023d111568d7487",
        "size": 4916,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0e29176f557725177661d5d4b023d111568d7487"
    },
    {
        "path": "P18_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f20682d2b0a8807a0a63fd359465e4563b488d92",
        "size": 2220,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f20682d2b0a8807a0a63fd359465e4563b488d92"
    },
    {
        "path": "P18_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "69f8d64c6b19e9fdfc890347c072bc96e11016b7",
        "size": 1817,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/69f8d64c6b19e9fdfc890347c072bc96e11016b7"
    },
    {
        "path": "P18_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3845ecc4773c83e35ccfd81f13f61512258635e3",
        "size": 2849,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3845ecc4773c83e35ccfd81f13f61512258635e3"
    },
    {
        "path": "P18_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "30dd6c2c91addfb3ef772b997f8aa43889a5c9ac",
        "size": 1888,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/30dd6c2c91addfb3ef772b997f8aa43889a5c9ac"
    },
    {
        "path": "P18_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "81c22d5499c7e4973085664eb4c5e936c875cad4",
        "size": 2161,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/81c22d5499c7e4973085664eb4c5e936c875cad4"
    },
    {
        "path": "P18_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bf424d03b18737b1e23460784824cff8d7a4ddc0",
        "size": 3390,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bf424d03b18737b1e23460784824cff8d7a4ddc0"
    },
    {
        "path": "P18_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2bc6776567171106adade453cb2d3a5947285473",
        "size": 1338,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2bc6776567171106adade453cb2d3a5947285473"
    },
    {
        "path": "P18_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1912d32d9e32b79a9ddc962642883cda39a2a333",
        "size": 4976,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1912d32d9e32b79a9ddc962642883cda39a2a333"
    },
    {
        "path": "P18_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b130e8126651d38035b986b3024901a92176a013",
        "size": 4629,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b130e8126651d38035b986b3024901a92176a013"
    },
    {
        "path": "P18_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8ffaf6b09619533c2a07cf29d96b742fdb46a96a",
        "size": 2162,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8ffaf6b09619533c2a07cf29d96b742fdb46a96a"
    },
    {
        "path": "P18_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "657f1af93d66ebe4af6ab169f4bb5755a91d6adb",
        "size": 2430,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/657f1af93d66ebe4af6ab169f4bb5755a91d6adb"
    },
    {
        "path": "P18_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c27b92e0cea0df6e99075ac9693212e3323f986f",
        "size": 2434,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c27b92e0cea0df6e99075ac9693212e3323f986f"
    },
    {
        "path": "P18_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "12ea2373ef7e05aa2e6ebc0bbf3dc3670dbe8636",
        "size": 3327,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/12ea2373ef7e05aa2e6ebc0bbf3dc3670dbe8636"
    },
    {
        "path": "P18_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "938c38cb2d91ea9dfa4cb20b720fb89315827686",
        "size": 2850,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/938c38cb2d91ea9dfa4cb20b720fb89315827686"
    },
    {
        "path": "P18_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a0b03f8d705a8fb2ce7c3a526329d2b3c0c1d0dc",
        "size": 1136,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a0b03f8d705a8fb2ce7c3a526329d2b3c0c1d0dc"
    },
    {
        "path": "P18_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1fd8a40bf1f919b12d132dfd8e88e3117b8dca3d",
        "size": 2301,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1fd8a40bf1f919b12d132dfd8e88e3117b8dca3d"
    },
    {
        "path": "P18_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "db659c7f7a67e3a596508a2a18977624d8266211",
        "size": 2981,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/db659c7f7a67e3a596508a2a18977624d8266211"
    },
    {
        "path": "P18_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "56d7c65e74eb09cce1c0942c2dc5014c36d3a705",
        "size": 2646,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/56d7c65e74eb09cce1c0942c2dc5014c36d3a705"
    },
    {
        "path": "P18_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8401f1bc73156e47c97bdcc3d72e19fd231d93fe",
        "size": 1884,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8401f1bc73156e47c97bdcc3d72e19fd231d93fe"
    },
    {
        "path": "P18_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "de572818312d656789c14be25978582e3dc1b570",
        "size": 1270,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/de572818312d656789c14be25978582e3dc1b570"
    },
    {
        "path": "P18_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5e19a5d9fafac8fbc8d94e3d57aca0755384375b",
        "size": 4498,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5e19a5d9fafac8fbc8d94e3d57aca0755384375b"
    },
    {
        "path": "P18_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "596ae2e00f13786626e19c16a7161a6b20fddc64",
        "size": 2157,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/596ae2e00f13786626e19c16a7161a6b20fddc64"
    },
    {
        "path": "P18_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "449442ae60a81cfcd1fa3757ff97296f27806223",
        "size": 2157,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/449442ae60a81cfcd1fa3757ff97296f27806223"
    },
    {
        "path": "P18_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "da436dea837cf39a1739ea527097b1cdcab62063",
        "size": 2440,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/da436dea837cf39a1739ea527097b1cdcab62063"
    },
    {
        "path": "P18_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "82b0a38189419d261f4f2d74056601a6dd94d6c9",
        "size": 1674,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/82b0a38189419d261f4f2d74056601a6dd94d6c9"
    },
    {
        "path": "P18_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ecaf20c9eba1ff44f25fbc47b548f297ed54d297",
        "size": 4221,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ecaf20c9eba1ff44f25fbc47b548f297ed54d297"
    },
    {
        "path": "P18_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c8fb780a0342802d9295f8148346ff7df7d83794",
        "size": 1338,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c8fb780a0342802d9295f8148346ff7df7d83794"
    },
    {
        "path": "P18_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ed81ca3256e272c15d6cd66ea7ec2941e1887312",
        "size": 2366,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ed81ca3256e272c15d6cd66ea7ec2941e1887312"
    },
    {
        "path": "P18_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0cee0b99721b2f7e77dc47b663d9bc7bb493798f",
        "size": 2771,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0cee0b99721b2f7e77dc47b663d9bc7bb493798f"
    },
    {
        "path": "P18_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "72664e3b5a1ddb9e545cb1edcc299341d5ee5b27",
        "size": 2910,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/72664e3b5a1ddb9e545cb1edcc299341d5ee5b27"
    },
    {
        "path": "P18_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f73dc29aa7fb1c687d6f0c5df18feda28d523436",
        "size": 1471,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f73dc29aa7fb1c687d6f0c5df18feda28d523436"
    },
    {
        "path": "P18_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f13403b89e838be75dbbfba7191b17f2d09762b6",
        "size": 2769,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f13403b89e838be75dbbfba7191b17f2d09762b6"
    },
    {
        "path": "P18_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "150d816a9ed687e82e88da0b06c6de0c1d2859ed",
        "size": 1948,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/150d816a9ed687e82e88da0b06c6de0c1d2859ed"
    },
    {
        "path": "P18_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "91314401b4ea3405e2a8a82ca95edd82ad216fda",
        "size": 6870,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/91314401b4ea3405e2a8a82ca95edd82ad216fda"
    },
    {
        "path": "P18_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "819f03dc22a52b5940f7d8c46509b5891e986387",
        "size": 5384,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/819f03dc22a52b5940f7d8c46509b5891e986387"
    },
    {
        "path": "P18_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f769ac7c8965a7e33ceb121d43d6b2cbd7508d28",
        "size": 726,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f769ac7c8965a7e33ceb121d43d6b2cbd7508d28"
    },
    {
        "path": "P18_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "273cdf82f2e8d0748c47bc16ebbe189106fbb496",
        "size": 1396,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/273cdf82f2e8d0748c47bc16ebbe189106fbb496"
    },
    {
        "path": "P18_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9d1c519a2a2bc5d9c07fe1da68c1e77318ca7055",
        "size": 13293,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9d1c519a2a2bc5d9c07fe1da68c1e77318ca7055"
    },
    {
        "path": "P18_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bc97485dc7b05bd2ff804a9b10eef283d178835b",
        "size": 1470,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bc97485dc7b05bd2ff804a9b10eef283d178835b"
    },
    {
        "path": "P18_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "76e71ada495ca4c750a9739e705467189696d993",
        "size": 1814,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/76e71ada495ca4c750a9739e705467189696d993"
    },
    {
        "path": "P18_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b85f1a88af456b42195225f2e07f6e7e1ad16950",
        "size": 7581,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b85f1a88af456b42195225f2e07f6e7e1ad16950"
    },
    {
        "path": "P18_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ce88e56c29b924b9edca207ad8b7aa0e722d7b39",
        "size": 5239,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ce88e56c29b924b9edca207ad8b7aa0e722d7b39"
    },
    {
        "path": "P18_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f7a167bc5c66cc7666334246b8e7710a31e4dbcf",
        "size": 1817,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f7a167bc5c66cc7666334246b8e7710a31e4dbcf"
    },
    {
        "path": "P18_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5af1599568b69eaf853b90b1d67086a7f9235291",
        "size": 2018,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5af1599568b69eaf853b90b1d67086a7f9235291"
    },
    {
        "path": "P18_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "866d39efe1129df56100f33e083013453d724fb6",
        "size": 2159,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/866d39efe1129df56100f33e083013453d724fb6"
    },
    {
        "path": "P18_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bfffef9c88b15b6577665cd20c94f9661897e1b0",
        "size": 2084,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bfffef9c88b15b6577665cd20c94f9661897e1b0"
    },
    {
        "path": "P18_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "81c7b71905e104c766ad697809938183fe84d201",
        "size": 2286,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/81c7b71905e104c766ad697809938183fe84d201"
    },
    {
        "path": "P18_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "81649d1d2bcf5dc9e64679957736406283cb9532",
        "size": 3540,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/81649d1d2bcf5dc9e64679957736406283cb9532"
    },
    {
        "path": "P18_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "19ffa3581c05e918e81c95f6dd740a9aad6b81c0",
        "size": 1406,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/19ffa3581c05e918e81c95f6dd740a9aad6b81c0"
    },
    {
        "path": "P18_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ff01742b2a3c971ca06149abcc20233745c1db47",
        "size": 1338,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ff01742b2a3c971ca06149abcc20233745c1db47"
    },
    {
        "path": "P18_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a0c8c87b4969fc629b9ca6f959830d48f0b150c5",
        "size": 3660,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a0c8c87b4969fc629b9ca6f959830d48f0b150c5"
    },
    {
        "path": "P18_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "376820b9229bfb2f16181cac43e922ee54b93e0d",
        "size": 1340,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/376820b9229bfb2f16181cac43e922ee54b93e0d"
    },
    {
        "path": "P18_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "72965cdc97acbcd082dca0a8619a753f3b3a7745",
        "size": 6076,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/72965cdc97acbcd082dca0a8619a753f3b3a7745"
    },
    {
        "path": "P18_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "07737f4ab681c3af496cfde7ec2b06a461545f15",
        "size": 1403,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/07737f4ab681c3af496cfde7ec2b06a461545f15"
    },
    {
        "path": "P18_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "02ff8e0c39fbd3a54159c78f262854c39bd77ae2",
        "size": 1951,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/02ff8e0c39fbd3a54159c78f262854c39bd77ae2"
    },
    {
        "path": "P18_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "81f8a7988a9f1add3cd16ce337c9e044c57d4367",
        "size": 1330,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/81f8a7988a9f1add3cd16ce337c9e044c57d4367"
    },
    {
        "path": "P18_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "91cc1e7581f5649c9daf12c6b060e14be0b90d5b",
        "size": 2781,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/91cc1e7581f5649c9daf12c6b060e14be0b90d5b"
    },
    {
        "path": "P18_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9734c86985c9b7837ae0a2cc1f62691fb8c887e8",
        "size": 14113,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9734c86985c9b7837ae0a2cc1f62691fb8c887e8"
    },
    {
        "path": "P19_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6744b0e3175c432910ee5184279857abc5a10c4a",
        "size": 17351,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6744b0e3175c432910ee5184279857abc5a10c4a"
    },
    {
        "path": "P19_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5b75819c2593c057d0ce82d1a6fac57d6c606233",
        "size": 14012,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5b75819c2593c057d0ce82d1a6fac57d6c606233"
    },
    {
        "path": "P19_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "45e98316122350e364975cb24a540ede43d4b358",
        "size": 12524,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/45e98316122350e364975cb24a540ede43d4b358"
    },
    {
        "path": "P19_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b18a83d129c82bed820d90dbb38113be55287b19",
        "size": 30347,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b18a83d129c82bed820d90dbb38113be55287b19"
    },
    {
        "path": "P19_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "145467bb8473c518028ef933b617ce3183261894",
        "size": 12340,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/145467bb8473c518028ef933b617ce3183261894"
    },
    {
        "path": "P19_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "041750cf9adfeca5092839a26f7fb7ee4d94c8dd",
        "size": 14534,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/041750cf9adfeca5092839a26f7fb7ee4d94c8dd"
    },
    {
        "path": "P19_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3e3b82dac53cef6e654fb5f9cfaea5fb8bbc2082",
        "size": 12503,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3e3b82dac53cef6e654fb5f9cfaea5fb8bbc2082"
    },
    {
        "path": "P19_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7482d9b6affe08cf445778a0fdb5a33c76fdb1a1",
        "size": 17933,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7482d9b6affe08cf445778a0fdb5a33c76fdb1a1"
    },
    {
        "path": "P19_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "54b3ac35bc2a2b68b2e1ad34ae70c44c23a3b89c",
        "size": 22024,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/54b3ac35bc2a2b68b2e1ad34ae70c44c23a3b89c"
    },
    {
        "path": "P19_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d2f7a3ee6466ebf6746b73c8957207b0b361891e",
        "size": 17360,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d2f7a3ee6466ebf6746b73c8957207b0b361891e"
    },
    {
        "path": "P19_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e2f75e9b5f4bb3cbd872fac47a8ef5da83afff1b",
        "size": 10682,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e2f75e9b5f4bb3cbd872fac47a8ef5da83afff1b"
    },
    {
        "path": "P19_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7cbb435af39e06a028fe5270cc6502126238f2e6",
        "size": 17127,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7cbb435af39e06a028fe5270cc6502126238f2e6"
    },
    {
        "path": "P19_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8fe51c89f4fdf0d9edf0a6769f2a926d12ec6672",
        "size": 15347,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8fe51c89f4fdf0d9edf0a6769f2a926d12ec6672"
    },
    {
        "path": "P19_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a8a59454b7c01c563b3b79249d81217358a4d999",
        "size": 19519,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a8a59454b7c01c563b3b79249d81217358a4d999"
    },
    {
        "path": "P19_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cf4179e8ee3797b5ea8e486656588dca29b12f01",
        "size": 13509,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cf4179e8ee3797b5ea8e486656588dca29b12f01"
    },
    {
        "path": "P19_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5be22bd96e86a41e2229ac3478be16e9c4ab013e",
        "size": 19441,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5be22bd96e86a41e2229ac3478be16e9c4ab013e"
    },
    {
        "path": "P19_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ab8670b659f9782b353e11bd9a43eb834c25b215",
        "size": 10347,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ab8670b659f9782b353e11bd9a43eb834c25b215"
    },
    {
        "path": "P19_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ffe7c9cced5bcc7b746b3652c6bbf4bfa4cba4ab",
        "size": 15418,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ffe7c9cced5bcc7b746b3652c6bbf4bfa4cba4ab"
    },
    {
        "path": "P19_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "17bc2470d036ac1eed8cde99d6c35c26131a9630",
        "size": 25565,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/17bc2470d036ac1eed8cde99d6c35c26131a9630"
    },
    {
        "path": "P19_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "645d61c0e5b85fa0f39b609bdb240ee0e360ae7f",
        "size": 22582,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/645d61c0e5b85fa0f39b609bdb240ee0e360ae7f"
    },
    {
        "path": "P19_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a13e1844c325a8d45886245c69097edef2942d5b",
        "size": 13813,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a13e1844c325a8d45886245c69097edef2942d5b"
    },
    {
        "path": "P19_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b7f83d7d26bf0acca33413bc08f89712bfc59ece",
        "size": 7198,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b7f83d7d26bf0acca33413bc08f89712bfc59ece"
    },
    {
        "path": "P19_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b5b1d917da945acc6940c73cd59d49ea2ebeb983",
        "size": 21614,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b5b1d917da945acc6940c73cd59d49ea2ebeb983"
    },
    {
        "path": "P19_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "39e592937df79769783ddf541571f064d9a35b07",
        "size": 19621,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/39e592937df79769783ddf541571f064d9a35b07"
    },
    {
        "path": "P19_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b3855f384b0c49da309b66baa8592ab6481d254f",
        "size": 13191,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b3855f384b0c49da309b66baa8592ab6481d254f"
    },
    {
        "path": "P19_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b51a3858236ef22b38249f67cb383f55923c2925",
        "size": 13197,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b51a3858236ef22b38249f67cb383f55923c2925"
    },
    {
        "path": "P19_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2ed051d5207dfe7e82075542ff853e7b531fd3ef",
        "size": 12823,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2ed051d5207dfe7e82075542ff853e7b531fd3ef"
    },
    {
        "path": "P19_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8c0753e1200754c05c2a153bcbd7318894714d31",
        "size": 15719,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8c0753e1200754c05c2a153bcbd7318894714d31"
    },
    {
        "path": "P19_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "716204a0e55a23e861476c30b4488e4a192347c3",
        "size": 12397,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/716204a0e55a23e861476c30b4488e4a192347c3"
    },
    {
        "path": "P19_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1315db7a5fd4da93c1fc21dac73821711d143b78",
        "size": 20140,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1315db7a5fd4da93c1fc21dac73821711d143b78"
    },
    {
        "path": "P19_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8c769ef20b001ba6b2ebb9ccdcb184963592208f",
        "size": 10702,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8c769ef20b001ba6b2ebb9ccdcb184963592208f"
    },
    {
        "path": "P19_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cc97ba7908991d1d0cac93315f410a5e8fc755ab",
        "size": 13066,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cc97ba7908991d1d0cac93315f410a5e8fc755ab"
    },
    {
        "path": "P19_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1705517e7fd912f8808b25fc1fbb0d49f02ae051",
        "size": 12021,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1705517e7fd912f8808b25fc1fbb0d49f02ae051"
    },
    {
        "path": "P19_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "192f9918a8577e7a7128a5f2a5229a96109e3968",
        "size": 12644,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/192f9918a8577e7a7128a5f2a5229a96109e3968"
    },
    {
        "path": "P19_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4ff268078fc9a935907d7946d9743a360c7c8207",
        "size": 7819,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4ff268078fc9a935907d7946d9743a360c7c8207"
    },
    {
        "path": "P19_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "81765550b92f5c824057b9693b0cbb0a1091f16d",
        "size": 12636,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/81765550b92f5c824057b9693b0cbb0a1091f16d"
    },
    {
        "path": "P19_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d643df1a3b7590ede83e857f8b03d4b7c77e9a76",
        "size": 19953,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d643df1a3b7590ede83e857f8b03d4b7c77e9a76"
    },
    {
        "path": "P19_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ff270a5b4e1e4967949f130d3d62f886c8c45024",
        "size": 10457,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ff270a5b4e1e4967949f130d3d62f886c8c45024"
    },
    {
        "path": "P19_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a1a846c0ccc37848c416eaa36d06b26eb117855b",
        "size": 11053,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a1a846c0ccc37848c416eaa36d06b26eb117855b"
    },
    {
        "path": "P19_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9359b57deb9711016c9bc8762c0ebbfffc6a6ce4",
        "size": 20365,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9359b57deb9711016c9bc8762c0ebbfffc6a6ce4"
    },
    {
        "path": "P19_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c5499a0f6456b436b10fb31c4d2234619d42c3f8",
        "size": 19019,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c5499a0f6456b436b10fb31c4d2234619d42c3f8"
    },
    {
        "path": "P19_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "58e4d3a44fb0c6f954e001e051c0d680d87e17db",
        "size": 18871,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/58e4d3a44fb0c6f954e001e051c0d680d87e17db"
    },
    {
        "path": "P19_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d1f6bde67bb28971e41a9ae57d85b16778c62ae0",
        "size": 18869,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d1f6bde67bb28971e41a9ae57d85b16778c62ae0"
    },
    {
        "path": "P19_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "88d4fa000d32dab3ea3a9dce957fcf730edb3bb6",
        "size": 19685,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/88d4fa000d32dab3ea3a9dce957fcf730edb3bb6"
    },
    {
        "path": "P19_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f9f175ee87a52bbb4877094b98e3badbc782334a",
        "size": 10807,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f9f175ee87a52bbb4877094b98e3badbc782334a"
    },
    {
        "path": "P19_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b83d5079e9156b75b0f574d2f124a8f439b66349",
        "size": 12831,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b83d5079e9156b75b0f574d2f124a8f439b66349"
    },
    {
        "path": "P19_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1008339c2acb32b2c59be17fb1e9e0f6b7982ab1",
        "size": 18887,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1008339c2acb32b2c59be17fb1e9e0f6b7982ab1"
    },
    {
        "path": "P19_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8de385257690879795836a9c378af2ac3dd09e3d",
        "size": 14394,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8de385257690879795836a9c378af2ac3dd09e3d"
    },
    {
        "path": "P19_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9d63898e68d393968d00a276bb3060547603222a",
        "size": 9593,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9d63898e68d393968d00a276bb3060547603222a"
    },
    {
        "path": "P19_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f84bafce92f070b4cf4ce8799afbe33a41c850b9",
        "size": 17826,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f84bafce92f070b4cf4ce8799afbe33a41c850b9"
    },
    {
        "path": "P19_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0a4776f5ca979ad193eb002c25de91929262ae16",
        "size": 19878,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0a4776f5ca979ad193eb002c25de91929262ae16"
    },
    {
        "path": "P19_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6b377e02f07dd1065f2a571687b8e885aaba3433",
        "size": 7984,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6b377e02f07dd1065f2a571687b8e885aaba3433"
    },
    {
        "path": "P19_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f2a21096dba8aa6313d8f6a5d3d0b5c878045702",
        "size": 13477,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f2a21096dba8aa6313d8f6a5d3d0b5c878045702"
    },
    {
        "path": "P19_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d09c75b0173aab0973d3d445ff485cb68dc6551f",
        "size": 13274,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d09c75b0173aab0973d3d445ff485cb68dc6551f"
    },
    {
        "path": "P19_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3fe403c52689900d05b60fb10305160bc3036a7d",
        "size": 28798,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3fe403c52689900d05b60fb10305160bc3036a7d"
    },
    {
        "path": "P19_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a99cf49b975a8cd82b565ba91b22ed6538a7c938",
        "size": 17232,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a99cf49b975a8cd82b565ba91b22ed6538a7c938"
    },
    {
        "path": "P19_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4258d504a726a30e360746aebbd8d6e4edd92879",
        "size": 17608,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4258d504a726a30e360746aebbd8d6e4edd92879"
    },
    {
        "path": "P19_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2123e5d3d8629b989a1ea40cb635347637072fb8",
        "size": 7943,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2123e5d3d8629b989a1ea40cb635347637072fb8"
    },
    {
        "path": "P19_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4d12680e055559b2e912ea85d5002a36ad7959f9",
        "size": 21513,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4d12680e055559b2e912ea85d5002a36ad7959f9"
    },
    {
        "path": "P19_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "104e4a5b79fa64290aa9cf94daf16fe1575df7ea",
        "size": 22425,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/104e4a5b79fa64290aa9cf94daf16fe1575df7ea"
    },
    {
        "path": "P20_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ad0ac72f04ecf1cbf45983fbf30eaae36a2e5cd8",
        "size": 7687,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ad0ac72f04ecf1cbf45983fbf30eaae36a2e5cd8"
    },
    {
        "path": "P20_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "af7db043d5f98d7d59840425b7384ceca06dcb32",
        "size": 6361,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/af7db043d5f98d7d59840425b7384ceca06dcb32"
    },
    {
        "path": "P20_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8082b64a74cc0ced89434d0fa6672917e3372835",
        "size": 12289,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8082b64a74cc0ced89434d0fa6672917e3372835"
    },
    {
        "path": "P20_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d52b69f488136075dfbb50c94204a64955bdd53f",
        "size": 11939,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d52b69f488136075dfbb50c94204a64955bdd53f"
    },
    {
        "path": "P20_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cdda7926ee0c07c96c8d385e27f1230173c650a9",
        "size": 10406,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cdda7926ee0c07c96c8d385e27f1230173c650a9"
    },
    {
        "path": "P20_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e2aa831171b3ba3187bba52ae29f86ab8d2477ea",
        "size": 10479,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e2aa831171b3ba3187bba52ae29f86ab8d2477ea"
    },
    {
        "path": "P20_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "509149de038351ed3f346f16eb4db8c0fc622dd6",
        "size": 5920,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/509149de038351ed3f346f16eb4db8c0fc622dd6"
    },
    {
        "path": "P20_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d4111367506db1d3d901dfec812dd07a69e5e0b2",
        "size": 17830,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d4111367506db1d3d901dfec812dd07a69e5e0b2"
    },
    {
        "path": "P20_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "da7585232ca5d0431c99544ea4849ee24cb0cb58",
        "size": 8138,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/da7585232ca5d0431c99544ea4849ee24cb0cb58"
    },
    {
        "path": "P20_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bdec81af863adbb4091bbe168decd44a71606656",
        "size": 7980,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bdec81af863adbb4091bbe168decd44a71606656"
    },
    {
        "path": "P20_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "74dc79718391ffc5c138fc038f546490246dd6f7",
        "size": 4085,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/74dc79718391ffc5c138fc038f546490246dd6f7"
    },
    {
        "path": "P20_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a383d278826fef0763a971e15516d4ee5e2ac9ed",
        "size": 9021,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a383d278826fef0763a971e15516d4ee5e2ac9ed"
    },
    {
        "path": "P20_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e3b50ce2ab84a483e6ce6e87eb3563e07c779cb8",
        "size": 10406,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e3b50ce2ab84a483e6ce6e87eb3563e07c779cb8"
    },
    {
        "path": "P20_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "13bd733d28929fc426e184ca1775e7a055b26d8e",
        "size": 7503,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/13bd733d28929fc426e184ca1775e7a055b26d8e"
    },
    {
        "path": "P20_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "097efc6a8e4eb96886c1903c8596e0a184c0ed86",
        "size": 10190,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/097efc6a8e4eb96886c1903c8596e0a184c0ed86"
    },
    {
        "path": "P20_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b6c1168dc7ddd307bb11863dd3ace887392f56b8",
        "size": 12322,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b6c1168dc7ddd307bb11863dd3ace887392f56b8"
    },
    {
        "path": "P20_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c5f57378354feda345b230986cefe930afe944b9",
        "size": 7612,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c5f57378354feda345b230986cefe930afe944b9"
    },
    {
        "path": "P20_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "93131134da7b8e51cccee9fe607384fda370db8a",
        "size": 10739,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/93131134da7b8e51cccee9fe607384fda370db8a"
    },
    {
        "path": "P20_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "850d386578b0e66b8beb8e535395113ef794374f",
        "size": 7661,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/850d386578b0e66b8beb8e535395113ef794374f"
    },
    {
        "path": "P20_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f63b4237e8724a13c508b2537b72587c7afaaa79",
        "size": 7643,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f63b4237e8724a13c508b2537b72587c7afaaa79"
    },
    {
        "path": "P20_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3e224aaf6601e7772a59ed81d68b2faf85cc1feb",
        "size": 6828,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3e224aaf6601e7772a59ed81d68b2faf85cc1feb"
    },
    {
        "path": "P20_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6e720ea8e6eb4646068eac2c4d84cbefea11ed97",
        "size": 3463,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6e720ea8e6eb4646068eac2c4d84cbefea11ed97"
    },
    {
        "path": "P20_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "408b0ae00a85789b3a8219bf4c4e6b34af8703ea",
        "size": 10811,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/408b0ae00a85789b3a8219bf4c4e6b34af8703ea"
    },
    {
        "path": "P20_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ba838ed4ae718bc8bcf816f87a380c7bcd59d32d",
        "size": 10509,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ba838ed4ae718bc8bcf816f87a380c7bcd59d32d"
    },
    {
        "path": "P20_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3f4cd3ca5807e46f98749bb51f276fe38b6fabd5",
        "size": 6560,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3f4cd3ca5807e46f98749bb51f276fe38b6fabd5"
    },
    {
        "path": "P20_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "29d672d5ab514b0df67770aafa999e54c873059a",
        "size": 13742,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/29d672d5ab514b0df67770aafa999e54c873059a"
    },
    {
        "path": "P20_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "220e7ccf63ba22a7d6a3a5f29ff0cbb5570e9f12",
        "size": 7511,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/220e7ccf63ba22a7d6a3a5f29ff0cbb5570e9f12"
    },
    {
        "path": "P20_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "06196d50e83acb6e74319ceeff2144ba7416f15e",
        "size": 12924,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/06196d50e83acb6e74319ceeff2144ba7416f15e"
    },
    {
        "path": "P20_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a567770c32965698c5ae3cadc82c79008cd06cbb",
        "size": 11490,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a567770c32965698c5ae3cadc82c79008cd06cbb"
    },
    {
        "path": "P20_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cfe54dc970c78e80c5c53a90668223b9b7b6c6cd",
        "size": 13313,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cfe54dc970c78e80c5c53a90668223b9b7b6c6cd"
    },
    {
        "path": "P20_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7818994f659463b2f124146368e378e39a13a637",
        "size": 8071,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7818994f659463b2f124146368e378e39a13a637"
    },
    {
        "path": "P20_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1f95703594cdca22e05bb1329ae334fccfa1e198",
        "size": 9835,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1f95703594cdca22e05bb1329ae334fccfa1e198"
    },
    {
        "path": "P20_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e3b0e759f1f7f1ac887b57dd6fa5228044ef0c67",
        "size": 9506,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e3b0e759f1f7f1ac887b57dd6fa5228044ef0c67"
    },
    {
        "path": "P20_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "925bcbead0340de8daf329e18a42078386209b78",
        "size": 4063,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/925bcbead0340de8daf329e18a42078386209b78"
    },
    {
        "path": "P20_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b9acf8b65d752cf5734fc8f3fa57d320804bcae0",
        "size": 5666,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b9acf8b65d752cf5734fc8f3fa57d320804bcae0"
    },
    {
        "path": "P20_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9122f2e5d067b307b12f0a55c4a33154f89de6fd",
        "size": 4559,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9122f2e5d067b307b12f0a55c4a33154f89de6fd"
    },
    {
        "path": "P20_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e0e4d0bfc3c09faf604d70b0de88359440dd0e64",
        "size": 6933,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e0e4d0bfc3c09faf604d70b0de88359440dd0e64"
    },
    {
        "path": "P20_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "446a64e5191df4654717f66fb1272451aa24d49f",
        "size": 8171,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/446a64e5191df4654717f66fb1272451aa24d49f"
    },
    {
        "path": "P20_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ab3d4cd6aa63172d6794e435d81179539a39c0b4",
        "size": 9609,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ab3d4cd6aa63172d6794e435d81179539a39c0b4"
    },
    {
        "path": "P20_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0412d558968e8b66008fe1927c1cd58ab4717584",
        "size": 7503,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0412d558968e8b66008fe1927c1cd58ab4717584"
    },
    {
        "path": "P20_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b983f20d0db71281ab560b2944dbb86e96809005",
        "size": 9974,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b983f20d0db71281ab560b2944dbb86e96809005"
    },
    {
        "path": "P20_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1d00b8b42bec15489173594693b009dadc8c67f6",
        "size": 6829,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1d00b8b42bec15489173594693b009dadc8c67f6"
    },
    {
        "path": "P20_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d2c2f7bd0bd8144ba80cb0726b5e111c1b5199c3",
        "size": 8789,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d2c2f7bd0bd8144ba80cb0726b5e111c1b5199c3"
    },
    {
        "path": "P20_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "90038d7fdec4ad8595c22e2de58519a612612020",
        "size": 14786,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/90038d7fdec4ad8595c22e2de58519a612612020"
    },
    {
        "path": "P20_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bfd6db90165dcf03a2798880192656af7a49fd6c",
        "size": 6065,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bfd6db90165dcf03a2798880192656af7a49fd6c"
    },
    {
        "path": "P20_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0fded5cd51a21c6b59dcdb03a62e2c4a44ed64f9",
        "size": 17537,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0fded5cd51a21c6b59dcdb03a62e2c4a44ed64f9"
    },
    {
        "path": "P20_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ef7e09cbc809898449eeb1fc0d62c0ca4898fccc",
        "size": 12991,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ef7e09cbc809898449eeb1fc0d62c0ca4898fccc"
    },
    {
        "path": "P20_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fa78f04ddd4ca404bd7c45ef94711bc98d96610e",
        "size": 8678,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fa78f04ddd4ca404bd7c45ef94711bc98d96610e"
    },
    {
        "path": "P20_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "45048090ae31a28f7fed7bb8bed83aa0a6f1498a",
        "size": 9133,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/45048090ae31a28f7fed7bb8bed83aa0a6f1498a"
    },
    {
        "path": "P20_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3374501af9ac57362bd685b65852cc37bdba39a8",
        "size": 5239,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3374501af9ac57362bd685b65852cc37bdba39a8"
    },
    {
        "path": "P20_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "934419b74e3988935d5ab06c5d87b5ff27640005",
        "size": 7612,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/934419b74e3988935d5ab06c5d87b5ff27640005"
    },
    {
        "path": "P20_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6f8e8bbeb876751206cb49cc3379686175f967b2",
        "size": 4233,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6f8e8bbeb876751206cb49cc3379686175f967b2"
    },
    {
        "path": "P20_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d444dd19b3e5f5b4fc1f21c0571aaaa89ddf8199",
        "size": 9267,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d444dd19b3e5f5b4fc1f21c0571aaaa89ddf8199"
    },
    {
        "path": "P20_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4f114f0830cb2e77e50241aceac197c70a691abe",
        "size": 10129,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4f114f0830cb2e77e50241aceac197c70a691abe"
    },
    {
        "path": "P20_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c1da11d3e95d7dd6fd63a462756bbffb19ba9c83",
        "size": 14618,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c1da11d3e95d7dd6fd63a462756bbffb19ba9c83"
    },
    {
        "path": "P20_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9ca20ba8058beaa3b1db68f671d9c663daf077dc",
        "size": 6473,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9ca20ba8058beaa3b1db68f671d9c663daf077dc"
    },
    {
        "path": "P20_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b760f536a13ddc5065915b789b670c83fa09f7b0",
        "size": 9774,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b760f536a13ddc5065915b789b670c83fa09f7b0"
    },
    {
        "path": "P20_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b72170cc9ca7635f1a26f94feff6b661505b4d69",
        "size": 4897,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b72170cc9ca7635f1a26f94feff6b661505b4d69"
    },
    {
        "path": "P20_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5f7ac5c4d12eab477382464aa293ee8f63709616",
        "size": 13615,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5f7ac5c4d12eab477382464aa293ee8f63709616"
    },
    {
        "path": "P20_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e496b1cb493f160cf9ac73240bb728bdbc76797f",
        "size": 15012,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e496b1cb493f160cf9ac73240bb728bdbc76797f"
    },
    {
        "path": "P21_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ee8973b61b66e9fbb436797517915f3e7b6cc304",
        "size": 7702,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ee8973b61b66e9fbb436797517915f3e7b6cc304"
    },
    {
        "path": "P21_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "79b340a8d09ab8a7cfbf398bec19573d65f4cc28",
        "size": 7975,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/79b340a8d09ab8a7cfbf398bec19573d65f4cc28"
    },
    {
        "path": "P21_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1dd392c8d21036c1a99a8aa5bfd44890efedc597",
        "size": 9286,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1dd392c8d21036c1a99a8aa5bfd44890efedc597"
    },
    {
        "path": "P21_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "045c6a24477283a0910ae79273f9c2dc2dd3312a",
        "size": 6897,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/045c6a24477283a0910ae79273f9c2dc2dd3312a"
    },
    {
        "path": "P21_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2ac71fe1eb34fa573a0bdfedccad35240e55791a",
        "size": 7090,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2ac71fe1eb34fa573a0bdfedccad35240e55791a"
    },
    {
        "path": "P21_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "941b00a807ae0817c562e71aa7600b82eb5a7c39",
        "size": 4151,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/941b00a807ae0817c562e71aa7600b82eb5a7c39"
    },
    {
        "path": "P21_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "591281acb7ebd73b3242076d8830dd6e33a8cf3c",
        "size": 5727,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/591281acb7ebd73b3242076d8830dd6e33a8cf3c"
    },
    {
        "path": "P21_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "563f2bd023b6f7d244c52c9c134aa1f6fe009152",
        "size": 7375,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/563f2bd023b6f7d244c52c9c134aa1f6fe009152"
    },
    {
        "path": "P21_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ca4292619b6d20fcada8553265f2fe7425d2be36",
        "size": 9288,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ca4292619b6d20fcada8553265f2fe7425d2be36"
    },
    {
        "path": "P21_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3e0da5e78a2590c7d55685f555019f17b7f01fa5",
        "size": 7769,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3e0da5e78a2590c7d55685f555019f17b7f01fa5"
    },
    {
        "path": "P21_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5effec9144b09fc91eed7ab371b62cb1fdd02815",
        "size": 4766,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5effec9144b09fc91eed7ab371b62cb1fdd02815"
    },
    {
        "path": "P21_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "30d060edc1c25b73b98432c1331f8fb498275622",
        "size": 9199,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/30d060edc1c25b73b98432c1331f8fb498275622"
    },
    {
        "path": "P21_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "57309778ed4fa66ecbf0cc4b0c7a04317d3c3de5",
        "size": 6887,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/57309778ed4fa66ecbf0cc4b0c7a04317d3c3de5"
    },
    {
        "path": "P21_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6e40789fda536d3fae847bec10beaa73ff31c4c4",
        "size": 5314,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6e40789fda536d3fae847bec10beaa73ff31c4c4"
    },
    {
        "path": "P21_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6b3992965e56802db9616291cdb2baa09358a7d7",
        "size": 6681,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6b3992965e56802db9616291cdb2baa09358a7d7"
    },
    {
        "path": "P21_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "29b44c931eeb31e58b6e534d72b7d59533263a7b",
        "size": 4356,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/29b44c931eeb31e58b6e534d72b7d59533263a7b"
    },
    {
        "path": "P21_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e2e056cdf9de47462d40371170a68c4be43043ba",
        "size": 5449,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e2e056cdf9de47462d40371170a68c4be43043ba"
    },
    {
        "path": "P21_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "594c7ad6553429e234c239b4d0b8cbec8d9f5457",
        "size": 7163,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/594c7ad6553429e234c239b4d0b8cbec8d9f5457"
    },
    {
        "path": "P21_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "08b2acbbc622629bf9667a99c7f48ed041cb5f92",
        "size": 10265,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/08b2acbbc622629bf9667a99c7f48ed041cb5f92"
    },
    {
        "path": "P21_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "42b63a4501c94ac01d1a3b9fcef91f58d16876c5",
        "size": 9252,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/42b63a4501c94ac01d1a3b9fcef91f58d16876c5"
    },
    {
        "path": "P21_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e75fe18f570b25788c306741cfc171111b61c37f",
        "size": 3864,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e75fe18f570b25788c306741cfc171111b61c37f"
    },
    {
        "path": "P21_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c455db870b2a5d6212fa40917c957da901bb76ea",
        "size": 8533,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c455db870b2a5d6212fa40917c957da901bb76ea"
    },
    {
        "path": "P21_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1caa24e1d9646ca5c0eda988420af73f3895f328",
        "size": 5584,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1caa24e1d9646ca5c0eda988420af73f3895f328"
    },
    {
        "path": "P21_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5851baad26c8f6891d99dd47ce063896c48e65b8",
        "size": 5183,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5851baad26c8f6891d99dd47ce063896c48e65b8"
    },
    {
        "path": "P21_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7eec700b817cf45483f8a85ad69634cb60940a0c",
        "size": 8814,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7eec700b817cf45483f8a85ad69634cb60940a0c"
    },
    {
        "path": "P21_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8967d018ff5169a828dc8f341fa6abf8410ecbd5",
        "size": 11461,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8967d018ff5169a828dc8f341fa6abf8410ecbd5"
    },
    {
        "path": "P21_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "91049b87d920a1f9a350300a78acc29183e06486",
        "size": 5870,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/91049b87d920a1f9a350300a78acc29183e06486"
    },
    {
        "path": "P21_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fd5ad3aeb8b921fa53aff61590410a5504579d54",
        "size": 5939,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fd5ad3aeb8b921fa53aff61590410a5504579d54"
    },
    {
        "path": "P21_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9b5e1953d5a873d48b5bc133d22a2949355f7732",
        "size": 4150,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9b5e1953d5a873d48b5bc133d22a2949355f7732"
    },
    {
        "path": "P21_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "664cb9e8694d6a9e935199de59e8cf6b4a35e243",
        "size": 6887,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/664cb9e8694d6a9e935199de59e8cf6b4a35e243"
    },
    {
        "path": "P21_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ab42e9fe3cde532a6974f085c619519d0ed31dd8",
        "size": 6343,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ab42e9fe3cde532a6974f085c619519d0ed31dd8"
    },
    {
        "path": "P21_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8d3e62119830b4cfd6e30fdeb5fc445e0375ffb6",
        "size": 4148,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8d3e62119830b4cfd6e30fdeb5fc445e0375ffb6"
    },
    {
        "path": "P21_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "43702df62d0d2bd5ff70ff674805efaff04cb4ac",
        "size": 9137,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/43702df62d0d2bd5ff70ff674805efaff04cb4ac"
    },
    {
        "path": "P21_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "36dcfff0b8bb33f6934e65ccc62fd15cb977964d",
        "size": 2772,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/36dcfff0b8bb33f6934e65ccc62fd15cb977964d"
    },
    {
        "path": "P21_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0d2c5eb705f74be0d88c310f09267eaa37a113fa",
        "size": 4005,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0d2c5eb705f74be0d88c310f09267eaa37a113fa"
    },
    {
        "path": "P21_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f2cd1bba319c3e34bb83a460b13c80f13213e084",
        "size": 5309,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f2cd1bba319c3e34bb83a460b13c80f13213e084"
    },
    {
        "path": "P21_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9627f68a508e404e3605bd6309bece74925c8002",
        "size": 5441,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9627f68a508e404e3605bd6309bece74925c8002"
    },
    {
        "path": "P21_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "60f40b48db4ebbcb65ac266ddb10a133e8274dd8",
        "size": 11861,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/60f40b48db4ebbcb65ac266ddb10a133e8274dd8"
    },
    {
        "path": "P21_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d73e2a7277d6869bd92fe2fb9b2a7fa0d2cac1d3",
        "size": 8052,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d73e2a7277d6869bd92fe2fb9b2a7fa0d2cac1d3"
    },
    {
        "path": "P21_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c13eab6819885cae8d123e8965a942bd6c76c3e9",
        "size": 6141,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c13eab6819885cae8d123e8965a942bd6c76c3e9"
    },
    {
        "path": "P21_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "12bc477a49a66d901d3ed087d7d0b3d0c9906396",
        "size": 5909,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/12bc477a49a66d901d3ed087d7d0b3d0c9906396"
    },
    {
        "path": "P21_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "45ea7d451264d59a25c6fb8d31e7d1e08b22e763",
        "size": 7640,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/45ea7d451264d59a25c6fb8d31e7d1e08b22e763"
    },
    {
        "path": "P21_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d3cff06880e2c406978a34c92969976e0069b696",
        "size": 9912,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d3cff06880e2c406978a34c92969976e0069b696"
    },
    {
        "path": "P21_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b0e2bc6f236ef4abbfeb8824864c6ea1a9ab1006",
        "size": 7664,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b0e2bc6f236ef4abbfeb8824864c6ea1a9ab1006"
    },
    {
        "path": "P21_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "be55cc9158e5c589838806540c2da85d5d1a15cb",
        "size": 7554,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/be55cc9158e5c589838806540c2da85d5d1a15cb"
    },
    {
        "path": "P21_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a288af28d5f9675106da728724048cc2435b2753",
        "size": 18042,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a288af28d5f9675106da728724048cc2435b2753"
    },
    {
        "path": "P21_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "018aad191f6088637a365bc67c515eacf3bcf0a0",
        "size": 6345,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/018aad191f6088637a365bc67c515eacf3bcf0a0"
    },
    {
        "path": "P21_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "54b0088c8bee2ed2d0f2685fd127e2f8bb48ca8e",
        "size": 4263,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/54b0088c8bee2ed2d0f2685fd127e2f8bb48ca8e"
    },
    {
        "path": "P21_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3a4e9f0dac20a2c2bd6371bccfd7d9756a2d1d74",
        "size": 16456,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3a4e9f0dac20a2c2bd6371bccfd7d9756a2d1d74"
    },
    {
        "path": "P21_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1cb3e84468e07bf4e0fdfc17c28814f8fba18912",
        "size": 7504,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1cb3e84468e07bf4e0fdfc17c28814f8fba18912"
    },
    {
        "path": "P21_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "82367a5c3ee7e33d332b149cd4c86588308aa09f",
        "size": 3673,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/82367a5c3ee7e33d332b149cd4c86588308aa09f"
    },
    {
        "path": "P21_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a1157b96b465160b0d1b005a22c52cf50161bc1c",
        "size": 6658,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a1157b96b465160b0d1b005a22c52cf50161bc1c"
    },
    {
        "path": "P21_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2b50b23026005d38ff900b0cb8d40854976885ff",
        "size": 2535,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2b50b23026005d38ff900b0cb8d40854976885ff"
    },
    {
        "path": "P21_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c70df5ac6b5bfea8d962e6b668c2011e49826d2f",
        "size": 8604,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c70df5ac6b5bfea8d962e6b668c2011e49826d2f"
    },
    {
        "path": "P21_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2b501a6e12082bca3a491fd851973895fbee0837",
        "size": 4203,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2b501a6e12082bca3a491fd851973895fbee0837"
    },
    {
        "path": "P21_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d9e18af77fd38572f8419a4c84ea79ae067c82fd",
        "size": 5232,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d9e18af77fd38572f8419a4c84ea79ae067c82fd"
    },
    {
        "path": "P21_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0b3015c647f541802471bc13c7b3ebe30f48c534",
        "size": 3926,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0b3015c647f541802471bc13c7b3ebe30f48c534"
    },
    {
        "path": "P21_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "176028e27657642a37f1a9372ea329c72aa4842a",
        "size": 10836,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/176028e27657642a37f1a9372ea329c72aa4842a"
    },
    {
        "path": "P21_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6a78584a5e5178a97e79e269e3c243e8c9375db4",
        "size": 14178,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6a78584a5e5178a97e79e269e3c243e8c9375db4"
    },
    {
        "path": "P22_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "95cddcad6c1da450de86947feaea564998c5dc32",
        "size": 4212,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/95cddcad6c1da450de86947feaea564998c5dc32"
    },
    {
        "path": "P22_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "51423f72f00dcb03d2c8f11bea473b2f7a66c92c",
        "size": 9226,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/51423f72f00dcb03d2c8f11bea473b2f7a66c92c"
    },
    {
        "path": "P22_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a1a8a92f8f15d1a3a81a90e32ddfc074878a2ef3",
        "size": 9625,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a1a8a92f8f15d1a3a81a90e32ddfc074878a2ef3"
    },
    {
        "path": "P22_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e83c947b1fb69615d5e1f598bbc7ac2b188d72c8",
        "size": 8268,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e83c947b1fb69615d5e1f598bbc7ac2b188d72c8"
    },
    {
        "path": "P22_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7552d339c6e8b9ce442e1661119b8fa316d374fe",
        "size": 6690,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7552d339c6e8b9ce442e1661119b8fa316d374fe"
    },
    {
        "path": "P22_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4712f32096e587846fe22fc65bb775278e47af16",
        "size": 6000,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4712f32096e587846fe22fc65bb775278e47af16"
    },
    {
        "path": "P22_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "23743326ccca2153c806116fae439091508d71a3",
        "size": 7278,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/23743326ccca2153c806116fae439091508d71a3"
    },
    {
        "path": "P22_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "02ef62bd499d9a0e3bc5aa5f099a14e9ff701d91",
        "size": 6964,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/02ef62bd499d9a0e3bc5aa5f099a14e9ff701d91"
    },
    {
        "path": "P22_S09_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cdcec7ec991188998d225e77d7daa3560d2ee081",
        "size": 8734,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cdcec7ec991188998d225e77d7daa3560d2ee081"
    },
    {
        "path": "P22_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c8d13f22f9f15bac5fc42753a34ebb81f09e1f4f",
        "size": 6342,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c8d13f22f9f15bac5fc42753a34ebb81f09e1f4f"
    },
    {
        "path": "P22_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "02d2b2bf2937a52d0bcfbba3cc11e82d3ab0b90c",
        "size": 10788,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/02d2b2bf2937a52d0bcfbba3cc11e82d3ab0b90c"
    },
    {
        "path": "P22_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "68950e5afa5e4f85ac48d1baa87097758de4be53",
        "size": 10493,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/68950e5afa5e4f85ac48d1baa87097758de4be53"
    },
    {
        "path": "P22_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9b76ca80839eeba55d5590a3731fcfb19ddd35be",
        "size": 6708,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9b76ca80839eeba55d5590a3731fcfb19ddd35be"
    },
    {
        "path": "P22_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "71fea720e0b22d833837da83bf3b5401e6338fd7",
        "size": 4274,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/71fea720e0b22d833837da83bf3b5401e6338fd7"
    },
    {
        "path": "P22_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0133905444ecf57e4f063134bcb7051315f7754c",
        "size": 5572,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0133905444ecf57e4f063134bcb7051315f7754c"
    },
    {
        "path": "P22_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3ba8b6f7b4377ecf8ba26b22c1ebe02439bcdbab",
        "size": 7019,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3ba8b6f7b4377ecf8ba26b22c1ebe02439bcdbab"
    },
    {
        "path": "P22_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9a0eed0874b5ad70fb6c665b0791bd94f77ee198",
        "size": 3658,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9a0eed0874b5ad70fb6c665b0791bd94f77ee198"
    },
    {
        "path": "P22_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fc71b1e7292f78d895a0c44595711de576a0f9d7",
        "size": 5937,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fc71b1e7292f78d895a0c44595711de576a0f9d7"
    },
    {
        "path": "P22_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9fc930e0b9a719f54e458d4eaba0b9eeb90eb363",
        "size": 7165,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9fc930e0b9a719f54e458d4eaba0b9eeb90eb363"
    },
    {
        "path": "P22_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4e24c1e1d3cd06155990f40b67b13f7bb16d602a",
        "size": 8942,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4e24c1e1d3cd06155990f40b67b13f7bb16d602a"
    },
    {
        "path": "P22_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8701e230ba37c6f1a07b319b216d276a6b5f4144",
        "size": 4750,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8701e230ba37c6f1a07b319b216d276a6b5f4144"
    },
    {
        "path": "P22_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4837c86a7321e8052ca6fa4e7186373365131014",
        "size": 4617,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4837c86a7321e8052ca6fa4e7186373365131014"
    },
    {
        "path": "P22_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f4af2d151ff153183bb02aadf7316e423055843e",
        "size": 7365,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f4af2d151ff153183bb02aadf7316e423055843e"
    },
    {
        "path": "P22_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e7312c25152b7690681f5de6fb15c8326d967cdc",
        "size": 6434,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e7312c25152b7690681f5de6fb15c8326d967cdc"
    },
    {
        "path": "P22_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9344bfe0939aa81dc5676ee1453a999e4d4d100f",
        "size": 5045,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9344bfe0939aa81dc5676ee1453a999e4d4d100f"
    },
    {
        "path": "P22_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "262d4d157a412873c08c6a8410b27b3afcf6cdd9",
        "size": 9322,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/262d4d157a412873c08c6a8410b27b3afcf6cdd9"
    },
    {
        "path": "P22_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6fbe2da816ab4cbdae9a4fd91463d47c609d7cb6",
        "size": 4879,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6fbe2da816ab4cbdae9a4fd91463d47c609d7cb6"
    },
    {
        "path": "P22_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "38c11a2021b7aff8ff70bd7fb3f9678e7a0b303c",
        "size": 8187,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/38c11a2021b7aff8ff70bd7fb3f9678e7a0b303c"
    },
    {
        "path": "P22_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b96bc97343e33b356bb272ff7a82152f70df8df4",
        "size": 7906,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b96bc97343e33b356bb272ff7a82152f70df8df4"
    },
    {
        "path": "P22_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "64228e43a7a4bb9d431bf818e8290abd08f0eb36",
        "size": 6586,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/64228e43a7a4bb9d431bf818e8290abd08f0eb36"
    },
    {
        "path": "P22_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4031cffed3d9af5da7aacc53f4c191d25c093d06",
        "size": 5094,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4031cffed3d9af5da7aacc53f4c191d25c093d06"
    },
    {
        "path": "P22_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "02d57a8f02863d79d0881eff178a9ba48adc3f46",
        "size": 6470,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/02d57a8f02863d79d0881eff178a9ba48adc3f46"
    },
    {
        "path": "P22_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b132d7016042a63e2996919d50ccc30d6b74f5db",
        "size": 3114,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b132d7016042a63e2996919d50ccc30d6b74f5db"
    },
    {
        "path": "P22_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "86a1cd98306e8e0722295489b33ca9f875429bad",
        "size": 5229,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/86a1cd98306e8e0722295489b33ca9f875429bad"
    },
    {
        "path": "P22_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "639cba46c2aace81c863a90eb62a74608caffc07",
        "size": 6194,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/639cba46c2aace81c863a90eb62a74608caffc07"
    },
    {
        "path": "P22_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "29f9f2ac3aa1f0fb57c92a7e0e394928f800e9e4",
        "size": 3589,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/29f9f2ac3aa1f0fb57c92a7e0e394928f800e9e4"
    },
    {
        "path": "P22_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4a975f67125de04f40e045904bc4569890ab7e09",
        "size": 7578,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4a975f67125de04f40e045904bc4569890ab7e09"
    },
    {
        "path": "P22_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6d3544bbb8fe4acf0c82a0f7ff4fe00e5f2018ae",
        "size": 9835,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6d3544bbb8fe4acf0c82a0f7ff4fe00e5f2018ae"
    },
    {
        "path": "P22_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2137d5cd14238ad64305ef488aec401a8a18ef4a",
        "size": 4824,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2137d5cd14238ad64305ef488aec401a8a18ef4a"
    },
    {
        "path": "P22_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b5af1dc68f19f3a56bf18dedc99551d66bdd24c4",
        "size": 5991,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b5af1dc68f19f3a56bf18dedc99551d66bdd24c4"
    },
    {
        "path": "P22_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7d5b67a97c795e140a72ae651883bb9014c7feb5",
        "size": 6494,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7d5b67a97c795e140a72ae651883bb9014c7feb5"
    },
    {
        "path": "P22_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "af9f7d074a8ccdcb9d72ea183071e2d2952170d8",
        "size": 6611,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/af9f7d074a8ccdcb9d72ea183071e2d2952170d8"
    },
    {
        "path": "P22_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "84367d5931e5c4373aacb83660a9ae064584a628",
        "size": 4621,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/84367d5931e5c4373aacb83660a9ae064584a628"
    },
    {
        "path": "P22_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8e2eea5052aade68a8622445f33009ebd8a5f413",
        "size": 5725,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8e2eea5052aade68a8622445f33009ebd8a5f413"
    },
    {
        "path": "P22_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4134a55efd9107849f0fa606e9a4850ff1646edd",
        "size": 4762,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4134a55efd9107849f0fa606e9a4850ff1646edd"
    },
    {
        "path": "P22_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d30c2436324093f9d9bad78dd129fb48d120a383",
        "size": 7033,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d30c2436324093f9d9bad78dd129fb48d120a383"
    },
    {
        "path": "P22_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1dacfa8d99e4631e55c1cbb315a55c9e990b2ea4",
        "size": 5746,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1dacfa8d99e4631e55c1cbb315a55c9e990b2ea4"
    },
    {
        "path": "P22_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f750876e69244b5c2be396f0a05c796f6624128e",
        "size": 5928,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f750876e69244b5c2be396f0a05c796f6624128e"
    },
    {
        "path": "P22_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "923fd7d7568f1060facd0f757581025c037d0aae",
        "size": 4405,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/923fd7d7568f1060facd0f757581025c037d0aae"
    },
    {
        "path": "P22_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cdf9de139aacb69872c8c6fe21029b0bb6ede885",
        "size": 10398,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cdf9de139aacb69872c8c6fe21029b0bb6ede885"
    },
    {
        "path": "P22_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5c4c2530329c947771d6f60dcbcd36ea6184fc44",
        "size": 6209,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5c4c2530329c947771d6f60dcbcd36ea6184fc44"
    },
    {
        "path": "P22_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b5aaf671b67b6ac1ecc97486566f5ed46de3be47",
        "size": 4897,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b5aaf671b67b6ac1ecc97486566f5ed46de3be47"
    },
    {
        "path": "P22_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "03ba32225dc0027247afb3ad865def0c6ecf478a",
        "size": 6386,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/03ba32225dc0027247afb3ad865def0c6ecf478a"
    },
    {
        "path": "P22_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4af394c95fe64bb114cd6229bb9b6563c6170a76",
        "size": 5460,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4af394c95fe64bb114cd6229bb9b6563c6170a76"
    },
    {
        "path": "P22_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "62fefdba58b1d84ad7928d8f4c8f71d4164be155",
        "size": 6491,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/62fefdba58b1d84ad7928d8f4c8f71d4164be155"
    },
    {
        "path": "P22_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "09c77e640a44b0c676358a8aeb1f92526decaa8a",
        "size": 6203,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/09c77e640a44b0c676358a8aeb1f92526decaa8a"
    },
    {
        "path": "P22_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "62f62e4a77435ae60939583fa0445253943160cb",
        "size": 5103,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/62f62e4a77435ae60939583fa0445253943160cb"
    },
    {
        "path": "P22_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7fde91d33a29cb0d3cdcc9bbff050f13b9c13bcd",
        "size": 5994,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7fde91d33a29cb0d3cdcc9bbff050f13b9c13bcd"
    },
    {
        "path": "P22_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "874fad5085d5d08707fe512302278b355a71b8f6",
        "size": 6352,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/874fad5085d5d08707fe512302278b355a71b8f6"
    },
    {
        "path": "P22_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "59ae1245b4c6504a1f3092d701bdddb87a5c2ac3",
        "size": 10661,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/59ae1245b4c6504a1f3092d701bdddb87a5c2ac3"
    },
    {
        "path": "P23_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a848c4080ea6a9a5f68fff813725eeeb290370a3",
        "size": 5100,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a848c4080ea6a9a5f68fff813725eeeb290370a3"
    },
    {
        "path": "P23_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "66631b9cb3c0038a6ce90d925075d6300a62e32c",
        "size": 5229,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/66631b9cb3c0038a6ce90d925075d6300a62e32c"
    },
    {
        "path": "P23_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bde74f0555c53bf9400c8d00e22ae46012495cea",
        "size": 6620,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bde74f0555c53bf9400c8d00e22ae46012495cea"
    },
    {
        "path": "P23_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "306bd9a60d42baf36c8e02d569ccbf66bcb679d3",
        "size": 7773,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/306bd9a60d42baf36c8e02d569ccbf66bcb679d3"
    },
    {
        "path": "P23_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a77ede78574cc4645d14c669528493ef2e7c9465",
        "size": 5716,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a77ede78574cc4645d14c669528493ef2e7c9465"
    },
    {
        "path": "P23_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3574904387ad43ca57561488d4fca11c58fe8822",
        "size": 5167,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3574904387ad43ca57561488d4fca11c58fe8822"
    },
    {
        "path": "P23_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a3c7be2657dc1d2366646ff44508c0cb92b5d05f",
        "size": 7763,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a3c7be2657dc1d2366646ff44508c0cb92b5d05f"
    },
    {
        "path": "P23_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cf510fda7b559aa81a9db4fc2b56ade446749133",
        "size": 8751,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cf510fda7b559aa81a9db4fc2b56ade446749133"
    },
    {
        "path": "P23_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "aa2411cdd333e6a4fa9fe90b50c68d1a5a2c1e81",
        "size": 9378,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/aa2411cdd333e6a4fa9fe90b50c68d1a5a2c1e81"
    },
    {
        "path": "P23_S10_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "95c8595362472faa6af05edaaa579ccd22a0c661",
        "size": 9563,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/95c8595362472faa6af05edaaa579ccd22a0c661"
    },
    {
        "path": "P23_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8080f3a015e80e4543c885fc9f758040ceebbc77",
        "size": 4272,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8080f3a015e80e4543c885fc9f758040ceebbc77"
    },
    {
        "path": "P23_S12_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4f4780674afd626ca09f741523cc4ac81b0a7586",
        "size": 4555,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4f4780674afd626ca09f741523cc4ac81b0a7586"
    },
    {
        "path": "P23_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "af979984bb6f3bc6cb225e539f8e17a8ec6c1d93",
        "size": 6127,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/af979984bb6f3bc6cb225e539f8e17a8ec6c1d93"
    },
    {
        "path": "P23_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3c061a753a5d766ba3e0fd915fc93aaeac0d6472",
        "size": 5780,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3c061a753a5d766ba3e0fd915fc93aaeac0d6472"
    },
    {
        "path": "P23_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4d07bc4d46eeaefb695e1776fad161e8ad6d673e",
        "size": 5652,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4d07bc4d46eeaefb695e1776fad161e8ad6d673e"
    },
    {
        "path": "P23_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "db26e75d5f512f7416a485f49eb30eafd2ee26d2",
        "size": 5656,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/db26e75d5f512f7416a485f49eb30eafd2ee26d2"
    },
    {
        "path": "P23_S17_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8572fc1b56f49683e196494c9b91007c185673b3",
        "size": 3939,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8572fc1b56f49683e196494c9b91007c185673b3"
    },
    {
        "path": "P23_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8f9d5fae6211d425a8ad0967e9d2b9d1d99f50e0",
        "size": 9206,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8f9d5fae6211d425a8ad0967e9d2b9d1d99f50e0"
    },
    {
        "path": "P23_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "adcb6ee92bee6911945876165839eb8d7906476e",
        "size": 8463,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/adcb6ee92bee6911945876165839eb8d7906476e"
    },
    {
        "path": "P23_S20_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f57c0c442b414d69435f6d0593101497b9643224",
        "size": 8053,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f57c0c442b414d69435f6d0593101497b9643224"
    },
    {
        "path": "P23_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "75bd03b543a33e94e810cd3d05d1b872c21e1dbb",
        "size": 5449,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/75bd03b543a33e94e810cd3d05d1b872c21e1dbb"
    },
    {
        "path": "P23_S22_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "12fcd5f01b6043a2afbbda04dab4c2613de60fe4",
        "size": 4883,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/12fcd5f01b6043a2afbbda04dab4c2613de60fe4"
    },
    {
        "path": "P23_S23_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "09bbf00cec4793e510225bf8f756c7953c72ef67",
        "size": 8100,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/09bbf00cec4793e510225bf8f756c7953c72ef67"
    },
    {
        "path": "P23_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "25f188b0f3bde8cb050f94579f565b65124a564c",
        "size": 9066,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/25f188b0f3bde8cb050f94579f565b65124a564c"
    },
    {
        "path": "P23_S25_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9aededce340bf005e1c0f17d9982ea259be82196",
        "size": 6458,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9aededce340bf005e1c0f17d9982ea259be82196"
    },
    {
        "path": "P23_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4ce90df564f501474051e0c6eb242a8b06728442",
        "size": 8182,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4ce90df564f501474051e0c6eb242a8b06728442"
    },
    {
        "path": "P23_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "182ca09a424dac27cb12b684ae76afc62b96f692",
        "size": 6315,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/182ca09a424dac27cb12b684ae76afc62b96f692"
    },
    {
        "path": "P23_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8239a787c636b32461bf0a0fce689e27986bae71",
        "size": 8237,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8239a787c636b32461bf0a0fce689e27986bae71"
    },
    {
        "path": "P23_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f1ec3ad6aedf9244c340a82fc0244cc829da8c89",
        "size": 8039,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f1ec3ad6aedf9244c340a82fc0244cc829da8c89"
    },
    {
        "path": "P23_S30_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4bd78eca9e95b4cc98181f2d25445252264da7a2",
        "size": 5444,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4bd78eca9e95b4cc98181f2d25445252264da7a2"
    },
    {
        "path": "P23_S31_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a0fcd8222bd6946f094651859c12904ba5c0b24d",
        "size": 4142,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a0fcd8222bd6946f094651859c12904ba5c0b24d"
    },
    {
        "path": "P23_S32_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6abf104229dfa8880a54151a025e0ba2cad91b6f",
        "size": 6403,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6abf104229dfa8880a54151a025e0ba2cad91b6f"
    },
    {
        "path": "P23_S33_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e9ea3dbcdc33d7587dc91b13470233dc75179b05",
        "size": 5158,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e9ea3dbcdc33d7587dc91b13470233dc75179b05"
    },
    {
        "path": "P23_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "61353cf0091f7807d35fb7edd2abc66ff0347f49",
        "size": 8385,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/61353cf0091f7807d35fb7edd2abc66ff0347f49"
    },
    {
        "path": "P23_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4c37c46670d65f55c6fb467673ea6025cf2c29a2",
        "size": 3467,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4c37c46670d65f55c6fb467673ea6025cf2c29a2"
    },
    {
        "path": "P23_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fa4ae92ef49b2bcefe589033bbb2845e4294abc1",
        "size": 5242,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fa4ae92ef49b2bcefe589033bbb2845e4294abc1"
    },
    {
        "path": "P23_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3c35476d2ea44f4b80b468020771a599b7eb18dd",
        "size": 4069,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3c35476d2ea44f4b80b468020771a599b7eb18dd"
    },
    {
        "path": "P23_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d8c66b9cd0075d6a9e6f413ea7a78272fc68b226",
        "size": 6404,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d8c66b9cd0075d6a9e6f413ea7a78272fc68b226"
    },
    {
        "path": "P23_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "00f2771e3c86802d2ca49df5a10fb4ad44acd5ec",
        "size": 5841,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/00f2771e3c86802d2ca49df5a10fb4ad44acd5ec"
    },
    {
        "path": "P23_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f02790770d76dbd9c59ed286994b9d2895517908",
        "size": 8869,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f02790770d76dbd9c59ed286994b9d2895517908"
    },
    {
        "path": "P23_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "86fe52bbb2bae85636e7fc2ce5b47394c407f723",
        "size": 3247,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/86fe52bbb2bae85636e7fc2ce5b47394c407f723"
    },
    {
        "path": "P23_S42_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0fb6d39c68994df2d716d97c862d0463d28f87a0",
        "size": 6681,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0fb6d39c68994df2d716d97c862d0463d28f87a0"
    },
    {
        "path": "P23_S43_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3398a23e6c1934dc973a8ca4a2f77d7ff4f85264",
        "size": 6615,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3398a23e6c1934dc973a8ca4a2f77d7ff4f85264"
    },
    {
        "path": "P23_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "66eaceb22d15b74d5faf17bcd29097f93c734e96",
        "size": 4968,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/66eaceb22d15b74d5faf17bcd29097f93c734e96"
    },
    {
        "path": "P23_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7a5556bf15e8aedc9135cadee9436bf566b15d58",
        "size": 2975,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7a5556bf15e8aedc9135cadee9436bf566b15d58"
    },
    {
        "path": "P23_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8bd38b5256e139e1f19a903521832bb51d5c218a",
        "size": 5794,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8bd38b5256e139e1f19a903521832bb51d5c218a"
    },
    {
        "path": "P23_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fc4806be78b1ea59426b878e3958047596e633cc",
        "size": 7712,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fc4806be78b1ea59426b878e3958047596e633cc"
    },
    {
        "path": "P23_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "28d147d776562e7885f309c4d7f4b31b796b64e7",
        "size": 4691,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/28d147d776562e7885f309c4d7f4b31b796b64e7"
    },
    {
        "path": "P23_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "18d172de9eea62fa6a3e7f58889a324ea5f46d36",
        "size": 5160,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/18d172de9eea62fa6a3e7f58889a324ea5f46d36"
    },
    {
        "path": "P23_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9e8f7a0aa0b28ccca28fb1d76d7857792d981859",
        "size": 6012,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9e8f7a0aa0b28ccca28fb1d76d7857792d981859"
    },
    {
        "path": "P23_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "291008623e320e0d525b6d750797efa32b6880bc",
        "size": 8648,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/291008623e320e0d525b6d750797efa32b6880bc"
    },
    {
        "path": "P23_S52_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4feeb723db704d732ad73fec8b6ef63f63f0426f",
        "size": 2772,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4feeb723db704d732ad73fec8b6ef63f63f0426f"
    },
    {
        "path": "P23_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "74d09816c035e2f4e495e3db05b40b36062d50dd",
        "size": 6011,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/74d09816c035e2f4e495e3db05b40b36062d50dd"
    },
    {
        "path": "P23_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d6eaf1568a0593e64797094f1ab7fcc753b5ad86",
        "size": 6067,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d6eaf1568a0593e64797094f1ab7fcc753b5ad86"
    },
    {
        "path": "P23_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "92090cbee9dc3f1de18fb071063b669ff0c71865",
        "size": 11320,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/92090cbee9dc3f1de18fb071063b669ff0c71865"
    },
    {
        "path": "P23_S56_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ec3dbcfd47566c8fe9c15af097ed7c46dbc6ab4d",
        "size": 7151,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ec3dbcfd47566c8fe9c15af097ed7c46dbc6ab4d"
    },
    {
        "path": "P23_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2cd5e9c835543a46160039a75ee6770ac9111906",
        "size": 6659,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2cd5e9c835543a46160039a75ee6770ac9111906"
    },
    {
        "path": "P23_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b405189d9ec60b4459dfeb40a95f66bc9c66b186",
        "size": 2880,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b405189d9ec60b4459dfeb40a95f66bc9c66b186"
    },
    {
        "path": "P23_S59_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "75c252837b31f125874a525aa58b88b2594b52f2",
        "size": 9747,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/75c252837b31f125874a525aa58b88b2594b52f2"
    },
    {
        "path": "P23_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "aa6e08283b972c52fd8a72c47d2873bb766f3714",
        "size": 10325,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/aa6e08283b972c52fd8a72c47d2873bb766f3714"
    },
    {
        "path": "P24_S01_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "07a9c10b739e639b0529dfeafe4e5c49f938d416",
        "size": 3871,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/07a9c10b739e639b0529dfeafe4e5c49f938d416"
    },
    {
        "path": "P24_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a4a1ad07b0ec5ceba00081a6e73d62c86a7d885e",
        "size": 4003,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a4a1ad07b0ec5ceba00081a6e73d62c86a7d885e"
    },
    {
        "path": "P24_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bf2f7d10b154564a9dc1fc4aae7e952078c0ee46",
        "size": 9242,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bf2f7d10b154564a9dc1fc4aae7e952078c0ee46"
    },
    {
        "path": "P24_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "eddeb3ebc3b54d078ff0b116f720bc006f39ba15",
        "size": 11362,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/eddeb3ebc3b54d078ff0b116f720bc006f39ba15"
    },
    {
        "path": "P24_S05_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "85f3ca4ed4b092cead8bd0e4892472d850860d3b",
        "size": 11040,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/85f3ca4ed4b092cead8bd0e4892472d850860d3b"
    },
    {
        "path": "P24_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8ad728cfb4290608f907b76ac25100c0e7057968",
        "size": 5445,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8ad728cfb4290608f907b76ac25100c0e7057968"
    },
    {
        "path": "P24_S08_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a18e349568e8381dd3963c906519c514aede26a1",
        "size": 5875,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a18e349568e8381dd3963c906519c514aede26a1"
    },
    {
        "path": "P24_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7ce3abd2e76e1b5339b25776003c541d6706f060",
        "size": 5061,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7ce3abd2e76e1b5339b25776003c541d6706f060"
    },
    {
        "path": "P24_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a8211e941042c87440a803c788efeecf6cfbc650",
        "size": 2572,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a8211e941042c87440a803c788efeecf6cfbc650"
    },
    {
        "path": "P24_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7aaf20121de231ae54f3d9021e774a07ed7621fd",
        "size": 5101,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7aaf20121de231ae54f3d9021e774a07ed7621fd"
    },
    {
        "path": "P24_S13_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0810cdc92a62a9fcad6240ae5cd99e81fccd5b71",
        "size": 4148,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0810cdc92a62a9fcad6240ae5cd99e81fccd5b71"
    },
    {
        "path": "P24_S14_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "51c54e55f978706f356adbe6a6d470c7a3b6b810",
        "size": 6394,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/51c54e55f978706f356adbe6a6d470c7a3b6b810"
    },
    {
        "path": "P24_S15_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cbaf537c85940e3bc0beb594822a3bd9c777aa9c",
        "size": 4152,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cbaf537c85940e3bc0beb594822a3bd9c777aa9c"
    },
    {
        "path": "P24_S16_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "77d60e8c3daf782873d794f94b524c1093883d87",
        "size": 4759,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/77d60e8c3daf782873d794f94b524c1093883d87"
    },
    {
        "path": "P24_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "192edeebefe8e2e5e9695155dbce0a7dfcb657e7",
        "size": 3883,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/192edeebefe8e2e5e9695155dbce0a7dfcb657e7"
    },
    {
        "path": "P24_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e9aad9d1d0476cd6c132e3c4a4187366d797c77e",
        "size": 4768,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e9aad9d1d0476cd6c132e3c4a4187366d797c77e"
    },
    {
        "path": "P24_S19_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2d4e3e4b51a1103d5136539ef0287a9d2fcbd4bc",
        "size": 5323,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2d4e3e4b51a1103d5136539ef0287a9d2fcbd4bc"
    },
    {
        "path": "P24_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "62f8230075164999128c10915a3132b51e582446",
        "size": 5496,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/62f8230075164999128c10915a3132b51e582446"
    },
    {
        "path": "P24_S21_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5f1f580f426972d2b9058ab08eef96a5d21b32ce",
        "size": 3328,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5f1f580f426972d2b9058ab08eef96a5d21b32ce"
    },
    {
        "path": "P24_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "45baaad6b2ed93ba43d3197932e61c67330aabb7",
        "size": 3797,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/45baaad6b2ed93ba43d3197932e61c67330aabb7"
    },
    {
        "path": "P24_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0cbbeca031db2f6252d14ecdbfb0df1653eeef5a",
        "size": 4692,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0cbbeca031db2f6252d14ecdbfb0df1653eeef5a"
    },
    {
        "path": "P24_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d0201c2990df2b4f9d3516304966bf56ada8dc60",
        "size": 7011,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d0201c2990df2b4f9d3516304966bf56ada8dc60"
    },
    {
        "path": "P24_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f505691bbea90d5a05f23b9d01bbcaa6831290e1",
        "size": 5516,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f505691bbea90d5a05f23b9d01bbcaa6831290e1"
    },
    {
        "path": "P24_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "99ce333068ea2253f81a170d1dcfdc26f6af0795",
        "size": 4010,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/99ce333068ea2253f81a170d1dcfdc26f6af0795"
    },
    {
        "path": "P24_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "575c7042d84ca573fd02500424dcf186292b076c",
        "size": 4410,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/575c7042d84ca573fd02500424dcf186292b076c"
    },
    {
        "path": "P24_S28_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f173b5d89960e745dddf74109163cae6619657b0",
        "size": 5786,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f173b5d89960e745dddf74109163cae6619657b0"
    },
    {
        "path": "P24_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8e48e9cd366fbe81a6172eaf6cda3ba2beea434e",
        "size": 4490,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8e48e9cd366fbe81a6172eaf6cda3ba2beea434e"
    },
    {
        "path": "P24_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b70a15cc2f35e50d0026b001d1f2e886dcfee612",
        "size": 4776,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b70a15cc2f35e50d0026b001d1f2e886dcfee612"
    },
    {
        "path": "P24_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c9a9b5931f0328b890984b0b17867f3da6265b34",
        "size": 3800,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c9a9b5931f0328b890984b0b17867f3da6265b34"
    },
    {
        "path": "P24_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bb52ac5f8e11c656c2fd7da43ea5f6e961c3f971",
        "size": 6198,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bb52ac5f8e11c656c2fd7da43ea5f6e961c3f971"
    },
    {
        "path": "P24_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a49149c4d82df4f12562a7e6c16bc2a9d38652ea",
        "size": 2698,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a49149c4d82df4f12562a7e6c16bc2a9d38652ea"
    },
    {
        "path": "P24_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cbc28079f9b870dfcaf4186216ab1d1f72f58c35",
        "size": 2567,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cbc28079f9b870dfcaf4186216ab1d1f72f58c35"
    },
    {
        "path": "P24_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a8437f71cb53616b01f81940135bd73f4fa666bf",
        "size": 3243,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a8437f71cb53616b01f81940135bd73f4fa666bf"
    },
    {
        "path": "P24_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "17627047e5a51098bce671455eed513f2bc7581f",
        "size": 3528,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/17627047e5a51098bce671455eed513f2bc7581f"
    },
    {
        "path": "P24_S37_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f2508205110e1138cc59c8d21cde1138ab4bc5b1",
        "size": 3939,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f2508205110e1138cc59c8d21cde1138ab4bc5b1"
    },
    {
        "path": "P24_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dfd428de4152606305f88cef4ccfde0caa36caa2",
        "size": 2983,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dfd428de4152606305f88cef4ccfde0caa36caa2"
    },
    {
        "path": "P24_S39_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0d57cf32ac97394f1a8961bc131f2f47b3a84e9c",
        "size": 2848,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0d57cf32ac97394f1a8961bc131f2f47b3a84e9c"
    },
    {
        "path": "P24_S40_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3cca8b00c76d34732b4eb9f067ca5b925e881241",
        "size": 4225,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3cca8b00c76d34732b4eb9f067ca5b925e881241"
    },
    {
        "path": "P24_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a279227f468523a9e5fc875cdf968146b34144d7",
        "size": 5915,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a279227f468523a9e5fc875cdf968146b34144d7"
    },
    {
        "path": "P24_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7a895b5481c1a78261202e0bb29eae73ddf88be5",
        "size": 5384,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7a895b5481c1a78261202e0bb29eae73ddf88be5"
    },
    {
        "path": "P24_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "567d1c5e7e29f87f92a1a81b52577e6ff64cb658",
        "size": 4823,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/567d1c5e7e29f87f92a1a81b52577e6ff64cb658"
    },
    {
        "path": "P24_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "617d09637fcc514533727cb38a3689b553630c30",
        "size": 4086,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/617d09637fcc514533727cb38a3689b553630c30"
    },
    {
        "path": "P24_S45_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "120e5b37be3056ec106ab9e41c5e2e06c5b8de14",
        "size": 4298,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/120e5b37be3056ec106ab9e41c5e2e06c5b8de14"
    },
    {
        "path": "P24_S46_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4a942623b73283083ec3d9a97d995336a459b900",
        "size": 3992,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4a942623b73283083ec3d9a97d995336a459b900"
    },
    {
        "path": "P24_S47_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f37e5366a09ab6310fea3fdddeba99608775d6df",
        "size": 7726,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f37e5366a09ab6310fea3fdddeba99608775d6df"
    },
    {
        "path": "P24_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0c7c75db093649f37bc0835623153c96b1203f49",
        "size": 3247,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0c7c75db093649f37bc0835623153c96b1203f49"
    },
    {
        "path": "P24_S49_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cda82510c26059ec05779fd40131769c7b6bc2c2",
        "size": 3380,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cda82510c26059ec05779fd40131769c7b6bc2c2"
    },
    {
        "path": "P24_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "875d806bf9247ea2736324d16a93d72f4b7f93d5",
        "size": 6491,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/875d806bf9247ea2736324d16a93d72f4b7f93d5"
    },
    {
        "path": "P24_S51_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "737caa4974406f090abb4af21a1af7928c71829a",
        "size": 17133,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/737caa4974406f090abb4af21a1af7928c71829a"
    },
    {
        "path": "P24_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1ab8bc2515c7f2ca5b4abfd5b278d908202748ae",
        "size": 2716,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1ab8bc2515c7f2ca5b4abfd5b278d908202748ae"
    },
    {
        "path": "P24_S53_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "19f2b2d82f1455cad00df3ee00242eae6fb6bea2",
        "size": 5664,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/19f2b2d82f1455cad00df3ee00242eae6fb6bea2"
    },
    {
        "path": "P24_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d9173f5ee911565d1d710f95e0c919406bfbf61f",
        "size": 3885,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d9173f5ee911565d1d710f95e0c919406bfbf61f"
    },
    {
        "path": "P24_S55_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b2e42d5bdb20670962e6fba2ba1b52a9ede1c4dd",
        "size": 8533,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b2e42d5bdb20670962e6fba2ba1b52a9ede1c4dd"
    },
    {
        "path": "P24_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "066a0f7946d00e0679902a87ab110673d6e68527",
        "size": 6064,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/066a0f7946d00e0679902a87ab110673d6e68527"
    },
    {
        "path": "P24_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6b653a3f55a2eef95743cdd5500868a4681f4eff",
        "size": 8888,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6b653a3f55a2eef95743cdd5500868a4681f4eff"
    },
    {
        "path": "P24_S58_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1198ae14dac75c9fc94d6eb81f05796303ba98c2",
        "size": 4483,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1198ae14dac75c9fc94d6eb81f05796303ba98c2"
    },
    {
        "path": "P24_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "eeddd1795fdfe3e0fcd7a57877d9ef8dbe4a1862",
        "size": 13804,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/eeddd1795fdfe3e0fcd7a57877d9ef8dbe4a1862"
    },
    {
        "path": "P24_S60_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d46b407ed6fe6c7ffc2d22c08436e81e8b85d49f",
        "size": 14672,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d46b407ed6fe6c7ffc2d22c08436e81e8b85d49f"
    },
    {
        "path": "P26_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6242c677c56340e0cb118fdbdc0721b0c73e28ce",
        "size": 17962,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6242c677c56340e0cb118fdbdc0721b0c73e28ce"
    },
    {
        "path": "P26_S02_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "83d1c9ae612c1ae7c4463e703ca36ec8c14da79f",
        "size": 11855,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/83d1c9ae612c1ae7c4463e703ca36ec8c14da79f"
    },
    {
        "path": "P26_S03_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fcc6d690f64c486e73941bd1227cd112c700e01d",
        "size": 17132,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fcc6d690f64c486e73941bd1227cd112c700e01d"
    },
    {
        "path": "P26_S04_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "49d891e1cc3022ff605bb3ba0bf3d7ea2ff15eba",
        "size": 21009,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/49d891e1cc3022ff605bb3ba0bf3d7ea2ff15eba"
    },
    {
        "path": "P26_S06_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "48f90a0c9be4fe58424fb8c75c9fd2f8571f7b05",
        "size": 18914,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/48f90a0c9be4fe58424fb8c75c9fd2f8571f7b05"
    },
    {
        "path": "P26_S07_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ca4a6e892a7b31dad29d5c3ebe8110d56208a6d6",
        "size": 14159,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ca4a6e892a7b31dad29d5c3ebe8110d56208a6d6"
    },
    {
        "path": "P26_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6a09ecb57733d73af91972eab591cd5fd8e50572",
        "size": 19009,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6a09ecb57733d73af91972eab591cd5fd8e50572"
    },
    {
        "path": "P26_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7634d11291bc8378b15f6a01602497f761b85f52",
        "size": 18822,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7634d11291bc8378b15f6a01602497f761b85f52"
    },
    {
        "path": "P26_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "54f88a20d68fb44ca4cc96785df0669a3b9866ba",
        "size": 13493,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/54f88a20d68fb44ca4cc96785df0669a3b9866ba"
    },
    {
        "path": "P26_S11_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0ee2c701e10ed0243af80767e5592c7fb019acd3",
        "size": 11659,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0ee2c701e10ed0243af80767e5592c7fb019acd3"
    },
    {
        "path": "P26_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b994d69a302795449fd6d72f96de0dca637cf648",
        "size": 16373,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b994d69a302795449fd6d72f96de0dca637cf648"
    },
    {
        "path": "P26_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "825f99e9d9ee4b4088b45875aebd0fa753e51bbb",
        "size": 18018,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/825f99e9d9ee4b4088b45875aebd0fa753e51bbb"
    },
    {
        "path": "P26_S18_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b793a428120431efa286baaaa951920c6a0324f2",
        "size": 13064,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b793a428120431efa286baaaa951920c6a0324f2"
    },
    {
        "path": "P26_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "aeedb13b57f2fceb65da3acb027d3dbfba23979e",
        "size": 19596,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/aeedb13b57f2fceb65da3acb027d3dbfba23979e"
    },
    {
        "path": "P26_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6d77593c990c55b59ab70cba1ae0acc95681f047",
        "size": 16263,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6d77593c990c55b59ab70cba1ae0acc95681f047"
    },
    {
        "path": "P26_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5eda4e4f7c7f407ed2ea13e85713fbec5aadffab",
        "size": 10931,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5eda4e4f7c7f407ed2ea13e85713fbec5aadffab"
    },
    {
        "path": "P26_S24_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "51cd8c32d454b9d92990d316e0d497781ea32a52",
        "size": 16998,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/51cd8c32d454b9d92990d316e0d497781ea32a52"
    },
    {
        "path": "P26_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "06dfa76479c1d2502aed166a7a221397c387ee95",
        "size": 12293,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/06dfa76479c1d2502aed166a7a221397c387ee95"
    },
    {
        "path": "P26_S26_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "38b033f2ca9ab8f02272de8928a454d48dc6ff05",
        "size": 16950,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/38b033f2ca9ab8f02272de8928a454d48dc6ff05"
    },
    {
        "path": "P26_S29_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d5be713177dad8bd67d22b28c7b946be6c2dad72",
        "size": 17514,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d5be713177dad8bd67d22b28c7b946be6c2dad72"
    },
    {
        "path": "P26_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3937a3f59064b39003e45ff78f90e3508d2ba811",
        "size": 10351,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3937a3f59064b39003e45ff78f90e3508d2ba811"
    },
    {
        "path": "P26_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2802639506ce676b069e5e4135690fa273e9a1fd",
        "size": 13061,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2802639506ce676b069e5e4135690fa273e9a1fd"
    },
    {
        "path": "P26_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "75e8497d90e0b1cdb4fe4ae92f85af0ed1fa527c",
        "size": 11580,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/75e8497d90e0b1cdb4fe4ae92f85af0ed1fa527c"
    },
    {
        "path": "P26_S34_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "10277cc56a639ae313f75690e49d54a094e03f97",
        "size": 9607,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/10277cc56a639ae313f75690e49d54a094e03f97"
    },
    {
        "path": "P26_S35_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "26da939e22b198c5715b181f5feed323ec088608",
        "size": 14291,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/26da939e22b198c5715b181f5feed323ec088608"
    },
    {
        "path": "P26_S36_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7c6cac38ee621b618ea2988541293d0ac3ea9d89",
        "size": 11462,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7c6cac38ee621b618ea2988541293d0ac3ea9d89"
    },
    {
        "path": "P26_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "11b71b4c2a6b859b97e2ab15e894ce3e96f721ce",
        "size": 15733,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/11b71b4c2a6b859b97e2ab15e894ce3e96f721ce"
    },
    {
        "path": "P26_S38_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5648d1e8c8578f91888068b86ae8fbb4b09001e4",
        "size": 10503,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5648d1e8c8578f91888068b86ae8fbb4b09001e4"
    },
    {
        "path": "P26_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "584f3228a222b280b48b1f45bfe7817296a29f74",
        "size": 19047,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/584f3228a222b280b48b1f45bfe7817296a29f74"
    },
    {
        "path": "P26_S41_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "048959395dae2b2ed53f1733a89c0e7bc1a726bb",
        "size": 13718,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/048959395dae2b2ed53f1733a89c0e7bc1a726bb"
    },
    {
        "path": "P26_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ec356e245339973bbaad53e543b68a272797fd79",
        "size": 12945,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ec356e245339973bbaad53e543b68a272797fd79"
    },
    {
        "path": "P26_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dc5c7f7a680d8abcf30af450dff6edb3d52c1d8b",
        "size": 10837,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dc5c7f7a680d8abcf30af450dff6edb3d52c1d8b"
    },
    {
        "path": "P26_S44_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0253057d14a741ec2590ab622f8f0b67d35285ab",
        "size": 16610,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0253057d14a741ec2590ab622f8f0b67d35285ab"
    },
    {
        "path": "P26_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2092f259e202dfdb3c8d0f2d469e7af85ebc8a69",
        "size": 13259,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2092f259e202dfdb3c8d0f2d469e7af85ebc8a69"
    },
    {
        "path": "P26_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2635e3c6ebb3c670bede2d472e593a6a851f0bd3",
        "size": 10777,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2635e3c6ebb3c670bede2d472e593a6a851f0bd3"
    },
    {
        "path": "P26_S48_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "96c3e60d078d78e87c2ee3597b45737db4886235",
        "size": 17137,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/96c3e60d078d78e87c2ee3597b45737db4886235"
    },
    {
        "path": "P26_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "92a28b79fad62c5920cf87a43b0d26c6c6c75112",
        "size": 11690,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/92a28b79fad62c5920cf87a43b0d26c6c6c75112"
    },
    {
        "path": "P26_S50_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3d171c70f0eb94f0f9f0a1d7f877781c4332fbee",
        "size": 13963,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3d171c70f0eb94f0f9f0a1d7f877781c4332fbee"
    },
    {
        "path": "P26_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "bb543a56ddeeb9d275bc608390390162d3fe7c70",
        "size": 15652,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/bb543a56ddeeb9d275bc608390390162d3fe7c70"
    },
    {
        "path": "P26_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "81309d7e6484b145dea3c59329bc4a7fcd629292",
        "size": 6233,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/81309d7e6484b145dea3c59329bc4a7fcd629292"
    },
    {
        "path": "P26_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "87045fd50ab94e191c166fbe74f1fecba8c62879",
        "size": 17492,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/87045fd50ab94e191c166fbe74f1fecba8c62879"
    },
    {
        "path": "P26_S54_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "88db939945c75dedc2e394e85c664160a36fd6c1",
        "size": 15408,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/88db939945c75dedc2e394e85c664160a36fd6c1"
    },
    {
        "path": "P26_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c331fa3d54d99ec5e06dbc9219f75da8cc7ff126",
        "size": 17763,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c331fa3d54d99ec5e06dbc9219f75da8cc7ff126"
    },
    {
        "path": "P26_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "8a3d7877bbac7fe3ac32efddf78b4eb19f68c1e8",
        "size": 16597,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/8a3d7877bbac7fe3ac32efddf78b4eb19f68c1e8"
    },
    {
        "path": "P26_S57_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "14164e90ada51dd524a8b866111d5dc93b0dd10e",
        "size": 13811,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/14164e90ada51dd524a8b866111d5dc93b0dd10e"
    },
    {
        "path": "P26_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5156f1b0a76a81564f31e367e749e0d3043f0a8d",
        "size": 9944,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5156f1b0a76a81564f31e367e749e0d3043f0a8d"
    },
    {
        "path": "P27_S01_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2db3b190adcca3273fb41fde6d14cb91ab4841ed",
        "size": 9426,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2db3b190adcca3273fb41fde6d14cb91ab4841ed"
    },
    {
        "path": "P27_S02_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5560fd340bb15a0ff925fbb417a77e52fef5659a",
        "size": 5920,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5560fd340bb15a0ff925fbb417a77e52fef5659a"
    },
    {
        "path": "P27_S03_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "b63f7b095571e410fd0fa762612f8a12865e21c8",
        "size": 10414,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/b63f7b095571e410fd0fa762612f8a12865e21c8"
    },
    {
        "path": "P27_S04_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "71fb99ba9d5336d9197053e56d438265ecbf196f",
        "size": 10070,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/71fb99ba9d5336d9197053e56d438265ecbf196f"
    },
    {
        "path": "P27_S05_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "270ea1645e621476ff5d7381c7a34e1fe0ea8403",
        "size": 8134,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/270ea1645e621476ff5d7381c7a34e1fe0ea8403"
    },
    {
        "path": "P27_S06_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fe27d6143c9e8879aa66068e3c70be55d5d77cb4",
        "size": 6080,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fe27d6143c9e8879aa66068e3c70be55d5d77cb4"
    },
    {
        "path": "P27_S07_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9671c3f2837f5efb2f9589c5e07f344eac496524",
        "size": 6885,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9671c3f2837f5efb2f9589c5e07f344eac496524"
    },
    {
        "path": "P27_S08_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6e2a7bcc0204e162e7aabad10ba6e1575fcbdd38",
        "size": 9790,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6e2a7bcc0204e162e7aabad10ba6e1575fcbdd38"
    },
    {
        "path": "P27_S09_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6c84599bbab3160dd523bc9c2577a61f51d76968",
        "size": 8681,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6c84599bbab3160dd523bc9c2577a61f51d76968"
    },
    {
        "path": "P27_S10_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "468b228c7587a32209469b4da803aca1b083d4f0",
        "size": 8360,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/468b228c7587a32209469b4da803aca1b083d4f0"
    },
    {
        "path": "P27_S11_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "69cad0549dbf35389e4a70489bf9a5a98a2c3c21",
        "size": 7902,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/69cad0549dbf35389e4a70489bf9a5a98a2c3c21"
    },
    {
        "path": "P27_S12_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0c4fc3f7643d0ad45f84441b7dd216101e6cfe4f",
        "size": 5106,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0c4fc3f7643d0ad45f84441b7dd216101e6cfe4f"
    },
    {
        "path": "P27_S13_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1932e7aa6d8615f6f34d9cd7a77b1049c08d0aa5",
        "size": 9219,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1932e7aa6d8615f6f34d9cd7a77b1049c08d0aa5"
    },
    {
        "path": "P27_S14_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1129917c65dc5c5fa89abb46f653231f728195c3",
        "size": 7040,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1129917c65dc5c5fa89abb46f653231f728195c3"
    },
    {
        "path": "P27_S15_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f5783427581ed2929cc69001e6351bbb2e566e60",
        "size": 5747,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f5783427581ed2929cc69001e6351bbb2e566e60"
    },
    {
        "path": "P27_S16_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c8684d15135e300ba8966584c6fa30be34836597",
        "size": 9852,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c8684d15135e300ba8966584c6fa30be34836597"
    },
    {
        "path": "P27_S17_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f1079d448114238a0d5a2ca3e91cc003bb49f766",
        "size": 7033,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f1079d448114238a0d5a2ca3e91cc003bb49f766"
    },
    {
        "path": "P27_S18_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "aa3c5bf6bfee9b67e6d597a47c1014035793eb4c",
        "size": 8746,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/aa3c5bf6bfee9b67e6d597a47c1014035793eb4c"
    },
    {
        "path": "P27_S19_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "764b0b56870e1bd855751c6a93f2cb74c1c40d54",
        "size": 9772,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/764b0b56870e1bd855751c6a93f2cb74c1c40d54"
    },
    {
        "path": "P27_S20_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "272b728781cd289f452b722118132b7213a5e89a",
        "size": 6557,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/272b728781cd289f452b722118132b7213a5e89a"
    },
    {
        "path": "P27_S21_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "cd1d1d93322494a5cc6d9ca0f302f00e29b99231",
        "size": 9497,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/cd1d1d93322494a5cc6d9ca0f302f00e29b99231"
    },
    {
        "path": "P27_S22_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4c1eb86879df653c4cf706cb49dc4fb4fe6b8b51",
        "size": 4479,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4c1eb86879df653c4cf706cb49dc4fb4fe6b8b51"
    },
    {
        "path": "P27_S23_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a565c89452cc41f169923d418efa1dc4a47944ed",
        "size": 13634,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a565c89452cc41f169923d418efa1dc4a47944ed"
    },
    {
        "path": "P27_S24_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ea665677d543c465ba2e195fd8808fff08661c90",
        "size": 8050,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ea665677d543c465ba2e195fd8808fff08661c90"
    },
    {
        "path": "P27_S25_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "044286702b82ad7e122564f8871f056d8f211a5b",
        "size": 5379,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/044286702b82ad7e122564f8871f056d8f211a5b"
    },
    {
        "path": "P27_S26_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "f170ae96a6f2ff6930c649c2ead83ddfbdb5167b",
        "size": 12143,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/f170ae96a6f2ff6930c649c2ead83ddfbdb5167b"
    },
    {
        "path": "P27_S27_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a70b0c8b26b9a697259918ec23351ef0afa7fb43",
        "size": 7425,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a70b0c8b26b9a697259918ec23351ef0afa7fb43"
    },
    {
        "path": "P27_S28_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fc215ce5212ee6d9691192fd4ece4d35d29967b6",
        "size": 8721,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fc215ce5212ee6d9691192fd4ece4d35d29967b6"
    },
    {
        "path": "P27_S29_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "436fdee96015cd74795c47002143160a5597a50c",
        "size": 9488,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/436fdee96015cd74795c47002143160a5597a50c"
    },
    {
        "path": "P27_S30_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "0130c06fd584fd3d3d4b8726c166a3c6c2db7363",
        "size": 10193,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/0130c06fd584fd3d3d4b8726c166a3c6c2db7363"
    },
    {
        "path": "P27_S31_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "fddf7a1fcf495997d3d6ffeeb548d7bf620b43f6",
        "size": 5566,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/fddf7a1fcf495997d3d6ffeeb548d7bf620b43f6"
    },
    {
        "path": "P27_S32_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5bebe7b7f3ef1b593eabc75110d7fce62b8ad349",
        "size": 9202,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5bebe7b7f3ef1b593eabc75110d7fce62b8ad349"
    },
    {
        "path": "P27_S33_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2bff73a83cf440a525185a881e791334cca6fa14",
        "size": 6206,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2bff73a83cf440a525185a881e791334cca6fa14"
    },
    {
        "path": "P27_S34_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1e1aa71407af474a0136bc08d1efe249446847f9",
        "size": 6680,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1e1aa71407af474a0136bc08d1efe249446847f9"
    },
    {
        "path": "P27_S35_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "becdf9b20cdb7bb8cff8555aa95a6e0129788cff",
        "size": 4331,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/becdf9b20cdb7bb8cff8555aa95a6e0129788cff"
    },
    {
        "path": "P27_S36_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e2b848569befde0a13c8ff9ad3255ad8c1ec0cdc",
        "size": 7139,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e2b848569befde0a13c8ff9ad3255ad8c1ec0cdc"
    },
    {
        "path": "P27_S37_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "550dc427e9d785d9d731ce58d1063f3f6fa0dda4",
        "size": 7422,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/550dc427e9d785d9d731ce58d1063f3f6fa0dda4"
    },
    {
        "path": "P27_S38_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a4199f373f83c2f57c3a0ae9e25f4fa144b41a2b",
        "size": 6823,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a4199f373f83c2f57c3a0ae9e25f4fa144b41a2b"
    },
    {
        "path": "P27_S39_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "7f3a8d4dc2e9b03d47461047e6392b698168f64e",
        "size": 6664,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/7f3a8d4dc2e9b03d47461047e6392b698168f64e"
    },
    {
        "path": "P27_S40_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "4ae4ca66aac4859c237e6b13b609423e78e05ed0",
        "size": 10859,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/4ae4ca66aac4859c237e6b13b609423e78e05ed0"
    },
    {
        "path": "P27_S41_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "64dbcde5d187a099e5c810e04e85c27eb10ef598",
        "size": 11269,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/64dbcde5d187a099e5c810e04e85c27eb10ef598"
    },
    {
        "path": "P27_S42_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "a1bc85ceb9db14c41a13150919d12f36d43ca832",
        "size": 7625,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/a1bc85ceb9db14c41a13150919d12f36d43ca832"
    },
    {
        "path": "P27_S43_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "6b5508dc788b31d7b077c40f7d2a9d0d7a283325",
        "size": 10176,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/6b5508dc788b31d7b077c40f7d2a9d0d7a283325"
    },
    {
        "path": "P27_S44_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c6fba907698c9ac86fa1571e7ea9afed77f3a4a7",
        "size": 9712,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c6fba907698c9ac86fa1571e7ea9afed77f3a4a7"
    },
    {
        "path": "P27_S45_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e46df11bd46a528662c83bdbe4a1d06d0037ea5b",
        "size": 5591,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e46df11bd46a528662c83bdbe4a1d06d0037ea5b"
    },
    {
        "path": "P27_S46_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3e2a70573e7e6c8b93dc3139d61bbc9cf212256f",
        "size": 6855,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3e2a70573e7e6c8b93dc3139d61bbc9cf212256f"
    },
    {
        "path": "P27_S47_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "16b11bcc07366a9bcadc10b06dffdbb8cc1bc777",
        "size": 9019,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/16b11bcc07366a9bcadc10b06dffdbb8cc1bc777"
    },
    {
        "path": "P27_S48_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "66293b717031d98561fa442f20914a699e217e0b",
        "size": 5799,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/66293b717031d98561fa442f20914a699e217e0b"
    },
    {
        "path": "P27_S49_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "61bc2c6038674d5ef3a7a64d6be2b8abd8104b3e",
        "size": 5924,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/61bc2c6038674d5ef3a7a64d6be2b8abd8104b3e"
    },
    {
        "path": "P27_S50_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "d688aa50ed0393b560fee617fd1a5b607e410133",
        "size": 7328,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/d688aa50ed0393b560fee617fd1a5b607e410133"
    },
    {
        "path": "P27_S51_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "3f8b895ad87d391367d66d55d0b7d8061b70c1a2",
        "size": 5583,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/3f8b895ad87d391367d66d55d0b7d8061b70c1a2"
    },
    {
        "path": "P27_S52_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "2c471e578f76395ecc1d50caede767014addd67f",
        "size": 4142,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/2c471e578f76395ecc1d50caede767014addd67f"
    },
    {
        "path": "P27_S53_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "ed78fba02aceebbb091a171e217cdb8eb91b83eb",
        "size": 7356,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/ed78fba02aceebbb091a171e217cdb8eb91b83eb"
    },
    {
        "path": "P27_S54_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "e279932dea6505cac0d7a557cfaaa44db46708c4",
        "size": 6078,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/e279932dea6505cac0d7a557cfaaa44db46708c4"
    },
    {
        "path": "P27_S55_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "c1561536b5499fd832a24047a4494b235628d57e",
        "size": 8014,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/c1561536b5499fd832a24047a4494b235628d57e"
    },
    {
        "path": "P27_S56_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "9b3f60171c748d70b0c659d8806590c377774e55",
        "size": 7220,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/9b3f60171c748d70b0c659d8806590c377774e55"
    },
    {
        "path": "P27_S57_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "1d0f02f1e91f02d8dab9997e031fae7a8709ea47",
        "size": 7305,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/1d0f02f1e91f02d8dab9997e031fae7a8709ea47"
    },
    {
        "path": "P27_S58_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "886885b62b3fad48d68bc4cef1725e36442ba1fa",
        "size": 3720,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/886885b62b3fad48d68bc4cef1725e36442ba1fa"
    },
    {
        "path": "P27_S59_fake.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "5d6c900ed823936eb5c8e1d1020a1fdc5c4cba76",
        "size": 7649,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/5d6c900ed823936eb5c8e1d1020a1fdc5c4cba76"
    },
    {
        "path": "P27_S60_true.csv",
        "mode": "100644",
        "type": "blob",
        "sha": "dbff3cf6e44c61ca6e35046ac8ce4fb706dddf18",
        "size": 11691,
        "url": "https://api.github.com/repos/rameshdhungana/cs620-project/git/blobs/dbff3cf6e44c61ca6e35046ac8ce4fb706dddf18"
    }
]

true_files = []
fake_files = []
dataset_folder_path = "https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data"
github_eye_dateset_blob_url = "https://api.github.com/repos/rameshdhungana/cs620-project/git/trees/dba8d32958460bfdc8891c8d9a275831cddc0a36"

for file in tree:
    if "true.csv" in file['path']:
        true_files.append("{dataset_folder_path}/{path}".format(
            dataset_folder_path=dataset_folder_path, path=file['path']))
    if "fake.csv" in file['path']:
        fake_files.append("{dataset_folder_path}/{path}".format(
            dataset_folder_path=dataset_folder_path, path=file['path']))

# print(true_files)
# print(len(true_files))
print(fake_files)
print(len(true_files))


dataset_folder_path = "https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data"
github_eye_dateset_blob_url = "https://api.github.com/repos/rameshdhungana/cs620-project/git/trees/dba8d32958460bfdc8891c8d9a275831cddc0a36"

# list containing the url for True news data
true_files = ['https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S36_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S60_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S47_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S08_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S50_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S60_true.csv']

# list containing the url for Fake news csv
fake_files = ['https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S35_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S42_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S28_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S42_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S21_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S59_fake.csv']

print("Total number of csv files with eye datasets involved with true news:", len(true_files))
# read all true files and merge
true_df = pd.concat(map(pd.read_csv, true_files), ignore_index=True)
print(true_df.head())

print("Total number of csv files with eye datasets involved with fake news:", len(fake_files))
# read all fake files and merge
fake_df = pd.concat(map(pd.read_csv, fake_files), ignore_index=True)
print(fake_df.head())


true_df["news_type"] = "true"
fake_df["news_type"] = "fake"
total_df = pd.concat([true_df, fake_df])
print(total_df.head())

df = pd.DataFrame({'True News': [true_succade_count, fake_succade_count],
                   'Fake news': [true_fixation_count, fake_fixation_count]}, index=['Total Succades', 'Total Fixations'])
ax = df.plot.bar(rot=0)


# merging true_df and fake_df for comparison purpose
true_df["news"] = "true"
fake_df["news"] = "fake"
total_df = pd.concat([true_df, fake_df])


dataset_folder_path = "https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data"
github_eye_dateset_blob_url = "https://api.github.com/repos/rameshdhungana/cs620-project/git/trees/dba8d32958460bfdc8891c8d9a275831cddc0a36"

# list containing the url for True news data
true_files = ['https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S36_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S60_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S47_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S08_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S17_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S23_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S30_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S31_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S32_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S33_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S42_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S56_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S59_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S60_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S08_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S13_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S16_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S21_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S28_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S39_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S40_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S45_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S46_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S49_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S50_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S53_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S24_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S26_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S29_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S34_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S36_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S38_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S41_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S44_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S54_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S01_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S02_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S03_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S04_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S05_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S06_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S07_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S09_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S10_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S11_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S12_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S14_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S15_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S18_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S19_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S20_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S22_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S25_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S35_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S37_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S43_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S47_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S48_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S50_true.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S51_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S52_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S55_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S57_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S58_true.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S60_true.csv']


# list containing the url for Fake news csv
fake_files = ['https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P01_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P02_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S35_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P03_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P04_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P05_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P06_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P07_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S42_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P08_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P09_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P10_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P11_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P12_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P13_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S28_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P14_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P15_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P16_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P18_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P19_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S42_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P20_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P21_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S09_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P22_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S10_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S12_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S20_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S22_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S25_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S43_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S52_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P23_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S01_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S05_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S14_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S15_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S19_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S37_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S47_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S51_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S55_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S58_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S59_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P24_S60_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S02_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S03_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S04_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S06_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S07_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S11_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S18_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S21_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S35_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S48_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S50_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P26_S57_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S08_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S13_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S16_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S17_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S21_fake.csv',
              'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S23_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S24_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S26_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S27_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S28_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S29_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S30_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S31_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S32_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S33_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S34_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S36_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S38_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S39_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S40_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S41_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S42_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S44_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S45_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S46_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S49_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S53_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S54_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S56_fake.csv', 'https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data/P27_S59_fake.csv']

print("Total number of csv files with eye datasets involved with true news:", len(true_files))
# read all true files and merge
true_df = pd.concat(map(pd.read_csv, true_files), ignore_index=True)
true_df_copy = true_df.copy()
print(true_df.head())

print("Total number of csv files with eye datasets involved with fake news:", len(fake_files))
# read all fake files and merge
fake_df = pd.concat(map(pd.read_csv, fake_files), ignore_index=True)
fake_df_copy = fake_df.copy()
print(fake_df.head())


dataset_folder_path = "https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/datasets/D3-Eye-movements-data"
github_eye_dateset_blob_url = "https://api.github.com/repos/rameshdhungana/cs620-project/git/trees/dba8d32958460bfdc8891c8d9a275831cddc0a36"

# list containing the url for True news data
fake_files = []
f_file = open(
    "https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/fake_files.txt")
for filename in f_file.readlines():
    csv_data = pd.read_csv(filename)
    fake_files.append(csv_data)
f_file.close()

t_file = open(
    "https://raw.githubusercontent.com/rameshdhungana/cs620-project/main/true_files.txt")
for filename in f_file.readlines():
    csv_data = pd.read_csv(filename)
    fake_files.append(csv_data)
t_file.close()


print("Total number of csv files with eye datasets involved with true news:", len(true_files))
# read all true files and merge
true_df = pd.concat(map(pd.read_csv, true_files), ignore_index=True)
true_df_copy = true_df.copy()
print(true_df.head())

print("Total number of csv files with eye datasets involved with fake news:", len(fake_files))
# read all fake files and merge
fake_df = pd.concat(map(pd.read_csv, fake_files), ignore_index=True)
fake_df_copy = fake_df.copy()
print(fake_df.head())


# josqua backup>>>>

if __name__ == "__main__":
    # Reading the D3-Eye-movements-data dataset.
    # Creating Three Arrays, each is for all data items, true data items, and false items
    dataframes = []
    true_dataframes = []
    false_dataframes = []

    # Creating Array For Filenames
    true_filenames = []
    false_filenames = []
    # Iterates through each file in the D3-Eye-movements-data directory
    # Takes the CSV and convert it into a DataFrame
    file1 = open('./Data/true.txt')
    for filename in file1.readlines():
        csv_data = pd.read_csv(filename)
        true_dataframes.append(csv_data)
        true_filenames.append(filename)
        # Will Add the Same DataFrame to the array for all data items
        dataframes.append(csv_data)
    # Concatenating ALL Arrays into their respective DataFrames
    file1.close()
    #file1 = open('./Data/fake.txt')
    # for filename in file1.readlines():
    #    csv_data = pd.read_csv(filename)
    #    false_dataframes.append(csv_data)
    #    false_filenames.append(filename)
    true_eye_movement = pd.concat(true_dataframes)
    # false_eye_movement=pd.concat(false_dataframes)
    eye_movement = pd.concat(dataframes)

    # Printing the Results
    #print("ALL DATA")
    # print(eye_movement)

    #print("ALL TRUE DATA")
    # print(true_eye_movement)

    #print("ALL FALSE DATA")
    # print(false_eye_movement)


# Scatter Plotting on Each File from their respective DataFrame and Filename Array
for t in range(len(true_df)):
    ax = plt.gca()
    true_df[t].plot(kind='scatter',x='meanX',y='meanY',color='blue', ax=ax)
    true_df[t].plot(kind='line',x='startSaccadeX',y='startSaccadeY', color='green', ax=ax)
    print("File: {}".format(true_df[t]))
    plt.show()

for f in range(len(fake_df)):
    ax = plt.gca()
    fake_df[f].plot(kind='scatter',x='meanX',y='meanY',color='blue', ax=ax)
    fake_df[f].plot(kind='line',x='endSaccadeX',y='endSaccadeY', color='red', ax=ax)
    print("File: {}".format(fake_df[f]))
    plt.show()