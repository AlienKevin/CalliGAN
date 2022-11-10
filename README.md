# CalliGAN
CalliGAN - Tensorflow Implementation (AI for Content Creation Workshop CVPR 2020)

# Introduction
This is the implementation of paper "CalliGAN - Style and structure-aware Chinese Calligraphy Generator" accepted by AI for Content Creation Workshop CVPR 2020.</br>
The purpose of this paper is to generate Chinese calligraphy characters.

# Dataset
Chinese calligraphy characters used in this paper can be downloaded from website: http://163.20.160.14/~word/modules/myalbum/.</br>
The crawler script is also provided in this respo.

# Commands

## Set up Conda for M1 Macs
```
conda init
conda activate tf_m1
```

## Train
```
python3 train.py --experiment_dir=experiment0
```

## Inference

```
python infer.py --experiment_dir experiment0 --model_dir experiment0/checkpoint/experiment_0_batch_16 --source_obj experiment0/data/cns_test.obj --embedding_ids 0 --save_dir=outputs
```
