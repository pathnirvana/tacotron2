cd tacotron2/
git submodule init; 
git submodule update

git clone https://github.com/nvidia/apex
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./apex

pip install -r requirements.txt