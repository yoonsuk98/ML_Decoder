import os.path

import cv2
from tqdm import tqdm
from glob import glob

scaling_factor=4

org_folder='./dataset/MSCOCO_2014/'
org_train_dir='{}/train2014'.format(org_folder)
org_val_dir='{}/val2014'.format(org_folder)
org_test_dir='{}/test2014'.format(org_folder)

down_folder='./dataset/down_{}_MSCOCO_2014/'.format(scaling_factor)
down_train_dir='{}/train2014'.format(down_folder)
down_val_dir='{}/val2014'.format(down_folder)
down_test_dir='{}/test2014'.format(down_folder)

bicubic_folder='./dataset/bicubic_{}_MSCOCO_2014/'.format(scaling_factor)
bicubic_train_dir='{}/train2014'.format(bicubic_folder)
bicubic_val_dir='{}/val2014'.format(bicubic_folder)
bicubic_test_dir='{}/test2014'.format(bicubic_folder)



patch_size=192
def remove_smaller_patch():
    for i, f in enumerate(glob(org_test_dir + '/*')):
        img=cv2.imread(f,cv2.IMREAD_UNCHANGED)
        img_name=os.path.basename(f)
        if img.shape[0]<patch_size or img.shape[1]<patch_size:
            os.remove(f)
            print("remove {} {}".format(img_name,img.shape))
def remove_1ch_img():

    for i, f in enumerate(glob(org_val_dir + '/*')):
        img=cv2.imread(f,cv2.IMREAD_UNCHANGED)
        img_name=os.path.basename(f)
        if len(img.shape)<3:
            # os.remove(f)
            print("remove {} {}".format(img_name,img.shape))
            img = cv2.imread(f)
            cv2.imwrite(f, img)

    # for i, f in enumerate(glob(org_test_dir + '/*')):
    #     img=cv2.imread(f,cv2.IMREAD_UNCHANGED)
    #     img_name=os.path.basename(f)
    #     if len(img.shape)<3:
    #         # os.remove(f)
    #         print("remove {} {}".format(img_name,img.shape))
    #         img = cv2.imread(f)
    #         cv2.imwrite(f,img)
def downsampling(org_dir,down_dir,folder):
    try:
        os.mkdir(folder)
    except:
        pass

    try:
        os.mkdir(down_dir)
    except:
        pass
    for i,f in enumerate(tqdm(glob(org_dir+'/*'))):
        img_name=os.path.basename(f)
        img=cv2.imread(f)
        down_img=cv2.resize(img,(0,0),fx=float(1.0/scaling_factor),fy=float(1.0/scaling_factor),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('{}/{}'.format(down_dir,img_name),down_img)

def upsampling(org_dir,up_dir,folder):
    try:
        os.mkdir(folder)
    except:
        pass

    try:
        os.mkdir(up_dir)
    except:
        pass

    for i,f in enumerate(tqdm(glob(org_dir+'/*'))):
        img_name=os.path.basename(f)
        img=cv2.imread(f)
        down_img=cv2.resize(img,(0,0),fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('{}/{}'.format(up_dir,img_name),down_img)

resolutions=[]
def print_resolution(org_dir):

    for i, f in enumerate(glob(org_dir + '/*')):
        img=Image.open(f)
        if img.size not in resolutions:resolutions.append(img.size)


if __name__=="__main__":

    # downsampling(org_train_dir,down_train_dir,down_folder)
    downsampling(org_val_dir, down_val_dir,down_folder)
    downsampling(org_test_dir, down_test_dir, down_folder)
    # upsampling(down_train_dir,bicubic_train_dir,bicubic_folder)
    # upsampling(down_val_dir, bicubic_val_dir, bicubic_folder)

    # print_resolution(org_train_dir)
    # print_resolution(org_test_dir)
    # print_resolution(org_val_dir)
    # print(len(resolutions))

    # remove_1ch_img()
    # remove_smaller_patch()