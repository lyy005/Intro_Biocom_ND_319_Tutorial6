cd Desktop/Intro_Biocom_ND_319_Tutorial6

import pandas as pd
import numpy as np

score=pd.read_table("UWvMSU_1-22-13.txt")
A=np.zeros((len(score),3))
B=pd.DataFrame(A, columns=['time','UW_score','MSU_score'])
B.time=score.time

temp_UW=0
temp_MSU=0

for i in range(0,len(score),1):
    if score.team[i] == "UW":
        temp_UW += score.score[i]
        B.UW_score[i] = temp_UW
    else:
        temp_MSU += score.score[i]
        B.MSU_score[i] = temp_MSU
