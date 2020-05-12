import PySimpleGUI as sg
import fileinput
import subprocess
import os


dirname = os.path.dirname(os.path.abspath(__file__))
startPath = os.path.join(dirname, 'nginx\\start.bat')
stopPath = os.path.join(dirname, 'nginx\\stop.bat')
filename = os.path.join(dirname, 'nginx\\conf\\nginx.conf')

sg.theme('Reddit')

# All the stuff inside your window.
layout = [[sg.Text(' ')],
          [sg.Text('Youtube Key', size=(15, 1)), sg.InputText()],
          [sg.Text('Facebook Key', size=(15, 1)), sg.InputText()],
          #   [sg.Text('Platform #3', size=(15, 1)), sg.InputText(key="-IN1-"), sg.Button('Remove')],
          #   [sg.Text('Platform #4', size=(15, 1)), sg.InputText(key="-IN3-"), sg.Button('Remove')],
          #   [sg.Text('Platform #5', size=(15, 1)), sg.InputText(key="-IN5-"), sg.Button('Remove')],
          [sg.Text(' ')],
          [sg.Button('Start', button_color=('white', 'springgreen4')), sg.Button('Restart NGINX', button_color=('white', 'black'), disabled=True),
           sg.Button('Stop', button_color=('white', 'firebrick3'), disabled=True)],
          [sg.Button('Stunnel', disabled=True, button_color=('white', 'springgreen4')), sg.Button('READ ME')]]


# Create the Window
window = sg.Window('MultiStream Config', layout)

window.Finalize()

if (os.path.isfile('C:\\Program Files (x86)\\stunnel\\config\\stunnel.conf')):
    window['Stunnel'].update(disabled=False)

# with open(filename, 'r') as file:
#         data = file.readlines()

# window.Finalize()

# if (data[30]):
#     test = data[30].split('push ')
#     idk = test[1].split(';')
#     window['-IN1-'].update(idk[0])

# if(data[31]):
#     print(data[31])
# test1 = data[31].split('push ')
# idk1 = test1[1].split(';')
# window['-IN1-'].update(idk1[0])

# if(data[32]):
#     print(data[32])
# test2 = data[32].split('push ')
# idk2 = test2[1].split(';')
# window['-IN1-'].update(idk2[0])


# Event Loop to process "events" and get the "values" of the inputs
while True:

    with open(filename, 'r') as file:
        data = file.readlines()

    event, values = window.read()
    keyword = "push rtmp://a.rtmp.youtube.com/live2/"

    if event in (None, ):   # if user closes window or clicks cancel
        break

    # Start everything
    if event in ('Start'):

        if(values[0]):
            data[28] = '    			push rtmp://a.rtmp.youtube.com/live2/' + \
                values[0]+';\n'
        if(values[1]):
            data[29] = '                        push rtmp://127.0.0.1:19350/rtmp/' + \
                values[1]+';\n'
        # if(values[2] and values[3]):
        #     data[30] = '                        push '+ values[2] + \
        #         values[3]+';\n'

        with open(filename, 'w') as file:
            file.writelines(data)

        subprocess.call(startPath)
        # [r'./nginx/stop.bat'])
        window['Start'].update(disabled=True)
        window['Stop'].update(disabled=False)
        window['Restart NGINX'].update(disabled=False)

    # Restart NGINX
    if event in ('Restart NGINX'):
        if(values[0]):
            print('You entered: ', values[0])
            data[28] = '    			push rtmp://a.rtmp.youtube.com/live2/' + \
                values[0]+';\n'
        if(values[1]):
            print('You entered: ', values[1])
            data[29] = '                        push rtmp://127.0.0.1:19350/rtmp/' + \
                values[1]+';\n'

        with open(filename, 'w') as file:
            file.writelines(data)

        subprocess.call(stopPath)
        subprocess.call(startPath)

    # Stop NGINX
    if event in ('Stop'):
        print('Stoping Nginx and Stunnel')
        subprocess.Popen(stopPath)
        window['Start'].update(disabled=False)
        window['Stop'].update(disabled=True)
        window['Restart NGINX'].update(disabled=True)

    # Open Read Me
    if event in ('READ ME'):
        # print('Hello')
        subprocess.Popen(['notepad.exe', 'README.txt'])

    # Start Stunnel
    if event in ('Stunnel'):
        subprocess.Popen('C:/Program Files (x86)/stunnel/bin/stunnel.exe')

window.close()
