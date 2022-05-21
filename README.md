# Toward_Explainable_Intelligent_Reasoning_on_RAVEN_Datasets

Human relies on generalizable hierarchical perception and abstract reasoning abilities to solve complicated Raven's Progressive Matrices. Here we build explainable algorithms to approximate this human reasoning process. Our model implements human-like transferable object perception and domain-general rule abstraction through Explainable-VAE (E-VAE) feature extraction model and cognitive-map reasoning back end. The supervised E-VAE module extracts explainable features and represents individual objects with generalizable dimensions. We apply these dimensions to understand the entities abstractively and interact with objects' images. The cognitive-map back-end module forms cognitive maps for abstract rules in RAVEN problems. Different problems activate different cognitive maps and make predictions accordingly. The model generates answers and possible images for RAVEN problems in a human-like explainable way with high accuracy. It transfers well to unseen domains and has the potential to adapt to real-life situations. We intend to make the model more biologically possible in the future.

## Explainable-VAE
You can use the following code to train the Explainable VAE model

`$ cd sVAE`

`$ python run_others.py -c configs/bbvae_bvae.yaml`

You can change the address of the images and labels in dataset_others.py

You can adjust the size of the training dataset by running the following line (50% of the original dataset).

`$python run_numbers.py -c configs/bbvae_bvae.yaml -p 0.5`

More information for the original beta-VAE model locate at https://github.com/AntixK/PyTorch-VAE

After training the E-VAE model, please put the checkpoint files in the CMs/log folder.

## Cognitive Map
You can use `relation_trim.py`, `run_position.py`, and `run_position_3.py` to train attribute relationship cognitive maps, two-by-two position relationship cognitive maps, and three-by-three relationship cognitive maps. They take the output of the Explainable-VAE module as input and learn abstract relationships.

## Full Model Testing
The code for solving a single RAVEN problem is available in solve_all.py, The function takes two inputs: the RAVEN problems' images, and a “draw” index indicating whether you want to generate a figure for the problem.

You can use the following code to test the full model:

`$ cd CMs`

`$python run_raven.py`

`$python run_iraven.py`

`$python run_fair.py`

`$python run_all.py`

The first three files run on the RAVEN, I-RAVEN, and RAVEN-fair datasets. run_all.py runs with artificially designed cognitive maps.
By default, run_all.py does not generate images. You can change:

`solve_and_draw(data,0)`

into 

`solve_and_draw(data,1)`

to produce possible answer images for the problems.







