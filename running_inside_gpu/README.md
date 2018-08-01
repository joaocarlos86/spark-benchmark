# CUDA

## Variables - For CUDA 9

You will need to set the following variables:

```
export NUMBAPRO_NVVM=/usr/local/cuda-9.0/nvvm/lib64/libnvvm.so
export NUMBAPRO_LIBDEVICE=/usr/local/cuda-9.0/nvvm/libdevice/
```

# How to install CUDA drivers (GCP - CUDA 9):

https://cloud.google.com/compute/docs/gpus/add-gpus#install-gpu-driver

```
#!/bin/bash
echo "Checking for CUDA and installing."
# Check for CUDA and try to install.
if ! dpkg-query -W cuda-9-0; then
  # The 16.04 installer works with 16.10.
  curl -O http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
  dpkg -i ./cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
  apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
  apt-get update
  apt-get install cuda-9-0 -y
fi
# Enable persistence mode
nvidia-smi -pm 1
```

# Monitoring the GPU (while executing something against it)

```
watch nvidia-smi
```
