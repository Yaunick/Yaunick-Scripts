#------------------------------------------

user_input_width_for_entering_name = 600

#------------------------------------------

if RPR_GetResourcePath():
  import sys
  def nothing():
    pass
  if sys.version_info.major == 3 and sys.version_info.minor >= 5:
  
    import urllib.request, os, zipfile, webbrowser
    from tkinter import *
    
    def download_url(url, save_path):
      try:
        with urllib.request.urlopen(url,timeout = 5) as dl_file:
          with open(save_path, 'wb') as out_file:
            out_file.write(dl_file.read())
            bool = True
      except:
        bool = False
      return bool
      
    link_scripts = "https://www.dropbox.com/s/nld95hmulu5rdtu/For%20adding%20in%20REAPER.zip?dl=1"
    repo_link = "https://github.com/Yaunick/Yaunick-Scripts"
    
    def main_path_yan():
      main_path = RPR_GetResourcePath() + '/Scripts/Yaunick-scripts'
      if not os.path.exists(main_path):
        os.mkdir(main_path)
      return main_path
    
    def install_all_scripts():
      root.destroy()
      
      RPR_ClearConsole()
      RPR_ShowConsoleMsg('Loading...Please wait')
      
      main_path = main_path_yan()
        
      if not os.path.exists(main_path + '/file.zip'):
        if download_url(link_scripts, main_path + '/file.zip') == True:
          
          zip = zipfile.ZipFile(main_path + '/file.zip')
          zip_list_scripts = zip.namelist()
          
          table_na = []
          count = 0
          b_ad = 0
          for name in zip_list_scripts:
            if not os.path.exists(main_path + '/' + name):
              zip.extract(name, main_path)
              clear_name = name[8 : len(name)-4]
              table_na.append('\n-- ' + clear_name)
            if count == len(zip_list_scripts) - 1:
              b_ad = 1
            if name[0 : 19] != 'Yaunick_MIDIEditor_':
              RPR_AddRemoveReaScript(1, 0, main_path + '/' + name, b_ad)
            else:
              RPR_AddRemoveReaScript(1, 32060, main_path + '/' + name, b_ad)
            count = count + 1
          
          RPR_ClearConsole()
          if len(table_na) > 0:
            RPR_ShowConsoleMsg(''.join(table_na) + '\n\n\nSuccess! All scripts have been checked and added in Action List from source path.\nSee the list of ' + 
            str(len(table_na)) + ' downloaded new script(s) to source path')
          else:
            RPR_ShowConsoleMsg('Success! All scripts have been checked and added in Action List from source path. \n\n0 new scripts downloaded to source path')
          
          zip.close()
          os.remove(main_path + '/file.zip')
        else:
          RPR_ClearConsole()
          RPR_ShowConsoleMsg('No network or server connection! Error')
      else:
        RPR_ClearConsole()
        RPR_ShowConsoleMsg('Please remove or rename the "file.zip" from the "' + main_path + '" folder! Error')
    
    def install_script_by_name():
      root.destroy()
      
      inputs = RPR_GetUserInputs('User inputs window for entering scripts name to install or reinstall or update', 1, 
      'Set the script FULL name:,extrawidth=' + str(user_input_width_for_entering_name), '', 1024)
      if inputs[0]:
        if inputs[4] != '' and inputs[4].isspace() != True:
          
          RPR_ClearConsole()
          RPR_ShowConsoleMsg('Loading...Please wait')
          
          main_path = main_path_yan()
        
          if not os.path.exists(main_path + '/file.zip'):
            if download_url(link_scripts, main_path + '/file.zip') == True:   
              
              new_str = inputs[4].rstrip()
              new_str = new_str.lstrip() 
              if new_str[0 : 8] == 'Script: ':
                new_str = new_str[8 : len(new_str)]
              if new_str[len(new_str)-4 : len(new_str)] != '.lua':
                new_str = new_str + '.lua'
              if new_str[0 : 8] != 'Yaunick_':
                new_str = 'Yaunick_' + new_str
              
              zip = zipfile.ZipFile(main_path + '/file.zip')
            
              bool_fnd = 0
              for na in zip.namelist():
                if new_str == na:
                  bool_fnd = 1
                  new_str = na
                  break
    
              if bool_fnd == 1:
                zip.extract(new_str, main_path)
                
                if new_str[0 : 19] != 'Yaunick_MIDIEditor_':
                  RPR_AddRemoveReaScript(1, 0, main_path + '/' + new_str, 1)
                else:
                  RPR_AddRemoveReaScript(1, 32060, main_path + '/' + new_str, 1)
                
                RPR_ClearConsole()
                RPR_ShowConsoleMsg('Success! "' + new_str + '" script downloaded and reinstalled')
              else:
                RPR_ClearConsole()
                RPR_ShowConsoleMsg('No file with this name! Error')
                
              zip.close()
              os.remove(main_path + '/file.zip')
              
            else:
              RPR_ClearConsole()
              RPR_ShowConsoleMsg('No network or server connection! Error')
          else:
            RPR_ClearConsole()
            RPR_ShowConsoleMsg('Please remove or rename the "file.zip" from the "' + main_path + '" folder! Error')
        else:
          RPR_ClearConsole()
          RPR_ShowConsoleMsg('You enter empty name! Error')
    
    def uninstall_all_scripts():
      root.destroy()
      
      nex = RPR_MB('Are you sure to want to uninstall ALL scripts?', 'Warning',1)
      if nex == 1:
    
        RPR_ClearConsole()
        RPR_ShowConsoleMsg('Loading...Please wait')
                      
        main_path = main_path_yan()
        
        if not os.path.exists(main_path + '/file.zip'):
          if download_url(link_scripts, main_path + '/file.zip') == True:
      
            zip = zipfile.ZipFile(main_path + '/file.zip')
            zip_list_scripts = zip.namelist()
            zip.close()
            os.remove(main_path + '/file.zip')
            table_na = []
          
            for name in zip_list_scripts:
              if os.path.exists(main_path + '/' + name):
                table_na.append(name)
    
            if len(table_na) == 0:
              RPR_ClearConsole()
              RPR_ShowConsoleMsg('No scripts installed, there is nothing uninstall') 
            else:
              
              count = 0
              b_ad = 0
              for name in table_na:
                if count == len(table_na) - 1:
                  b_ad = 1
                if name[0 : 19] != 'Yaunick_MIDIEditor_':
                  RPR_AddRemoveReaScript(0, 0, main_path + '/' + name, b_ad)
                else:
                  RPR_AddRemoveReaScript(0, 32060, main_path + '/' + name, b_ad)
                os.remove(main_path + '/' + name)
                count = count + 1
            
              RPR_ClearConsole()
              if len(table_na) > 1:
                RPR_ShowConsoleMsg('Success! All ' + str(len(table_na)) + ' scripts uninstalled in source path and action list')
              else:
                RPR_ShowConsoleMsg('Success! 1 script uninstalled in source path and action list')
          else:
            RPR_ClearConsole()
            RPR_ShowConsoleMsg('No network or server connection! Error')
        else:
          RPR_ClearConsole()
          RPR_ShowConsoleMsg('Please remove or rename the "file.zip" from the "' + main_path + '" folder! Error')
    
    def open_repo():
      root.destroy()
      webbrowser.open(repo_link, new=2)
    
    root = Tk()
    root.title("Yaunick_INSTALLATION_Lua scripts manager")
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2.8
    root.wm_geometry("+%d+%d" % (x, y))
 
    
    btn1 = Button(text="Install all scripts that are not in the Action list", background="gray82", foreground="black", 
    activebackground="gray86", width=40, height=1, padx="20", pady="10", font="Arial 12 bold", command=install_all_scripts)
                 
    btn2 = Button(text="Install or update script by name", background="gray78", foreground="black", activebackground="gray84",
    width=40, height=1, padx="20", pady="10", font="Arial 12 bold", command=install_script_by_name)     
                 
    btn3 = Button(text="Uninstall all scripts from the Action list", background="gray72", foreground="black", activebackground="gray79", 
    width=40, height=1, padx="20", pady="10", font="Arial 12 bold", command=uninstall_all_scripts)
                 
    btn4 = Button(text="View my repository", background="gray68", foreground="black",activebackground="gray76", 
    width=40, height=1, padx="20", pady="10", font="Arial 12 bold", command=open_repo)
    
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    
    root.attributes("-topmost", True)
    root.mainloop()
    
  else:
    RPR_ClearConsole()
    RPR_ShowConsoleMsg('Please instal Python version 3.5 or higher. Error')
  RPR_defer('nothing')
