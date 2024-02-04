## Telegram bot with Neural Style Transfer (optimization method) 
This repo contains a code of a simple Telegram chatbot based on aiogram library with PyTorch implementation of the original NST (Neural Style Transfer ) paper (:link: [Gatys et al.](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)). 
based on Vgg19 CNN network as a final work fpr "Deep Learning (семестр 1, осень 2023)" course. 



### What is Neural Style Transfer  algorithm?
The algorithm transfers style from one input image (the style image) onto another input image (the content image) using CNN nets (usually VGG-19) and gives a composite, stylized image out which keeps the content from the content image but takes the style from the style image.

<p align="center">
<img src="readme_pics/style_1.webp" width="260"/>
<img src="readme_pics/style_2.webp" width="260"/>
</p>

Vgg19 CNN model principal sheme: 
<p align="center">
<img src="readme_pics/Vgg19.png" width="570"/>
</p>
## Examples

Transfering style gives beautiful artistic results:


### Optimization initialization

Starting with different initialization images: noise (white or gaussian), content and style leads to different results. <br/>
Empirically content image gives the best results as explored in [this research paper](https://arxiv.org/pdf/1602.07188.pdf) also. <br/>
Here you can see results for content, random and style initialization in that order (left to right):



You can also see that with style initialization we had some content from the artwork leaking directly into our output.


In steps 45, 129 and 510 of the  using layers relu1_1, relu2_1, relu3_1, relu4_1 and relu5_1 for style representation.

## Setup

1. Open Anaconda Prompt and navigate into project directory `cd path_to_repo`
2. Run `conda env create` (while in project directory)
3. Run `activate pytorch-nst`


## How to run 
1. create a telegram chatbot using @botfather, generate bot token key
2. set BOT_TOKEN as envirerment variable 
3. run app.py 
users input and results images will be stored in the /data/ folder 

## Acknowledgements



@misc{Gordić2020nst,
  author = {Gordić, Aleksa},
  title = {pytorch-neural-style-transfer},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/gordicaleksa/pytorch-neural-style-transfer}},
}




## Licence

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/gordicaleksa/pytorch-neural-style-transfer/blob/master/LICENCE)