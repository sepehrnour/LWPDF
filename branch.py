import PyPDF2
import os
import PySimpleGUI as sg
menu_def = [['Help', 'About...']]
rightclick = ['&Edit', ['C&ut', '&Copy','&Paste', '&Undo']]
working_directory = os.getcwd()
sg.theme('DarkBlue14')
merge = PyPDF2.PdfMerger()
layout = [[sg.MenubarCustom(menu_definition = menu_def)],
   [sg.Text("File Locator", pad = 14),
    sg.Input(), sg.FileBrowse(('Browse'), initial_folder = working_directory, file_types = [("PDF Files", "*.pdf*")]),
    sg.Button("Add to Merge"),
    sg.Button("Finalize Merge"),
   ],
   [
    [sg.HorizontalSeparator()],
    [sg.Text('Merged PDF name:', pad = 14), sg.Input(enable_events = True, key = '-PDFName-', expand_x = True)],
   ],
]
client = sg.Window("PDF Merger", layout, size=(775, 165),use_custom_titlebar=True, right_click_menu=rightclick, icon='F:\Z.ico')
while True:
   event, values = client.read()
   print(event, values)
   if event == 'About...':
        sg.popup_ok('About this program', 'Light-weight PDF Merging program.', 'Created by Sepehr Nourbakhsh, Copyright 2023 \n'
                'PySimpleGUI Version', sg.get_versions(),  grab_anywhere=True, keep_on_top=True)
   elif event == "Add to Merge":
        filename = values['Browse']
        merge.append(filename)
        sg.popup_ok('PDF file added to merge queue', title = 'Merge', button_color = 'blue')
   elif event == 'Copy':
      txt = client['-IN-'].get()
   elif event == 'Paste':
      client['-OUT-'].update(value=txt)
   elif event == sg.WIN_CLOSED :
      break
   elif event == "Finalize Merge":
        client['-PDFName-'].update(values['-PDFName-'][:-1])
        finalname = values['-PDFName-'] + '.pdf'
        merge.write(finalname)
        sg.popup_ok('PDF files have been merged, output available in the programs operating directory', title = 'Merge successfull', button_color = 'blue')
client.close()