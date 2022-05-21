from generate_att import generate_Att_from_img,generate_Att_from_img_center_single,generate_Att_from_img_threebythree,generate_Att_from_img_in_out_single,generate_Att_from_img_outin4,generate_Att_from_img_leftright,generate_Att_from_img_updown
from reasoning.general_template_panel_and_ind import general_template,types_template
from reasoning.place_template_panel_and_ind import place_template,place_types_template
from reasoning.check_sort import check_panel_sort,check_panel_predict,check_place_predict,check_types_match,check_types_place
from reasoning.Other_features_for_given_type import Type_specific_lists
from reasoning.draw_fig import pre_draw,pre_draw_centersingle,pre_draw_outin,pre_draw_outin4,pre_draw_simple,pre_draw_outin4_simple
from reasoning.draw_img import draw_pic,draw_pic_centersingle,draw_pic_threebythree,draw_pic_outin,draw_pic_outin4,draw_pic_leftright,draw_pic_updown
from cnn import ConvNet
import torch
import numpy as np
from torchvision import transforms
model_cnn = ConvNet(7)
state_dict_cnn=torch.load('log/model49.ckpt', map_location='cpu')
model_cnn.load_state_dict(state_dict_cnn)
model_cnn=model_cnn.eval()

def solve_and_draw(data,draw):
    Answer=0
    img=transforms.functional.to_tensor(data[0,:,:])
    problem_set=torch.argmax(model_cnn.forward(img.reshape(1,1,160,160))).detach().numpy()

    Candidate=np.ones(8)
    if problem_set==0:
        Type,Color,Size,Angle=generate_Att_from_img_center_single(data)
        Angle_predict,Angle_template=general_template(Angle[0:8])
        Color_predict,Color_template=general_template(Color[0:8])
        Size_predict,Size_template=general_template(Size[0:8])
        Type_predict,Type_template=general_template(Type[0:8])

        if Type_template==2:
            Type_template=-1
            Type_predict=-1 #no arithmetic for categorical variables
        if Size_predict>=8:
            Size_template=-1
            Size_predict=-1

        for predict,panel in zip([Color_predict,Size_predict,Type_predict],[Color,Size,Type]):
            Candidate=check_panel_predict(predict,panel,Candidate)
    #     for predict,panel in zip([Color_predict,Size_predict,Type_predict],[Color,Size,Type]):
    #         Candidate=check_panel_predict(predict,panel,Candidate)

        Answer=np.argmax(Candidate)

        if draw==1:
            att=pre_draw_centersingle(Type_predict,Color_predict,Size_predict,Angle_predict)
            img=draw_pic_centersingle(att)

    if problem_set==1:
        Exist,Type,Color,Size,Angle,Exist_panel,Angle_panel,Color_panel,Size_panel,Type_panel=generate_Att_from_img(data)
        Exist_predict,Exist_template=general_template(Exist_panel[0:8])
        Angle_predict,Angle_template=general_template(Angle_panel[0:8])
        Color_predict,Color_template=general_template(Color_panel[0:8])
        Size_predict,Size_template=general_template(Size_panel[0:8])
        Type_predict,Type_template=general_template(Type_panel[0:8])
        Place_predict,Place_template=place_template(Exist[:,:,0:8],problem_set)

        if Type_template==2:
            Type_template=-1
            Type_predict=-1 #no arithmetic for categorical variables
        if Size_predict>=8:
            Size_template=-1
            Size_predict=-1

        for predict,panel in zip([Exist_predict,Color_predict,Size_predict,Type_predict],[Exist_panel,Color_panel,Size_panel,Type_panel]):
            Candidate=check_panel_predict(predict,panel,Candidate)

        Candidate=check_place_predict(Place_template,Exist,Place_predict,Candidate)

        for item,Att in zip([Color_template,Size_template,Type_template],[Color,Size,Type]):
            if item==-1:
                Candidate=check_panel_sort(Att,Candidate)

        if Type_template==-1:
            Angle_types,Color_types,Size_types,Place_types,Type_types,Candidate=Type_specific_lists(Type,Angle,Color,Size,Candidate)
            Angle_types_predict,Angle_types_template=types_template(Angle_types[:,0:8])
            Color_types_predict,Color_types_template=types_template(Color_types[:,0:8])
            Size_types_predict,Size_types_template=types_template(Size_types[:,0:8])
            Place_types_predict,Place_types_template=place_types_template(Place_types[:,0:8,:,:],problem_set)
            
            if Size_types_predict.any()>=8:
                Size_types_template=-1
                Size_types_predict=-1*np.ones(Size_types_predict.shape)

            for predict,types in zip([Color_types_predict,Size_types_predict,Place_types_predict],[Color_types,Size_types,Place_types]):
                Candidate=check_types_match(predict,types,Candidate)

            Candidate=check_types_place(Place_types_predict,Place_types,Candidate)

        Answer=np.argmax(Candidate)

        if draw==1:
            if Type_template==-1:
                att,Place=pre_draw(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Type_types,Color_types_predict,Size_types_predict,Angle_types_predict,Place_predict,Place_types_predict)
            else:
                att,Place=pre_draw_simple(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Place_predict,problem_set)
            img=draw_pic(att,Place)

    if problem_set==2:
        Exist,Type,Color,Size,Angle,Exist_panel,Angle_panel,Color_panel,Size_panel,Type_panel=generate_Att_from_img_threebythree(data)
        Exist_predict,Exist_template=general_template(Exist_panel[0:8])
        Angle_predict,Angle_template=general_template(Angle_panel[0:8])
        Color_predict,Color_template=general_template(Color_panel[0:8])
        Size_predict,Size_template=general_template(Size_panel[0:8])
        Type_predict,Type_template=general_template(Type_panel[0:8])
        Place_predict,Place_template=place_template(Exist[:,:,0:8],problem_set)

        if Type_template==2:
            Type_template=-1
            Type_predict=-1 #no arithmetic for categorical variables
        if Size_predict>=8:
            Size_template=-1
            Size_predict=-1

        for predict,panel in zip([Exist_predict,Color_predict,Size_predict,Type_predict],[Exist_panel,Color_panel,Size_panel,Type_panel]):
            Candidate=check_panel_predict(predict,panel,Candidate)

        Candidate=check_place_predict(Place_template,Exist,Place_predict,Candidate)

        for item,Att in zip([Color_template,Size_template,Type_template],[Color,Size,Type]):
            if item==-1:
                Candidate=check_panel_sort(Att,Candidate)

        if Type_template==-1:
            Angle_types,Color_types,Size_types,Place_types,Type_types,Candidate=Type_specific_lists(Type,Angle,Color,Size,Candidate)
            Angle_types_predict,Angle_types_template=types_template(Angle_types[:,0:8])
            Color_types_predict,Color_types_template=types_template(Color_types[:,0:8])
            Size_types_predict,Size_types_template=types_template(Size_types[:,0:8])
            Place_types_predict,Place_types_template=place_types_template(Place_types[:,0:8,:,:],problem_set)
            
            if Size_types_predict.any()>=8:
                Size_types_template=-1
                Size_types_predict=-1*np.ones(Size_types_predict.shape)

            for predict,types in zip([Color_types_predict,Size_types_predict,Place_types_predict],[Color_types,Size_types,Place_types]):
                Candidate=check_types_match(predict,types,Candidate)

            Candidate=check_types_place(Place_types_predict,Place_types,Candidate)

        Answer=np.argmax(Candidate)

        if draw==1:
            if Type_template==-1:
                att,Place=pre_draw(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Type_types,Color_types_predict,Size_types_predict,Angle_types_predict,Place_predict,Place_types_predict)
            else:
                att,Place=pre_draw_simple(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Place_predict,problem_set)
            img=draw_pic_threebythree(att,Place)

    if problem_set==3:
        Type,Color,Size,Angle,Type_out,Color_out,Size_out,Angle_out=generate_Att_from_img_in_out_single(data)
        Angle_predict,Angle_template=general_template(Angle[0:8])
        Color_predict,Color_template=general_template(Color[0:8])
        Size_predict,Size_template=general_template(Size[0:8])
        Type_predict,Type_template=general_template(Type[0:8])

        if Type_template==2:
            Type_template=-1
            Type_predict=-1 #no arithmetic for categorical variables
        if Size_predict>=8:
            Size_template=-1
            Size_predict=-1

        for predict,panel in zip([Color_predict,Size_predict,Type_predict],[Color,Size,Type]):
            Candidate=check_panel_predict(predict,panel,Candidate)
    #     for predict,panel in zip([Color_predict,Size_predict,Type_predict],[Color,Size,Type]):
    #         Candidate=check_panel_predict(predict,panel,Candidate)
        Angle_out_predict,Angle_out_template=general_template(Angle_out[0:8])
        Color_out_predict,Color_out_template=general_template(Color_out[0:8])
        Size_out_predict,Size_out_template=general_template(Size_out[0:8])
        Type_out_predict,Type_out_template=general_template(Type_out[0:8])

        if Type_out_template==2:
            Type_out_template=-1
            Type_out_predict=-1 #no arithmetic for categorical variables
        if Size_out_predict>=8:
            Size_out_template=-1
            Size_out_predict=-1

        for predict,panel in zip([Color_out_predict,Size_out_predict,Type_out_predict],[Color_out,Size_out,Type_out]):
            Candidate=check_panel_predict(predict,panel,Candidate)

        Answer=np.argmax(Candidate)

        if draw==1:
            att,att_out=pre_draw_outin(Type_predict,Color_predict,Size_predict,Angle_predict,Type_out_predict,Color_out_predict,Size_out_predict,Angle_out_predict)
            img=draw_pic_outin(att,att_out)

    if problem_set==4:
        Exist,Type,Color,Size,Angle,Exist_panel,Angle_panel,Color_panel,Size_panel,Type_panel,Type_out,Color_out,Size_out,Angle_out=generate_Att_from_img_outin4(data)
        Exist_predict,Exist_template=general_template(Exist_panel[0:8])
        Angle_predict,Angle_template=general_template(Angle_panel[0:8])
        Color_predict,Color_template=general_template(Color_panel[0:8])
        Size_predict,Size_template=general_template(Size_panel[0:8])
        Type_predict,Type_template=general_template(Type_panel[0:8])
        Place_predict,Place_template=place_template(Exist[:,:,0:8],problem_set)

        if Type_template==2:
            Type_template=-1
            Type_predict=-1 #no arithmetic for categorical variables
        if Size_predict>=8:
            Size_template=-1
            Size_predict=-1

        for predict,panel in zip([Exist_predict,Color_predict,Size_predict,Type_predict],[Exist_panel,Color_panel,Size_panel,Type_panel]):
            Candidate=check_panel_predict(predict,panel,Candidate)

        Candidate=check_place_predict(Place_template,Exist,Place_predict,Candidate)

        for item,Att in zip([Color_template,Size_template,Type_template],[Color,Size,Type]):
            if item==-1:
                Candidate=check_panel_sort(Att,Candidate)

        if Type_template==-1:
            Angle_types,Color_types,Size_types,Place_types,Type_types,Candidate=Type_specific_lists(Type,Angle,Color,Size,Candidate)
            Angle_types_predict,Angle_types_template=types_template(Angle_types[:,0:8])
            Color_types_predict,Color_types_template=types_template(Color_types[:,0:8])
            Size_types_predict,Size_types_template=types_template(Size_types[:,0:8])
            Place_types_predict,Place_types_template=place_types_template(Place_types[:,0:8,:,:],problem_set)
            
            if Size_types_predict.any()>=8:
                Size_types_template=-1
                Size_types_predict=-1*np.ones(Size_types_predict.shape)

            for predict,types in zip([Color_types_predict,Size_types_predict,Place_types_predict],[Color_types,Size_types,Place_types]):
                Candidate=check_types_match(predict,types,Candidate)

            Candidate=check_types_place(Place_types_predict,Place_types,Candidate)

        Angle_out_predict,Angle_out_template=general_template(Angle_out[0:8])
        Color_out_predict,Color_out_template=general_template(Color_out[0:8])
        Size_out_predict,Size_out_template=general_template(Size_out[0:8])
        Type_out_predict,Type_out_template=general_template(Type_out[0:8])

        if Type_out_template==2:
            Type_out_template=-1
            Type_out_predict=-1 #no arithmetic for categorical variables
        if Size_out_predict>=8:
            Size_out_template=-1
            Size_out_predict=-1

        for predict,panel in zip([Color_out_predict,Size_out_predict,Type_out_predict],[Color_out,Size_out,Type_out]):
            Candidate=check_panel_predict(predict,panel,Candidate)

        Answer=np.argmax(Candidate)
        if draw==1:
            if Type_template==-1:
                att,Place,att_out=pre_draw_outin4(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Type_types,Color_types_predict,Size_types_predict,Angle_types_predict,Place_predict,Place_types_predict,Type_out_predict,Color_out_predict,Size_out_predict,Angle_out_predict)
            else:
                att,Place,att_out=pre_draw_outin4_simple(Exist_predict,Type_predict,Color_predict,Size_predict,Angle_predict,Type_template,Place_predict,Type_out_predict,Color_out_predict,Size_out_predict,Angle_out_predict,problem_set)
            img=draw_pic_outin4(att,Place,att_out)

    if problem_set==5:
        Type_1,Color_1,Size_1,Angle_1,Type_2,Color_2,Size_2,Angle_2=generate_Att_from_img_leftright(data)
        Angle_predict,Angle_template=general_template(Angle_1[0:8])
        Color_predict,Color_template=general_template(Color_1[0:8])
        Size_predict,Size_template=general_template(Size_1[0:8])
        Type_predict,Type_template=general_template(Type_1[0:8])

        if Type_template==2:
            Type_template=-1
            Type_predict=-1 #no arithmetic for categorical variables
        if Size_predict>=8:
            Size_template=-1
            Size_predict=-1

        for predict,panel in zip([Color_predict,Size_predict,Type_predict],[Color_1,Size_1,Type_1]):
            Candidate=check_panel_predict(predict,panel,Candidate)
    #     for predict,panel in zip([Color_predict,Size_predict,Type_predict],[Color,Size,Type]):
    #         Candidate=check_panel_predict(predict,panel,Candidate)
        Angle_2_predict,Angle_2_template=general_template(Angle_2[0:8])
        Color_2_predict,Color_2_template=general_template(Color_2[0:8])
        Size_2_predict,Size_2_template=general_template(Size_2[0:8])
        Type_2_predict,Type_2_template=general_template(Type_2[0:8])

        if Type_2_template==2:
            Type_2_template=-1
            Type_2_predict=-1 #no arithmetic for categorical variables
        if Size_2_predict>=8:
            Size_2_template=-1
            Size_2_predict=-1

        for predict,panel in zip([Color_2_predict,Size_2_predict,Type_2_predict],[Color_2,Size_2,Type_2]):
            Candidate=check_panel_predict(predict,panel,Candidate)

        Answer=np.argmax(Candidate)
        if draw==1:
            att,att_2=pre_draw_outin(Type_predict,Color_predict,Size_predict,Angle_predict,Type_2_predict,Color_2_predict,Size_2_predict,Angle_2_predict)
            img=draw_pic_leftright(att,att_2)

    if problem_set==6:
        Type_1,Color_1,Size_1,Angle_1,Type_2,Color_2,Size_2,Angle_2=generate_Att_from_img_updown(data)
        Angle_predict,Angle_template=general_template(Angle_1[0:8])
        Color_predict,Color_template=general_template(Color_1[0:8])
        Size_predict,Size_template=general_template(Size_1[0:8])
        Type_predict,Type_template=general_template(Type_1[0:8])

        if Type_template==2:
            Type_template=-1
            Type_predict=-1 #no arithmetic for categorical variables
        if Size_predict>=8:
            Size_template=-1
            Size_predict=-1

        for predict,panel in zip([Color_predict,Size_predict,Type_predict],[Color_1,Size_1,Type_1]):
            Candidate=check_panel_predict(predict,panel,Candidate)
    #     for predict,panel in zip([Color_predict,Size_predict,Type_predict],[Color,Size,Type]):
    #         Candidate=check_panel_predict(predict,panel,Candidate)
        Angle_2_predict,Angle_2_template=general_template(Angle_2[0:8])
        Color_2_predict,Color_2_template=general_template(Color_2[0:8])
        Size_2_predict,Size_2_template=general_template(Size_2[0:8])
        Type_2_predict,Type_2_template=general_template(Type_2[0:8])

        if Type_2_template==2:
            Type_2_template=-1
            Type_2_predict=-1 #no arithmetic for categorical variables
        if Size_predict>=8:
            Size_2_template=-1
            Size_2_predict=-1

        for predict,panel in zip([Color_2_predict,Size_2_predict,Type_2_predict],[Color_2,Size_2,Type_2]):
            Candidate=check_panel_predict(predict,panel,Candidate)

        Answer=np.argmax(Candidate)
        if draw==1:
            att,att_2=pre_draw_outin(Type_predict,Color_predict,Size_predict,Angle_predict,Type_2_predict,Color_2_predict,Size_2_predict,Angle_2_predict)
            img=draw_pic_updown(att,att_2)
    return Answer
        