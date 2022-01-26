from tkinter import *
from tkinter import ttk
from turtle import update
import cv2
import numpy as np
from PIL import ImageTk, Image
from image_processing import *
import kociemba

class gui:
    grid = []
    face = []
    sollution = ["U'","U","U2","R"]
    green_str = "FFFFFFFFF"
    white_str = "UUUUUUUUU"
    red_str =   "RRRRRRRRR"
    orange_str = "LLLLLLLLL"
    blue_str = "BBBBBBBBB"
    yellow_str="DDDDDDDDD"
    green_side = [0,0,0,0,0,0,0,0,0]
    yellow_side = [5,5,5,5,5,5,5,5,5]
    blue_side = [4,4,4,4,4,4,4,4,4]
    orange_side = [3,3,3,3,3,3,3,3,3]
    white_side = [1,1,1,1,1,1,1,1,1]
    red_side = [2,2,2,2,2,2,2,2,2]
    solve_status = True


    def get_face_rep_with_arrow(self,face_stat,clockwise = True,Double = False):


        image =  np.zeros((150,150,3), np.uint8)

        for i in range(1,10):
            pos = []
            if i == 1:
                pos = [[6,6],[48,48]] 
            elif i == 4:
                pos = [[6,54],[48,96]]
            elif i == 7:
                pos = [[6,102],[48,144]]
            elif i == 2:
                pos = [[54,6],[96,48]]
            elif i == 5:
                pos = [[54,54],[96,96]]
            elif i == 8:
                pos = [[54,102],[96,144]]
            elif i == 3:
                pos = [[102,6],[144,48]]
            elif i == 6:
                pos = [[102,54],[144,96]]
            elif i == 9:
                pos = [[102,102],[144,144]]

            if(face_stat[i-1] == 0):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(0,200,0),-1)
            elif(face_stat[i-1] == 1):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(255,255,255),-1)
            elif(face_stat[i-1] == 2):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(204,0,0),-1)
            elif(face_stat[i-1] == 3):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(255,153,51),-1)
            elif(face_stat[i-1] == 4):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(90,90,255),-1)
            elif(face_stat[i-1] == 5):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(255,255,51),-1)
        img = np.ones((210,210,3), np.uint8)
        img[:,:,0] = img[:,:,0]*237
        img[:,:,1] = img[:,:,1]*240
        img[:,:,2] = img[:,:,2]*240

        img[29:179,29:179] = image
        if not clockwise:
            img = cv2.arrowedLine(img,(190,17),(10,17),(0,0,0),4)
            if Double:
                img = cv2.arrowedLine(img,(20,190),(200,190),(0,0,0),4)
        elif clockwise:
            img = cv2.arrowedLine(img,(20,17),(200,17),(0,0,0),3)
            if Double:
                img = cv2.arrowedLine(img,(190,190),(10,190),(0,0,0),3)  
            
        img =  Image.fromarray(img)
        img =  ImageTk.PhotoImage(img)
        return img

    def get_face_rep(self,face_stat):


        image =  np.zeros((150,150,3), np.uint8)

        for i in range(1,10):
            pos = []
            if i == 1:
                pos = [[6,6],[48,48]] 
            elif i == 4:
                pos = [[6,54],[48,96]]
            elif i == 7:
                pos = [[6,102],[48,144]]
            elif i == 2:
                pos = [[54,6],[96,48]]
            elif i == 5:
                pos = [[54,54],[96,96]]
            elif i == 8:
                pos = [[54,102],[96,144]]
            elif i == 3:
                pos = [[102,6],[144,48]]
            elif i == 6:
                pos = [[102,54],[144,96]]
            elif i == 9:
                pos = [[102,102],[144,144]]

            if(face_stat[i-1] == 0):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(0,200,0),-1)
            elif(face_stat[i-1] == 1):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(255,255,255),-1)
            elif(face_stat[i-1] == 2):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(204,0,0),-1)
            elif(face_stat[i-1] == 3):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(255,153,51),-1)
            elif(face_stat[i-1] == 4):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(90,90,255),-1)
            elif(face_stat[i-1] == 5):
                image = cv2.rectangle(image,tuple(pos[0]),tuple(pos[1]),(255,255,51),-1)
            
        image =  Image.fromarray(image)
        image =  ImageTk.PhotoImage(image)
        return image
   
    def scan_green(self):
        if(len(self.face) == 9):
            self.green_str,green_side = classifiy_grid(self.face)
            if(green_side[4] == 0):
                self.green_side = green_side
                img0 = self.get_face_rep(self.green_side)
                self.panel0 = Label(self.root, image=img0)
                self.panel0.image = img0
                self.panel0.place(x=370,y=190,in_=self.root)
    
    def scan_white(self):
        if(len(self.face) == 9):
            self.white_str,side = classifiy_grid(self.face)
            if(side[4] == 1):
                self.white_side = side
                img1 = self.get_face_rep(self.white_side)
                self.panel1 = Label(self.root, image=img1)
                self.panel1.image = img1
                self.panel1.place(x=370,y=40,in_=self.root)

    def scan_red(self):
        if(len(self.face) == 9):
            self.red_str,side = classifiy_grid(self.face)
            if(side[4] == 2):
                self.red_side = side
                img2 = self.get_face_rep(self.red_side)
                self.panel2 = Label(self.root, image=img2)
                self.panel2.image = img2
                self.panel2.place(x=520,y=190,in_=self.root)

    def scan_orange(self):
        if(len(self.face) == 9):
            self.orange_str,side = classifiy_grid(self.face)
            if(side[4] == 3):
                self.orange_side = side
                img3 = self.get_face_rep(self.orange_side)
                self.panel3 = Label(self.root, image=img3)
                self.panel3.image = img3
                self.panel3.place(x=220,y=190,in_=self.root)

    def scan_blue(self):
        if(len(self.face) == 9):
            self.blue_str,side = classifiy_grid(self.face)
            if(side[4] == 4):
                self.blue_side = side
                img4 = self.get_face_rep(self.blue_side)
                self.panel4 = Label(self.root, image=img4)
                self.panel4.image = img4
                self.panel4.place(x=70,y=190,in_=self.root)

    def scan_yellow(self):
        if(len(self.face) == 9):
            self.yellow_str,side = classifiy_grid(self.face)
            if(side[4] == 5):
                self.yellow_side = side
                img5 = self.get_face_rep(self.yellow_side)
                self.panel5 = Label(self.root, image=img5)
                self.panel5.image = img5
                self.panel5.place(x=370,y=340,in_=self.root)

    def update_grid_status(self):

        img0 = self.get_face_rep(self.green_side)
        self.panel0 = Label(self.root, image=img0)
        self.panel0.image = img0
        self.panel0.place(x=370,y=190,in_=self.root)

        img1 = self.get_face_rep(self.white_side)
        self.panel1 = Label(self.root, image=img1)
        self.panel1.image = img1
        self.panel1.place(x=370,y=40,in_=self.root)

        img2 = self.get_face_rep(self.red_side)
        self.panel2 = Label(self.root, image=img2)
        self.panel2.image = img2
        self.panel2.place(x=520,y=190,in_=self.root)

        img3 = self.get_face_rep(self.orange_side)
        self.panel3 = Label(self.root, image=img3)
        self.panel3.image = img3
        self.panel3.place(x=220,y=190,in_=self.root)

        img4 = self.get_face_rep(self.blue_side)
        self.panel4 = Label(self.root, image=img4)
        self.panel4.image = img4
        self.panel4.place(x=70,y=190,in_=self.root)

        img5 = self.get_face_rep(self.yellow_side)
        self.panel5 = Label(self.root, image=img5)
        self.panel5.image = img5
        self.panel5.place(x=370,y=340,in_=self.root)
    
    def solve_reset(self):
        self.solve_status = False
        self.grid = []
        self.face = []
        self.sollution = []
        self.green_str = "FFFFFFFFF"
        self.white_str = "UUUUUUUUU"
        self.red_str =   "RRRRRRRRR"
        self.orange_str = "LLLLLLLLL"
        self.blue_str = "BBBBBBBBB"
        self.yellow_str="DDDDDDDDD"
        self.green_side = [0,0,0,0,0,0,0,0,0]
        self.yellow_side = [5,5,5,5,5,5,5,5,5]
        self.blue_side = [4,4,4,4,4,4,4,4,4]
        self.orange_side = [3,3,3,3,3,3,3,3,3]
        self.white_side = [1,1,1,1,1,1,1,1,1]
        self.red_side = [2,2,2,2,2,2,2,2,2]
        self.update_grid_status()
        self.panel.destroy()

    def step(self):
        self.update_solve()
        try:
            self.sollution.pop(0)
        except:
            pass
        if self.sollution == [] or self.solve_status == False:
            self.next.destroy()
            self.panel.destroy()
   
    def update_solve(self):
        try:
            self.panel.destroy()
        except:
            pass
        if self.solve_status and self.sollution != []:
            
            if self.sollution[0] == "U":
                img = self.get_face_rep_with_arrow(self.white_side,True,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[0],self.green_side[1],self.green_side[2]]
                self.green_side[0],self.green_side[1],self.green_side[2] = self.red_side[0],self.red_side[1],self.red_side[2]
                self.red_side[0],self.red_side[1],self.red_side[2] =self.blue_side[0],self.blue_side[1],self.blue_side[2]
                self.blue_side[0],self.blue_side[1],self.blue_side[2] = self.orange_side[0],self.orange_side[1],self.orange_side[2]
                self.orange_side[0],self.orange_side[1],self.orange_side[2] = temp1[0],temp1[1],temp1[2]
                temp2 = self.white_side
                self.white_side = [temp2[6],temp2[3],temp2[0],temp2[7],temp2[4],temp2[1],temp2[8],temp2[5],temp2[2]]
                self.update_grid_status()
            
            elif self.sollution[0] == "U2":
                img = self.get_face_rep_with_arrow(self.white_side,True,True)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[0],self.green_side[1],self.green_side[2]]
                temp2 = [self.red_side[0],self.red_side[1],self.red_side[2]]
                self.green_side[0],self.green_side[1],self.green_side[2] = self.blue_side[0],self.blue_side[1],self.blue_side[2]
                self.red_side[0],self.red_side[1],self.red_side[2] = self.orange_side[0],self.orange_side[1],self.orange_side[2]
                self.blue_side[0],self.blue_side[1],self.blue_side[2] = temp1[0],temp1[1],temp1[2]
                self.orange_side[0],self.orange_side[1],self.orange_side[2] = temp2[0],temp2[1],temp2[2]
                temp3 = self.white_side
                self.white_side = [temp3[8],temp3[7],temp3[6],temp3[5],temp3[4],temp3[3],temp3[2],temp3[1],temp3[0]]
                self.update_grid_status()
            
            elif self.sollution[0] == "U'":
                img = self.get_face_rep_with_arrow(self.white_side,False,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)            
                temp1 = [self.green_side[0],self.green_side[1],self.green_side[2]]
                self.green_side[0],self.green_side[1],self.green_side[2] = self.orange_side[0],self.orange_side[1],self.orange_side[2]
                self.orange_side[0],self.orange_side[1],self.orange_side[2] =self.blue_side[0],self.blue_side[1],self.blue_side[2]
                self.blue_side[0],self.blue_side[1],self.blue_side[2] = self.red_side[0],self.red_side[1],self.red_side[2]
                self.red_side[0],self.red_side[1],self.red_side[2] = temp1[0],temp1[1],temp1[2]
                temp2 = self.white_side
                self.white_side = [temp2[2],temp2[5],temp2[8],temp2[1],temp2[4],temp2[7],temp2[0],temp2[3],temp2[6]]
                self.update_grid_status()
            




            elif self.sollution[0] == "R":
                img = self.get_face_rep_with_arrow(self.red_side,True,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[2],self.green_side[5],self.green_side[8]]
                self.green_side[2],self.green_side[5],self.green_side[8] = self.yellow_side[2],self.yellow_side[5],self.yellow_side[8]
                self.yellow_side[2],self.yellow_side[5],self.yellow_side[8] = self.blue_side[6],self.blue_side[3],self.blue_side[0]
                self.blue_side[6],self.blue_side[3],self.blue_side[0] = self.white_side[2],self.white_side[5],self.white_side[8]
                self.white_side[2],self.white_side[5],self.white_side[8] = temp1[0],temp1[1],temp1[2]
                temp2 = self.red_side
                self.red_side = [temp2[6],temp2[3],temp2[0],temp2[7],temp2[4],temp2[1],temp2[8],temp2[5],temp2[2]]
                self.update_grid_status()

            elif self.sollution[0] == "R2":
                img = self.get_face_rep_with_arrow(self.red_side,True,True)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[2],self.green_side[5],self.green_side[8]]
                temp2 = [self.white_side[2],self.white_side[5],self.white_side[8]]
                self.green_side[2],self.green_side[5],self.green_side[8] = self.blue_side[6],self.blue_side[3],self.blue_side[0]
                self.white_side[2],self.white_side[5],self.white_side[8] = self.yellow_side[2],self.yellow_side[5],self.yellow_side[8]
                self.blue_side[6],self.blue_side[3],self.blue_side[0] = temp1[0],temp1[1],temp1[2]
                self.yellow_side[2],self.yellow_side[5],self.yellow_side[8] = temp2[0],temp2[1],temp2[2]
                temp3 = self.red_side
                self.red_side = [temp3[8],temp3[7],temp3[6],temp3[5],temp3[4],temp3[3],temp3[2],temp3[1],temp3[0]]
                self.update_grid_status()

            elif self.sollution[0] == "R'":
                img = self.get_face_rep_with_arrow(self.red_side,False,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root) 

                temp1 = [self.green_side[2],self.green_side[5],self.green_side[8]]
                self.green_side[2],self.green_side[5],self.green_side[8] = self.white_side[2],self.white_side[5],self.white_side[8]
                self.white_side[2],self.white_side[5],self.white_side[8] = self.blue_side[6],self.blue_side[3],self.blue_side[0]
                self.blue_side[6],self.blue_side[3],self.blue_side[0] = self.yellow_side[2],self.yellow_side[5],self.yellow_side[8]
                self.yellow_side[2],self.yellow_side[5],self.yellow_side[8] = temp1[0],temp1[1],temp1[2]
                temp2 = self.red_side
                self.red_side = [temp2[2],temp2[5],temp2[8],temp2[1],temp2[4],temp2[7],temp2[0],temp2[3],temp2[6]]
                self.update_grid_status()




            elif self.sollution[0] == "L":
                img = self.get_face_rep_with_arrow(self.orange_side,True,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[0],self.green_side[3],self.green_side[6]]
                self.green_side[0],self.green_side[3],self.green_side[6] = self.white_side[0],self.white_side[3],self.white_side[6]
                self.white_side[0],self.white_side[3],self.white_side[6] = self.blue_side[8],self.blue_side[5],self.blue_side[2]
                self.blue_side[8],self.blue_side[5],self.blue_side[2] = self.yellow_side[0],self.yellow_side[3],self.yellow_side[6]
                self.yellow_side[0],self.yellow_side[3],self.yellow_side[6] = temp1[0],temp1[1],temp1[2]
                temp2 = self.orange_side
                self.orange_side = [temp2[6],temp2[3],temp2[0],temp2[7],temp2[4],temp2[1],temp2[8],temp2[5],temp2[2]]
                self.update_grid_status()

            elif self.sollution[0] == "L2":
                img = self.get_face_rep_with_arrow(self.orange_side,True,True)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[0],self.green_side[3],self.green_side[6]]
                temp2 = [self.white_side[0],self.white_side[3],self.white_side[6]]
                self.green_side[0],self.green_side[3],self.green_side[6] = self.blue_side[8],self.blue_side[5],self.blue_side[2]
                self.white_side[0],self.white_side[3],self.white_side[6] =  self.yellow_side[0],self.yellow_side[3],self.yellow_side[6]
                self.blue_side[8],self.blue_side[5],self.blue_side[2] = temp1[0],temp1[1],temp1[2]
                self.yellow_side[0],self.yellow_side[3],self.yellow_side[6] = temp2[0],temp2[1],temp2[2]
                temp3 = self.orange_side
                self.orange_side = [temp3[8],temp3[7],temp3[6],temp3[5],temp3[4],temp3[3],temp3[2],temp3[1],temp3[0]]
                self.update_grid_status()

            elif self.sollution[0] == "L'":
                img = self.get_face_rep_with_arrow(self.orange_side,False,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[0],self.green_side[3],self.green_side[6]]
                self.green_side[0],self.green_side[3],self.green_side[6] = self.yellow_side[0],self.yellow_side[3],self.yellow_side[6]
                self.yellow_side[0],self.yellow_side[3],self.yellow_side[6] = self.blue_side[8],self.blue_side[5],self.blue_side[2]
                self.blue_side[8],self.blue_side[5],self.blue_side[2] = self.white_side[0],self.white_side[3],self.white_side[6]
                self.white_side[0],self.white_side[3],self.white_side[6] = temp1[0],temp1[1],temp1[2]
                temp2 = self.orange_side
                self.orange_side =  [temp2[2],temp2[5],temp2[8],temp2[1],temp2[4],temp2[7],temp2[0],temp2[3],temp2[6]]
                self.update_grid_status()




            elif self.sollution[0] == "B":
                img = self.get_face_rep_with_arrow(self.blue_side,True,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.white_side[2],self.white_side[1],self.white_side[0]]
                self.white_side[2],self.white_side[1],self.white_side[0] = self.red_side[8],self.red_side[5],self.red_side[2]
                self.red_side[8],self.red_side[5],self.red_side[2] = self.yellow_side[6],self.yellow_side[7],self.yellow_side[8]
                self.yellow_side[6],self.yellow_side[7],self.yellow_side[8] = self.orange_side[0],self.orange_side[3],self.orange_side[6]
                self.orange_side[0],self.orange_side[3],self.orange_side[6] = temp1[0],temp1[1],temp1[2]
                temp2 = self.blue_side
                self.blue_side = [temp2[6],temp2[3],temp2[0],temp2[7],temp2[4],temp2[1],temp2[8],temp2[5],temp2[2]]
                self.update_grid_status()
            elif self.sollution[0] == "B2":
                img = self.get_face_rep_with_arrow(self.blue_side,True,True)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.white_side[2],self.white_side[1],self.white_side[0]]
                temp2 = [self.red_side[8],self.red_side[5],self.red_side[2]]
                self.white_side[2],self.white_side[1],self.white_side[0] = self.yellow_side[6],self.yellow_side[7],self.yellow_side[8]
                self.red_side[8],self.red_side[5],self.red_side[2] =  self.orange_side[0],self.orange_side[3],self.orange_side[6]
                self.yellow_side[6],self.yellow_side[7],self.yellow_side[8] = temp1[0],temp1[1],temp1[2]
                self.orange_side[0],self.orange_side[3],self.orange_side[6] = temp2[0],temp2[1],temp2[2]
                temp3 = self.blue_side
                self.blue_side = [temp3[8],temp3[7],temp3[6],temp3[5],temp3[4],temp3[3],temp3[2],temp3[1],temp3[0]]
                self.update_grid_status()

            elif self.sollution[0] == "B'":
                img = self.get_face_rep_with_arrow(self.blue_side,False,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)                

                temp1 = [self.white_side[2],self.white_side[1],self.white_side[0]]
                self.white_side[2],self.white_side[1],self.white_side[0] = self.orange_side[0],self.orange_side[3],self.orange_side[6]
                self.orange_side[0],self.orange_side[3],self.orange_side[6] = self.yellow_side[6],self.yellow_side[7],self.yellow_side[8]
                self.yellow_side[6],self.yellow_side[7],self.yellow_side[8] = self.red_side[8],self.red_side[5],self.red_side[2]
                self.red_side[8],self.red_side[5],self.red_side[2] = temp1[0],temp1[1],temp1[2]
                temp2 = self.blue_side
                self.blue_side =  [temp2[2],temp2[5],temp2[8],temp2[1],temp2[4],temp2[7],temp2[0],temp2[3],temp2[6]]
                self.update_grid_status()




            elif self.sollution[0] == "F":
                img = self.get_face_rep_with_arrow(self.green_side,True,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.white_side[6],self.white_side[7],self.white_side[8]]
                self.white_side[6],self.white_side[7],self.white_side[8] = self.orange_side[8],self.orange_side[5],self.orange_side[2]
                self.orange_side[8],self.orange_side[5],self.orange_side[2] = self.yellow_side[2],self.yellow_side[1],self.yellow_side[0]
                self.yellow_side[2],self.yellow_side[1],self.yellow_side[0] = self.red_side[0],self.red_side[3],self.red_side[6]
                self.red_side[0],self.red_side[3],self.red_side[6] = temp1[0],temp1[1],temp1[2]
                temp2 = self.green_side
                self.green_side = [temp2[6],temp2[3],temp2[0],temp2[7],temp2[4],temp2[1],temp2[8],temp2[5],temp2[2]]
                self.update_grid_status()

            elif self.sollution[0] == "F2":
                img = self.get_face_rep_with_arrow(self.green_side,True,True)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.white_side[6],self.white_side[7],self.white_side[8]]
                temp2 = [self.red_side[0],self.red_side[3],self.red_side[6]]
                self.white_side[6],self.white_side[7],self.white_side[8] = self.yellow_side[2],self.yellow_side[1],self.yellow_side[0]
                self.red_side[0],self.red_side[3],self.red_side[6] =  self.orange_side[8],self.orange_side[5],self.orange_side[2]
                self.yellow_side[2],self.yellow_side[1],self.yellow_side[0] = temp1[0],temp1[1],temp1[2]
                self.orange_side[8],self.orange_side[5],self.orange_side[2] = temp2[0],temp2[1],temp2[2]
                temp3 = self.green_side
                self.green_side = [temp3[8],temp3[7],temp3[6],temp3[5],temp3[4],temp3[3],temp3[2],temp3[1],temp3[0]]
                self.update_grid_status()

            elif self.sollution[0] == "F'":
                img = self.get_face_rep_with_arrow(self.green_side,False,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.white_side[6],self.white_side[7],self.white_side[8]]
                self.white_side[6],self.white_side[7],self.white_side[8] = self.red_side[0],self.red_side[3],self.red_side[6]
                self.red_side[0],self.red_side[3],self.red_side[6] = self.yellow_side[2],self.yellow_side[1],self.yellow_side[0]
                self.yellow_side[2],self.yellow_side[1],self.yellow_side[0] = self.orange_side[8],self.orange_side[5],self.orange_side[2]
                self.orange_side[8],self.orange_side[5],self.orange_side[2] = temp1[0],temp1[1],temp1[2]
                temp2 = self.green_side
                self.green_side =  [temp2[2],temp2[5],temp2[8],temp2[1],temp2[4],temp2[7],temp2[0],temp2[3],temp2[6]]
                self.update_grid_status()





            elif self.sollution[0] == "D":
                img = self.get_face_rep_with_arrow(self.yellow_side,True,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[6],self.green_side[7],self.green_side[8]]
                self.green_side[6],self.green_side[7],self.green_side[8] = self.orange_side[6],self.orange_side[7],self.orange_side[8]
                self.orange_side[6],self.orange_side[7],self.orange_side[8] = self.blue_side[6],self.blue_side[7],self.blue_side[8]
                self.blue_side[6],self.blue_side[7],self.blue_side[8] = self.red_side[6],self.red_side[7],self.red_side[8]
                self.red_side[6],self.red_side[7],self.red_side[8] = temp1[0],temp1[1],temp1[2]
                temp2 = self.yellow_side
                self.yellow_side = [temp2[6],temp2[3],temp2[0],temp2[7],temp2[4],temp2[1],temp2[8],temp2[5],temp2[2]]
                self.update_grid_status()

            elif self.sollution[0] == "D2":
                img = self.get_face_rep_with_arrow(self.yellow_side,True,True)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[6],self.green_side[7],self.green_side[8]]
                temp2 = [self.red_side[6],self.red_side[7],self.red_side[8]]
                self.green_side[6],self.green_side[7],self.green_side[8] = self.blue_side[6],self.blue_side[7],self.blue_side[8]
                self.red_side[6],self.red_side[7],self.red_side[8] = self.orange_side[6],self.orange_side[7],self.orange_side[8]
                self.blue_side[6],self.blue_side[7],self.blue_side[8] = temp1[0],temp1[1],temp1[2]
                self.orange_side[6],self.orange_side[7],self.orange_side[8] = temp2[0],temp2[1],temp2[2]
                temp3 = self.yellow_side
                self.yellow_side = [temp3[8],temp3[7],temp3[6],temp3[5],temp3[4],temp3[3],temp3[2],temp3[1],temp3[0]]
                self.update_grid_status()

            elif self.sollution[0] == "D'":
                img = self.get_face_rep_with_arrow(self.yellow_side,False,False)
                self.panel = Label(self.root, image=img)
                self.panel.image = img
                self.panel.place(x=1000,y=450,in_=self.root)

                temp1 = [self.green_side[6],self.green_side[7],self.green_side[8]]
                self.green_side[6],self.green_side[7],self.green_side[8] = self.red_side[6],self.red_side[7],self.red_side[8]
                self.red_side[6],self.red_side[7],self.red_side[8] = self.blue_side[6],self.blue_side[7],self.blue_side[8]
                self.blue_side[6],self.blue_side[7],self.blue_side[8] = self.orange_side[6],self.orange_side[7],self.orange_side[8]
                self.orange_side[6],self.orange_side[7],self.orange_side[8] = temp1[0],temp1[1],temp1[2]
                temp2 = self.yellow_side
                self.yellow_side = [temp2[2],temp2[5],temp2[8],temp2[1],temp2[4],temp2[7],temp2[0],temp2[3],temp2[6]]
                self.update_grid_status()

        else:
            try:
                self.panel.destroy()
            except:
                pass

    def solve_cube(self):
        str = self.white_str + self.red_str + self.green_str + self.yellow_str + self.orange_str + self.blue_str
        self.sollution = kociemba.solve(str)
        self.sollution = self.sollution.split(" ")
        self.solve_status = True
        print(self.sollution)
        self.next = Button(self.root, text ="step",width=15,height=1, command = self.step,bg="#DCDCDC")
        self.next.place(x=770,y=510,in_=self.root)

    def __init__(self):
        self.root = Tk()
        self.root.title("Rubik's Cube Solver")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.cap = cv2.VideoCapture(0)
        self.app = Frame(self.root, bg="white")
        self.app.place(x=738,y=20,in_=self.root)
        self.lmain = Label(self.app)
        self.lmain.grid()

        self.zone1 = LabelFrame(self.root,text="Cube Status")
        self.zone1.config(font=("Arial", 13))
        self.zone1.place(height=500,width=700,x = 20,y = 20)

        self.zone2 = LabelFrame(self.root,text="Update Status")
        self.zone2.config(font=("Arial", 13))
        self.zone2.place(height=70,width=900,x = 10,y = 600)

        self.update_grid_status()

        scan_green = Button(self.root, text ="scan Green",width=15,height=1, command = self.scan_green,bg="#DCDCDC")
        scan_green.place(x=20,y=627,in_=self.root)

        scan_white = Button(self.root, text ="scan White",width=15,height=1, command = self.scan_white,bg="#DCDCDC")
        scan_white.place(x=170,y=627,in_=self.root)

        scan_red = Button(self.root, text ="scan Red",width=15,height=1, command = self.scan_red,bg="#DCDCDC")
        scan_red.place(x=320,y=627,in_=self.root)

        scan_orange = Button(self.root, text ="scan Orange",width=15,height=1, command = self.scan_orange,bg="#DCDCDC")
        scan_orange.place(x=470,y=627,in_=self.root)
        
        scan_blue = Button(self.root, text ="scan Blue",width=15,height=1, command = self.scan_blue,bg="#DCDCDC")
        scan_blue.place(x=620,y=627,in_=self.root)

        scan_yellow = Button(self.root, text ="scan Yellow",width=15,height=1, command = self.scan_yellow,bg="#DCDCDC")
        scan_yellow.place(x=770,y=627,in_=self.root)

        solve = Button(self.root, text ="Solve",width=15,height=1, command = self.solve_cube,bg="#79FF6B")
        solve.place(x=770,y=430,in_=self.root)

        reset = Button(self.root, text ="Reset",width=15,height=1, command = self.solve_reset,bg="#FF0000")
        reset.place(x=770,y=470,in_=self.root)

        # self.next = Button(self.root, text ="step",width=15,height=1, command = self.step,bg="#DCDCDC")
        # self.next.place(x=770,y=510,in_=self.root)

    def video_stream(self):
        _,self.frame1 = self.cap.read()
        frame,self.grid = detect_grid(self.frame1)
        if len(self.grid) == 9:
            self.face = self.grid
        frame  = cv2.resize(frame,(512,384))
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(30, self.video_stream)
    
    def on_closing(self):
        self.cap.release()
        self.root.destroy()
   
    def run(self):
        self.video_stream()
        self.root.mainloop()
      
x = gui()
x.run()