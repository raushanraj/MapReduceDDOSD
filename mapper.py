#/usr/bin/python
import sys

try:
    x=sys.stdin
    for line in x:
        try:
            x=sys.stdin
        except:
            continue
        data=line.strip().split("|")
        http_response_code="200"
        
        http_request_method="GET"
        frame_number="1"
        frame_time="0"
        frame_time_delta="0"
        frame_time_data_displayed="0"
        frame_time_relative="0"
        http_request_uri=" "
        ip_src="000.000.000.000"
        ip_dst="000.000.000.000" 
        try:
            frame_number=data[0].strip()
        except:
            pass
        try:
            frame_time=data[1].strip()
        except:
            pass
        try:
            frame_time_delta=data[2].strip()
        except:
            pass
        try:
            frame_time_data_displayed=data[4].strip()
        except:
            pass
        try:
            frame_time_relative=data[5].strip()
        except:
            pass
        
        try:
            http_request_uri=data[6].strip()
        except:
            pass
        try:
            ip_src=data[7].strip()
        except:
            pass
        try:
            ip_dst=data[8].strip()
        except:
            pass
        try:
            http_response_code=data[9].strip()
        except:
            pass
        try:
            http_request_method=data[10].strip()
        except:
            pass

        
        x=0
        y=1
        source="000.000.000.000"
        destination="000.000.000.000"
        request_count=x
        response_count=x
        packet_count=y

        if ip_src:
            source=ip_src
        if ip_dst:
            destination=ip_dst

        if http_response_code:
            response_count=y
      
        if http_request_method.strip()=="GET":   #filter out non-HTTP request
            request_count=y
            print "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}".format(source,destination,http_request_method,http_response_code,frame_time_relative,request_count,response_count,packet_count)
except:
    pass
