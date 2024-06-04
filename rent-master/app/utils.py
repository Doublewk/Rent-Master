import json
import requests
from django.core.paginator import EmptyPage
# 自定义分页逻辑的函数
def get_page_range(paginator, current_page_num):
    if paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator.page_range
    try:
        current_page = paginator.page(current_page_num)  # 当前页
    except EmptyPage as e:
        current_page = paginator.page(1)
    list = [page_range, current_page]
    return list
#填写文心一言的公钥和私钥
API_KEY = "dkdeQpesz4lc9ehn0sLGCxl7"
SECRET_KEY = "sLgezCziGRDUEPXDKyrgY9N3V0aknygF"

def main(prompt):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return eval(response.text.replace('false', '"false"'))['result']

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials",
              "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

