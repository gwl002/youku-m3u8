headers={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
    "Referer":"http://m.youku.com/video/id_XMjc4MTI0Mzc0MA==.html?"
}

get_m3u8_url="https://ups.youku.com/ups/get.json?vid={0}&ccode=0501&client_ip=0.0.0.0&client_ts={1}&utid={2}&callback=json1495673955480"

cna_Url="https://log.mmstat.com/eg.js"

def youku2m3u8(videoUrl):
    if not re.search("^https?",videoUrl):
        videoUrl="http:"+videoUrl
    matches=re.search("http:\/\/v\.youku\.com\/v_show\/id_(.+)\.html",videoUrl)
    if matches:
        vid=matches.group(1)
        headers["Referer"]=videoUrl
        t=str(int(time.time()))
        try:
            r2=requests.get(cna_Url,headers=headers)
            utid=r2.cookies["cna"]
            content=requests.get(get_m3u8_url.format(vid,t,utid)).text
            jsonp=re.search('json\d+\((.+)\)',content).group(1)
            m3u8_url=json.loads(jsonp)["data"]["stream"][2]["m3u8_url"]
        except Exception as e:
            print(e)
            return None
        else:
            videoUrl=m3u8_url
    return videoUrl
