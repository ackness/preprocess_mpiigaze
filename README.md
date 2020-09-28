# MPIIGaze Preprocessing

## Info

First you should download dataset from [MPIIGaze](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild).

[Official MPIIGaze Normalize Code](http://datasets.d2.mpi-inf.mpg.de//MPIIGaze/data_normalization_code.zip) were written by matlab code and return `Gray` eye regions images.

These repo is rewritten by python according to the matlab source code and return `RGB` images.

## Usage

```bash
python preprocess_mpii.py -p "path/to/mpii/Original"

for example:
python preprocess_mpii.py -p ./MPIIGaze/Data/Original/
```

You will get a dict which seems like this:

```
{'p02/day07/0001.jpg': 
    {'right_eye': 
        {'img': array([[[ 89,  80,  95],
                   [ 95,  86, 100],
                   [100,  87,  97],
                   ...,
                   [ 73,  45,  46],
                   [ 84,  51,  54],
                   [ 91,  58,  62]],
           
                  [[104,  93, 107],
                   [109,  96, 110],
                   [111,  96, 108],
                   ...,
                   [ 81,  51,  53],
                   [ 92,  58,  62],
                   [100,  65,  69]],
           
                  [[117, 103, 113],
                   [120, 105, 116],
                   [120, 105, 115],
                   ...,
                   [ 92,  57,  61],
                   [ 98,  61,  66],
                   [105,  67,  72]],
           
                  ...,
           
                  [[184, 179, 190],
                   [182, 178, 187],
                   [179, 174, 185],
                   ...,
                   [106,  82,  85],
                   [113,  90,  93],
                   [120,  97, 100]],
           
                  [[183, 176, 189],
                   [184, 177, 189],
                   [185, 177, 190],
                   ...,
                   [116,  92,  96],
                   [124, 100, 103],
                   [130, 107, 110]],
           
                  [[187, 178, 193],
                   [188, 179, 192],
                   [189, 180, 192],
                   ...,
                   [129, 107, 109],
                   [137, 116, 117],
                   [142, 121, 123]]], dtype=uint8),
       'headpose': array([0.25371083, 0.13010662]),
       'gaze': array([-0.03550274,  0.08322771])},

    ...
}
```