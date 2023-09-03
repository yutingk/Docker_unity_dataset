import cv2
import os
import glob 
import tqdm

class TermalProcess:
    def __init__(self, datadir = './images/'):
        self.datadir = datadir
        self.bags = sorted(os.listdir(self.datadir))
        print(f'Folder in dataset :', len(self.bags) ,' -----> ', self.bags, '\n')
        self.thermal_image_paths = [[] for _ in self.bags] 
        
        for i, bag in enumerate (self.bags):
            thermal_image_dir = os.path.join(self.datadir, bag, '_thermal_image_compressed')
            thermal_image_pattern = os.path.join(thermal_image_dir, '*.png')
            self.thermal_image_paths[i].extend(glob.glob(thermal_image_pattern))
            print(f'Thermal image number in bag {bag}:', len(self.thermal_image_paths[i]))

    def gray2rgb(self, img=None):
        if img is None:
            print('Image not found')
            return None
        else:
            img_new = cv2.applyColorMap(img, cv2.COLORMAP_JET)
            return img_new
    
    def main(self):
        for j in tqdm.tqdm(range(len(self.bags))):
            for k in tqdm.tqdm(range(len(self.thermal_image_paths[j])), desc=f'Processing {self.bags[j]}', leave=True):
                # # print(self.thermal_image_paths[j][k])
                filename = os.path.basename(self.thermal_image_paths[j][k])
                directory = os.path.join(self.datadir, self.bags[j], '_thermal_image_converted')
                img = cv2.imread(self.thermal_image_paths[j][k], cv2.IMREAD_GRAYSCALE)
                img_new = self.gray2rgb(img)
                # cv2.imshow('img', img_new)
                # cv2.waitKey(1000)
                os.makedirs(directory, exist_ok=True)
                cv2.imwrite(os.path.join(directory, filename), img_new)
        print('\n ===== Finish ===== \n')
        
if __name__ =='__main__':
    termal_processing = TermalProcess(datadir = './images/')
    termal_processing.main()