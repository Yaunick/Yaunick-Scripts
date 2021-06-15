
# **Warning!**


- Many of the scripts require SWS extension version 2.10.0 or higher, follow the links to install

  https://www.sws-extension.org/download/pre-release/

  https://www.sws-extension.org/

  Also I do not test the scripts in Reaper below version 6, so I am not responsible for their work in older versions. All scripts work in new versions! If this is not    a case, and if the scripts fail to update for the sake of compatibility, the scripts will be removed

  Also, I don't work on systems other than Windows, although scripts should compile on Mac and Linux systems as well

  The scripts from “Mouse” category must be assigned in the “mouse modifiers” settings, for other use they are not suitable

  > ***Translation into Russian/Перевод для русских.** Многие скрипты требуют SWS расширение версии 2.10.0 или выше.
  Скачать его можно по ссылкам выше. Также я не тестирую скрипты в Reaper ниже 6 версии, поэтому я не несу ответственности за их работу в более старых версиях. 
  Все скрипты работают в новых версиях! Если это окажется не так, а также если скрипты не получится обновить ради совместимости, эти скрипты будут удалены. 
  Кроме того, я не работаю на других системах, кроме Windows, хотя скрипты должны компилироваться в других ОС. 
  Скрипты из категории «Мышь» должны быть назначены в Mouse modifiers, для другого использования они не подходят.* 

# **Installation scripts** (via Python)

- See information here with screenshots and GIFs!!!

  See Screenshots and GIFs</summary>
  https://telegra.ph/How-to-download-install-all-my-scripts-03-09
  
  > ***Translation into Russian/Перевод для русских.** Смотреть подробную информацию по установке моих скриптов, для этого перейти по ссылке выше*

# **Customize scripts**

- See information here with screenshots!!!

  See Screenshots
  https://telegra.ph/Customize-scripts-03-19

  > ***Translation into Russian/Перевод для русских.** Смотреть подробную информацию по настройке моих скриптов, для этого перейти по ссылке выше*

# **Tracks**

- ### **Create audio track from multichannel VSTi (selected track)**

  - This script creates an audio track (output) for a multichannel instrument. For example Kontakt 6. In the script you need to enter the name of the track and the channel number of it. The channel is input as a midi channel, the audio channel is automatically detected (1 - 1/2, 2 - 3/4, 3 - 5/6, etc.). At the beginning of the script, you can change some parameters

    See GIF:
    https://telegra.ph/Create-audio-track-from-multichannel-VSTi-selected-track-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт создает аудио трек (вывод) для многоканального инструмента.Например Kontakt 6. 
    В скрипте нужно ввести название трека и номер его канала. Канал вводится по принципу midi-канала, аудиоканал определяется автоматически 
    (1 - 1/2, 2 - 3/4, 3 - 5/6 и т.д.). В начале скрипта вы можете изменить некоторые параметры.*

- ### **Create midi and audio track from multichannel VSTi (selected track)**

  - This script creates a midi track (input) and an audio track (output) for a multichannel instrument. For example Kontakt 6. In the script you need to enter the name of the tracks and the channel number of it. The channel is input as a midi channel, the audio channel is automatically detected (1 - 1/2, 2 - 3/4, 3 - 5/6, etc.). If you enter 0, one midi track will be created with the ‘All’ channel. At the beginning of the script, you can change some parameters. By default, the midi track will be hidden in the MCP panel and the audio track will be hidden in the TCP panel

    See GIF:
    https://telegra.ph/Create-midi-and-audio-track-from-multichannel-VSTi-selected-track-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт создает миди трек (вход) и аудио трек (вывод) для многоканального инструмента.Например Kontakt 6. В скрипте нужно ввести название трека и номер его канала.Канал вводится по принципу midi-канала, аудиоканал определяется автоматически (1 - 1/2, 2 - 3/4, 3 - 5/6 и т.д.). Если ввести 0, будет создан только один миди трек с каналом All. В начале скрипта вы можете изменить некоторые параметры. По умолчанию миди трек будет скрыт в панели MCP, а аудио трек будет скрыт в панели TCP* 

