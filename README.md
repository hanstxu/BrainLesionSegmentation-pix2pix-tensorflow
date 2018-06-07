# BrainLesionSegmentation-pix2pix-tensorflow

Used Tensorflow implementation of [pix2pix](https://phillipi.github.io/pix2pix/) by Isola et al to generate brain lesion segmentations of brain MRI scans.

Images that we used for our project are included in the repository for sample
purposes.

## Setup

### Prerequisites
- Tensorflow 1.4.1
- bash
- Python3

### Recommended
- Linux with Tensorflow GPU edition + cuDNN

## Getting Started

### Converting MRI Images to PNG Formats

Use `mritopng.py` to convert an entire folder of DICOM images to PNG.

```
python mritopng.py -f <src_folder> <dst_folder>
```

### Creating Datasets from Existing Images

To combine images from two directories (i.e. paired images in each directory
have the same names):

```
./create_dataset.sh <First-Directory-of-Images> <Second-Directory-of-Images> 
```

Example:

```
./create_dataset.sh images/FeaturesPNG images/LabelsPNG
```

### Divide Datasets into Training/Test Sets

To put 80% of the dataset into the training set
and 20% of the dataset into the test set:

```
./split.sh
```

### Create the Training Model/Test the Model ###

To create a training model as well as test the resulting model:

```
./run.sh
```

Note that this may take awhile (i.e. at least 10 hours), depending on how big
your dataset is.

### Get Statistics on the Accuracy of the Model ###

To get the average, min, and max DICE score:

```
python compare.py
```

## Citation
If you use this code for your research, please cite the paper this code is based
on: <a href="https://arxiv.org/pdf/1611.07004v1.pdf">Image-to-Image Translation
Using Conditional Adversarial Networks</a>:

```
@article{pix2pix2016,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  journal={arxiv},
  year={2016}
}
```

## Acknowledgments
This is a port of [pix2pix](https://github.com/phillipi/pix2pix) from Torch to
Tensorflow.  It also contains colorspace conversion code ported from Torch.
Thanks to the Tensorflow team for making such a quality library!  And special
thanks to Phillip Isola for answering my questions about the pix2pix code.
