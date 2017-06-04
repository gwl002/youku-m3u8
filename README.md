#### 可以将优酷视屏地址转成一个可以直接播放的m3u8地址
**  youku_m3u8.py中的方法好像失效了，请看youku2m3u8.py

#### 上面的提到方法好像失效了，没办法只好自己抓包分析了，最后发现在https://ups.youku.com/ups/get.json?vid={0}&ccode=0501&client_ip=0.0.0.0&client_ts={1}&utid={2}&callback=json1495673955480"这个链接中可以提取到m3u8信息，
其中只有一个参数utid是必须的，其他的随便填。
#### 继续找，发现utid是来自cookie cna中的，找各种请求response header中的set-cookie中是否有cna
#### 找了好久没找到，都是莫名奇妙直接出现在cookie中了
#### 只好清空浏览器所有cookie重新找
#### 终于发现https://log.mmstat.com/eg.js这个请求response header中有 set-cookie cna的值，提取出来填上终于成功获得了m3u8地址
#### 代码请看youku2m3u8.py