- ### **Create midi track from multichannel VSTi (selected track)**

  - This script creates a midi track (input for a multichannel instrument. For example Kontakt 6. In the script you need to enter the name of the track and the channel number of it. The channel is input as a midi channel. Entering 0 creates a midi track with the ‘All’ channel. At the beginning of the script, you can change some parameters. By default, the midi track will be hidden in the MCP panel.

    See GIF:
    https://telegra.ph/Create-midi-track-from-multichannel-VSTi-selected-track-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт создает миди трек (вход) для многоканального инструмента.Например Kontakt 6. В скрипте нужно ввести название трека и номер его канала.Канал вводится по принципу midi-канала. Если ввести 0, будет создан только один миди трек с каналом All. В начале скрипта вы можете изменить некоторые параметры. По умолчанию миди трек будет скрыт в панели MCP*

- ### **Create new track (audio+midi) from multichannel VSTi (selected track)**

  - This script creates a track for a multichannel instrument with feedback send. One track is a carrier of audio and midi information. To do this, the script itself activates a special project setting (if not activated). The channel is entered as a midi channel. At the beginning of the script, you can change some parameters

    See GIF:
    https://telegra.ph/Create-new-track-audiomidi-from-multichannel-VSTi-selected-track-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт создает трек для многоканального инструмента с фидбек посылом. Один трек является носителем аудио и миди информации. Для этого скрипт сам активирует специальную настройку проекта (если не активирована). Канал вводится по принципу миди канала. В начале скрипта можно изменить некоторые параметры*

- ### **Create send track or create sends from selected track to existed track**

  - This script creates from the selected tracks either a new track with a send (BUS channel, etc.), or a new send to an existing track with the same name that is entered in the script. At the beginning of the script, you can change some parameters

    See GIF:
    https://telegra.ph/Create-send-track-or-create-sends-from-selected-track-to-existed-track-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт создает из выбранных треков либо новую дорожку с посылом (шина и т. п.), Либо новый посыл на существующий трек с тем же именем, которое введено в скрипт. В начале скрипта вы можете изменить некоторые параметры.*

- ### **Create send track or create sends from selected track to existed track (windowless)**

  - Same as the previous script - windowless version. At the beginning of the script, you can change some parameters

    See GIF:
    https://telegra.ph/Create-send-track-or-create-sends-from-selected-track-to-existed-track-windowless-12-20

    > ***Translation into Russian/Перевод для русских.** То же, что и предыдущий скрипт – версия без окна. В начале скрипта вы можете изменить некоторые параметры.*

- ### **Create multichannel routing (send track) from selected tracks**

  - This script creates multi-channel routing from selected tracks to a new track. Simply put, this script creates sends from the selected tracks to a new track, so the new track turns out to be multichannel (if there are more than 2 sends from tracks). You can select up to 16 tracks. The script consists of two stages of data entry. The first step is to set the numbers of channels. The scheme is as follows ("-" is a dash, numbers through symbols "/" correspond to mono channels in a stereo pair; there are 4 options in total):

    1)     x-y
    2)     x-y/(y + 1)
    3)     x/(x + 1)-y
    4)     x/(x + 1)-y/(y + 1)

    Where x or y = mono send and x/(x + 1) or y/(y + 1) = stereo send. The right and left sides will get off with a "-" line, where the left side is source send, and the right side is destination send. Also “x” can be equal to “y” in both parts. In the second step, you need to specify a name for the new track, as well as the parameters of the master send on the original tracks, and what send mode will be made for the new sends. If you specify the name of an existing track, then sends will be created to it. At the beginning of the script, you can change some parameters

    See GIF:
    https://telegra.ph/Create-multichannel-routing-send-track-from-selected-tracks-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт создает многоканальный роутинг от выбранных треков к новому треку. Проще говоря, этот скрипт создает посылы из выбранных треков к новому треку, поэтому если посылов будет более двух, новый трек окажется многоканальным. Выбрать можно не более 16 треков. Скрипт состоит из двух этапов ввода данных. В первом этапе нужно ввести номера каналов в посылах. Схема следующая (знак "-" является тире, а не минусом, числа через символ "/" соответствуют моно каналам в стерео паре, в итоге получается всего 4 варианта): x-y или x-y/(y+1) или x/(x+1)-y или x/(x+1)-y/(y+1), где x или y = моно посыл, а x/(x+1) или y/(y+1) = стерео посыл. Правая и левая часть отделаются чертой "-", где левая часть - source send, а правая часть - destination send. Также “x” может быть равен “y” в обеих частях. Во втором этапе нужно указать название для нового трека, а также параметры мастер посыла на исходных треках, и какой send mode будет сделан у новых посылов. Если указать имя существующего трека, то посылы будут созданы к нему. В начале скрипта можно указать некоторые свои параметры.*

