# T5_Base_API

A FastAPI that translate text from English, French, German and Romanian. It works by taking a user input and translating it to any of the 4 languages specified by the user.

## Links to Model Documentation

[Hugging face](https://huggingface.co/t5-base)

[Github](https://github.com/google-research/text-to-text-transfer-transformer)

[Research Paper](https://jmlr.org/papers/volume21/20-074/20-074.pdf)

[Google Blog](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html)

## Model Features

- Summarize data.
- Compute stsb sentence.
- Find cola sentence.
- Transalte languages.
- Model type: Language Model.
- Supported Languages: English, German, Romanian and French
- License: Apache 2.0
- Pre-trained on [Supervised](https://arxiv.org/abs/1805.12471) and [Unsupervised](https://huggingface.co/datasets/c4) data.

## Hardware Requirements

Model was trained on Google Cloud TPU Pods

#### Memory

- CPU: 8GB
- GPU: 4GB

#### Storage

2GB

## Installatin & Usage

### Local

#### Clone Repo
```
git clone https://github.com/Daquiver1/t5_base_api.git
```

#### Navigate into repo
```
cd t5_base_api
```

#### Setup Poetry
```
pip install poetry
```

#### Install packages
```
poetry install
```

#### Run Application
```
uvicorn main:app --port 80
```

### Docker

Build dockerimage
Run dockerimage
