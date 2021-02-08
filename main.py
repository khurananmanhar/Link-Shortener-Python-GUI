#pip install pyshorteners
import pyshorteners as pyshorteners
#pip install PySimpleGUI
import PySimpleGUI as sg
sg.theme('DarkBlue12')   
layout = [  [sg.Text("Enter URL Here")],    
            [sg.Input()],
            [sg.Button('Ok')] ]
window = sg.Window('Window Title', layout)     
event, values = window.read()         
popUp = pyshorteners.Shortener().tinyurl.short(values[0]) 
print(popUp)         
sg.popup(popUp)
window.close()      
