from aip import AipSpeech
import requests
import key

# 百度语音AI
APP_ID = key.APP_ID 
API_KEY = key.API_KEY
SECRET_KEY = key.SECRET_KEY

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 语音合成
def tts(command):
    if len(command) != 0:
        word = command

    result  = client.synthesis(word,'zh',1, {
        'vol': 5,'per':0, 'aue':6
    })
	
    if not isinstance(result, dict):
        with open('voice/audio.wav', 'wb') as f:
            f.write(result)
        f.close()
        print('tts successful')

# 读取文件 
def get_file_content(filePath):   
    with open(filePath, 'rb') as fp: 
        return fp.read()   

# 语音识别 
def stt(filename):         
    # 识别本地文件 
    result = client.asr(get_file_content(filename), 
                        'pcm', 
                        16000, 
                        {'dev_pid': 1537,}     
                        ) 
    print(result)
    print(result['result'][0])
    return result['result'][0]


# 天气实况
def now():
    WEATHER_KEY = key.WEATHER_KEY # 和风天气api

    url = 'https://devapi.qweather.com/v7/weather/now'
    value = {
        'location': '101210101',
        'key': WEATHER_KEY,
    }
    req = requests.get(url, params=value)

    js = req.json()

    we = js['now']
    text = we['text']
    temp = we['temp']
    feelsLike = we['feelsLike']
    windDir = we['windDir']
    windScale = we['windScale']
    windSpeed = we['windSpeed']
    humidity = we['humidity']

    url = 'https://devapi.qweather.com/v7/air/now'
    value = {
        'location': '101210101',
        'key': WEATHER_KEY,
    }
    req = requests.get(url, params=value)
    js = req.json()
    air_now = js['now']

    res = '您所在的位置是浙江省杭州市，当前天气状况为' + text + ',实际温度' + temp + '度,体感温度' + feelsLike + '度,风向为' + windDir + ',风力' + windScale + '级，风速' + windSpeed + '米每秒，相对湿度为百分之' + humidity + '，空气质量指数' + air_now['aqi']
    return res

# 明天天气
def tomorrow():
    req = requests.get('https://devapi.qweather.com/v7/weather/3d?location=101210101&key=26daca46e5e64e90b7f66672241a8d2a')
    js = req.json()
    tom = js['daily'][1]
    res = '明天最高温度' + tom['tempMax'] + '，最低温度' + tom['tempMin'] + ',白天天气' + tom['textDay'] + ',夜间天气' + tom['textNight']
    return res

# 聊天机器人
def chat(command):
    url = 'http://api.qingyunke.com/api.php'

    value = {
        'key': 'free',
        'appid': '0',
        'msg': command
    }
    req = requests.get(url, params=value)
    js = req.json()
    print(js['content'])
    return js['content']

if __name__ == '__main__':
    print(now())
