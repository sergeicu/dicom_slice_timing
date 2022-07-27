"""

Usage: 
    python extract_slice_timing.py dicomfile savedir
    
Output: 
    $savedir/sliceTiming.txt 

e.g. 

$ cat sliceTiming.txt

(0019,1029) FD 1477.49999998\3167.4999999800002\1267.4999999900001\2957.4999999900001\1054.9999999900001\2745\845\2535\632.49999997999998\2322.4999999800002\422.49999998999999\2112.4999999900001\209.99999998999999\1899.9999999900001\0\1690 # 128,16 Unknown Tag & Data


"""

import sys 
import os    
import json

import pydicom


def save_to_text(slicetiming, directory):
    
    # set fixed vars 
    prefix="(0019,1029) FD "
    suffix=" # 128,16 Unknown Tag & Data"
    savename="sliceTiming.txt"
    
    # check dir 
    assert os.path.exists(directory)
    fullsavename = directory + "/" + savename
    
    # convert (join with '\' instead of ',')
    l=[str(i) for i in slicetiming]
    line = '\\'.join(l)
    
    # create full line 
    full_line= prefix + line + suffix 
    
    
    
    # save 
    with open(fullsavename, 'w') as f:
        f.write(full_line)
        
    print(f"File saved to: {fullsavename}")

        
if __name__ == '__main__':
    

    # read input args
    f=sys.argv[1]
    savedir=sys.argv[2]
    assert os.path.exists(f)
    assert os.path.exists(savedir)
    
    # check if dicom or json 
    if f.endswith('.json'):
        
        with open(f) as file:
            data=json.load(file)
        slicetiming=data['SliceTiming']

    else: 
        # get meta 
        meta = pydicom.dcmread(f) 

        # get slice timing 
        tagnum=['0019','1029']
        tag=meta["0x"+tagnum[0], "0x"+tagnum[1]]
        slicetiming = tag.value
        assert slicetiming
        
    # save 
<<<<<<< HEAD
    assert isinstance(slicetiming, list)
    save_to_text(slicetiming, savedir)
=======
    save_to_text(slicetiming, savedir)
>>>>>>> 3cf47f417dac4926f62c49c14d9c49fac42f5a04
