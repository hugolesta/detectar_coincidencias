import os
import glob
import re

path = 'D:/Python/detectar_coincidencias/1'
extension = '*.txt'

def corta(fileobj):
    data = []
    for line in fileobj.readlines():
        if '----- Original message -----' in line:
            break
        elif '------ This is a copy of the message, including all the headers. ------' in line:
            break
        elif 'This is a MIME-encapsulated message.' in line:
            break
        elif 'This is a multi-part message in MIME format.' in line:
            break
        elif '<html>' in line:
            break
        else:
            data.append(line.strip())
    return data

def comparar_linea(file1, file2):
    data1 = corta(file1)
    data2 = corta(file2)
    same = set(data1).intersection(data2)
    discard = ['\n','MIME-Version: 1.0','Return-Path: <>','DKIM-Signature: v=1; a=rsa-sha1; c=relaxed/relaxed;','Precedence: bulk','Content-Type: multipart/alternative;','Content-Transfer-Encoding: quoted-printable','Content-Type: text/html;','Content-Transfer-Encoding: base64','Content-Type: text/plain; charset=UTF-8','padding-top:0px; font-family: Arial, Helvetica, sans-serif; color: =','Auto-Submitted: auto-replied','message-id:date:content-transfer-encoding;','X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;','DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;','Subject: Delivery Status Notification (Failure)','d=1e100.net; s=20161025;','From: Mail Delivery Subsystem <mailer-daemon@googlemail.com>','h=x-gm-message-state:mime-version:from:to:auto-submitted:subject','h=mime-version:from:to:auto-submitted:subject:references:in-reply-to','Subject: Mail delivery failed: returning message to sender','This message was created automatically by mail delivery software.','recipients. This is a permanent error. The following address(es) failed:','A message that you sent could not be delivered to one or more of its']
    for descartar in discard:
        same.discard(descartar)
    return same

def buscarCoincidencias(path, extension):
    with open('coincidencias.txt', 'w') as file_out:
        os.chdir(path)
        files = glob.glob(extension)
        for i in range(len(files)):
            for j in range(i+1, len(files)):
                with open(files[i]) as file1:
                    with open(files[j], 'r') as file2:
                        same = comparar_linea(file1, file2)
                        inicio = False
                        for contain in same:
                            if contain:
                                if not inicio:
                                    file_out.write(files[i] + "-"+ files[j] + ": ")
                                    inicio = True
                                file_out.write(contain + '[|||]')
                        file_out.write('\n')
                        file_out.write('\n') 

buscarCoincidencias(path, extension)