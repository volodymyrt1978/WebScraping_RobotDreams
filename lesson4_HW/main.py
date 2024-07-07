import requests
import re


def use_post():
    payload = {
    "action": "facetwp_refresh",
    "data": {
        "facets": {
            "recherche": [],
            "ou": [],
            "type_de_contrat": [],
            "fonction": [],
            "load_more": [
                3
            ]
        },
        "frozen_facets": {
            "ou": "hard"
        },
        "http_params": {
            "get": [],
            "uri": "emplois",
            "url_vars": []
        },
        "template": "wp",
        "extras": {
            "counts": True,
            "sort": "default"
        },
        "soft_refresh": 1,
        "is_bfcache": 1,
        "first_load": 0,
        "paged": 1
    }
}
    response = requests.post('https://www.lejobadequat.com/emplois',json=payload)
    content = response.json()['template']
        
    pattern = r"\"jobCard_title\"\>.*\<"
    list = re.findall(pattern, content)
    
    resultFile = open('vacancies.txt',mode='w', encoding='utf-8')
    for v in range(len(list)):
        list[v]=list[v].strip("\"jobCard_title\">,<")
        resultFile.write(str(list[v])+"\n")
    resultFile.close()

            
    

if __name__ == '__main__':
    use_post()