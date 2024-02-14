from django.shortcuts import render
import csv
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_bank(request):
    with open('C:\\Users\\gotlu\\OneDrive\\Desktop\\Django projects\\kavya\\Scripts\\CSV\\app\\bank.csv','r')as FO:
        IOD = csv.reader(FO)
        for i in IOD:
            bn = i[0].strip()
            BO = Bank(bank_name = bn)
            BO.save()
    return HttpResponse('Bank data is inserted successfully')


def insert_branch(request):
    with open('C:\\Users\\gotlu\\OneDrive\\Desktop\\Django projects\\kavya\\Scripts\\CSV\\app\\branch1.csv','r')as FO:
        IOD = csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn = i[0]
            BO = Bank.objects.filter(bank_name= bn)
            if BO:
                ifsc = i[1]
                br = i[2]
                add = i[3]
                con = i[4]
                ci = i[5]
                dis = i[6]
                sta = i[7]

                BRO = Branch(bank_name = BO[0],IFSC = ifsc,branch=br,address=add,contact=con,city=ci,district=dis,state=sta)
                BRO.save()
        
    return HttpResponse('Branch data is inserted Successfully')