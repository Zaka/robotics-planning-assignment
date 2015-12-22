# robotics-planning-assignment

## Installation

- Python packages to install
matplotlib
numpy
pil (python image library)
pil.imagetk

  Must be installed with root priviledges, maybe you have to install
  pip first.
  
  pip install pypng 

## Images are preprocessed using to get rid of alpha channel and have
the color represented by one float32 instead of an RGB array:

convert -flatten -background white -alpha remove orig.png dst.png 

