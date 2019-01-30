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

## Running API

1. Install dependencies `pip install -r python_requirements.txt` (It's recommended to create separate enviorment, for example with conda python distribution: `conda create -n api python=3.6` and activate it with `source activate api` or `conda activate api`).
2. Run Flask app which provides REST API `python python/api.py`.

## h5py error while loading model during object init.

```shell
Traceback (most recent call last):
  File "python/api.py", line 22, in <module>
    predictor = Predictor(config=config)
  File "/home/szymon/Projects/Projekt-BBD/python/ml.py", line 31, in __init__
    self.model = keras.models.load_model(config.model_path)
  File "/home/szymon/miniconda3/envs/bbd/lib/python3.6/site-packages/keras/engine/saving.py", line 417, in load_model
    f = h5dict(filepath, 'r')
  File "/home/szymon/miniconda3/envs/bbd/lib/python3.6/site-packages/keras/utils/io_utils.py", line 186, in __init__
    self.data = h5py.File(path, mode=mode)
  File "/home/szymon/miniconda3/envs/bbd/lib/python3.6/site-packages/h5py/_hl/files.py", line 394, in __init__
    swmr=swmr)
  File "/home/szymon/miniconda3/envs/bbd/lib/python3.6/site-packages/h5py/_hl/files.py", line 170, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5f.pyx", line 85, in h5py.h5f.open
OSError: Unable to open file (file signature not found)
```

If `models/CNN_binary_v1.h5` size <100MB you need to run:
```shell
git lfs fetch
git lfs pull
```