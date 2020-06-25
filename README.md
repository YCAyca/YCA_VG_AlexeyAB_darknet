# YCA_VG_AlexeyAB_darknet

This a repo forked from VG_AlexeyAB_darknet(https://github.com/vincentgong7/VG_AlexeyAB_darknet) which is forked from AlexeyAB_darknet(https://github.com/AlexeyAB/darknet) with more features on YOLO batch/test detector. You can download and build the solution after arranging below paths in Visual Studio or do the equivalent steps if you will use another system.

Linker -> General -> Additional Library Dependencies <br>
Linker -> Input -> Additional Dependincies <br>
C/C++ -> General -> Additional Include Directories <br>

General placements and system environment definitions are shown below:

<img src="readme_imgs/paths1.png" alt="" width="30%" /> <br><br> <img src="readme_imgs/paths2.png" alt="" width="30%" />

To build darknet.sln look at Figure1 and to build darknet_no_gpu look at Figure2

<img src="readme_imgs/darknet.png" alt="" width="100%" /> <b><i> Figure 1 </b></i> <br> <br> <br>

<img src="readme_imgs/darknet_no_gpu.png" alt="" width="100%" />  <b><i> Figure 2 </b></i>  <br> <br> <br>

<b>! Dont forget to add .dll files next to the darknet.exe / darknet_no_gpu.exe file after build </b> <br><br>
<img src="readme_imgs/dlls.png" alt="" width="40%" /> <br> <br> <br>

I use VS2019 and opencv_3.2 for this code. You can download opencv version from  https://opencv.org/opencv-3-2/ <br>

This repo contains only the solution and dataset I already used and tested. (darknet.sln for train and darknet_no_gpu.sln for test)
So If you want to use another solution you can easily take it from the base repo I mentioned above.  

# General Usage

To train your custom dataset, use one of these commands after replacing "SATA" folder, "obj.data" file, "yolov3_sata.cfg" file with your custom dataset and files and add pretrained weights(https://pjreddie.com/media/files/darknet53.conv.74   https://drive.google.com/file/d/18v36esoXCh-PsOKwyP2GWrpYDptDY8Zf/view?usp=sharing) to the related folder. 

<i> darknet.exe  detector train data/SATA/obj.data cfg/yolov3_sata.cfg weights/pretrained/darknet53.conv.74 (to train with yolov3 using pretrained weights) </i>

<i> darknet.exe  detector train data/SATA/obj.data cfg/yolov3_sata.cfg weights/pretrained/yolov3-tiny.conv.11 (to train with tiny yolov3 using pretrained weights) </i>

To test your model with a single image use this command after replacing "SATA" folder, "obj.data" file, "image.png" file and sata.weights(use your weights trained with the training command!)

<i> darknet_no_gpu.exe detector test data/SATA/obj.data cfg/yolov3_sata.cfg weights/sata.weights -filename data/SATA/image.png </i>

To test your model with a batch of test image use this command after replacing "SATA" folder, "obj.data" file, "image.png" file and sata.weights(use your weights trained with the training command!)

<i> darknet_no_gpu.exe detector batch data/SATA/obj.data cfg/yolov3-tiny_sata.cfg weights/yolov3-tiny_sata.weights -in_folder data/SATA/in_images/ -out_folder data/SATA/out_images/ -out results/result.txt </i>

<img src="readme_imgs/sata_folder.png" alt="" width="40%" />  <b><i> Inside view of a sample "SATA"(the folder contains your dataset, obj.data obj.name files and output folders) folder. </b></i>  <br> <br> <br>

# Added features

## 1)Multiple Threshold

With this feature, you can make predictions with multiple prediction thresholds at the same time. The performance is x times faster when you use x different threshold. (e.g The prediction duration with 3 threshold with multi threshold feautres is 1.33468e+06 msec and the sum of 3 different threshold one by one is 1.06509e+06 msec x 3. using 500 coco input images)

When you use multi threshold feauture, you obtain different result.txt files and output image folders for each threshold value. You need to give the base folder and file name during running the code via terminal. Not all the folder and file names separately. (e.g When you type out_folder data/COCO/out_images/ the app creates different output image folders via the given threshold values like data/COCO/out_images.25/ data/COCO/out_images.90/ when the given threshold values are 0.25 and 0.90. Likewise when you type -out results/result.txt the app creates different output files via the given threshold values like results/result.25 results/result.90 when the given threshold values are 0.25 and 0.90)

<img src="readme_imgs/coco_results.png" alt="" width="40%" /> <b><i> outputs created in data/COCO folder </b></i> <br> <br> <br>

<img src="build/darknet/x64/data/COCO/out_images.25/000000000001.png" alt="" width="40%" /> <img src="build/darknet/x64/data/COCO/out_images.90/000000000001.png" alt="" width="40%" />

Figure : Different results of prediction with threshold values 0.25 & 0.90

<img src="build/darknet/x64/data/COCO/out_images.25/000000000016.png" alt="" width="40%" /> <img src="build/darknet/x64/data/COCO/out_images.90/000000000016.png" alt="" width="40%" />

Figure : Different results of prediction with threshold values 0.25 & 0.90

In summary, we can say that more detailed objects are detected with the 0.25 threshold. As for 0.90 threshold, the accuracy rate will be higher since the prediction will only detect objects having high probability. You can use the multi-threshold feature for making comparisons with different values and to choose best prediction threshold for your model.

## Usage

darknet_no_gpu.exe detector batch data/COCO/obj.data cfg/yolov3_coco.cfg weights/yolov3_coco.weights -in_folder data/COCO/in_images/ -out_folder data/COCO/out_images/ -out results/result.txt -multi_thresh 3 0.90 0.50 0.25 

## 2) Log Files

I updated the code so it creates a train_log file who includes some information about training process like iteration number, avg loss, etc. You can see the train_log at the same location with .exe file without doing anything. <br>

<img src="readme_imgs/train_log.png" alt="" width="75%" />  <br>

I updated the code so it creates a valid_log file who includes some information about performance of the model like class aP's, mAP, detection time etc. You can use the command below and compare different weights saved at different stages during training.  <br>

<i> darknet.exe detector map data/SATA/obj.data cfg/yolov3_satav2.cfg backup/yolov3_satav2_8000.weights  </i> <br>
<i> darknet.exe detector map data/SATA/obj.data cfg/yolov3_satav2.cfg backup/yolov3_satav2_10000.weights </i> <br>
<i> darknet.exe detector map data/SATA/obj.data cfg/yolov3_satav2.cfg backup/yolov3_satav2_15000.weights </i> <br> <br>

<img src="readme_imgs/valid_log.png" alt="" width="50%" />


## Important Notes

When typing multi threshold values, make sure to give the values in decreasing order. <br>
You can use the command without -out or -out_folder if you dont want to obtain these outputs. <br>
If you dont want to use multi threshold feauture but to determine one threshold value use -thresh xx command. <br>

# Command descriptions of other features from base repos

Use "-save_labels" for saving labels as yolo annotation files <br>