- ### **Rename selected tracks (like in Pro Tools)**

  - This script renames tracks as in Pro Tools DAW. You need to select the tracks, and the script will sequentially assign them the required name. The "ok" button switches the tracks forward, and "esc" switches back. To exit in the middle of the tracks, enter the word "esc" in any letter size and press "ok"

    See GIF
    https://telegra.ph/Rename-selected-tracks-like-in-Pro-Tools-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт переименовывает треки, как в Pro Tools DAW.Вам нужно выбрать треки, и скрипт последовательно присвоит им нужное имя.Кнопка «ок» переключает треки вперед, а «esc» - назад.Чтобы выйти в середине треков, введите слово «esc» любым размером букв и нажмите «ОК».*

- ### **Render selected tracks to multichannel track obeying time selection (ignore routing)**

  - This script renders a multi-channel wav file from the selected tracks. You need to select up to 16 tracks and indicate the number of channels on each of them (no more than 64 in total). This is usually mono (enter 1) or stereo (enter 2). The script obeys the time selection (if any)

    See GIF:
    https://telegra.ph/Render-selected-tracks-to-multichannel-track-obeying-time-selection-ignore-routing-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт рендерит из выделенных треков многоканальный wav файл. Нужно выбрать до 16 треков и указать кол-во каналов на каждом из них (в сумме не более 64). Обычно это моно (пишем 1) или стерео (пишем 2). Скрипт подчиняется time selection (если есть)*

- ### **Render selected tracks to stereo track obeying time selection (ignore routing)**

  - This script create a stereo track from the selected tracks. That is, it makes the sum in stereo. Nothing complicated :) The script obeys the time selection (if any)

    See GIF:
    https://telegra.ph/Render-selected-tracks-to-stereo-track-obeying-time-selection-ignore-routing-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт рендерит стерео трек из выбранных треков. То есть делает сумму в стерео. Ничего сложного :) Скрипт подчиняется time selection (если есть)*

- ### **Create folder track from selected tracks**

  - This script creates a folder track from the selected tracks. If the tracks are selected out of order, the script will reorder them to the folder automatically. At the beginning of the script you can change some parameters

    See GIF:
    https://telegra.ph/Create-folder-track-from-selected-tracks-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт создает трек-папку из выбранных треков. Если треки выбраны не по порядку, скрипт автоматически их переместит в папку. В начале скрипта вы можете изменить некоторые параметры.*

- ### **Decrease all first identical sends from selected tracks at once** 

  - This script decreases the value of the sends by the X dB value that is specified at the beginning of the script. The script will not work and will give an error if at least one track is selected without sends, or with several sends, or if the send tracks do not match between the selected tracks

    See GIF: 
    https://telegra.ph/Decrease-all-first-identical-sends-from-selected-tracks-at-once-03-08

    > ***Translation into Russian/Перевод для русских.** Этот скрипт уменьшает значение посылов на значение X дБ, указанное в начале скрипта.Скрипт не будет работать и выдаст ошибку, если хотя бы один трек выбран без посылов, или с несколькими посылами, или если посыл-треки не совпадают между выбранными треками*

