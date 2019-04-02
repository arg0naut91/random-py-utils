import wmi # You'll also need pywin32 for this to run
import smtplib 
import time
import getpass

start = time.time()

# Insert what you consider to be an excess of GPU/CPU temperature or GPU fan activity

gputemp = 75
cputemp = 50
gpufan = 70

# Insert e-mail data

sendingmail = <insert your email here>
receivingmail = <insert wherever you would like the e-mail to be sent>
uname = <insert your username>
passw = getpass.getpass('Enter your password:')
smtpserv = <insert your SMTP server>
smtpport = <insert your port>

# How often should the hardware be checked (in secs)?

freqs = 60.0

# Start the loop

while True:
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    sensor_info = w.Sensor()

    a = []

    for sensor in sensor_info:
        if sensor.SensorType==u'Temperature':
            a.append(sensor.Value)
        
    a1 = [[i] for i in a]

    integers = [int(l[0]) for l in a1]

    GPUTemp = integers[0]
    CPUTemp = integers[7]

    b = []

    for sensor in sensor_info:
        if sensor.SensorType==u'Control':
            b.append(sensor.Value)

    b1 = [[i] for i in b]

    integers2 = [int(l[0]) for l in b1]

    GPUFan = integers2[0]

    server = smtplib.SMTP(smtpserv, smtpport)
    server.ehlo()
    server.starttls()
    server.login(uname, passw)

    msg = """From: <insert sender>
To: <insert receiver>
Subject: Python ALERT! Computer running too hot!

Your computer is running too hot and should be shut down.\n\nSpecifications:\n\nGPU Temperature: """ + str(GPUTemp)+ """ degrees Celsius\nCPU Temperature: """ + str(CPUTemp)+ """ degrees Celsius\nGPU Fan: """ + str(GPUFan)+ """%\n\nThank you for your attention,\nYour Python
"""
 
    if (GPUTemp > gputemp) or (CPUTemp > cputemp) or (GPUFan > gpufan):
        server.sendmail(youremail, receivingmail, msg)
    time.sleep(freqs - ((time.time() - start) % freqs))
