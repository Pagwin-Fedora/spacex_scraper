from urllib import request
import json
BASE_URL="https://classof2020mosaic.com"
GET_ID_POSTFIX="/getPhoto.php"
GET_PICTURE_POSTFIX="/upload_flat_complete/thumbnail/{0}.jpg"

for i in range(1,301):
    for n in range(1,301):
        requestData = request.Request(BASE_URL+GET_ID_POSTFIX,data="indexX={0}&indexY={1}".format(i,n).encode("utf-8"),method="POST")
        vals = {}
        with request.urlopen(requestData) as returnData:
            vals = json.loads(returnData.read())
        with request.urlopen(BASE_URL+GET_PICTURE_POSTFIX.format(vals["info"]["code"])) as returnedBuffer:
            with open("{0}x{1}.jpg".format(i,n),'wb+') as outFile:
                outFile.write(returnedBuffer.read())