- ### **Increase all first identical sends from selected tracks at once**

  - This script increases the value of the sends by the X dB value that is specified at the beginning of the script. The script will not work and will give an error if at least one track is selected without sends, or with several sends, or if the send tracks do not match between the selected tracks

    See GIF:
    https://telegra.ph/Increase-all-first-identical-sends-from-selected-tracks-at-once-03-08

    > ***Translation into Russian/Перевод для русских.** Этот скрипт увеличивает значение посылов на значение X дБ, указанное в начале скрипта.Скрипт не будет работать и выдаст ошибку, если хотя бы один трек выбран без посылов, или с несколькими посылами, или если посыл-треки не совпадают между выбранными треками*

# **Items**

- ### **Add or open Melodyne VST3 in selected items**

  - This script adds + opens (or only opens) melodyne of vst 3 format to the selected items. In this case, the name of the plugin in the FX browser must correspond to "VST3: Melodyne (Celemony)"

    See GIF:
    https://telegra.ph/Add-or-open-Melodyne-VST3-in-selected-items-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт добавляет + открывает (либо только открывает) melodyne vst 3 на выделенные айтемы. При этом название плагина в FX browser должно соответствовать "VST3: Melodyne (Celemony)"*

- ### **Mixdown selection (like in Studio One)**

  - This script completely repeats the function from Studio One DAW. You need to select the items and then the script renders the items to new stereo track. The entire chain of FX is counted up to the master channel. At the beginning of the script, you can change some parameters

    See GIF:
    https://telegra.ph/Mixdown-selection-like-in-Studio-One-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт полностью повторяет функцию из Studio One DAW. Вам нужно выбрать айтемы, а затем скрипт срендерит айтемы в новый стерео трек. Вся цепочка FX учитывается до мастер-канала. В начале скрипта вы можете изменить некоторые параметры.*

- ### **Bounce selection (like in Studio One)**

  - This script repeats the function from Studio One DAW. You need to select the item(s). Then the script renders each item separately to one new track. If items from several tracks are selected, then items are rendered to the same number of new tracks. By default, a window is called to indicate the render tail

    See GIF:
    https://telegra.ph/Bounce-selection-like-in-Studio-One-02-19

    > ***Translation into Russian/Перевод для русских.** Этот скрипт повторяет функцию из Studio One DAW. Вам нужно выбрать айтемы. Затем скрипт срендерит каждый айтем отдельно в один новый трек. Если выбраны айтемы из нескольких треков, то они срендерятся в то же количество новых треков. По умолчанию вызывается окно, чтобы указать хвост рендера.*

- ### **Unselect every even item of selected items**

  - This script unselects all even items relative to the selected items.

    See GIF:
    https://telegra.ph/Unselect-every-even-item-of-selected-items-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт снимает выделение со всех четных айтемов относительно выбранных айтемов.*

- ### **Unselect every odd item of selected items**

  - This script unselects all odd items relative to the selected items.

    See GIF:
    https://telegra.ph/Unselect-every-odd-item-of-selected-items-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт снимает выделение со всех нечетных айтемов относительно выбранных айтемов.*

- ### **Adjust take pitch using mousewheel (fine)**

  - This script increases or decreases the pitch of items depending on the direction you scroll the mouse wheel. Pitch change happens smoothly

    See GIF:
    https://telegra.ph/Adjust-take-pitch-using-mousewheel-fine-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт увеличивает или уменьшает питч на выделенных айтемах в зависимости от направления прокрутки мыши. Изменение питча происходит плавно*

- ### **Adjust take pitch using mousewheel (semitones)**

  - This script increases or decreases the step of elements depending on the direction of the scroll of the mouse wheel. The pitch change occurs by semitones

    See GIF:
    https://telegra.ph/Adjust-take-pitch-using-mousewheel-semitones-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт увеличивает или уменьшает питч на выделенных айтемах в зависимости от направления прокрутки мыши. Изменение питча происходит по полутонам*

