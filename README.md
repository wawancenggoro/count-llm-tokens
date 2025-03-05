# Count LLM Tokens

This repository can be used to count the number of input tokens from an open source models in huggingface.

## Installation

Run the following command to install:

`pip install -r requirements.txt`

## Run the token counter

Run the following command to run the token counter:

`python tokenizer.py --model [MODEL_NAME] --textfile [PATH_TO_TEXT_FILE]`

Example command:

`python tokenizer.py --model 'meta-llama/Llama-3.3-70B-Instruct' --textfile sample-text.txt`

This repository supports counting input tokens from all available models in huggingface. For example, the following models available in Lintasarta Deka LLM are supported:
* meta-llama/Llama-3.3-70B-Instruct
* meta-llama/Llama-3.2-90B-Vision
* Qwen/Qwen2.5-72B-Instruct
* Qwen/Qwen2-VL-72B-Instruct
* deepseek-ai/DeepSeek-R1-Distill-Llama-70B

To access Llama models, you need to login to huggingface via huggingface-cli: https://huggingface.co/docs/huggingface_hub/en/guides/cli
