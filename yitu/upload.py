#!/usr/bin/python

import urllib
import http.client
import requests
from base64 import b64encode
from requests.auth import HTTPBasicAuth
import json
import os
from random import randrange
from urllib3 import encode_multipart_formdata
import time

host = "http://p125.yitutech.com"
login_suffix = "/auth/login"
create_subject_suffix = "/subject"
upload_photo_suffix = "/subject/photo"
username = "admin"
password = ""
photos_path = "/home/lbhe/Documents/hebei-pujiao/query/"
company_id = 37

def Login():
    payload = {'username':username, 'password':password}
    respon = requests.post(host + login_suffix, payload)
    return respon.cookies

def CreateSubject(subjectType, name, cookie):
    print("subject_type:{}, name:{}".format(subjectType, name))
    payload = {'subject_type':subjectType, 'name': name, "company_id":company_id}
    url = host + create_subject_suffix
    respon = requests.post(url, payload, cookies=cookie)
    return respon.text

def UploadOnePhoto(photoPath, subjectId, cookie):
    url = host + upload_photo_suffix
    payload = {"subject_id": subjectId}
    photoStr = {'photo': open(photoPath, 'rb')}
    respon = requests.post(url, payload, files=photoStr, cookies=cookie)
    print("UploadOnePhoto:{}".format(respon.text))
    return

if __name__ == "__main__":
    cookies = Login()
    print("cookie:{}".format(cookies))

    photos = os.listdir(photos_path)
    flag = True
    for photo in photos:
        try:
            photoName = os.path.splitext(photo)[0]
            photoType = os.path.splitext(photo)[-1]
            #if flag and photoName != "Q270":
            #    continue
            #elif flag:
            #    flag = False

            print("===================Start upload:{}================".format(photo))
            responStr = CreateSubject(randrange(4), photoName, cookies)
            respon = json.loads(responStr)
            subjectId = respon["data"]["id"]
            print("subject_id:{}".format(subjectId))
            print("photo:{}".format(photos_path + photo))
            UploadOnePhoto(photos_path + photo, subjectId, cookies)
        except (requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout, requests.exceptions.ConnectionTimeout) as e:
            cookies = Login()
            print(e)
        except:
            print("Unknown exception.sleeping...")
            time.sleep(60)

    print("Done.")