- ### **Increase or decrease peaks on all items using mousewheel**

  - This script increases or decreases the scale of peaks (without changing the volume) on all items in the project. Changes occur depending on the direction of the mouse scrolling

    See GIF:
    https://telegra.ph/Increase-or-decrease-peaks-on-all-items-using-mousewheel-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт увеличивает или уменьшает масштаб (размер) пиков на всех айтемах в проекте, не меняя при этом громкости. Изменения масштаба зависят от направления прокрутки колеса мыши*

- ### **Warn about all items that have the offline takes**

  - This script looks through all the items in the project and will give a warning about whether there are offline takes in the project or not

    See GIF:
    https://telegra.ph/Warn-about-all-items-that-have-the-offline-takes-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт просматривает все айтемы в проекте и выдаст предупреждение о том, есть ли offline тейки в проекте или нет*

- ### **Show or hide peaks on all items (global)**

  - This script displays or hides peaks on all items at once (global setting from prefs)

    See GIF:
    https://telegra.ph/Show-or-hide-peaks-on-all-items-global-12-20

    > ***Translation into Russian/Перевод для русских.** Этот скрипт отображает или скрывает пики для всех айтемов сразу (глобальная настройка из prefs)*

- ### **Split selected items at grid and set mute state for every even item**

  - This script splits the selected items according to the frequency of the grid in the project, then sets a mute state for each even item

    See GIF:
    https://telegra.ph/Split-selected-items-at-grid-and-set-mute-state-for-every-even-item-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт разрезает айтемы в соответствии с частотой сетки проекта, а затем выставляет mute для каждого четного айтема*

- ### **Split selected items at grid and set mute state for every odd item**

  - This script splits the selected items according to the frequency of the grid in the project, then sets a mute state for each odd item

    See GIF:
    https://telegra.ph/Split-selected-items-at-grid-and-set-mute-state-for-every-odd-item-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт разрезает айтемы в соответствии с частотой сетки проекта, а затем выставляет mute для каждого нечетного айтема*

- ### **Trim left edge of item or selected items to mouse cursor**

  - This script trims the left edge of the item or selected items under the mouse cursor. Suitable for shortcut only

    See GIF:
    https://telegra.ph/Trim-left-edge-of-item-or-selected-items-to-mouse-cursor-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт обрезает левую часть айтема или выбранных айтемов под курсором мыши. Подходит только для шортката*

- ### **Trim right edge of item or selected items to mouse cursor**

  - This script trims the right edge of the item or selected items under the mouse cursor. Suitable for shortcut only

    See GIF:
    https://telegra.ph/Trim-right-edge-of-item-or-selected-items-to-mouse-cursor-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт обрезает левую часть айтема или выбранных айтемов под курсором мыши. Подходит только для шортката*

- ### **Glue selected items independently**

  - This script glues items independently of each other. That is, the items are not merging, but the item parameters are applied (rendered) - become destructive. At the beginning of the script, you can choose which glue action to use.

    See GIF:
    https://telegra.ph/Glue-selected-items-independently-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт склеивает айтемы независимо друг от друга. То есть айтемы не соединяются, но применяются (рендерятся) параметры айтема - становятся деструктивными. В начале скрипта можно выбрать, какой экшн Glue использовать*
	
- ### **Render selected pre-glued items that have active MIDI takes and source track instrument to new take without FX**

  - This script allows you to deactivate the VSTi by rendering midi takes to a new audio take. FX after the instrument will not be rendered. If there are several midi takes, then they will first be glued into one. The script will not work if there is no instrument on the track, or if there are multiple instruments. FX before the instrument (for example midi FX) will be taken into account when rendering. By default, the script launches a window in which you need to enter the length of the render tail. This can be configured at the beginning of the script, it is also possible to set the instrument to bypass or offline
  
	See GIF:
	https://telegra.ph/Render-selected-pre-glued-items-that-have-active-MIDI-takes-and-source-track-instrument-to-new-take-without-FX-03-24
  
	> ***Translation into Russian/Перевод для русских.** Этот скрипт позволяет деактивировать VSTi путем рендеринга миди тейка в новый аудио тейк. Эффекты после инструмента не будут рендерится. Если миди-тейков несколько, то сначала они будут склеены в один. Скрипт не будет работать, если на дорожке нет инструмента или есть несколько инструментов. Эффекты до инструмента (midi-эффекты) будут учтены при рендеринге. По умолчанию скрипт запускает окно, в котором нужно ввести длину хвоста рендеринга. Это можно настроить в начале скрипта, также можно увести инструмент в bypass или offline.*

