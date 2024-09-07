import numpy as np
import pandas as pd
import math
def Weight_Adjustment(Erorr_Rsulat,Erorr_Theta,datex,datey):
    New_Theta = []
    for i in range(4):
        now = Erorr_Theta[i] + (datey - Erorr_Rsulat) * datex[0,i]
        New_Theta.append(now)
        #print(f'new theta\n\t{i} - {New_Theta[i]}')
    
    return New_Theta
def Training_My_Perceptron(dateX,theta,dateY,PrintInfo = False):
    
    Attempts_Counter = 0
    Tabel_Title = '|bias|Input1|Input2|Input3|W bias|W1|W2|W3|PeOut|output|'
    Stop_Training = False
    Expected_Output =[]
    while True:
        Attempts_Counter +=1
        if PrintInfo:
            print(f'\t\t|----( Try Number \"{Attempts_Counter}\" )----|')
            print(Tabel_Title)
        for i in range(dateX.shape[0]):
            Temp = 0
            for j in range(dateX.shape[1]):
                Temp += dateX[i,j] * theta[j]
            if Temp >= 0:
                Expected_Output.append(1)
            else:
                Expected_Output.append(0)
            if PrintInfo:
                print(f'|{dateX[i,0]}|{dateX[i,1]}|{dateX[i,2]}|{dateX[i,3]}|{theta[0]}|{theta[1]}|{theta[2]}|{theta[3]}|{Expected_Output[i]}|{dateY[i]}')
                print('-'*len(Tabel_Title))
        if PrintInfo:
            print('-'*len(Tabel_Title)+'\n\n')
        
        for i in range(dateX.shape[0]):
            if Expected_Output[i] != dateY[i]:
                theta = Weight_Adjustment(Erorr_Rsulat=Expected_Output[i],Erorr_Theta=theta,datex=dateX[i],datey=dateY[i])
                Stop_Training = False
                Expected_Output.clear()
                break
            Stop_Training = True
        if Stop_Training :
            if PrintInfo:
                print("End of Training")
            break
    return theta

def UseOfThe_MyPerceptron(Theta_Trained):
    Requests_Number = int(input("How Many Requests Do We Have To Process ???\n\tEnter Here:"))
    Input_User_Date = [1]
    Message_List = ['How much is your total salary per year?\n\tEnter Here:',
                    'How much do you belong?\n\tEnter Here:',
                    'How many hours do you work per week?\n\tEnter Here:',
                    'If you can take the loan\n',
                    'Unfortunately you cannot take the loan.\n']
    for i in range(Requests_Number):
        TmpeUseing = 0
        Input_User_Date.clear()
        Input_User_Date.append(1)
        print(f'\n----------------------------------------------------\nRequests No .{i+1}\n---------------------------------------\n')
        
        Input_User_Date.append(int(input(Message_List[2])))
        Input_User_Date.append(int(input(Message_List[1])))
        Input_User_Date.append(int(input(Message_List[0])))
        for j in range(4):
            TmpeUseing += Input_User_Date[j]*Theta_Trained[j]
        if TmpeUseing >= 0:
            print(Message_List[3])
        else:
            print(Message_List[4])
    
    




date = pd.read_csv('./Perceptron_Data.csv')

Date_X = date.iloc[:,:-1]
Date_Y = date.iloc[:,-1:]
Date_X.insert(0 , 'Ones' , 1)

Date_Input = np.matrix(Date_X.values)
print(f"==>> Date_Input: {Date_Input}")
Date_Output = Date_Y.values
Date_Output = Date_Output[:,0]
Theta = [0.1,-0.1,0.2,-0.1]

Theta_Update = Training_My_Perceptron(Date_Input,Theta,Date_Output,False)

UseOfThe_MyPerceptron(Theta_Update)