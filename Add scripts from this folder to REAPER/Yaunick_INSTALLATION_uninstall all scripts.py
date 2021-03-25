# Update date: 23.03.2021
# Version: 1.0
# Category: Installation
# Description: Uninstall all scripts
# Author: Yaunick
# Contact: b.yanushevich@gmail.com
# Donation: https://paypal.me/yaunick?locale.x=ru_RU

if RPR_GetResourcePath: 
  import sys
  def nothing():
    pass
  if sys.version_info.major == 3 and sys.version_info.minor >= 5:
    nex = RPR_MB('Are you sure to want to uninstall ALL scripts?', 'Warning',1)
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
        except Exception:
          bool = False
        return bool
                    
      main_path = RPR_GetResourcePath() + '/Scripts/Yaunick-scripts'
      if not os.path.exists(main_path):
        os.mkdir(main_path)
      
      if not os.path.exists(main_path + '/file.zip'):
        if download_url("https://www.dropbox.com/s/nld95hmulu5rdtu/For%20adding%20in%20REAPER.zip?dl=1", main_path + '/file.zip') == True:
    
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
  else:
    RPR_ClearConsole()
    RPR_ShowConsoleMsg('Please instal Python version 3.5 or higher. Error')
  RPR_defer('nothing')

