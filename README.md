# Projekt-BBD

## Requirements

* Python 3.6 (`pip install -r python_requirements.txt`)
* Docker

## ISIC dataset
<img src="sample_images/ISIC_0000000.jpg?raw=true" height="300">
<img src="sample_images/ISIC_0000010.jpg?raw=true" height="300">
<img src="sample_images/ISIC_0000020.jpg?raw=true" height="300">

[ISIC Gallery](https://www.isic-archive.com/#!/topWithHeader/onlyHeaderTop/gallery)  

[ISIC Archive Downloader](https://github.com/GalAvineri/ISIC-Archive-Downloader)

Usage:  
```bash
python ../ISIC-Archive-Downloader/download_archive.py --num-images 1000 -s --images-dir data/ISIC/benign/images --descs-dir data/ISIC/benign/description --seg-dir data/ISIC/benign/segmentation --seg-skill expert --filter benign --p 100
python ../ISIC-Archive-Downloader/download_archive.py --num-images 1000 -s --images-dir data/ISIC/malignant/images --descs-dir data/ISIC/malignant/description --seg-dir data/ISIC/malignant/segmentation --seg-skill expert --filter malignant --p 100
```

## Docker container

1. Build container `docker build -t Projekt-BBD .`
2. 
