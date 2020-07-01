import pyautogui
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Tibia - Runar')],
    [sg.Text('Qual magia deseja usar para Runar?'), sg.InputText()],
    [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window('Tibia Rune Maker', layout)

event, values = window.read()

print('Boa escolha, lembre de ajustar o tempo de recarga da mana para,', values[0])