# **Arrange**

- ### **Ableton loop (ctrl+L)**

  - This script completely repeats the function from Ableton live DAW on shortcut ctrl+L. You need to select items, the script will automatically set the loop points + activates repeat function. Re-running the script enables or disables the repeat function

    See GIF:
    https://telegra.ph/Ableton-loop-ctrlL-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт полностью повторяет функцию из Ableton Live DAW. Нужно выбрать айтемы и скрипт автоматически установит границы лупа + активирует функцию зацикливания из транспорт панели. Повторный запуск скрипта только запускает/отключает функцию зацикливания.*

- ### **Insert =START marker, then =END marker at edit cursor**

  - This script is needed to set the borders of the render in the "Entire Project" mode. The script inserts “= Start” marker, then “= End” marker, and if there are both markers, it erases them again inserts “= Start” marker. The function is best for setting in Preference in Mouse Modifiers – “Ruler” – “Double click”

    See GIF:
    https://telegra.ph/Insert-START-marker-then-END-marker-at-edit-cursor-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт нужен для установки границ рендера в режиме Entire Project. Сначала скрипт вставляет маркер «=START» затем маркер «=END». Если есть оба маркера, стирает все и ставит снова маркер «=START». Функция лучше всего подходит для двойного клика по таймлайну – для установки таковой нужно зайти в главные настройки Preference пункт Mouse Modifiers – “Ruler” – “Double click”*

- ### **Insert region between the start and end point (relative to edit cursor)**

  - This script creates a region in the same way as the previous script “Insert =START marker, then =END marker at edit cursor” by double clicking or at edit cursor position to set the start and end of new region

    See GIF:
    https://telegra.ph/Insert-region-between-the-start-and-end-point-relative-to-edit-cursor-03-11

    > ***Translation into Russian/Перевод для русских.** Этот скрипт создает регион таким же образом, как и предыдущий сценарий «Insert =START marker, then =END marker at edit cursor» двойным щелчком или в позиции курсора редактирования, чтобы установить начало и конец нового региона.*

- ### **Adjust grid using mousewheel (alternation of straight and triplet)**

  - This script switches the grid by scrolling the mousewheel. If you turn the wheel up, the grid gets smaller, if you turn down, the grid gets larger. Moreover, the straight and triplet grid alternate with each other. For example, if you make the grid smaller, then the order of values looks like this – 1/2, 1/2 triplet, 1/4, 1/4 triplet, etc. The script is configured in the Action List window to control the mousewheel

    See GIF:
    https://telegra.ph/Adjust-grid-using-mousewheel-alternation-of-straight-and-triplet-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт переключает сетку по прокрутке колеса мыши. Если крутить колесо вверх, скрипт делает сетку мельче, а если вниз, то делает сетку крупнее. Причем, обычная и триольная сетка чередуются между собой. Например, если делать сетку мельче, порядок значений следующий – половинная нота, половинная триолями, четвертная, четвертная триолями и т.д. по аналогии. Скрипт настраивается в окне Action list для управления колесом мыши.*

