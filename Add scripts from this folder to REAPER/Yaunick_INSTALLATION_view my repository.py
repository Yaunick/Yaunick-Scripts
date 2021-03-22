# Update date: 23.03.2021
# Version: 1.0
# Category: Installation
# Description: View my repository
# Author: Yaunick
# Contact: b.yanushevich@gmail.com
# Donation: https://paypal.me/yaunick?locale.x=ru_RU

if RPR_GetResourcePath: 
  import sys
  def nothing():
    pass
  if sys.version_info.major == 3 and sys.version_info.minor >= 5:
    import webbrowser
    webbrowser.open('https://github.com/Yaunick/Yaunick-Scripts', new=2)
  else:
    RPR_ClearConsole()
    RPR_ShowConsoleMsg('Please instal Python version 3.5 or higher. Error')
  RPR_defer('nothing')
else:
  pass
