import os

DEVICE = 'cpu'
IMAGE_SIZE = 224,
MEAN = [0.485, 0.456, 0.406]
STD = [0.229, 0.224, 0.225]
DATA_PATH = "photos"
BASE_PATH = "dataset"
VAL_SPLIT = 0.1
FEATURE_EXTRACTION_BATCH_SIZE = 256
FINETUNE_BATCH_SIZE = 64
PRED_BATCH_SIZE = 4
EPOCHS = 20
LR = 0.001
LR_FINETUNE = 0.0005
WARMUP_PLOT = os.path.join("output", "warmup.png")
FINETUNE_PLOT = os.path.join("output", "finetune.png")
WARMUP_MODEL = os.path.join("output", "warmup_model.pth")
FINETUNE_MODEL = os.path.join("output", "finetune_model.pth")
TRAIN = os.path.join(BASE_PATH, "train")
VAL = os.path.join(BASE_PATH, "val")