# Cuda 9.0 installation on Ubuntu 18.04 LTS 
This file contains step by step instructions to install cuda v9.0 and cudnn 7.3.0 in ubuntu 18.04. This is a slightly updated and modified version from Github user [Mahedi-61](https://github.com/Mahedi-61).  The original version may be found [here](https://gist.github.com/Mahedi-61/2a2f1579d4271717d421065168ce6a73)

## Summary of Steps 
```
1.) Verify you hava a cuda capable GPU
2.) Install nvidia cuda toolkit's software dependencies
3.) Download and install the nvidia cuda toolkit and cudnn
4.) Setup environmental variables
5.) Verify the installation
6.) Add symbolic links to gcc-6 and g++-6
```


## 1.) Verify you hava a cuda capable GPU

#### verify gpu
```
lspci | grep -i nvidia
```

## 2.) Install nvidia cuda toolkit's software dependencies

#### install nvidia driver
Note that the driver version and exact steps for this will depend on your GPU.  This command helps you find what drivers will work with your gpu and reccommend one.  Your driver may be different.  We also install nvidia-modprobe, it’s a utility to load NVIDIA kernel modules and crate NVIDIA character device files automatically every time your machine booting up.  You may need to go through additional steps if secure boot is on, however I got mine working by turning secure boot off.  Additionally you will need to reboot.
```
sudo ubuntu-drivers devices
sudo apt-get install nvidia-driver-440 nvidia-modprobe
```

#### install other import packages
```
sudo apt-get install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
```

#### cuda 9 requires gcc>=6, g++>=6, verify that your system meets these requrements.
```
g++ -v
gcc -v
```

## 3.) Download and install the nvidia cuda toolkit and cudnn

#### downoad one of the "runfile (local)" installation packages from cuda toolkit archive 
```
wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run
```

#### make the download file executable
```
chmod +x cuda_9.0.176_384.81_linux.run 
sudo ./cuda_9.0.176_384.81_linux.run --override
```

#### answer following questions while installation begin
```
You are attempting to install on an unsupported configuration. Do you wish to continue? y
Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 384.81? n
Install the CUDA 9.0 Toolkit? y
```

#### install cudnn v7.3.0 for cuda 9
NOTE: in order to download cuDNN you have to be regeistered [here](https://developer.nvidia.com/cudnn)
```
To access the file you will first need to login and agree to terms of use
You will need to manually download version 7.3.0 for Cuda 9.0.
It will appear in your Downloads directory as cudnn-9.0-linux-x64-v7.3.0.29.tgz
```

#### extract cuda directory
```
cd ~/Downloads
tar -xzvf cudnn-9.0-linux-x64-v7.3.0.29.tgz
```

#### copy the following files into the cuda toolkit directory.
```
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-9.0/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-9.0/lib64/
sudo chmod a+r /usr/local/cuda-9.0/lib64/libcudnn*
```

## 4.) Setup your environment variables

#### add cuda-9.0/bin to your path and cuda-9.0/lib64 to your library path
```
echo 'export PATH=/usr/local/cuda-9.0/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

## 5.) Verify the installation

#### reboot to activate changes
```
reboot
```

#### verify installation
```
nvidia-smi
nvcc -V
```

#### your terminal output should look similar to this:
![nvidia-smi](https://user-images.githubusercontent.com/8731829/50403622-ae5e0780-0765-11e9-96c3-cf649dbaeac3.png)


## 6.) Add symbolic links to gcc-6 and g++-6 (only need to do this step if installing tensorflow)

#### Install gcc-6 and g++6, then symlink your cuda compilers to these
Trying to build Tensorflow with the default Ubuntu 18.04 gcc and g++ compilers will give the following error: ```unsupported GNU version! gcc versions later than 6 are not supported!```.  Thus we must link the cuda compiler to gcc-6 and g++6 in preparation for building Tensorflow from sources.

```
sudo apt install gcc-6
sudo apt install g++-6
sudo ln -s /usr/bin/gcc-6 /usr/local/cuda/bin/gcc
sudo ln -s /usr/bin/g++-6 /usr/local/cuda/bin/g++
```

