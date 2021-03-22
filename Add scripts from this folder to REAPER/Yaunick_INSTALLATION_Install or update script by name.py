# Update date: 23.03.2021
# Version: 1.0
# Category: Installation
# Description: Install or update script by name
# Author: Yaunick
# Contact: b.yanushevich@gmail.com
# Donation: https://paypal.me/yaunick?locale.x=ru_RU

run_defer = False
if RPR_GetResourcePath: 
  run_defer = True
  import sys
  def nothing():
    pass
  if sys.version_info.major == 3 and sys.version_info.minor >= 5:
    inputs = RPR_GetUserInputs('User inputs window for entering scripts name to install or reinstall or update', 1, 'Set the script FULL name:,extrawidth=500', '', 1024)
    if inputs[0]:
      if inputs[4] != '' and inputs[4].isspace() != True:
        import urllib.request, os, zipfile
        
        RPR_ClearConsole()
        RPR_ShowConsoleMsg('Loading...Please wait')
        
        def download_url(url, save_path):
          try:
            with urllib.request.urlopen(url,timeout = 5) as dl_file:
              with open(save_path, 'wb') as out_file:
                out_file.write(dl_file.read())
                bool = True
          except:
            bool = False
          return bool
                      
        main_path = RPR_GetResourcePath() + '/Scripts/Yaunick-scripts'
        if not os.path.exists(main_path):
          os.mkdir(main_path)
      
        if not os.path.exists(main_path + '/file.zip'):
          if download_url("https://www.dropbox.com/s/nld95hmulu5rdtu/For%20adding%20in%20REAPER.zip?dl=1", main_path + '/file.zip') == True:   
            
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
  else:
    RPR_ClearConsole()
    RPR_ShowConsoleMsg('Please instal Python version 3.5 or higher. Error')
if run_defer == True:
  RPR_defer('nothing')
