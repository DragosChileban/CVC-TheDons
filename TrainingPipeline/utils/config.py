import torch
import numpy
import random
import multiprocessing

# use seed to ensure reproducibility
SEED = 1234
random.seed(SEED)
torch.random.manual_seed(SEED)
numpy.random.seed(SEED)

ROOT = 'C:/Users/Andre/Documents/CVC_Project'

data_config = {
    'metadata_path' : ROOT + '/preprocessed/index.csv',
    'data_path' : ROOT + '/preprocessed',

    'image_size' : (224, 224)
}

train_config = {
    'round_name' : 'exp',
    'debug' : False,
    'lr_finder' : False,

    'batch_size' : 16,
    'num_workers' : multiprocessing.cpu_count(),
    'num_epochs' : 8,
    'lr' : 1e-4,
    'valid_step' : 40
}

results_path = ROOT + '/results/' + train_config['round_name']

results_config = {
    'results_path' : results_path,
    'checkpoints_path' : results_path + '/checkpoints', 
    'logs_path' : results_path + '/logs',
    'tensorboard_path' : results_path + '/tensorboard'
}

config = {**train_config, **data_config}
config = {**config, **results_config}