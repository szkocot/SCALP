# SCALP (Skin Cancer Classification Platform)

This project is an university assignment task.

## Goal

The goal of this project was to create a prototype platform for skin cancer classification.

## Introduction

Skin cancer is one of most common type of cancer. Early and precise diagnosys can help make this disease less seviere and to treat it easier.

## ISIC Dataset

> The International Skin Imaging Collaboration: Melanoma Project is an academia and industry partnership designed to facilitate the application of digital skin imaging to help reduce melanoma mortality. 
> -- <cite>[ISIC website][1]</cite>

<img src="https://github.com/szkocot/SCALP/blob/master/img/ISIC_0000000.jpg?raw=true" height="100">
<img src="https://github.com/szkocot/SCALP/blob/master/img/ISIC_0000010.jpg?raw=true" height="100">
<img src="https://github.com/szkocot/SCALP/blob/master/img/ISIC_0000020.jpg?raw=true" height="100">

It contains thousands of skin images, annotated by professionals as well as non-profesional volunteers.

Labels are following:
* malignant   
* benign   
* unknown   

It's download can be much easier, by using ISIC Archive Downloader[2]

## Functionalities

* Melanoma malignancy prediction using Convolutional Neural Network classifier   
* Visual representation of masked image and prediciton pie chart   
* Access and filtering ISIC database   


## Malignancy classification

Melanoma malignancy can be classified with over 70% accurancy.   
This value may seem to be low, but you need to consider, that image and expert label quality is not that good.   
Masking and resizin of melanoma images helped to improve results by few percent.   

<img src="https://github.com/szkocot/SCALP/blob/master/img/acc.png?raw=true">

References:   
[1]:https://isdis.org/isic-project/   
[2]:https://github.com/GalAvineri/ISIC-Archive-Downloader   