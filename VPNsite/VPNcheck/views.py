import requests, subprocess, time
from django.shortcuts import render

def index(request):
    result = 0


    if (request.method == 'POST'):
        url = 'https://ifconfig.io/ip'
        r = requests.get(url)
        path = '/code/monitor.ovpn'
        # your path to server cfg file
        process = subprocess.Popen(f"sudo openvpn --auth-nocache --config {path}", shell=True)
        time.sleep(5)
        r2 = requests.get(url)
        process.kill()
        if r.text != r2.text:
            subprocess.run("sudo killall openvpn", shell=True)
            result = 'Nice one!'

        else:
            result = 'Man, cringe...'
        subprocess.run("sudo killall openvpn", shell=True)

        context = {'info': result}

    context = {'info': result}
    return render(request, 'vpn/index.html', context)
