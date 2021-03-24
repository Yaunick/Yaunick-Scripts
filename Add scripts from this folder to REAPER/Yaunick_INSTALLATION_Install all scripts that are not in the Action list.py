# Update date: 23.03.2021
# Version: 1.0
# Category: Installation
# Description: Install all scripts that are not in the Action list
# Author: Yaunick
# Contact: b.yanushevich@gmail.com
# Donation: https://paypal.me/yaunick?locale.x=ru_RU

if RPR_GetResourcePath: 
  import sys
  def nothing():
    pass
  if sys.version_info.major == 3 and sys.version_info.minor >= 5:
  
    nex = RPR_MB('Do you want to install ALL new scripts?', 'Warning',1)
      
    if nex == 1:
    
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
  else:
    RPR_ClearConsole()
    RPR_ShowConsoleMsg('Please instal Python version 3.5 or higher. Error')
  RPR_defer('nothing')

