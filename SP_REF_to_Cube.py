import scipy.io
import os
import numpy as np
import h5py
import tifffile as tiff

#input folder
Folder = r"C://Windows Folder with SP_REF Files"

#get the file paths of SPREF
Filepaths = list(map(lambda X: os.path.join(Folder,X),os.listdir(Folder)))

for i in range(len(Filepaths)):
    try:
        f = scipy.io.loadmat(Filepaths[i]) #possibly not functional at the moment
        X = np.array(f.get("Composite_Image"))
    except:
        f = h5py.File(Filepaths[i], 'r')
        X = np.array(f.get("Composite_Image"))
    if i == 0:
        im = np.zeros([X.shape[0],X.shape[1],len(Filepaths)]) 
    im[:,:,i] = X
    
#saves as 32 bit single precision float
tiff.imwrite(Folder+"/.DataCube.tiff",im.astype(np.float32),planarconfig='contig')
