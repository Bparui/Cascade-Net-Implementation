from models.loss import model_psmnet_loss, stereo_psmnet_loss
from models.loss import model_gwcnet_loss
from models.psmnet import PSMNet

__models__ = {
    "gwcnet-c": PSMNet
}

__loss__ = {
    "gwcnet-c": stereo_psmnet_loss
}