# Depth Map estimation using Cascade Flow
This project aims to estimate depth maps of image pairs using neural network architectures

![input](https://github.com/Bparui/Cascade-Net-Implementation/blob/main/Imgs/input.png)

![depthmap](https://github.com/Bparui/Cascade-Net-Implementation/blob/main/Imgs/depthmap.png)

## Tasks
* Train the GwcNet-c model using the KITTI 2015 dataset
* Evaluating the trained model

## Training
We are using the [KITTI 2015](https://www.cvlibs.net/datasets/kitti/eval_scene_flow.php?benchmark=stereo). You can also use different datasets like [KITTI 2012](https://www.cvlibs.net/datasets/kitti/eval_stereo_flow.php?benchmark=stereo) , [Scene Flow Datasets](https://lmb.informatik.uni-freiburg.de/resources/datasets/SceneFlowDatasets.en.html)
GPU training
```
export NGPUS=1
export save_results_dir="./checkpoints"
./scripts/kitti15_save.sh $NGPUS $save_results_dir  --ndisps "48,24"  --disp_inter_r "4,1"   --dlossw "0.5,1.0,2.0"  --batch_size 2 --eval_freq 3  --model gwcnet-c
```

## Testing
```
export NGPUS=1
export save_results_dir="./checkpoints"
./scripts/kitti15_save.sh $NGPUS $save_results_dir --loadckpt $CKPT_FILE- --ndisps "48,24"  --disp_inter_r "4,1"   --batch_size 2 --mode test  --model gwcnet-c
```

Here,
* We are using a single GPU as we have constrained with the computation. Therefore ``NGPUS`` is set to ``1``. You can use the code in multi-GPU setting as well.
* Set the ``CKPT_FILE`` as your checkpoint file which you have generated after training.

## Save Depth Maps
```
export save_path="./outputs/predictions"
./scripts/kitti15_save.sh $save_results_dir  --loadckpt $CKPT_FILE --ndisps "48,24"  --disp_inter_r "4,1"   --batch_size 2 --model gwcnet-c
```
