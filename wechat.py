import urllib.request
import json
import sys
corpid='wwd075afe131d7dbd8'
secureid='RAipXmHZBs2I_c4whhBuZopytlpWy7hU7zIMVP8lkWc'

def gettoken(corpid,corpsecret):
    gettoken_url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+corpid+'&corpsecret='+secureid
    print(gettoken_url)
    token_file=urllib.request.urlopen(gettoken_url)
    token_data=token_file.read().decode('utf-8')
    token_json=json.loads(token_data)
    token_json.keys()
    token=token_json['access_token']
    print(token)
    return token

def sendmsg(access_token,user,subject,content):
    send_url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+access_token
    send_values={
        "touser":'HuangHaiHua',
        'toparty':'运维',
        'msgtype':'text',
        "agentid":'1000002',
        'text':{
            'content':subject+'\n'+content
        },
        'safe':'0'
    }
    send_data=json.dumps(send_values,ensure_ascii=False).encode('utf-8')
    send_request=urllib.request.Request(send_url,send_data)
    respone=urllib.request.urlopen(send_request)
    msg=respone.read()
    print("returned value:"+str(msg))

if __name__=='__main__':
    user=str(sys.argv[1])
    subject=str(sys.argv[2])
    content=str(sys.argv[3])

    accesstoken=gettoken(corpid,secureid)
    sendmsg(accesstoken,user,subject,content)
