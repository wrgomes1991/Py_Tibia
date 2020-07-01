import pyautogui
import PySimpleGUI as sg
import time

layout = [  [sg.Text('Tibia Runar no DP')],
            [sg.Text('Magia que vai usar para Runar?'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Tibia Runar - Will', layout)

rune = window.read()

print ("Boa escolha, runar,", rune[1] )

window.close()
