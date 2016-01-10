#!/usr/bin/python

import sys



oldsrc=None
olddest=None
req_count=1
res_count=0
timeinterval=5.0
threshold=8
unbalanced_ratio=0.65
oldtime=0.0
blocked_stack=[]
try:
    x=sys.stdin
    for line in x:
        try:
            x=sys.stdin
        except:
            continue
        data= line.strip().split("|")
        source="000.000.000.000"
        destination="000.000.000.000"
        method="GET"
        http_response_code="200"
        frame_time_relative="0.0"
        request_count="0"
        response_count="0"
        packet_count="0"

        try:
            source=data[0].strip()
        except:
            pass

        try:
            destination=data[1].strip()
        except:
            pass
        try:
            method=data[2].strip()
        except:
            pass
        try:
            http_response_code=data[3].strip()
        except:
            pass

        try:
            frame_time_relative=float(data[4].strip())
        except:
            pass
        try:
            request_count=int(data[5].strip())
        except:
            pass
        try:
            response_count=int(data[6].strip())
        except:
            pass

        try:
            packet_count=data[7].strip()
        except:
            pass
        if olddest and oldsrc:
            if olddest!=str(destination.strip()) or oldsrc!=str(source.strip()):
                if float(res_count/req_count)<=unbalanced_ratio and res_count>threshold:
                    if (oldsrc,olddest) not in blocked_stack:
                         print oldsrc,"\t",olddest,"\t",req_count
                         blocked_stack.append((oldsrc,olddest))
                req_count=1
                res_count=0
                oldtime=0.0
            else:
                if float(frame_time_relative)-oldtime<timeinterval:
                    req_count=req_count+1
                    res_count=res_count+1
                else:
                    if float(res_count/req_count)<=unbalanced_ratio and res_count>3:
                        if (oldsrc,olddest) not in blocked_stack:
                            print oldsrc,"\t",olddest,"\t",req_count
                            blocked_stack.append((oldsrc,olddest))
                    oldtime=0.0
                    req_count=1
                    res_count=0
            
        oldtime=float(frame_time_relative)
            

        olddest=str(destination.strip())
        oldsrc=str(source.strip())
            



    if olddest and oldsrc:
        if olddest!=destination or oldsrc!=source:
            if unbalanced_ratio <= float(res_count/req_count) <=0 and req_count > threshold:
                print oldsrc,"\t",olddest,"\t",req_count
except:
    pass
