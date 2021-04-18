#pip install pyshorteners
import pyshorteners
#pip install PySimpleGUI
import PySimpleGUI as sg
#pip install pyperclip
import pyperclip


sg.theme('DarkBlue12')   
layout = [  [sg.Text("Enter URL Here")],    
            [sg.Input()],
            [sg.Button('Ok')],
            [sg.Text("The link will automatically be copied")] ]
            
window = sg.Window('Window Title', layout)     
event, values = window.read()         
short = pyshorteners.Shortener().tinyurl.short(values[0]) 
pyperclip.copy(short)
print(short)         
window.close()      
