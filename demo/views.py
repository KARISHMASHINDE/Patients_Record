from django.shortcuts import render
from demo.models import Example
from demo.serializers import HospitalSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView,ListCreateAPIView,ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import filters
from rest_framework.decorators import api_view,permission_classes
from django.core.exceptions import ObjectDoesNotExist
import ast
import json
from django.db import connection
from rest_framework import filters
from rest_framework import generics


#List of hospital_id and mobile number
@api_view(['GET','POST'])
def HospitalList(request,pk=id):        
    if request.method == 'GET':
        data = []
        try:
            obj = Example.objects.all().order_by('-he_id')
            for x in obj:
                div = {
                    "he_hospital_id":x.he_hospital_id,
                    "he_mobile":x.he_mobile
                    }
                data.append({"field": div})
            json_data= json.dumps(data,indent=4, sort_keys=True, default=str)
            res= ast.literal_eval(json_data)
            status_code = status.HTTP_200_OK
            return Response(res, status = status_code)
        except ObjectDoesNotExist:
            data = {"error": " obj does not exist"}
            status_code = status.HTTP_400_BAD_REQUEST  
                       

#To get Patient details from hospital_id
@api_view(['GET','POST'])
def my_custom_sql(request):
        
    if request.method == 'POST':
        mobile=request.GET.get('he_mobile')
        user = Example.objects.filter(he_mobile = mobile)
        for x in user:
            host=x.he_hospital_id
            print(host)
            dist={
                'he_hospital_id':x.he_hospital_id
            }
            #print(dist)
        # json_data= json.dumps(dist,indent=4, sort_keys=True, default=str)
        # res= ast.literal_eval(json_data)

        # return Response({'res':res},status=status.HTTP_200_OK)
        with connection.cursor() as cursor:
            cursor.execute("select pa.PatientID_TreatmentID,pa.insname,pa.admission_date,pa.p_sname,st.status FROM preauth pa LEFT JOIN claim clm ON pa.VNUPatientID=clm.VNUPatientID LEFT JOIN status_track st ON pa.PatientID_TreatmentID=st.PatientID_TreatmentID LEFT JOIN master m ON pa.VNUPatientID=m.VNUPatientID WHERE pa.dischargedate AND pa.HospitalID=%s AND (st.status!='Create Pre-Auth') AND pa.PatientID_TreatmentID = st.PatientID_TreatmentID AND st.srno = (SELECT MAX(srno) FROM `status_track` WHERE PatientID_TreatmentID=pa.PatientID_TreatmentID) GROUP BY pa.PatientID_TreatmentID",(host))
            print(cursor)
            lst=[]
            for row in cursor:
                lst.append(row)
            x=json.dumps({'results': lst})
            res= ast.literal_eval(x)
            return Response(res)
        

                  