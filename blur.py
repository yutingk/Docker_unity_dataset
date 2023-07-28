import cv2
import numpy as np
import os
import glob 
import shutil

class blur():
    def __init__(self, datadir = './dataset'):
        self.datadir = datadir
        self.scenes = sorted(os.listdir(self.datadir))
        print(f'Folder in dataset : \n {self.scenes} \n')
        self.scenes_len = len(self.scenes)
        
        self.datadir_blur1, self.datadir_blur2, self.datadir_blur3= [], [], []

    def copy_folder(self):
        #creat folder
        for i in range(self.scenes_len): 
            self.datadir_blur1.append(self.scenes[i] + '_blur1')
            self.datadir_blur2.append(self.scenes[i] + '_blur2')
            self.datadir_blur3.append(self.scenes[i] + '_blur3')
            
            #copy file from dataset to blur dataset
            if (not(os.path.isdir(self.datadir + '/'+ self.datadir_blur1[i]))):
                shutil.copytree(self.datadir + '/' + self.scenes[i], './dataset/' + self.datadir_blur1[i])
                shutil.copytree(self.datadir + '/' + self.scenes[i], './dataset/' + self.datadir_blur2[i])
                shutil.copytree(self.datadir + '/' + self.scenes[i], './dataset/' + self.datadir_blur3[i])
            else:
                print('Folder already exist')
                pass
        print(f'Folder in blur dataset : \n {self.datadir_blur1} \n')    
        
    def read_img(self):
        blur_list = []
        
        for num in range(1, 4): 
            datadir_blur = getattr(self, f"datadir_blur{num}")          
            for k in range(len(datadir_blur)):
                folder = str(datadir_blur[k])
                blur_list.append(folder)
        
        print(blur_list)
        
        blur_level = 0
        for scene in blur_list:    
            blur_level += 1
            images_path_jpg = sorted(glob.glob(os.path.join(self.datadir + '/' +scene +'/*.main.jpg')))

            print(f'Number of images in {scene}= {len(images_path_jpg)}\n')
            for i in range (len(images_path_jpg)):
                blur_img = self.motion_blur_type(img = images_path_jpg[i], size = blur_level+1)
                path_parts = images_path_jpg[i].split("/")
                filename = path_parts[-1]
                filename_without_extension = filename.split(".")[0]
                number = filename_without_extension
                new_file = self.datadir + '/' + scene + '/' + str(number) + '.main.jpg'
                cv2.imwrite(new_file, blur_img)
        print('Done') 
        
    def motion_blur_type(self, img, size = 1):
        # #blur the image
        img = cv2.imread(img)
        # generating the kernel
        kernel_motion_blur = np.zeros((size, size))
        kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
        kernel_motion_blur = kernel_motion_blur / size

        # applying the kernel to the input image
        output = cv2.filter2D(img, -1, kernel_motion_blur)
        return output           
    
    def main(self):
        self.copy_folder()
        self.read_img()
        
        
if __name__ == '__main__':
    blur = blur(datadir = './dataset')
    blur.main()
