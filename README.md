# SCALP (Skin Cancer Classification Platform)

<img src="img/app.png?raw=true">

## Project Description

[Please refer to](PROJECT-DESC.md)

## Requirements

* Python 3.6 (3.5+ should work)
You can install dependencies with: `pip install -r python_requirements.txt`   
`python_requirements_extras.txt` contain additional dependencies, used for CNN training and other procedures.

* PostgresSQL 10+ 
You need to create `bbd` user and database with `bbd` owner. You can specify `bbd` user's password in `config.py` file. 
Database dump will be transfered to psql during initial flask server run.

### Downloading the data

[ISIC Archive Downloader](https://github.com/GalAvineri/ISIC-Archive-Downloader)

Example usage:  
```bash
python ../ISIC-Archive-Downloader/download_archive.py --num-images 1000 -s --images-dir data/ISIC/benign/images --descs-dir data/ISIC/benign/description --seg-dir data/ISIC/benign/segmentation --seg-skill expert --filter benign --p 100
python ../ISIC-Archive-Downloader/download_archive.py --num-images 1000 -s --images-dir data/ISIC/malignant/images --descs-dir data/ISIC/malignant/description --seg-dir data/ISIC/malignant/segmentation --seg-skill expert --filter malignant --p 100
```

By default Data should be located in `src/app/static/ISIC`. If you decide to choose other path, you should change it in both `db/dump.sql` and `config.py` files.

## Trubleshooting

### Model hdf5 file missing

If `models/CNN_binary_v1.h5` size is <100MB you need to run:
```shell
git lfs fetch
git lfs pull
```