- ### **Switch next grid (alternation of straight and triplet)**

  - This script switches the next smaller grid. Moreover, the straight and triplet grid alternate with each other (same as “Adjust grid using mousewheel (alternation of straight and triplet” script). The script is suitable for a shortcut or button

    See GIF:
    https://telegra.ph/Switch-next-grid-alternation-of-straight-and-triplet-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт переключает следующую меньшую сетку. Причем, обычная и триольная сетка чередуются между собой по аналогии с скриптом “Adjust grid using mousewheel (alternation of straight and triplet)”. Скрипт подходит для кнопки или горячей клавиши.*

- ### **Switch previous grid (alternation of straight and triplet)**

  - This script switches the previous larger grid. Moreover, the straight and triplet grid alternate with each other (same as “Adjust grid using mousewheel (alternation of straight and triplet” script). The script is suitable for a shortcut or button

    See GIF:
    https://telegra.ph/Switch-previous-grid-alternation-of-straight-and-triplet-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт переключает предыдущую бОльшую сетку. Причем, обычная и триольная сетка чередуются между собой по аналогии с скриптом “Adjust grid using mousewheel (alternation of straight and triplet)”. Скрипт подходит для кнопки или горячей клавиши.* 

- ### **Snap the grid at edit cursor using mousewheel or move edit cursor by step**

  - This script allows you to create a project grid to match the audio tempo. If you turn the mousewheel up, the cursor moves forward in accordance with the distance from the beginning of the item to the take marker (for example, the take marker is conveniently placed at a distance of one measure from the beginning of the song). If you roll the mousewheel down, the project grid is adjusted and tempo markers are created. The script uses automatic rewind to the cursor. The script cannot be used otherwise than on the mouse wheel

    See GIF:
    https://telegra.ph/Snap-the-grid-at-edit-cursor-using-mousewheel-or-move-edit-cursor-by-step-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт позволяет создать живую сетку проекта под темп аудио. Если крутить колесо мыши вверх, курсор перемещается вперед в соответствии с расстоянием от начала айтема до тейк маркера (например тейк маркер удобно поставить на расстоянии одного такта от начала песни). Если крутить колесо мыши вниз, подстраивается сетка проекта и создается темпо маркеры. Скрипт использует автоматическую перемотку к курсору. Этот скрипт нельзя использовать иначе, кроме как на колесе мыши*

# **Various**

- ### **Insert FX by name to master track or selected tracks or selected items**

  - This script adds an effect by name, which you must enter at the beginning of the script. Adds ReaEQ by default. If the last click was on a track, the script will add FX to that track. If the last click was on an item, the script will add FX to that item. If the last click was on the master track, the script will add FX to the master track. The FX name must be entered without the prefix “VST:”, “VST3:”, “JS:” etc. If you need to enter the name of the VST, VST3 (etc.) plug-in, then the name corresponds to the name in the FX browser. If you need to enter the name of the JS plugin, then the name corresponds to the file name in the Reaper configuration folder - "Effects"

    See GIF:
    https://telegra.ph/Insert-FX-by-name-to-master-track-or-selected-tracks-or-selected-items-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт добавляет эффект по имени, которое нужно ввести в начале скрипта. По умолчанию добавляет ReaEQ. Если последний клик был на треке, скрипт добавит FX на этот трек. Если последний клик был на айтеме, скрипт добавит FX на этот айтем. Если последний клик был на мастер треке, скрипт добавит FX на мастер-трек. Имя эффекта нужно вводить без приставки “VST:”, “VST3:”, “JS:” и т.д. Если вам нужно ввести имя плагина VST, VST3 (и т. д.), то его имя соответствует имени в браузере FX. Если нужно ввести название JS плагина, то его имя соответствует имени файла в папке конфигурации Reaper - «Effects»*

- ### **Split items at mouse cursor or set track to exclusive solo**

  - This script splits the item/selected items or sets the exclusive solo for the track depending on where you hover the mouse cursor. The script is only suitable for shortcut

    See GIF:
    https://telegra.ph/Split-items-at-mouse-cursor-or-set-track-to-exclusive-solo-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт разрезает айтем/выбранные айтемы или ставит трек в эксклюзивное соло в зависимости от того куда навести курсор мыши. Скрипт подходит только для горячей клавиши.*

- ### **Float instrument from insert or send at selected tracks**

  - This script opens the instrument from the original track(s) or their(s) send(s). At the beginning of the script, you can change some parameters.

    See GIF:
    https://telegra.ph/Float-instrument-from-insert-or-send-at-selected-tracks-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт открывает инструмент из оригинального трека (треков) или его (их) посыла (посылов). В начале скрипта можно изменить некоторые параметры.*

# **Mouse**

- ### **Float instruments from insert or send at selected track or toggle folder collapse**

  - This script opens the instrument from the original track or its send. If the track is a parent then collapses or unfolds children tracks. This script must be assigned in the prefs in mouse modifiers in the Track control panel section - "Double click" and / or in the Mixer control panel section - "Double click"

    See GIF:
    https://telegra.ph/Float-instruments-from-insert-or-send-at-selected-track-or-toggle-folder-collapse-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт открывает инструмент с оригинального трека или его посыла. Если трек является родительским (папкой), то сворачивает и разворачивает дочерние треки. Скрипт должен быть назначен в главных настройках Preference, в Mouse modifiers в разделе Track control panel - "Double click" и/или в разделе Mixer control panel - "Double click"*

- ### **Insert item at mouse cursor within a measure (like in Studio One)**

  - This script completely repeats the function from Studio One DAW. The function is implemented there by double click. You need to assign this script to Preference in Mouse Modifiers – “Track” – “Double click”. Double-clicking on an empty space of arrange creates a new item with a quantize to the measure.

    See GIF:
    https://telegra.ph/Insert-item-at-mouse-cursor-within-a-measure-like-in-Studio-One-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт полностью повторяет функцию из Studio One DAW. Функция реализуется там по двойному клику. Нужно назначить этот скрипт в Preference в Mouse Modifiers – “Track” – “Double click”. После чего при нажатии два раза левым кликом в пустом поле аранжировки создается новый айтем с жесткой привязкой к такту.* 

- ### **Set exclusive record arm for track or toggle folder collapse**

  - This script sets the track to exclusive record arm. If the track is a parent then collapses or unfolds children tracks. This script must be assigned in the prefs in mouse modifiers in the Track control panel section - "Double click" and / or in the Mixer control panel section - "Double click"

    See GIF:
    https://telegra.ph/Set-exclusive-record-arm-for-track-or-toggle-folder-collapse-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт устанавливает трек в эксклюзивную запись. Если трек является родительским (папкой), то сворачивает и разворачивает дочерние треки. Скрипт должен быть назначен в главных настройках Preference, в Mouse modifiers в разделе Track control panel - "Double click" и/или в разделе Mixer control panel  - "Double click"*

# **MIDI Editor**

- ### **MIDIEditor_Float instrument from midi editor (from insert or send at track)**

  - This script opens the instrument from the original track or their send from the active Midi editor. Accordingly, this script must be assigned to the Action list in the Midi Editor section (not Main section)

    See GIF:
    https://telegra.ph/Float-instrument-from-midi-editor-from-insert-or-send-at-track-12-21

    > ***Translation into Russian/Перевод для русских.** Этот скрипт открывает инструмент из оригинального трека или его посыла из активного миди редактора. Соответственно этот скрипт должен быть назначен в Action list в разделе Midi editor (не в разделе Main).*

- ### **MIDIEditor_Back notes (like in Studio One)**

  - This script is needed to record notes step by step using a midi keyboard. During such recording, the edit cursor is moved, the script allows you to erase notes, returning the edit cursor to a step in accordance with the last note or chord

    See GIF:
    https://telegra.ph/Back-notes-like-in-Studio-One-03-11

    > ***Translation into Russian/Перевод для русских.** Этот скрипт нужен для пошаговой записи нот с помощью MIDI-клавиатуры.Во время такой записи edit cursor перемещается, скрипт позволяет стирать ноты, возвращая edit cursor на шаг в соответствии с последней нотой или аккордом.*

# **End of guide!**
