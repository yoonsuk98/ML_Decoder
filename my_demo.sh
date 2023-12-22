#''' Training '''

#python train.py --data=./dataset/MSCOCO_2014/ --model-name=tresnet_l --image-size=448 --model-info default --gpu-num=0

#python train.py --data=./dataset/down_MSCOCO_2014/ --model-name=tresnet_l --image-size=448 --model-info downsampling --gpu-num=1

#python train.py --data=./dataset/down_MSCOCO_2014/ --model-name=tresnet_l --image-size=448 --model-info upsampling --gpu-num=2

#python train.py --data=./dataset/MSCOCO_2014/ --model-name=tresnet_m --image-size=224 --model-info default

#python train.py --data=./dataset/MSCOCO_2014/ --model-name=tresnet_xl --image-size=640 --model-info default

#python train.py --data=./dataset/MSCOCO_2014/ --model-name=tresnet_l --image-size=448 --model-info train_0816 --gpu-num=1 --lr=2e-4



#''' Validation '''

# tresnet_m, 224x224
#python validate.py --model-name=tresnet_m --model-path=./models_zoo/tresnet_m_COCO_224_84_2.pth --image-size=224 --data=./dataset/MSCOCO_2014/ --gpu-num=0
python validate.py --model-name=tresnet_m --model-path=./models_zoo/tresnet_m_COCO_224_84_2.pth --image-size=224 --data=./dataset/edsr_4_MSCOCO_2014/ --gpu-num=0

# tresnet_l, 448x448, default
#python validate.py --model-name=tresnet_l --model-path=./models_zoo/tresnet_l_COCO__448_90_0.pth --image-size=448 --data=./dataset/MSCOCO_2014/ --gpu-num=0

#python validate.py --model-name=tresnet_l --model-path=./models_zoo/tresnet_l_COCO__448_90_0.pth --image-size=448 --data=./dataset/edsr_4_MSCOCO_2014/ --gpu-num=0

# tresnet_xl, 640x640
#python validate.py --model-name=tresnet_xl --model-path=./models_zoo/tresnet_xl_COCO_640_91_4.pth --image-size=640 --data=./dataset/MSCOCO_2014/ --gpu-num=0
#python validate.py --model-name=tresnet_xl --model-path=./models_zoo/tresnet_xl_COCO_640_91_4.pth --image-size=640 --data=./dataset/edsr_4_MSCOCO_2014/ --gpu-num=0



#''' Inference '''

#python infer.py --model-name=tresnet_l --model-path=./models_zoo/tresnet_l_COCO__448_90_0.pth --pic-path=./pics/knh.jpg --image-size=448
