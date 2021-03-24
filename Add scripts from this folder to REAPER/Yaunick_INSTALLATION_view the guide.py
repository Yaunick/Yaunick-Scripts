# Update date: 23.03.2021
# Version: 1.0
# Category: Installation
# Description: View the guide
# Author: Yaunick
# Contact: b.yanushevich@gmail.com
# Donation: https://paypal.me/yaunick?locale.x=ru_RU

if RPR_GetResourcePath: 
  import sys
  def nothing():
    pass
  if sys.version_info.major == 3 and sys.version_info.minor >= 5:
    import webbrowser
    webbrowser.open('https://github.com/Yaunick/Yaunick-Scripts/blob/main/Guide%20to%20installing%20and%20using%20my%20scripts.md', new=2)
  else:
    RPR_ClearConsole()
    RPR_ShowConsoleMsg('Please instal Python version 3.5 or higher. Error')
  RPR_defer('nothing')
