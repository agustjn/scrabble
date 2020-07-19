ELEMENT AND FUNCTION CALL
REFERENCE
Here you will ﬁnd the details for all Elements, Objects, and Functions that are available to you. If you want to use a
complex element and don't understand the parameters, then this is the right place to come. For every element you're
shown the parameters used to create it as well as all methods available to call.


Currently PySimpleGUI (tkinter) only
This documentation is created using the PySimpleGUI.py ﬁle which means it's based on the tkinter code. Some of
the calls are different, might not exist at all, or there may be more methods/functions for the other PySimpleGUI
ports (Qt, Wx, Web).

Work is underway to get the PySimpleGUIQt docstrings completed and corrected.
                                                                                                            v: latest 
Caution - Some functions / methods may be internal
only yet exposed in this documentation
This section of the documentation is generated directly from the source code. As a result, sometimes internal only
functions or methods that you are not supposed to be calling are accidently shown in this documentation. Hopefully
these accidents don't happen often.

Here are all of the Elements, the Window & SystemTray classes, and all functions


Button Element
 Button Element - Deﬁnes all possible buttons. The shortcuts such as Submit, FileBrowse, ... each create a Button



 Button(button_text="",
   button_type=7,
   target=(None, None),
   tooltip=None,
   ﬁle_types=(('ALL Files', '*.*'),),
   initial_folder=None,
   disabled=False,
   change_submits=False,
   enable_events=False,
   image_ﬁlename=None,
   image_data=None,
   image_size=(None, None),
   image_subsample=None,
   border_width=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   disabled_button_color=None,
   use_ttk_buttons=None,
   font=None,
   bind_return_key=False,
   focus=False,
   pad=None,
   key=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                       Name                    Meaning

 str                        button_text             Text to be displayed on the button                               v: latest 
Type                     Name               Meaning

int                      button_type        You should NOT be setting this directly. ONLY the shortcut
                                            functions set this

Union[str, Tuple[int,    target             key or (row,col) target for the button. Note that -1 for column
int]]                                       means 1 element to the left of this one. The constant ThisRow is
                                            used to indicate the current row. The Button itself is a valid target
                                            for some types of button

str                      tooltip            text, that will appear when mouse hovers over the element

Tuple[Tuple[str, str],   ﬁle_types          the ﬁletypes that will be used to match ﬁles. To indicate all ﬁles:
...]                                        (("ALL Files", "."),). Note - NOT SUPPORTED ON MAC

str                      initial_folder     starting path for folders and ﬁles

bool                     disabled           If True button will be created disabled

bool                     click_submits      DO NOT USE. Only listed for backwards compat - Use
                                            enable_events instead

bool                     enable_events      Turns on the element speciﬁc events. If this button is a target,
                                            should it generate an event when ﬁlled in

str                      image_ﬁlename      image ﬁlename if there is a button image. GIFs and PNGs only.

Union[bytes, str]        image_data         Raw or Base64 representation of the image to put on button.
                                            Choose either ﬁlename or data

Tuple[int, int]          image_size         Size of the image in pixels (width, height)

int                      image_subsample    amount to reduce the size of the image. Divides the size by this
                                            number. 2=1/2, 3=1/3, 4=1/4, etc

int                      border_width       width of border around button in pixels

Tuple[int, int]          size               (width, height) of the button in characters wide, rows high

bool                     auto_size_button   if True the button size is sized to ﬁt the text

Tuple[str, str]          button_color       (text color, background color) of button. Easy to remember which
                                            is which if you say "ON" between colors. "red" on "green".

                                                                                                        v: latest 
 Type                         Name                      Meaning

 Tuple[str, str]              disabled_button_color     colors to use when button is disabled (text, background). Use
                                                        None for a color if don't want to change. Only ttk buttons support
                                                        both text and background colors. tk buttons only support
                                                        changing text color

 bool                         use_ttk_buttons           True = use ttk buttons. False = do not use ttk buttons. None
                                                        (Default) = use ttk buttons only if on a Mac and not with button
                                                        images

 Union[str, Tuple[str,        font                      speciﬁes the font family, size, etc
 int]]

 bool                         bind_return_key           If True the return key will cause this button to be pressed

 bool                         focus                     if True, initial focus will be put on this button

 (int, int) or ((int, int),   pad                       Amount of padding to put around element (left/right, top/bottom)
 (int,int)) or (int,                                    or ((left, right), (top, bottom))
 (int,int)) or ((int,
 int),int)

 Any                          key                       Used with window.FindElement and with return values to uniquely
                                                        identify this element to uniquely identify this element

 bool                         visible                   set visibility state of the element

 Any                          metadata                  User metadata that can be set to ANYTHING


Click
Generates a click of the button as if the user clicked the button Calls the tkinter invoke method for the button

 Click()



GetText
Returns the current text shown on a button

 GetText()


 Type               Name                Meaning
                                                                                                                   v: latest 

                    return              The text currently displayed on the button
SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Button Element. Must call Window.Read or Window.Finalize prior

 Update(text=None,
  button_color=(None, None),
  disabled=None,
  image_data=None,
  image_ﬁlename=None,
  visible=None,
  image_subsample=None,
  disabled_button_color=(None, None),
  image_size=None)


Parameter Descriptions:

 Type            Name                        Meaning

 str             text                        sets button text
                                                                                                          v: latest 
 Type           Name                      Meaning

 Tuple[str,     button_color              (text color, background color) of button. Easy to remember which is which
 str]                                     if you say "ON" between colors. "red" on "green"

 bool           disabled                  disable or enable state of the element

 Union[bytes,   image_data                Raw or Base64 representation of the image to put on button. Choose
 str]                                     either ﬁlename or data

 str            image_ﬁlename             image ﬁlename if there is a button image. GIFs and PNGs only.

 Tuple[str,     disabled_button_color     colors to use when button is disabled (text, background). Use None for a
 str]                                     color if don't want to change. Only ttk buttons support both text and
                                          background colors. tk buttons only support changing text color

 bool           visible                   control visibility of element

 int            image_subsample           amount to reduce the size of the image. Divides the size by this number.
                                          2=1/2, 3=1/3, 4=1/4, etc

 Tuple[int,     image_size                Size of the image in pixels (width, height)
 int]


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



click
Generates a click of the button as if the user clicked the button Calls the tkinter invoke method for the button

 click()



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,                                                                                           v: latest 
   expand_row=True)
get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                 Meaning

                  return               width and height of the element


get_text
Returns the current text shown on a button

get_text()


 Type           Name             Meaning

                return           The text currently displayed on the button


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type         Name          Meaning
                                                                                                          v: latest 

 bool         force         if True will call focus_force otherwise calls focus_set
set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                 Name         Meaning

 Tuple[int, int]      size         The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                               Meaning

 str                tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Button Element. Must call Window.Read or Window.Finalize prior
                                                                                                             v: latest 
 update(text=None,
   button_color=(None, None),
   disabled=None,
   image_data=None,
   image_ﬁlename=None,
   visible=None,
   image_subsample=None,
   disabled_button_color=(None, None),
   image_size=None)


Parameter Descriptions:

 Type           Name                      Meaning

 str            text                      sets button text

 Tuple[str,     button_color              (text color, background color) of button. Easy to remember which is which
 str]                                     if you say "ON" between colors. "red" on "green"

 bool           disabled                  disable or enable state of the element

 Union[bytes,   image_data                Raw or Base64 representation of the image to put on button. Choose
 str]                                     either ﬁlename or data

 str            image_ﬁlename             image ﬁlename if there is a button image. GIFs and PNGs only.

 Tuple[str,     disabled_button_color     colors to use when button is disabled (text, background). Use None for a
 str]                                     color if don't want to change. Only ttk buttons support both text and
                                          background colors. tk buttons only support changing text color

 bool           visible                   control visibility of element

 int            image_subsample           amount to reduce the size of the image. Divides the size by this number.
                                          2=1/2, 3=1/3, 4=1/4, etc

 Tuple[int,     image_size                Size of the image in pixels (width, height)
 int]



ButtonMenu Element
 The Button Menu Element. Creates a button that when clicked will show a menu similar to right click menu



                                                                                                             v: latest 
 ButtonMenu(button_text,
   menu_def,
   tooltip=None,
   disabled=False,
   image_ﬁlename=None,
   image_data=None,
   image_size=(None, None),
   image_subsample=None,
   border_width=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   font=None,
   pad=None,
   key=None,
   tearoff=False,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                         Name              Meaning

 str                          button_text       Text to be displayed on the button

 List[List[str]]              menu_def          A list of lists of Menu items to show when this element is
                                                clicked. See docs for format as they are the same for all
                                                menu types

 str                          tooltip           text, that will appear when mouse hovers over the element

 bool                         disabled          If True button will be created disabled

 str                          image_ﬁlename     image ﬁlename if there is a button image. GIFs and PNGs
                                                only.

 Union[bytes, str]            image_data        Raw or Base64 representation of the image to put on
                                                button. Choose either ﬁlename or data

 Tuple[int, int]              image_size        Size of the image in pixels (width, height)

 int                          image_subsample   amount to reduce the size of the image. Divides the size by
                                                this number. 2=1/2, 3=1/3, 4=1/4, etc

 int                          border_width      width of border around button in pixels
                                                                                                    v: latest 
 Tuple[int, int]              size              (width, height) of the button in characters wide, rows high
 Type                                      Name                 Meaning

 bool                                      auto_size_button     if True the button size is sized to ﬁt the text

 Tuple[str, str]                           button_color         (text color, background color) of button. Easy to remember
                                                                which is which if you say "ON" between colors. "red" on
                                                                "green"

 Union[str, Tuple[str, int]]               font                 speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int)) or   pad                  Amount of padding to put around element (left/right,
 (int,(int,int)) or ((int, int),int)                            top/bottom) or ((left, right), (top, bottom))

 Any                                       key                  Used with window.FindElement and with return values to
                                                                uniquely identify this element to uniquely identify this
                                                                element

 bool                                      tearoff              Determines if menus should allow them to be torn off

 bool                                      visible              set visibility state of the element

 Any                                       metadata             User metadata that can be set to ANYTHING


Click
Generates a click of the button as if the user clicked the button Calls the tkinter invoke method for the button

 Click()



SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type           Name               Meaning

 bool           force              if True will call focus_force otherwise calls focus_set


SetTooltip                                                                                                         v: latest 
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').
 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type              Name                            Meaning

 str               tooltip_text                    the text to show in tooltip.


Update
Changes some of the settings for the ButtonMenu Element. Must call Window.Read or Window.Finalize prior

 Update(menu_deﬁnition, visible=None)


Parameter Descriptions:

 Type             Name                     Meaning

 List[List]       menu_deﬁnition           (New menu deﬁnition (in menu deﬁnition format)

 bool             visible                  control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()                                                                                                v: latest 


 Type              Name                 Meaning
 Type              Name                   Meaning

                   return                 width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels
                                                                                                             v: latest 

set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                            Meaning

 str                tooltip_text                    the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the ButtonMenu Element. Must call Window.Read or Window.Finalize prior

 update(menu_deﬁnition, visible=None)


Parameter Descriptions:

 Type             Name                      Meaning

 List[List]       menu_deﬁnition            (New menu deﬁnition (in menu deﬁnition format)

 bool             visible                   control visibility of element



Canvas Element
                                                                                                             v: latest 
 Canvas(canvas=None,
   background_color=None,
   size=(None, None),
   pad=None,
   key=None,
   tooltip=None,
   right_click_menu=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                                            Name               Meaning

 (tk.Canvas)                                     canvas             Your own tk.Canvas if you already created it. Leave
                                                                    blank to create a Canvas

 str                                             background_color   color of background

 Tuple[int,int]                                  size               (width in char, height in rows) size in pixels to make
                                                                    canvas

 (int, int) or ((int, int),(int,int)) or (int,   pad                Amount of padding to put around element
 (int,int)) or ((int, int),int)

 Any                                             key                Used with window.FindElement and with return values
                                                                    to uniquely identify this element

 str                                             tooltip            text, that will appear when mouse hovers over the
                                                                    element

 List[List[Union[List[str],str]]]                right_click_menu   A list of lists of Menu items to show when this element
                                                                    is right clicked. See user docs for exact format.

 bool                                            visible            set visibility state of the element

 Any                                             metadata           User metadata that can be set to ANYTHING


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)

                                                                                                                     v: latest 
Parameter Descriptions:

 Type             Name             Meaning
 Type         Name               Meaning

 bool         force              if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                               Meaning

 str                  tooltip_text                       the text to show in tooltip.


TKCanvas
property: TKCanvas
Returns the underlying tkiner Canvas widget

 Type                   Name                     Meaning

                        return                   The tkinter canvas widget


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)

                                                                                                          v: latest 
get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type              Name                   Meaning

                   return                 width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:
                                                                                                             v: latest 
 Type                 Name        Meaning
 Type                 Name         Meaning

 Tuple[int, int]      size         The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                               Meaning

 str                tooltip_text                       the text to show in tooltip.


tk_canvas
property: tk_canvas
Returns the underlying tkiner Canvas widget

 Type                  Name                     Meaning

                       return                   The tkinter canvas widget


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()




Checkbox Element                                                                                             v: latest 

 Checkbox Element - Displays a checkbox and text next to it
 Checkbox(text,
   default=False,
   size=(None, None),
   auto_size_text=None,
   font=None,
   background_color=None,
   text_color=None,
   change_submits=False,
   enable_events=False,
   disabled=False,
   key=None,
   pad=None,
   tooltip=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                          Name               Meaning

 str                           text               Text to display next to checkbox

 bool                          default            Set to True if you want this checkbox initially checked

 Tuple[int, int]               size               (width, height) width = characters-wide, height =
                                                  rows-high

 bool                          auto_size_text     if True will size the element to match the length of the
                                                  text

 Union[str, Tuple[str, int]]   font               speciﬁes the font family, size, etc

 str                           background_color   color of background

 str                           text_color         color of the text

 bool                          change_submits     DO NOT USE. Only listed for backwards compat - Use
                                                  enable_events instead

 bool                          enable_events      Turns on the element speciﬁc events. Checkbox
                                                  events happen when an item changes

 bool                          disabled           set disable state

 Any                           key                Used with window.FindElement and with return
                                                  values to uniquely identify this element  v: latest 
 Type                                            Name                 Meaning

 (int, int) or ((int, int),(int,int)) or (int,   pad                  Amount of padding to put around element (left/right,
 (int,int)) or ((int, int),int)                                       top/bottom) or ((left, right), (top, bottom))

 str                                             tooltip              text, that will appear when mouse hovers over the
                                                                      element

 bool                                            visible              set visibility state of the element

 Any                                             metadata             User metadata that can be set to ANYTHING


Get
Return the current state of this checkbox

Get()


 Type                     Name                      Meaning

                          return                    Current state of checkbox


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type            Name              Meaning

 bool            force             if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:
                                                                                                                  v: latest 
 Type                    Name                               Meaning
 Type                Name                            Meaning

 str                 tooltip_text                    the text to show in tooltip.


Update
Changes some of the settings for the Checkbox Element. Must call Window.Read or Window.Finalize prior.
Note that changing visibility may cause element to change locations when made visible after invisible

 Update(value=None,
   text=None,
   background_color=None,
   text_color=None,
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type     Name                      Meaning

 bool     value                     if True checks the checkbox, False clears it

 str      text                      Text to display next to checkbox

 str      background_color          color of background

 str      text_color                color of the text. Note this also changes the color of the checkmark

 bool     disabled                  disable or enable element

 bool     visible                   control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions
                                                                                                            v: latest 
 expand(expand_x=False,
   expand_y=False,
   expand_row=True)
get
Return the current state of this checkbox

get()


 Type                 Name                     Meaning

                      return                   Current state of checkbox


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                    Meaning

                  return                  width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type         Name             Meaning
                                                                                                          v: latest 

 bool         force            if True will call focus_force otherwise calls focus_set
set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                 Name         Meaning

 Tuple[int, int]      size         The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                               Meaning

 str                tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Checkbox Element. Must call Window.Read or Window.Finalize prior.
                                                                                                       v: latest 
Note that changing visibility may cause element to change locations when made visible after invisible
 update(value=None,
   text=None,
   background_color=None,
   text_color=None,
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type     Name                       Meaning

 bool     value                      if True checks the checkbox, False clears it

 str      text                       Text to display next to checkbox

 str      background_color           color of background

 str      text_color                 color of the text. Note this also changes the color of the checkmark

 bool     disabled                   disable or enable element

 bool     visible                    control visibility of element



Column Element
 A container element that is used to create a layout within your window's layout



 Column(layout,
   background_color=None,
   size=(None, None),
   pad=None,
   scrollable=False,
   vertical_scroll_only=False,
   right_click_menu=None,
   key=None,
   visible=True,
   justiﬁcation="left",
   element_justiﬁcation="left",
   metadata=None)


Parameter Descriptions:

 Type                             Name                     Meaning
                                                                                                                v: latest 
 List[List[Element]]              layout                   Layout that will be shown in the Column container
 Type                               Name                    Meaning

 str                                background_color        color of background of entire Column

 Tuple[int, int]                    size                    (width, height) size in pixels (doesn't work quite right,
                                                            sometimes only 1 dimension is set by tkinter

 (int, int) or ((int, int),         pad                     Amount of padding to put around element (left/right,
 (int,int)) or (int,(int,int)) or                           top/bottom) or ((left, right), (top, bottom))
 ((int, int),int)

 bool                               scrollable              if True then scrollbars will be added to the column

 bool                               vertical_scroll_only    if Truen then no horizontal scrollbar will be shown

 List[List[Union[List[str],str]]]   right_click_menu        A list of lists of Menu items to show when this element is
                                                            right clicked. See user docs for exact format.

 any                                key                     Value that uniquely identiﬁes this element from all other
                                                            elements. Used when Finding an element or in return
                                                            values. Must be unique to the window

 bool                               visible                 set visibility state of the element

 str                                justiﬁcation            set justiﬁcation for the Column itself. Note entire row
                                                            containing the Column will be affected

 str                                element_justiﬁcation    All elements inside the Column will have this justiﬁcation
                                                            'left', 'right', 'center' are valid values

 Any                                metadata                User metadata that can be set to ANYTHING


AddRow
Not recommended user call. Used to add rows of Elements to the Column Element.

 AddRow(args=*<1 or N object>)


Parameter Descriptions:

 Type                               Name               Meaning

 List[Element]                      *args              The list of elements for this row
                                                                                                                   v: latest 


Layout
Can use like the Window.Layout method, but it's better to use the layout parameter when creating

 Layout(rows)


Parameter Descriptions:

 Type                                          Name                     Meaning

 List[List[Element]]                           rows                     The rows of Elements

 (Column)                                      RETURN                   Used for chaining


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Column Element. Must call Window.Read or Window.Finalize prior

 Update(visible=None)
                                                                                                          v: latest 
Parameter Descriptions:
 Type               Name                     Meaning

 bool               visible                  control visibility of element


add_row
Not recommended user call. Used to add rows of Elements to the Column Element.

 add_row(args=*<1 or N object>)


Parameter Descriptions:

 Type                             Name              Meaning

 List[Element]                    *args             The list of elements for this row


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                    Meaning

                  return                  width and height of the element

                                                                                                          v: latest 
hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



layout
Can use like the Window.Layout method, but it's better to use the layout parameter when creating

 layout(rows)


Parameter Descriptions:

 Type                                          Name                     Meaning

 List[List[Element]]                           rows                     The rows of Elements

 (Column)                                      RETURN                   Used for chaining


set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.
                                                                                                             v: latest 
 set_size(size=(None, None))


Parameter Descriptions:
 Type                 Name         Meaning

 Tuple[int, int]      size         The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                               Meaning

 str                tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Column Element. Must call Window.Read or Window.Finalize prior

 update(visible=None)


Parameter Descriptions:

 Type                Name                      Meaning

 bool                visible                   control visibility of element
                                                                                                             v: latest 


Combo Element
 ComboBox Element - A combination of a single-line input and a drop-down menu. User can type in their own value or choo


 Combo(values,
   default_value=None,
   size=(None, None),
   auto_size_text=None,
   background_color=None,
   text_color=None,
   change_submits=False,
   enable_events=False,
   disabled=False,
   key=None,
   pad=None,
   tooltip=None,
   readonly=False,
   font=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                      Name               Meaning

 List[Any] or              values             values to choose. While displayed as text, the items returned are what
 Tuple[Any]                                   the caller supplied, not text

 Any                       default_value      Choice to be displayed as initial value. Must match one of values
                                              variable contents

 Tuple[int, int] (width,   size               width = characters-wide, height = rows-high
 height)

 bool                      auto_size_text     True if element should be the same size as the contents

 str                       background_color   color of background

 str                       text_color         color of the text

 bool                      change_submits     DEPRICATED DO NOT USE. Use enable_events instead

 bool                      enable_events      Turns on the element speciﬁc events. Combo event is when a choice
                                              is made

 bool                      disabled           set disable state for element
                                                                                                             v: latest 
 Union[str, Tuple[str,     font               speciﬁes the font family, size, etc
 int]]
 Type                       Name                    Meaning

 bool                       visible                 set visibility state of the element

 Any                        metadata                User metadata that can be set to ANYTHING


Get
Returns the current (right now) value of the Combo. DO NOT USE THIS AS THE NORMAL WAY OF READING A
COMBO! You should be using values from your call to window.Read instead. Know what you're doing if you use it.

Get()


 Type          Name                   Meaning

               return                 Returns the value of what is currently chosen


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                                Meaning

 str                  tooltip_text                        the text to show in tooltip.

                                                                                                          v: latest 
Update
Changes some of the settings for the Combo Element. Must call Window.Read or Window.Finalize prior
 Update(value=None,
   values=None,
   set_to_index=None,
   disabled=None,
   readonly=None,
   font=None,
   visible=None)


Parameter Descriptions:

 Type                     Name           Meaning

 Any                      value          change which value is current selected hased on new list of previous list of
                                         choices

 List[Any]                values         change list of choices

 int                      set_to_index   change selection to a particular choice starting with index = 0

 bool                     disabled       disable or enable state of the element

 bool                     readonly       if True make element readonly (user cannot change any choices)

 Union[str, Tuple[str,    font           speciﬁes the font family, size, etc
 int]]

 bool                     visible        control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)


                                                                                                            v: latest 
get
Returns the current (right now) value of the Combo. DO NOT USE THIS AS THE NORMAL WAY OF READING A
COMBO! You should be using values from your call to window.Read instead. Know what you're doing if you use it.

get()


 Type          Name            Meaning

               return          Returns the value of what is currently chosen


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                 Meaning

                  return               width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type         Name          Meaning
                                                                                                          v: latest 
 bool         force         if True will call focus_force otherwise calls focus_set
set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                 Name         Meaning

 Tuple[int, int]      size         The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                               Meaning

 str                tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Combo Element. Must call Window.Read or Window.Finalize prior
                                                                                                             v: latest 
 update(value=None,
   values=None,
   set_to_index=None,
   disabled=None,
   readonly=None,
   font=None,
   visible=None)


Parameter Descriptions:

 Type                     Name           Meaning

 Any                      value          change which value is current selected hased on new list of previous list of
                                         choices

 List[Any]                values         change list of choices

 int                      set_to_index   change selection to a particular choice starting with index = 0

 bool                     disabled       disable or enable state of the element

 bool                     readonly       if True make element readonly (user cannot change any choices)

 Union[str, Tuple[str,    font           speciﬁes the font family, size, etc
 int]]

 bool                     visible        control visibility of element



Frame Element
 A Frame Element that contains other Elements. Encloses with a line around elements and a text label.




                                                                                                            v: latest 
 Frame(title,
   layout,
   title_color=None,
   background_color=None,
   title_location=None,
   relief="groove",
   size=(None, None),
   font=None,
   pad=None,
   border_width=None,
   key=None,
   tooltip=None,
   right_click_menu=None,
   visible=True,
   element_justiﬁcation="left",
   metadata=None)


Parameter Descriptions:

 Type                               Name               Meaning

 str                                title              text that is displayed as the Frame's "label" or title

 List[List[Elements]]               layout             The layout to put inside the Frame

 str                                title_color        color of the title text

 str                                background_color   background color of the Frame

 enum                               title_location     location to place the text title. Choices include:
                                                       TITLE_LOCATION_TOP TITLE_LOCATION_BOTTOM
                                                       TITLE_LOCATION_LEFT TITLE_LOCATION_RIGHT
                                                       TITLE_LOCATION_TOP_LEFT TITLE_LOCATION_TOP_RIGHT
                                                       TITLE_LOCATION_BOTTOM_LEFT
                                                       TITLE_LOCATION_BOTTOM_RIGHT

 enum                               relief             relief style. Values are same as other elements with reliefs.
                                                       Choices include RELIEF_RAISED RELIEF_SUNKEN
                                                       RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE
                                                       RELIEF_SOLID

 Tuple[int, int]                    size               (width, height) (note this parameter may not always work)

 Union[str, Tuple[str, int]]        font               speciﬁes the font family, size, etc

 (int, int) or ((int, int),         pad                                                                  v: latest 
                                                       Amount of padding to put around element (left/right,
 (int,int)) or (int,(int,int)) or                      top/bottom) or ((left, right), (top, bottom))
 ((int, int),int)
 Type                               Name                    Meaning

 int                                border_width            width of border around element in pixels

 any                                key                     Value that uniquely identiﬁes this element from all other
                                                            elements. Used when Finding an element or in return
                                                            values. Must be unique to the window

 str                                tooltip                 text, that will appear when mouse hovers over the element

 List[List[Union[List[str],str]]]   right_click_menu        A list of lists of Menu items to show when this element is
                                                            right clicked. See user docs for exact format.

 bool                               visible                 set visibility state of the element

 str                                element_justiﬁcation    All elements inside the Frame will have this justiﬁcation
                                                            'left', 'right', 'center' are valid values

 Any                                metadata                User metadata that can be set to ANYTHING


AddRow
Not recommended user call. Used to add rows of Elements to the Frame Element.

 AddRow(args=*<1 or N object>)


Parameter Descriptions:

 Type                               Name               Meaning

 List[Element]                      *args              The list of elements for this row


Layout
Can use like the Window.Layout method, but it's better to use the layout parameter when creating

 Layout(rows)


Parameter Descriptions:

 Type                                          Name                      Meaning

 List[List[Element]]                           rows                      The rows of Elements                   v: latest 

 (Frame)                                       RETURN                    Used for chaining
SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Frame Element. Must call Window.Read or Window.Finalize prior

 Update(value=None, visible=None)


Parameter Descriptions:

 Type              Name                  Meaning

 Any               value                 New text value to show on frame

 bool              visible               control visibility of element


add_row
Not recommended user call. Used to add rows of Elements to the Frame Element.
                                                                                                          v: latest 
 add_row(args=*<1 or N object>)


Parameter Descriptions:
 Type                             Name              Meaning

 List[Element]                    *args             The list of elements for this row


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                    Meaning

                  return                  width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



layout
Can use like the Window.Layout method, but it's better to use the layout parameter when creating

 layout(rows)                                                                                             v: latest 

Parameter Descriptions:
 Type                                          Name                     Meaning

 List[List[Element]]                           rows                     The rows of Elements

 (Frame)                                       RETURN                   Used for chaining


set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').
                                                                                                             v: latest 
 set_tooltip(tooltip_text)


Parameter Descriptions:
 Type              Name                               Meaning

 str               tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Frame Element. Must call Window.Read or Window.Finalize prior

 update(value=None, visible=None)


Parameter Descriptions:

 Type             Name                  Meaning

 Any              value                 New text value to show on frame

 bool             visible               control visibility of element



Graph Element
 Creates an area for you to draw on. The MAGICAL property this Element has is that you interact
 with the element using your own coordinate system. This is an important point!! YOU deﬁne where the location
 is for (0,0). Want (0,0) to be in the middle of the graph like a math 4-quadrant graph? No problem! Set your
 lower left corner to be (-100,-100) and your upper right to be (100,100) and you've got yourself a graph with
 (0,0) at the center.
 One of THE coolest of the Elements.
 You can also use ﬂoat values. To do so, be sure and set the ﬂoat_values parameter.
 Mouse click and drag events are possible and return the (x,y) coordinates of the mouse
 Drawing primitives return an "id" that is referenced when you want to operation on that item (e.g. to erase it)  v: latest 
 Graph(canvas_size,
   graph_bottom_left,
   graph_top_right,
   background_color=None,
   pad=None,
   change_submits=False,
   drag_submits=False,
   enable_events=False,
   key=None,
   tooltip=None,
   right_click_menu=None,
   visible=True,
   ﬂoat_values=False,
   metadata=None)


Parameter Descriptions:

 Type                                   Name                Meaning

 Tuple[int, int]                        canvas_size         (width, height) size of the canvas area in pixels

 Tuple[int, int]                        graph_bottom_left   (x,y) The bottoms left corner of your coordinate system

 Tuple[int, int]                        graph_top_right     (x,y) The top right corner of your coordinate system

 str                                    background_color    background color of the drawing area

 (int, int) or ((int, int),(int,int))   pad                 Amount of padding to put around element (left/right,
 or (int,(int,int)) or ((int,                               top/bottom) or ((left, right), (top, bottom))
 int),int)

 bool                                   change_submits      * DEPRICATED DO NOT USE! Same as enable_events

 bool                                   drag_submits        if True and Events are enabled for the Graph, will report Events
                                                            any time the mouse moves while button down

 bool                                   enable_events       If True then clicks on the Graph are immediately reported as
                                                            an event. Use this instead of change_submits

 any                                    key                 Value that uniquely identiﬁes this element from all other
                                                            elements. Used when Finding an element or in return values.
                                                            Must be unique to the window

 str                                    tooltip             text, that will appear when mouse hovers over the element

 List[List[Union[List[str],str]]]       right_click_menu    A list of lists of Menu items to show when this element v: latest
                                                                                                                  is  right 
                                                            clicked. See user docs for exact format.
 Type                            Name                 Meaning

 bool                            visible              set visibility state of the element (Default = True)

 bool                            ﬂoat_values          If True x,y coordinates are returned as ﬂoats, not ints

 Any                             metadata             User metadata that can be set to ANYTHING


BringFigureToFront
Changes Z-order of ﬁgures on the Graph. Brings the indicated ﬁgure to the front of all other drawn ﬁgures

 BringFigureToFront(ﬁgure)


Parameter Descriptions:

 Type       Name           Meaning

 int        ﬁgure          value returned by tkinter when creating the ﬁgure / drawing


DeleteFigure
Remove from the Graph the ﬁgure represented by id. The id is given to you anytime you call a drawing primitive

 DeleteFigure(id)


Parameter Descriptions:

 Type      Name           Meaning

 int       id             the id returned to you when calling one of the drawing methods


DrawArc
Draws different types of arcs. Uses a "bounding box" to deﬁne location

 DrawArc(top_left,
   bottom_right,
   extent,
   start_angle,
   style=None,
   arc_color="black",
   line_width=1)
                                                                                                                 v: latest 

Parameter Descriptions:
 Type                          Name                Meaning

 Union[Tuple[int, int],        top_left            the top left point of bounding rectangle
 Tuple[ﬂoat, ﬂoat]]

 Union[Tuple[int, int],        bottom_right        the bottom right point of bounding rectangle
 Tuple[ﬂoat, ﬂoat]]

 ﬂoat                          extent              Andle to end drawing. Used in conjunction with start_angle

 ﬂoat                          start_angle         Angle to begin drawing. Used in conjunction with extent

 str                           style               Valid choices are One of these Style strings- 'pieslice', 'chord', 'arc',
                                                   'ﬁrst', 'last', 'butt', 'projecting', 'round', 'bevel', 'miter'

 str                           arc_color           color to draw arc with

 Union[int, None]              RETURN              id returned from tkinter that you'll need if you want to manipulate the
                                                   arc


DrawCircle
Draws a circle, cenetered at the location provided. Can set the ﬁll and outline colors

 DrawCircle(center_location,
   radius,
   ﬁll_color=None,
   line_color="black",
   line_width=1)


Parameter Descriptions:

 Type                                     Name                Meaning

 Union [Tuple[int, int], Tuple[ﬂoat,      center_location     Center location using USER'S coordinate system
 ﬂoat]]

 Union[int, ﬂoat]                         radius              Radius in user's coordinate values.

 str                                      ﬁll_color           color of the point to draw

 str                                      line_color          color of the outer line that goes around the circle (sorry, can't
                                                              set thickness)
                                                                                                                        v: latest 
 int                                      line_width          width of the line around the circle, the outline, in pixels
 Type                                 Name             Meaning

 Union[int, None]                     RETURN           id returned from tkinter that you'll need if you want to
                                                       manipulate the circle


DrawImage
Places an image onto your canvas. It's a really important method for this element as it enables so much

 DrawImage(ﬁlename=None,
   data=None,
   location=(None, None),
   color="black",
   font=None,
   angle=0)


Parameter Descriptions:

 Type                                  Name       Meaning

 str                                   ﬁlename    if image is in a ﬁle, path and ﬁlename for the image. (GIF and PNG
                                                  only!)

 Union[str, bytes]                     data       if image is in Base64 format or raw? format then use instead of
                                                  ﬁlename

 Union[Tuple[int, int], Tuple[ﬂoat,    location   the (x,y) location to place image's top left corner
 ﬂoat]]

 str                                   color      text color

 Union[str, Tuple[str, int]]           font       speciﬁes the font family, size, etc

 ﬂoat                                  angle      Angle 0 to 360 to draw the text. Zero represents horizontal text

 Union[int, None]                      RETURN     id returned from tkinter that you'll need if you want to manipulate
                                                  the image


DrawLine
Draws a line from one point to another point using USER'S coordinates. Can set the color and width of line

 DrawLine(point_from,
   point_to,                                                                                                  v: latest 
   color="black",
   width=1)
Parameter Descriptions:

 Type                                 Name         Meaning

 Union[Tuple[int, int], Tuple[ﬂoat,   point_from   Starting point for line
 ﬂoat]]

 Union[Tuple[int, int], Tuple[ﬂoat,   point_to     Ending point for line
 ﬂoat]]

 str                                  color        Color of the line

 int                                  width        width of line in pixels

 Union[int, None]                     RETURN       id returned from tktiner or None if user closed the window. id is
                                                   used when you


DrawOval
Draws an oval based on coordinates in user coordinate system. Provide the location of a "bounding rectangle"

 DrawOval(top_left,
   bottom_right,
   ﬁll_color=None,
   line_color=None,
   line_width=1)


Parameter Descriptions:

 Type                                 Name            Meaning

 Union[Tuple[int, int], Tuple[ﬂoat,   top_left        the top left point of bounding rectangle
 ﬂoat]]

 Union[Tuple[int, int], Tuple[ﬂoat,   bottom_right    the bottom right point of bounding rectangle
 ﬂoat]]

 str                                  ﬁll_color       color of the interrior

 str                                  line_color      color of outline of oval

 int                                  line_width      width of the line around the oval, the outline, in pixels

 Union[int, None]                     RETURN          id returned from tkinter that you'll need if you want to
                                                      manipulate the oval                                       v: latest 
DrawPoint
Draws a "dot" at the point you specify using the USER'S coordinate system

 DrawPoint(point,
   size=2,
   color="black")


Parameter Descriptions:

 Type                                  Name         Meaning

 Union [Tuple[int, int], Tuple[ﬂoat,   point        Center location using USER'S coordinate system
 ﬂoat]]

 Union[int, ﬂoat]                      size         Radius? (Or is it the diameter?) in user's coordinate values.

 str                                   color        color of the point to draw

 Union[int, None]                      RETURN       id returned from tkinter that you'll need if you want to manipulate
                                                    the point


DrawPolygon
Draw a polygon given list of points

 DrawPolygon(points,
   ﬁll_color=None,
   line_color=None,
   line_width=None)


Parameter Descriptions:

 Type                                  Name           Meaning

 List[Union[Tuple[int, int],           points         list of points that deﬁne the polygon
 Tuple[ﬂoat, ﬂoat]]]

 str                                   ﬁll_color      color of the interior

 str                                   line_color     color of outline

 int                                   line_width     width of the line in pixels

 Union[int, None]                      RETURN         id returned from tkinter that you'll need if you want to  v: latest 
                                                      manipulate the rectangle
DrawRectangle
Draw a rectangle given 2 points. Can control the line and ﬁll colors

 DrawRectangle(top_left,
   bottom_right,
   ﬁll_color=None,
   line_color=None,
   line_width=None)


Parameter Descriptions:

 Type                           Name            Meaning

 Union[Tuple[int, int],         top_left        the top left point of rectangle
 Tuple[ﬂoat, ﬂoat]]

 Union[Tuple[int, int],         bottom_right    the bottom right point of rectangle
 Tuple[ﬂoat, ﬂoat]]

 str                            ﬁll_color       color of the interior

 str                            line_color      color of outline

 int                            line_width      width of the line in pixels

 Union[int, None]               RETURN          Union[int, None] id returned from tkinter that you'll need if you want
                                                to manipulate the rectangle


DrawText
Draw some text on your graph. This is how you label graph number lines for example

 DrawText(text,
   location,
   color="black",
   font=None,
   angle=0,
   text_location="center")


Parameter Descriptions:

 Type                                Name            Meaning

 str                                 text            text to display                                         v: latest 
 Type                                    Name               Meaning

 Union[Tuple[int, int], Tuple[ﬂoat,      location           location to place ﬁrst letter
 ﬂoat]]

 str                                     color              text color

 Union[str, Tuple[str, int]]             font               speciﬁes the font family, size, etc

 ﬂoat                                    angle              Angle 0 to 360 to draw the text. Zero represents horizontal text

 enum                                    text_location      "anchor" location for the text. Values start with
                                                            TEXT_LOCATION_

 Union[int, None]                        RETURN             id returned from tkinter that you'll need if you want to
                                                            manipulate the text


Erase
Erase the Graph - Removes all ﬁgures previously "drawn" using the Graph methods (e.g. DrawText)

 Erase()



GetBoundingBox
Given a ﬁgure, returns the upper left and lower right bounding box coordinates

 GetBoundingBox(ﬁgure)


Parameter Descriptions:

 Type                                                           Name        Meaning

 object                                                         ﬁgure       a previously drawing ﬁgure

 Union[Tuple[int, int, int, int], Tuple[ﬂoat, ﬂoat, ﬂoat,       RETURN      upper left x, upper left y, lower right x, lower
 ﬂoat]]                                                                     right y


GetFiguresAtLocation
Returns a list of ﬁgures located at a particular x,y location within the Graph

 GetFiguresAtLocation(location)                                                                                         v: latest 


Parameter Descriptions:
 Type                                     Name        Meaning

 Union[Tuple[int, int], Tuple[ﬂoat,       location    point to check
 ﬂoat]]

 List[int]                                RETURN      a list of previously drawn "Figures" (returned from the drawing
                                                      primitives)


Move
Moves the entire drawing area (the canvas) by some delta from the current position. Units are indicated in your
coordinate system indicated number of ticks in your coordinate system

 Move(x_direction, y_direction)


Parameter Descriptions:

 Type                     Name                 Meaning

 Union[int, ﬂoat]         x_direction          how far to move in the "X" direction in your coordinates

 Union[int, ﬂoat]         y_direction          how far to move in the "Y" direction in your coordinates


MoveFigure
Moves a previously drawn ﬁgure using a "delta" from current position

 MoveFigure(ﬁgure,
  x_direction,
  y_direction)


Parameter Descriptions:

 Type                 Name              Meaning

 id                   ﬁgure             Previously obtained ﬁgure-id. These are returned from all Draw methods

 Union[int, ﬂoat]     x_direction       delta to apply to position in the X direction

 Union[int, ﬂoat]     y_direction       delta to apply to position in the Y direction


RelocateFigure                                                                                                  v: latest 
Move a previously made ﬁgure to an arbitrary (x,y) location. This differs from the Move methods because it uses
absolute coordinates versus relative for Move
 RelocateFigure(ﬁgure,
   x,
   y)


Parameter Descriptions:

 Type                 Name      Meaning

 id                   ﬁgure     Previously obtained ﬁgure-id. These are returned from all Draw methods

 Union[int, ﬂoat]     x         location on X axis (in user coords) to move the upper left corner of the ﬁgure

 Union[int, ﬂoat]     y         location on Y axis (in user coords) to move the upper left corner of the ﬁgure


SendFigureToBack
Changes Z-order of ﬁgures on the Graph. Sends the indicated ﬁgure to the back of all other drawn ﬁgures

 SendFigureToBack(ﬁgure)


Parameter Descriptions:

 Type        Name           Meaning

 int         ﬁgure          value returned by tkinter when creating the ﬁgure / drawing


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name            Meaning

 bool         force           if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').
                                                                                                             v: latest 
 SetTooltip(tooltip_text)
Parameter Descriptions:

 Type             Name                             Meaning

 str              tooltip_text                     the text to show in tooltip.


TKCanvas
property: TKCanvas
Returns the underlying tkiner Canvas widget

 Type               Name                   Meaning

                    return                 The tkinter canvas widget


Update
Changes some of the settings for the Graph Element. Must call Window.Read or Window.Finalize prior

 Update(background_color=None, visible=None)


Parameter Descriptions:

 Type           Name                                      Meaning

 ???            background_color                          color of background

 bool           visible                                   control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



bring_ﬁgure_to_front
Changes Z-order of ﬁgures on the Graph. Brings the indicated ﬁgure to the front of all other drawn ﬁgures

 bring_ﬁgure_to_front(ﬁgure)
                                                                                                             v: latest 
Parameter Descriptions:
 Type         Name         Meaning

 int          ﬁgure        value returned by tkinter when creating the ﬁgure / drawing


change_coordinates
Changes the corrdinate system to a new one. The same 2 points in space are used to deﬁne the coorinate system -
the bottom left and the top right values of your graph.

 change_coordinates(graph_bottom_left, graph_top_right)


Parameter Descriptions:

 Type                      Name                      Meaning

 Tuple[int, int] (x,y)     graph_bottom_left         The bottoms left corner of your coordinate system

 Tuple[int, int] (x,y)     graph_top_right           The top right corner of your coordinate system


delete_ﬁgure
Remove from the Graph the ﬁgure represented by id. The id is given to you anytime you call a drawing primitive

 delete_ﬁgure(id)


Parameter Descriptions:

 Type        Name         Meaning

 int         id           the id returned to you when calling one of the drawing methods


draw_arc
Draws different types of arcs. Uses a "bounding box" to deﬁne location

 draw_arc(top_left,
   bottom_right,
   extent,
   start_angle,
   style=None,
   arc_color="black",
   line_width=1)

                                                                                                          v: latest 
Parameter Descriptions:
 Type                           Name                Meaning

 Union[Tuple[int, int],         top_left            the top left point of bounding rectangle
 Tuple[ﬂoat, ﬂoat]]

 Union[Tuple[int, int],         bottom_right        the bottom right point of bounding rectangle
 Tuple[ﬂoat, ﬂoat]]

 ﬂoat                           extent              Andle to end drawing. Used in conjunction with start_angle

 ﬂoat                           start_angle         Angle to begin drawing. Used in conjunction with extent

 str                            style               Valid choices are One of these Style strings- 'pieslice', 'chord', 'arc',
                                                    'ﬁrst', 'last', 'butt', 'projecting', 'round', 'bevel', 'miter'

 str                            arc_color           color to draw arc with

 Union[int, None]               RETURN              id returned from tkinter that you'll need if you want to manipulate the
                                                    arc


draw_circle
Draws a circle, cenetered at the location provided. Can set the ﬁll and outline colors

 draw_circle(center_location,
   radius,
   ﬁll_color=None,
   line_color="black",
   line_width=1)


Parameter Descriptions:

 Type                                      Name                Meaning

 Union [Tuple[int, int], Tuple[ﬂoat,       center_location     Center location using USER'S coordinate system
 ﬂoat]]

 Union[int, ﬂoat]                          radius              Radius in user's coordinate values.

 str                                       ﬁll_color           color of the point to draw

 str                                       line_color          color of the outer line that goes around the circle (sorry, can't
                                                               set thickness)
                                                                                                                         v: latest 
 int                                       line_width          width of the line around the circle, the outline, in pixels
 Type                                 Name             Meaning

 Union[int, None]                     RETURN           id returned from tkinter that you'll need if you want to
                                                       manipulate the circle


draw_image
Places an image onto your canvas. It's a really important method for this element as it enables so much

 draw_image(ﬁlename=None,
   data=None,
   location=(None, None),
   color="black",
   font=None,
   angle=0)


Parameter Descriptions:

 Type                                  Name       Meaning

 str                                   ﬁlename    if image is in a ﬁle, path and ﬁlename for the image. (GIF and PNG
                                                  only!)

 Union[str, bytes]                     data       if image is in Base64 format or raw? format then use instead of
                                                  ﬁlename

 Union[Tuple[int, int], Tuple[ﬂoat,    location   the (x,y) location to place image's top left corner
 ﬂoat]]

 str                                   color      text color

 Union[str, Tuple[str, int]]           font       speciﬁes the font family, size, etc

 ﬂoat                                  angle      Angle 0 to 360 to draw the text. Zero represents horizontal text

 Union[int, None]                      RETURN     id returned from tkinter that you'll need if you want to manipulate
                                                  the image


draw_line
Draws a line from one point to another point using USER'S coordinates. Can set the color and width of line

 draw_line(point_from,
   point_to,                                                                                                  v: latest 
   color="black",
   width=1)
Parameter Descriptions:

 Type                                 Name         Meaning

 Union[Tuple[int, int], Tuple[ﬂoat,   point_from   Starting point for line
 ﬂoat]]

 Union[Tuple[int, int], Tuple[ﬂoat,   point_to     Ending point for line
 ﬂoat]]

 str                                  color        Color of the line

 int                                  width        width of line in pixels

 Union[int, None]                     RETURN       id returned from tktiner or None if user closed the window. id is
                                                   used when you


draw_oval
Draws an oval based on coordinates in user coordinate system. Provide the location of a "bounding rectangle"

 draw_oval(top_left,
   bottom_right,
   ﬁll_color=None,
   line_color=None,
   line_width=1)


Parameter Descriptions:

 Type                                 Name            Meaning

 Union[Tuple[int, int], Tuple[ﬂoat,   top_left        the top left point of bounding rectangle
 ﬂoat]]

 Union[Tuple[int, int], Tuple[ﬂoat,   bottom_right    the bottom right point of bounding rectangle
 ﬂoat]]

 str                                  ﬁll_color       color of the interrior

 str                                  line_color      color of outline of oval

 int                                  line_width      width of the line around the oval, the outline, in pixels

 Union[int, None]                     RETURN          id returned from tkinter that you'll need if you want to
                                                      manipulate the oval                                       v: latest 
draw_point
Draws a "dot" at the point you specify using the USER'S coordinate system

 draw_point(point,
   size=2,
   color="black")


Parameter Descriptions:

 Type                                  Name         Meaning

 Union [Tuple[int, int], Tuple[ﬂoat,   point        Center location using USER'S coordinate system
 ﬂoat]]

 Union[int, ﬂoat]                      size         Radius? (Or is it the diameter?) in user's coordinate values.

 str                                   color        color of the point to draw

 Union[int, None]                      RETURN       id returned from tkinter that you'll need if you want to manipulate
                                                    the point


draw_polygon
Draw a polygon given list of points

 draw_polygon(points,
   ﬁll_color=None,
   line_color=None,
   line_width=None)


Parameter Descriptions:

 Type                                  Name           Meaning

 List[Union[Tuple[int, int],           points         list of points that deﬁne the polygon
 Tuple[ﬂoat, ﬂoat]]]

 str                                   ﬁll_color      color of the interior

 str                                   line_color     color of outline

 int                                   line_width     width of the line in pixels

 Union[int, None]                      RETURN         id returned from tkinter that you'll need if you want to  v: latest 
                                                      manipulate the rectangle
draw_rectangle
Draw a rectangle given 2 points. Can control the line and ﬁll colors

 draw_rectangle(top_left,
   bottom_right,
   ﬁll_color=None,
   line_color=None,
   line_width=None)


Parameter Descriptions:

 Type                           Name            Meaning

 Union[Tuple[int, int],         top_left        the top left point of rectangle
 Tuple[ﬂoat, ﬂoat]]

 Union[Tuple[int, int],         bottom_right    the bottom right point of rectangle
 Tuple[ﬂoat, ﬂoat]]

 str                            ﬁll_color       color of the interior

 str                            line_color      color of outline

 int                            line_width      width of the line in pixels

 Union[int, None]               RETURN          Union[int, None] id returned from tkinter that you'll need if you want
                                                to manipulate the rectangle


draw_text
Draw some text on your graph. This is how you label graph number lines for example

 draw_text(text,
   location,
   color="black",
   font=None,
   angle=0,
   text_location="center")


Parameter Descriptions:

 Type                                Name            Meaning

 str                                 text            text to display                                         v: latest 
 Type                                    Name               Meaning

 Union[Tuple[int, int], Tuple[ﬂoat,      location           location to place ﬁrst letter
 ﬂoat]]

 str                                     color              text color

 Union[str, Tuple[str, int]]             font               speciﬁes the font family, size, etc

 ﬂoat                                    angle              Angle 0 to 360 to draw the text. Zero represents horizontal text

 enum                                    text_location      "anchor" location for the text. Values start with
                                                            TEXT_LOCATION_

 Union[int, None]                        RETURN             id returned from tkinter that you'll need if you want to
                                                            manipulate the text


erase
Erase the Graph - Removes all ﬁgures previously "drawn" using the Graph methods (e.g. DrawText)

 erase()



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_bounding_box
Given a ﬁgure, returns the upper left and lower right bounding box coordinates

 get_bounding_box(ﬁgure)


Parameter Descriptions:

 Type                                                           Name        Meaning

 object                                                         ﬁgure       a previously drawing ﬁgure
                                                                                                                        v: latest 
 Union[Tuple[int, int, int, int], Tuple[ﬂoat, ﬂoat, ﬂoat,       RETURN      upper left x, upper left y, lower right x, lower
 ﬂoat]]                                                                     right y
get_ﬁgures_at_location
Returns a list of ﬁgures located at a particular x,y location within the Graph

 get_ﬁgures_at_location(location)


Parameter Descriptions:

 Type                                  Name        Meaning

 Union[Tuple[int, int], Tuple[ﬂoat,    location    point to check
 ﬂoat]]

 List[int]                             RETURN      a list of previously drawn "Figures" (returned from the drawing
                                                   primitives)


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

 get_size()


 Type              Name                 Meaning

                   return               width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



move
Moves the entire drawing area (the canvas) by some delta from the current position. Units are indicated in your
coordinate system indicated number of ticks in your coordinate system

 move(x_direction, y_direction)


Parameter Descriptions:
                                                                                                             v: latest 
 Type                     Name              Meaning
 Type                     Name                 Meaning

 Union[int, ﬂoat]         x_direction          how far to move in the "X" direction in your coordinates

 Union[int, ﬂoat]         y_direction          how far to move in the "Y" direction in your coordinates


move_ﬁgure
Moves a previously drawn ﬁgure using a "delta" from current position

 move_ﬁgure(ﬁgure,
  x_direction,
  y_direction)


Parameter Descriptions:

 Type                Name               Meaning

 id                  ﬁgure              Previously obtained ﬁgure-id. These are returned from all Draw methods

 Union[int, ﬂoat]    x_direction        delta to apply to position in the X direction

 Union[int, ﬂoat]    y_direction        delta to apply to position in the Y direction


relocate_ﬁgure
Move a previously made ﬁgure to an arbitrary (x,y) location. This differs from the Move methods because it uses
absolute coordinates versus relative for Move

 relocate_ﬁgure(ﬁgure,
   x,
   y)


Parameter Descriptions:

 Type                Name      Meaning

 id                  ﬁgure     Previously obtained ﬁgure-id. These are returned from all Draw methods

 Union[int, ﬂoat]    x         location on X axis (in user coords) to move the upper left corner of the ﬁgure

 Union[int, ﬂoat]    y         location on Y axis (in user coords) to move the upper left corner of the ﬁgure

                                                                                                            v: latest 
send_ﬁgure_to_back
Changes Z-order of ﬁgures on the Graph. Sends the indicated ﬁgure to the back of all other drawn ﬁgures
 send_ﬁgure_to_back(ﬁgure)


Parameter Descriptions:

 Type         Name            Meaning

 int          ﬁgure           value returned by tkinter when creating the ﬁgure / drawing


set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name        Meaning

 Tuple[int, int]       size        The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Objectsuch   as: 
                                                                                                             v: latest
window.Element('key').SetToolTip('New tip').
 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                            Meaning

 str                tooltip_text                    the text to show in tooltip.


tk_canvas
property: tk_canvas
Returns the underlying tkiner Canvas widget

 Type                  Name                 Meaning

                       return               The tkinter canvas widget


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Graph Element. Must call Window.Read or Window.Finalize prior

 update(background_color=None, visible=None)


Parameter Descriptions:

 Type            Name                                      Meaning

 ???             background_color                          color of background
                                                                                                             v: latest 

 bool            visible                                   control visibility of element
Image Element
 Image Element - show an image in the window. Should be a GIF or a PNG only



 Image(ﬁlename=None,
   data=None,
   background_color=None,
   size=(None, None),
   pad=None,
   key=None,
   tooltip=None,
   right_click_menu=None,
   visible=True,
   enable_events=False,
   metadata=None)


Parameter Descriptions:

 Type                                      Name               Meaning

 str                                       ﬁlename            image ﬁlename if there is a button image. GIFs and PNGs
                                                              only.

 Union[bytes, str]                         data               Raw or Base64 representation of the image to put on
                                                              button. Choose either ﬁlename or data

                                           background_color   color of background

 Tuple[int, int]                           size               (width, height) size of image in pixels

 (int, int) or ((int, int),(int,int)) or   pad                Amount of padding to put around element (left/right,
 (int,(int,int)) or ((int, int),int)                          top/bottom) or ((left, right), (top, bottom))

 Any                                       key                Used with window.FindElement and with return values to
                                                              uniquely identify this element to uniquely identify this
                                                              element

 str                                       tooltip            text, that will appear when mouse hovers over the element

 List[List[Union[List[str],str]]]          right_click_menu   A list of lists of Menu items to show when this element is
                                                              right clicked. See user docs for exact format.

 bool                                      visible            set visibility state of the element
                                                                                                                v: latest 
 bool                                      enable_events      Turns on the element speciﬁc events. For an Image
                                                              element, the event is "image clicked"
 Type                                  Name                  Meaning

 Any                                   metadata              User metadata that can be set to ANYTHING


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Image Element. Must call Window.Read or Window.Finalize prior

 Update(ﬁlename=None,
   data=None,
   size=(None, None),
   visible=None)


Parameter Descriptions:

 Type                                 Name          Meaning

 str                                  ﬁlename       ﬁlename to the new image to display.                  v: latest 


 Union[str, tkPhotoImage]             data          Base64 encoded string OR a tk.PhotoImage object
 Type                             Name             Meaning

 Tuple[int,int]                   size             size of a image (w,h) w=characters-wide, h=rows-high

 bool                             visible          control visibility of element


UpdateAnimation
Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next
frame and will automatically advance to the next frame at the right time. NOTE - does NOT perform a sleep call to
delay

 UpdateAnimation(source, time_between_frames=0)


Parameter Descriptions:

 Type                Name                          Meaning

 Union[str,bytes]    source                        Filename or Base64 encoded string containing Animated GIF

 int                 time_between_frames           Number of milliseconds to wait between showing frames


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()                                                                                                  v: latest 


 Type               Name                 Meaning
 Type              Name                   Meaning

                   return                 width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels
                                                                                                             v: latest 

set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                            Meaning

 str                tooltip_text                    the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Image Element. Must call Window.Read or Window.Finalize prior

 update(ﬁlename=None,
   data=None,
   size=(None, None),
   visible=None)


Parameter Descriptions:

 Type                              Name          Meaning

 str                               ﬁlename       ﬁlename to the new image to display.

 Union[str, tkPhotoImage]          data          Base64 encoded string OR a tk.PhotoImage object

 Tuple[int,int]                    size          size of a image (w,h) w=characters-wide, h=rows-high
                                                                                                             v: latest 
 bool                              visible       control visibility of element
update_animation
Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next
frame and will automatically advance to the next frame at the right time. NOTE - does NOT perform a sleep call to
delay

 update_animation(source, time_between_frames=0)


Parameter Descriptions:

 Type                Name                          Meaning

 Union[str,bytes]    source                        Filename or Base64 encoded string containing Animated GIF

 int                 time_between_frames           Number of milliseconds to wait between showing frames


update_animation_no_buffering
Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next
frame and will automatically advance to the next frame at the right time. NOTE - does NOT perform a sleep call to
delay

 update_animation_no_buffering(source, time_between_frames=0)


Parameter Descriptions:

 Type                Name                          Meaning

 Union[str,bytes]    source                        Filename or Base64 encoded string containing Animated GIF

 int                 time_between_frames           Number of milliseconds to wait between showing frames



InputText Element
 Display a single text input ﬁeld. Based on the tkinter Widget `Entry`




                                                                                                            v: latest 
 InputText(default_text="",
   size=(None, None),
   disabled=False,
   password_char="",
   justiﬁcation=None,
   background_color=None,
   text_color=None,
   font=None,
   tooltip=None,
   change_submits=False,
   enable_events=False,
   do_not_clear=True,
   key=None,
   focus=False,
   pad=None,
   use_readonly_for_disable=True,
   right_click_menu=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                          Name               Meaning

 str                           default_text       Text initially shown in the input box as a default
                                                  value(Default value = '')

 Tuple[int, int] (width,       size               w=characters-wide, h=rows-high
 height)

 bool                          disabled           set disable state for element (Default = False)

 char                          password_char      Password character if this is a password ﬁeld (Default
                                                  value = '')

 str                           justiﬁcation       justiﬁcation for data display. Valid choices - left, right,
                                                  center

 str                           background_color   color of background in one of the color formats

 str                           text_color         color of the text

 Union[str, Tuple[str, int]]   font               speciﬁes the font family, size, etc

 str                           tooltip            text, that will appear when mouse hovers over the
                                                  element                                       v: latest 

 bool                          change_submits     * DEPRICATED DO NOT USE! Same as enable_events
 Type                                 Name                          Meaning

 bool                                 enable_events                 If True then changes to this element are immediately
                                                                    reported as an event. Use this instead of
                                                                    change_submits (Default = False)

 bool                                 do_not_clear                  If False then the ﬁeld will be set to blank after ANY
                                                                    event (button, any event) (Default = True)

 any                                  key                           Value that uniquely identiﬁes this element from all
                                                                    other elements. Used when Finding an element or in
                                                                    return values. Must be unique to the window

 bool                                 focus                         Determines if initial focus should go to this element.

 (int, int) or ((int, int),           pad                           . Amount of padding to put around element. Normally
 (int,int)) or (int,(int,int)) or                                   (horizontal pixels, vertical pixels) but can be split apart
 ((int, int),int)                                                   further into ((horizontal left, horizontal right), (vertical
                                                                    above, vertical below))

 bool                                 use_readonly_for_disable      If True (the default) tkinter state set to 'readonly'.
                                                                    Otherwise state set to 'disabled'

 List[List[Union[List[str],str]]]     right_click_menu              A list of lists of Menu items to show when this element
                                                                    is right clicked. See user docs for exact format.

 bool                                 visible                       set visibility state of the element (Default = True)

 Any                                  metadata                      User metadata that can be set to ANYTHING


Get
Read and return the current value of the input element. Must call Window.Read or Window.Finalize prior

Get()


 Type           Name                Meaning

                return              current value of Input ﬁeld or '' if error encountered


SetFocus
Sets the current focus to be on this element
                                                                                                                       v: latest 

 SetFocus(force=False)
Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Input Element. Must call Window.Read or Window.Finalize prior

 Update(value=None,
   disabled=None,
   select=None,
   visible=None,
   text_color=None,
   background_color=None,
   move_cursor_to="end")


Parameter Descriptions:

 Type            Name                    Meaning

 str             value                   new text to display as default text in Input ﬁeld

 bool            disabled                disable or enable state of the element (sets Entry Widget to readonly or
                                         normal)

 bool            select                  if True, then the text will be selected

 bool            visible                 change visibility of element
                                                                                                              v: latest 
 str             text_color              change color of text being typed
 Type           Name                 Meaning

 str            background_color     change color of the background

 Union[int,     move_cursor_to       Moves the cursor to a particular offset. Defaults to 'end'
 str]


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get
Read and return the current value of the input element. Must call Window.Read or Window.Finalize prior

get()


 Type         Name          Meaning

              return        current value of Input ﬁeld or '' if error encountered


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                Meaning

                  return              width and height of the element
                                                                                                          v: latest 

hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)                                                                                   v: latest 

Parameter Descriptions:
 Type              Name                             Meaning

 str               tooltip_text                     the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Input Element. Must call Window.Read or Window.Finalize prior

 update(value=None,
   disabled=None,
   select=None,
   visible=None,
   text_color=None,
   background_color=None,
   move_cursor_to="end")


Parameter Descriptions:

 Type            Name                 Meaning

 str             value                new text to display as default text in Input ﬁeld

 bool            disabled             disable or enable state of the element (sets Entry Widget to readonly or
                                      normal)

 bool            select               if True, then the text will be selected

 bool            visible              change visibility of element

 str             text_color           change color of text being typed
                                                                                                             v: latest 

 str             background_color     change color of the background
 Type            Name                    Meaning

 Union[int,      move_cursor_to          Moves the cursor to a particular offset. Defaults to 'end'
 str]



Listbox Element
 A List Box. Provide a list of values for the user to choose one or more of. Returns a list of selected rows
 when a window.Read() is executed.



 Listbox(values,
   default_values=None,
   select_mode=None,
   change_submits=False,
   enable_events=False,
   bind_return_key=False,
   size=(None, None),
   disabled=False,
   auto_size_text=None,
   font=None,
   no_scrollbar=False,
   background_color=None,
   text_color=None,
   key=None,
   pad=None,
   tooltip=None,
   right_click_menu=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                             Name                   Meaning

 List[Any] or Tuple[Any]          values                 list of values to display. Can be any type including mixed types
                                                         as long as they have str method

 List[Any]                        default_values         which values should be initially selected

 [enum]                           select_mode            Select modes are used to determine if only 1 item can be
                                                         selected or multiple and how they can be selected. Valid
                                                         choices begin with "LISTBOX_SELECT_MODE_" and include:
                                                         LISTBOX_SELECT_MODE_SINGLE
                                                         LISTBOX_SELECT_MODE_MULTIPLE                          v: latest 
                                                         LISTBOX_SELECT_MODE_BROWSE
                                                         LISTBOX_SELECT_MODE_EXTENDED
 Type                                 Name               Meaning

 bool                                 change_submits     DO NOT USE. Only listed for backwards compat - Use
                                                         enable_events instead

 bool                                 enable_events      Turns on the element speciﬁc events. Listbox generates events
                                                         when an item is clicked

 bool                                 bind_return_key    If True, then the return key will cause a the Listbox to generate
                                                         an event

 Tuple(int, int) (width,              size               width = characters-wide, height = rows-high
 height)

 bool                                 disabled           set disable state for element

 bool                                 auto_size_text     True if element should be the same size as the contents

 Union[str, Tuple[str, int]]          font               speciﬁes the font family, size, etc

 str                                  background_color   color of background

 str                                  text_color         color of the text

 Any                                  key                Used with window.FindElement and with return values to
                                                         uniquely identify this element

 (int, int) or ((int, int),           pad                Amount of padding to put around element (left/right,
 (int,int)) or (int,(int,int)) or                        top/bottom) or ((left, right), (top, bottom))
 ((int, int),int)

 str                                  tooltip            text, that will appear when mouse hovers over the element

 List[List[Union[List[str],str]]]     right_click_menu   A list of lists of Menu items to show when this element is right
                                                         clicked. See user docs for exact format.

 bool                                 visible            set visibility state of the element

 Any                                  metadata           User metadata that can be set to ANYTHING


GetIndexes
Returns the items currently selected as a list of indexes
                                                                                                                 v: latest 
GetIndexes()


 Type           Name                Meaning
 Type         Name             Meaning

              return           A list of offsets into values that is currently selected


GetListValues
Returns list of Values provided by the user in the user's format

 GetListValues()


 Type          Name                  Meaning

               return                List of values. Can be any / mixed types -> []


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                               Meaning

 str                  tooltip_text                       the text to show in tooltip.


SetValue
Set listbox highlighted choices
                                                                                                          v: latest 

 SetValue(values)
Parameter Descriptions:

 Type                Name             Meaning

 List[Any]           values           new values to choose based on previously set values


Update
Changes some of the settings for the Listbox Element. Must call Window.Read or Window.Finalize prior

 Update(values=None,
  disabled=None,
  set_to_index=None,
  scroll_to_index=None,
  select_mode=None,
  visible=None)


Parameter Descriptions:

 Type               Name                Meaning

 List[Any]          values              new list of choices to be shown to user

 bool               disabled            disable or enable state of the element

 Union[int, list,   set_to_index        highlights the item(s) indicated. If parm is an int one entry will be set. If is a list,
 tuple]                                 then each entry in list is highlighted

 int                scroll_to_index     scroll the listbox so that this index is the ﬁrst shown

 str                mode                changes the select mode according to tkinter's listbox widget

 bool               visible             control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
                                                                                                           v: latest 
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions
 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get
Returns the list of items currently selected in this listbox. It should be identical to the value you would receive when
performing a window.read() call.

 get()


 Type     Name         Meaning

          return       The list of currently selected items. The actual items are returned, not the indexes


get_indexes
Returns the items currently selected as a list of indexes

 get_indexes()


 Type         Name             Meaning

              return           A list of offsets into values that is currently selected


get_list_values
Returns list of Values provided by the user in the user's format

 get_list_values()


 Type          Name               Meaning

               return             List of values. Can be any / mixed types -> []


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

 get_size()


 Type              Name                   Meaning
                                                                                                               v: latest 
                   return                 width and height of the element
hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').
                                                                                                             v: latest 

 set_tooltip(tooltip_text)
Parameter Descriptions:

 Type                Name                            Meaning

 str                 tooltip_text                    the text to show in tooltip.


set_value
Set listbox highlighted choices

 set_value(values)


Parameter Descriptions:

 Type                Name           Meaning

 List[Any]           values         new values to choose based on previously set values


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Listbox Element. Must call Window.Read or Window.Finalize prior

 update(values=None,
   disabled=None,
   set_to_index=None,
   scroll_to_index=None,
   select_mode=None,
   visible=None)


Parameter Descriptions:                                                                                      v: latest 


 Type             Name                Meaning
 Type               Name               Meaning

 List[Any]          values             new list of choices to be shown to user

 bool               disabled           disable or enable state of the element

 Union[int, list,   set_to_index       highlights the item(s) indicated. If parm is an int one entry will be set. If is a list,
 tuple]                                then each entry in list is highlighted

 int                scroll_to_index    scroll the listbox so that this index is the ﬁrst shown

 str                mode               changes the select mode according to tkinter's listbox widget

 bool               visible            control visibility of element



Menu Element
 Menu Element is the Element that provides a Menu Bar that goes across the top of the window, just below titlebar.
 Here is an example layout. The "&" are shortcut keys ALT+key.
 Is a List of - "Item String" + List
 Where Item String is what will be displayed on the Menubar itself.
 The List that follows the item represents the items that are shown then Menu item is clicked
 Notice how an "entry" in a mennu can be a list which means it branches out and shows another menu, etc. (resursive)
 menu_def = [['&File', ['!&Open', '&Save::savekey', '---', '&Properties', 'E&xit']],
         ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
         ['&Debugger', ['Popout', 'Launch Debugger']],
         ['&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
         ['&Help', '&About...'], ]
 Finally, "keys" can be added to entries so make them unique. The "Save" entry has a key associated with it. You
 can see it has a "::" which signiﬁes the beginning of a key. The user will not see the key portion when the
 menu is shown. The key portion is returned as part of the event.


 Menu(menu_deﬁnition,
  background_color=None,
  size=(None, None),
  tearoff=False,
  font=None,
  pad=None,
  key=None,
  visible=True,
  metadata=None)


Parameter Descriptions:

 Type                               Name                 Meaning                                                      v: latest 


 List[List[Tuple[str, List[str]]]   menu_deﬁnition       ???
 Type                                   Name                Meaning

 str                                    background_color    color of the background

 Tuple[int, int]                        size                Not used in the tkinter port

 bool                                   tearoff             if True, then can tear the menu off from the window ans use as
                                                            a ﬂoating window. Very cool effect

 (int, int) or ((int, int),(int,int))   pad                 Amount of padding to put around element (left/right,
 or (int,(int,int)) or ((int,                               top/bottom) or ((left, right), (top, bottom))
 int),int)

 any                                    key                 Value that uniquely identiﬁes this element from all other
                                                            elements. Used when Finding an element or in return values.
                                                            Must be unique to the window

 bool                                   visible             set visibility state of the element

 Any                                    metadata            User metadata that can be set to ANYTHING


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type            Name              Meaning

 bool            force             if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                    Name                              Meaning                                                  v: latest 

 str                     tooltip_text                      the text to show in tooltip.
Update
Update a menubar - can change the menu deﬁnition and visibility. The entire menu has to be speciﬁed

 Update(menu_deﬁnition=None, visible=None)


Parameter Descriptions:

 Type                                        Name                        Meaning

 List[List[Tuple[str, List[str]]]            menu_deﬁnition              ???

 bool                                        visible                     control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type                Name             Meaning

                     return           width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an 
                                                                                                          v: latest
element, including the row container
 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:
                                                                                                             v: latest 
 Type                  Name                            Meaning
 Type                Name                           Meaning

 str                 tooltip_text                   the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Update a menubar - can change the menu deﬁnition and visibility. The entire menu has to be speciﬁed

 update(menu_deﬁnition=None, visible=None)


Parameter Descriptions:

 Type                                         Name                          Meaning

 List[List[Tuple[str, List[str]]]             menu_deﬁnition                ???

 bool                                         visible                       control visibility of element



Multiline Element
 Multiline Element - Display and/or read multiple lines of text. This is both an input and output element.
 Other PySimpleGUI ports have a separate MultilineInput and MultilineOutput elements. May want to split this
 one up in the future too.




                                                                                                                v: latest 
 Multiline(default_text="",
  enter_submits=False,
  disabled=False,
  autoscroll=False,
  border_width=None,
  size=(None, None),
  auto_size_text=None,
  background_color=None,
  text_color=None,
  change_submits=False,
  enable_events=False,
  do_not_clear=True,
  key=None,
  focus=False,
  font=None,
  pad=None,
  tooltip=None,
  right_click_menu=None,
  visible=True,
  metadata=None)


Parameter Descriptions:

 Type                         Name               Meaning

 str                          default_text       Initial text to show

 bool                         enter_submits      if True, the Window.Read call will return is enter key is
                                                 pressed in this element

 bool                         disabled           set disable state

 bool                         autoscroll         If True the contents of the element will automatically
                                                 scroll as more data added to the end

 int                          border_width       width of border around element in pixels

 Tuple[int,                   size               int] (width, height) width = characters-wide, height = rows-
                                                 high

 bool                         auto_size_text     if True will size the element to match the length of the text

 str                          background_color   color of background

 str                          text_color         color of the text
                                                                                                      v: latest 
 bool                         chfange_submits    DO NOT USE. Only listed for backwards compat - Use
                                                 enable_events instead
 Type                                      Name               Meaning

 bool                                      enable_events      Turns on the element speciﬁc events. Spin events happen
                                                              when an item changes

 bool                                      do_not_clear       if False the element will be cleared any time the
                                                              Window.Read call returns

 Any                                       key                Used with window.FindElement and with return values to
                                                              uniquely identify this element to uniquely identify this
                                                              element

 bool                                      focus              if True initial focus will go to this element

 Union[str, Tuple[str, int]]               font               speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int)) or   pad                Amount of padding to put around element (left/right,
 (int,(int,int)) or ((int, int),int)                          top/bottom) or ((left, right), (top, bottom))

 str                                       tooltip            text, that will appear when mouse hovers over the element

 List[List[Union[List[str],str]]]          right_click_menu   A list of lists of Menu items to show when this element is
                                                              right clicked. See user docs for exact format.

 bool                                      visible            set visibility state of the element

 Any                                       metadata           User metadata that can be set to ANYTHING


Get
Return current contents of the Multiline Element

Get()


 Type       Name          Meaning

            return        current contents of the Multiline Element (used as an input type of Multiline


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)
                                                                                                                   v: latest 
Parameter Descriptions:
 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                  Name                             Meaning

 str                   tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Multiline Element. Must call Window.Read or Window.Finalize prior

 Update(value=None,
  disabled=None,
  append=False,
  font=None,
  text_color=None,
  background_color=None,
  text_color_for_value=None,
  background_color_for_value=None,
  visible=None,
  autoscroll=None)


Parameter Descriptions:

 Type                   Name                 Meaning

 str                    value                new text to display

 bool                   disabled             disable or enable state of the element

 bool                   append               if True then new value will be added onto the end of the current value. if
                                             False then contents will be replaced.

 Union[str,             font                 speciﬁes the font family, size, etc                                v: latest 
 Tuple[str, int]]
 Type               Name                 Meaning

 str                text_color           color of the text

 str                background_color     color of background

 bool               visible              set visibility state of the element

 bool               autoscroll           if True then contents of element are scrolled down when new text is
                                         added to the end


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get
Return current contents of the Multiline Element

get()


 Type     Name       Meaning

          return     current contents of the Multiline Element (used as an input type of Multiline


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()

                                                                                                          v: latest 
 Type              Name                Meaning
 Type              Name                Meaning

                   return              width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



print
Print like Python normally prints except route the output to a multline element and also add colors if desired

 print(args=*<1 or N object>,
   end=None,
   sep=None,
   text_color=None,
   background_color=None,
   autoscroll=True)


Parameter Descriptions:

 Type              Name                             Meaning

 List[Any]         args                             The arguments to print

 str               end                              The end char to use just like print uses

 str               sep                              The separation character like print uses

 str               text_color                       The color of the text

 str               background_color                 The background color of the line


set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)


                                                                                                            v: latest 
set_focus
Sets the current focus to be on this element
 set_focus(force=False)


Parameter Descriptions:

 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                   Name          Meaning

 Tuple[int, int]        size          The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type                  Name                               Meaning

 str                   tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row                                                                                                     v: latest 
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.
 unhide_row()



update
Changes some of the settings for the Multiline Element. Must call Window.Read or Window.Finalize prior

 update(value=None,
   disabled=None,
   append=False,
   font=None,
   text_color=None,
   background_color=None,
   text_color_for_value=None,
   background_color_for_value=None,
   visible=None,
   autoscroll=None)


Parameter Descriptions:

 Type                Name                   Meaning

 str                 value                  new text to display

 bool                disabled               disable or enable state of the element

 bool                append                 if True then new value will be added onto the end of the current value. if
                                            False then contents will be replaced.

 Union[str,          font                   speciﬁes the font family, size, etc
 Tuple[str, int]]

 str                 text_color             color of the text

 str                 background_color       color of background

 bool                visible                set visibility state of the element

 bool                autoscroll             if True then contents of element are scrolled down when new text is
                                            added to the end



OptionMenu Element
 Option Menu is an Element available ONLY on the tkinter port of PySimpleGUI. It's is a widget that is unique
                                                                                                                    v: latest 
 to tkinter. However, it looks much like a ComboBox. Instead of an arrow to click to pull down the list of
 choices, another little graphic is shown on the widget to indicate where you click. After clicking to activate,
 it looks like a Combo Box that you scroll to select a choice.
 OptionMenu(values,
  default_value=None,
  size=(None, None),
  disabled=False,
  auto_size_text=None,
  background_color=None,
  text_color=None,
  key=None,
  pad=None,
  tooltip=None,
  visible=True,
  metadata=None)


Parameter Descriptions:

 Type                                            Name               Meaning

 List[Any] or Tuple[Any]                         values             Values to be displayed

 Any                                             default_value      the value to choose by default

 Tuple[int, int] (width, height)                 size               size in characters (wide) and rows (high)

 bool                                            disabled           control enabled / disabled

 bool                                            auto_size_text     True if size of Element should match the contents of
                                                                    the items

 str                                             background_color   color of background

 str                                             text_color         color of the text

 Any                                             key                Used with window.FindElement and with return
                                                                    values to uniquely identify this element

 (int, int) or ((int, int),(int,int)) or (int,   pad                Amount of padding to put around element (left/right,
 (int,int)) or ((int, int),int)                                     top/bottom) or ((left, right), (top, bottom))

 str                                             tooltip            (str) text that will appear when mouse hovers over
                                                                    this element

 bool                                            visible            (bool) set visibility state of the element


SetFocus
                                                                                                                  v: latest 
Sets the current focus to be on this element
 SetFocus(force=False)


Parameter Descriptions:

 Type         Name               Meaning

 bool         force              if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                               Meaning

 str                  tooltip_text                       the text to show in tooltip.


Update
Changes some of the settings for the OptionMenu Element. Must call Window.Read or Window.Finalize prior

 Update(value=None,
   values=None,
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type                    Name                   Meaning

 Any                     value                  the value to choose by default

 List[Any]               values                 Values to be displayed

 bool                    disabled               disable or enable state of the element

 bool                    visible                control visibility of element


bind                                                                                                      v: latest 
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                 Meaning

                  return               width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)
                                                                                                          v: latest 

Parameter Descriptions:
 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                   Name          Meaning

 Tuple[int, int]        size          The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type                  Name                               Meaning

 str                   tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()                                                                                                  v: latest 



update
Changes some of the settings for the OptionMenu Element. Must call Window.Read or Window.Finalize prior

 update(value=None,
   values=None,
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type                      Name                   Meaning

 Any                       value                  the value to choose by default

 List[Any]                 values                 Values to be displayed

 bool                      disabled               disable or enable state of the element

 bool                      visible                control visibility of element



Output Element
 Output Element - a multi-lined text area where stdout and stderr are re-routed to.



 Output(size=(None, None),
  background_color=None,
  text_color=None,
  pad=None,
  font=None,
  tooltip=None,
  key=None,
  right_click_menu=None,
  visible=True,
  metadata=None)


Parameter Descriptions:

 Type                                      Name                 Meaning

 Tuple[int, int]                           size                 (width, height) w=characters-wide, h=rows-high

 str                                       background_color     color of background

 str                                       text_color           color of the text
                                                                                                                  v: latest 
 (int, int) or ((int, int),(int,int)) or   pad                  Amount of padding to put around element (left/right,
 (int,(int,int)) or ((int, int),int)                            top/bottom) or ((left, right), (top, bottom))
 Type                                   Name                   Meaning

 Union[str, Tuple[str, int]]            font                   speciﬁes the font family, size, etc

 str                                    tooltip                text, that will appear when mouse hovers over the element

 Any                                    key                    Used with window.FindElement and with return values to
                                                               uniquely identify this element to uniquely identify this
                                                               element

 List[List[Union[List[str],str]]]       right_click_menu       A list of lists of Menu items to show when this element is
                                                               right clicked. See user docs for exact format.

 bool                                   visible                set visibility state of the element

 Any                                    metadata               User metadata that can be set to ANYTHING


Get
Returns the current contents of the output. Similar to Get method other Elements

Get()


 Type                  Name                   Meaning

                       return                 the current value of the output


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').                                                              v: latest 

 SetTooltip(tooltip_text)
Parameter Descriptions:

 Type               Name                             Meaning

 str                tooltip_text                     the text to show in tooltip.


TKOut
property: TKOut
Returns the TKOutput object used to create the element

 Type                   Name                       Meaning

                        return                     The TKOutput object


Update
Changes some of the settings for the Output Element. Must call Window.Read or Window.Finalize prior

 Update(value=None, visible=None)


Parameter Descriptions:

 Type       Name           Meaning

 str        value          string that will replace current contents of the output area

 bool       visible        control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,                                                                                        v: latest 
   expand_row=True)


Parameter Descriptions:
 Type         Name             Meaning

 Bool         expand_x         If True Element will expand in the Horizontal directions

 Bool         expand_y         If True Element will expand in the Vertical directions


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                 Meaning

                  return               width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type         Name          Meaning

 bool         force         if True will call focus_force otherwise calls focus_set

                                                                                                          v: latest 
set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                 Name         Meaning

 Tuple[int, int]      size         The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                               Meaning

 str                tooltip_text                       the text to show in tooltip.


tk_out
property: tk_out
Returns the TKOutput object used to create the element

 Type                    Name                        Meaning

                         return                      The TKOutput object


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear 
                                                                                                            at the
                                                                                                               v: latest 
bottom of the window / container, most likely.
 unhide_row()



update
Changes some of the settings for the Output Element. Must call Window.Read or Window.Finalize prior

 update(value=None, visible=None)


Parameter Descriptions:

 Type         Name         Meaning

 str          value        string that will replace current contents of the output area

 bool         visible      control visibility of element



Pane Element
 A sliding Pane that is unique to tkinter. Uses Columns to create individual panes



 Pane(pane_list,
   background_color=None,
   size=(None, None),
   pad=None,
   orientation="vertical",
   show_handle=True,
   relief="raised",
   handle_size=None,
   border_width=None,
   key=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                         Name                   Meaning

 List[Column]                 pane_list              Must be a list of Column Elements. Each Column supplied
                                                     becomes one pane that's shown

 str                          background_color       color of background

 Tuple[int, int]              size                   (width, height) w=characters-wide, h=rows-high How much
                                                                                                          v:room
                                                                                                              latest 
                                                     to reserve for the Pane
 Type                                 Name                 Meaning

 (int, int) or ((int, int),           pad                  Amount of padding to put around element (left/right,
 (int,int)) or (int,(int,int)) or                          top/bottom) or ((left, right), (top, bottom))
 ((int, int),int)

 str                                  orientation          'horizontal' or 'vertical' or ('h' or 'v'). Direction the Pane should
                                                           slide

 bool                                 show_handle          if True, the handle is drawn that makes it easier to grab and slide

 enum                                 relief               relief style. Values are same as other elements that use relief
                                                           values. RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT
                                                           RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID

 int                                  handle_size          Size of the handle in pixels

 int                                  border_width         width of border around element in pixels

 any                                  key                  Value that uniquely identiﬁes this element from all other
                                                           elements. Used when Finding an element or in return values.
                                                           Must be unique to the window

 bool                                 visible              set visibility state of the element

 Any                                  metadata             User metadata that can be set to ANYTHING


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type           Name                Meaning

 bool           force               if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').                                                              v: latest 

 SetTooltip(tooltip_text)
Parameter Descriptions:

 Type             Name                             Meaning

 str              tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Pane Element. Must call Window.Read or Window.Finalize prior

 Update(visible=None)


Parameter Descriptions:

 Type               Name                   Meaning

 bool               visible                control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                Meaning

                  return              width and height of the element                                     v: latest 



hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)
                                                                                                             v: latest 

Parameter Descriptions:
 Type              Name                              Meaning

 str               tooltip_text                      the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Pane Element. Must call Window.Read or Window.Finalize prior

 update(visible=None)


Parameter Descriptions:

 Type               Name                    Meaning

 bool               visible                 control visibility of element



ProgressBar Element
 Progress Bar Element - Displays a colored bar that is shaded as progress of some operation is made




                                                                                                             v: latest 
 ProgressBar(max_value,
   orientation=None,
   size=(None, None),
   auto_size_text=None,
   bar_color=(None, None),
   style=None,
   border_width=None,
   relief=None,
   key=None,
   pad=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                       Name             Meaning

 int                        max_value        max value of progressbar

 str                        orientation      'horizontal' or 'vertical'

 Tuple[int, int]            size             Size of the bar. If horizontal (chars wide, pixels high), vert (pixels wide,
                                             rows high)

 bool                       auto_size_text   Not sure why this is here

 Tuple[str, str]            bar_color        The 2 colors that make up a progress bar. One is the background, the other
                                             is the bar

 str                        style            Progress bar style deﬁned as one of these 'default', 'winnative', 'clam', 'alt',
                                             'classic', 'vista', 'xpnative'

 int                        border_width     The amount of pixels that go around the outside of the bar

 str                        relief           relief style. Values are same as progress meter relief values. Can be a
                                             constant or a string: RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT
                                             RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID (Default value =
                                             DEFAULT_PROGRESS_BAR_RELIEF)

 Any                        key              Used with window.FindElement and with return values to uniquely identify
                                             this element to uniquely identify this element

 (int, int) or ((int,       pad              Amount of padding to put around element (left/right, top/bottom) or ((left,
 int),(int,int)) or (int,                    right), (top, bottom))
 (int,int)) or ((int,                                                                                                v: latest 
 int),int)
 Type                     Name               Meaning

 bool                     visible            set visibility state of the element

 Any                      metadata           User metadata that can be set to ANYTHING


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name               Meaning

 bool         force              if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                               Meaning

 str                  tooltip_text                       the text to show in tooltip.


Update
Changes some of the settings for the ProgressBar Element. Must call Window.Read or Window.Finalize prior

 Update(visible=None)


Parameter Descriptions:

 Type                  Name                     Meaning

 bool                  visible                  control visibility of element
                                                                                                          v: latest 


UpdateBar
Change what the bar shows by changing the current count and optionally the max count

 UpdateBar(current_count, max=None)


Parameter Descriptions:

 Type             Name                                   Meaning

 int              current_count                          sets the current value

 int              max                                    changes the max value


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                Meaning

                  return              width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container
                                                                                                          v: latest 
 hide_row()
set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                   Name          Meaning

 Tuple[int, int]        size          The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type                  Name                               Meaning

 str                   tooltip_text                       the text to show in tooltip.                         v: latest 



unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the ProgressBar Element. Must call Window.Read or Window.Finalize prior

 update(visible=None)


Parameter Descriptions:

 Type               Name                     Meaning

 bool               visible                  control visibility of element


update_bar
Change what the bar shows by changing the current count and optionally the max count

 update_bar(current_count, max=None)


Parameter Descriptions:

 Type              Name                                     Meaning

 int               current_count                            sets the current value

 int               max                                      changes the max value



Radio Element
 Radio Button Element - Used in a group of other Radio Elements to provide user with ability to select only
 1 choice in a list of choices.
                                                                                                               v: latest 
 Radio(text,
   group_id,
   default=False,
   disabled=False,
   size=(None, None),
   auto_size_text=None,
   background_color=None,
   text_color=None,
   font=None,
   key=None,
   pad=None,
   tooltip=None,
   change_submits=False,
   enable_events=False,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                                            Name               Meaning

 str                                             text               Text to display next to button

 Any                                             group_id           Groups together multiple Radio Buttons. Any type
                                                                    works

 bool                                            default            Set to True for the one element of the group you want
                                                                    initially selected

 bool                                            disabled           set disable state

 Tuple[int,                                      size               int] (width, height) width = characters-wide, height =
                                                                    rows-high

 bool                                            auto_size_text     if True will size the element to match the length of the
                                                                    text

 str                                             background_color   color of background

 str                                             text_color         color of the text

 Union[str, Tuple[str, int]]                     font               speciﬁes the font family, size, etc

 Any                                             key                Used with window.FindElement and with return
                                                                    values to uniquely identify this element
                                                                                                                   v: latest 
 (int, int) or ((int, int),(int,int)) or (int,   pad                Amount of padding to put around element (left/right,
 (int,int)) or ((int, int),int)                                     top/bottom) or ((left, right), (top, bottom))
 Type                                    Name                   Meaning

 str                                     tooltip                text, that will appear when mouse hovers over the
                                                                element

 bool                                    change_submits         DO NOT USE. Only listed for backwards compat - Use
                                                                enable_events instead

 bool                                    enable_events          Turns on the element speciﬁc events. Radio Button
                                                                events happen when an item is selected

 bool                                    visible                set visibility state of the element

 Any                                     metadata               User metadata that can be set to ANYTHING


Get
A snapshot of the value of Radio Button -> (bool)

Get()


 Type            Name                 Meaning

                 return               True if this radio button is selected


ResetGroup
Sets all Radio Buttons in the group to not selected

 ResetGroup()



SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type        Name           Meaning

 bool        force          if True will call focus_force otherwise calls focus_set
                                                                                                            v: latest 

SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                Name                              Meaning

 str                 tooltip_text                      the text to show in tooltip.


Update
Changes some of the settings for the Radio Button Element. Must call Window.Read or Window.Finalize prior

 Update(value=None,
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type      Name              Meaning

 bool      value             if True change to selected and set others in group to unselected

 bool      disabled          disable or enable state of the element

 bool      visible           control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)
                                                                                                          v: latest 


get
A snapshot of the value of Radio Button -> (bool)

get()


 Type            Name                Meaning

                 return              True if this radio button is selected


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                 Meaning

                  return               width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



reset_group
Sets all Radio Buttons in the group to not selected

 reset_group()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)                                                                                   v: latest 


Parameter Descriptions:
 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                   Name          Meaning

 Tuple[int, int]        size          The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type                  Name                               Meaning

 str                   tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()                                                                                                  v: latest 



update
Changes some of the settings for the Radio Button Element. Must call Window.Read or Window.Finalize prior

 update(value=None,
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type       Name             Meaning

 bool       value            if True change to selected and set others in group to unselected

 bool       disabled         disable or enable state of the element

 bool       visible          control visibility of element



Slider Element
 A slider, horizontal or vertical



 Slider(range=(None, None),
   default_value=None,
   resolution=None,
   tick_interval=None,
   orientation=None,
   disable_number_display=False,
   border_width=None,
   relief=None,
   change_submits=False,
   enable_events=False,
   disabled=False,
   size=(None, None),
   font=None,
   background_color=None,
   text_color=None,
   key=None,
   pad=None,
   tooltip=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                               Name                     Meaning
                                                                                                      v: latest 
 Union[Tuple[int, int],             range                    slider's range (min value, max value)
 Tuple[ﬂoat, ﬂoat]]
Type                               Name                     Meaning

Union[int, ﬂoat]                   default_value            starting value for the slider

Union[int, ﬂoat]                   resolution               the smallest amount the slider can be moved

Union[int, ﬂoat]                   tick_interval            how often a visible tick should be shown next to slider

str                                orientation              'horizontal' or 'vertical' ('h' or 'v' also work)

bool                               disable_number_display   if True no number will be displayed by the Slider Element

int                                border_width             width of border around element in pixels

enum                               relief                   relief style. RELIEF_RAISED RELIEF_SUNKEN
                                                            RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE
                                                            RELIEF_SOLID

bool                               change_submits           * DEPRICATED DO NOT USE! Same as enable_events

bool                               enable_events            If True then moving the slider will generate an Event

bool                               disabled                 set disable state for element

Tuple[int, int]                    size                     (w=characters-wide, h=rows-high)

Union[str, Tuple[str, int]]        font                     speciﬁes the font family, size, etc

str                                background_color         color of slider's background

str                                text_color               color of the slider's text

any                                key                      Value that uniquely identiﬁes this element from all other
                                                            elements. Used when Finding an element or in return
                                                            values. Must be unique to the window

(int, int) or ((int, int),         pad                      Amount of padding to put around element (left/right,
(int,int)) or (int,(int,int)) or                            top/bottom) or ((left, right), (top, bottom))
((int, int),int)

str                                tooltip                  text, that will appear when mouse hovers over the
                                                            element

bool                               visible                  set visibility state of the element
                                                                                                                 v: latest 
Any                                metadata                 User metadata that can be set to ANYTHING
SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Slider Element. Must call Window.Read or Window.Finalize prior

 Update(value=None,
   range=(None, None),
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type                                                   Name          Meaning

 Union[int, ﬂoat]                                       value         sets current slider value

 Union[Tuple[int, int], Tuple[ﬂoat, ﬂoat]               range         Sets a new range for slider

 bool                                                   disabled      disable or enable state of the element
                                                                                                                v: latest 
 bool                                                   visible       control visibility of element
bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                 Meaning

                  return               width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element
                                                                                                          v: latest 

 set_focus(force=False)
Parameter Descriptions:

 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                   Name          Meaning

 Tuple[int, int]        size          The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type                  Name                               Meaning

 str                   tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.
                                                                                                               v: latest 

 unhide_row()
update
Changes some of the settings for the Slider Element. Must call Window.Read or Window.Finalize prior

 update(value=None,
   range=(None, None),
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type                                                  Name           Meaning

 Union[int, ﬂoat]                                      value          sets current slider value

 Union[Tuple[int, int], Tuple[ﬂoat, ﬂoat]              range          Sets a new range for slider

 bool                                                  disabled       disable or enable state of the element

 bool                                                  visible        control visibility of element



Spin Element
 A spinner with up/down buttons and a single line of text. Choose 1 values from list



 Spin(values,
   initial_value=None,
   disabled=False,
   change_submits=False,
   enable_events=False,
   size=(None, None),
   auto_size_text=None,
   font=None,
   background_color=None,
   text_color=None,
   key=None,
   pad=None,
   tooltip=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                                       Name                  Meaning
                                                                                                                v: latest 
 Tuple[Any] or List[Any]                    values                List of valid values
 Type                                            Name               Meaning

 Any                                             initial_value      Initial item to show in window. Choose from list of
                                                                    values supplied

 bool                                            disabled           set disable state

 bool                                            change_submits     DO NOT USE. Only listed for backwards compat - Use
                                                                    enable_events instead

 bool                                            enable_events      Turns on the element speciﬁc events. Spin events
                                                                    happen when an item changes

 Tuple[int, int]                                 size               (width, height) width = characters-wide, height =
                                                                    rows-high

 bool                                            auto_size_text     if True will size the element to match the length of the
                                                                    text

 Union[str, Tuple[str, int]]                     font               speciﬁes the font family, size, etc

 str                                             background_color   color of background

 str                                             text_color         color of the text

 Any                                             key                Used with window.FindElement and with return
                                                                    values to uniquely identify this element

 (int, int) or ((int, int),(int,int)) or (int,   pad                Amount of padding to put around element (left/right,
 (int,int)) or ((int, int),int)                                     top/bottom) or ((left, right), (top, bottom))

 str                                             tooltip            text, that will appear when mouse hovers over the
                                                                    element

 bool                                            visible            set visibility state of the element

 Any                                             metadata           User metadata that can be set to ANYTHING


Get
Return the current chosen value showing in spinbox. This value will be the same as what was provided as list of
choices. If list items are ints, then the item returned will be an int (not a string)

Get()
                                                                                                                  v: latest 

 Type                     Name                         Meaning
 Type                   Name                      Meaning

                        return                    The currently visible entry


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name               Meaning

 bool         force              if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                               Meaning

 str                  tooltip_text                       the text to show in tooltip.


Update
Changes some of the settings for the Spin Element. Must call Window.Read or Window.Finalize prior

 Update(value=None,
   values=None,
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type                   Name                  Meaning

 Any                    value                 set the current value from list of choices                  v: latest 


 List[Any]              values                set available choices
 Type                Name                Meaning

 bool                disabled            disable or enable state of the element

 bool                visible             control visibility of element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get
Return the current chosen value showing in spinbox. This value will be the same as what was provided as list of
choices. If list items are ints, then the item returned will be an int (not a string)

get()


 Type                Name                   Meaning

                     return                 The currently visible entry


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                Meaning

                  return              width and height of the element
                                                                                                          v: latest 

hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)                                                                                   v: latest 

Parameter Descriptions:
 Type              Name                             Meaning

 str               tooltip_text                     the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Spin Element. Must call Window.Read or Window.Finalize prior

 update(value=None,
   values=None,
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type                  Name               Meaning

 Any                   value              set the current value from list of choices

 List[Any]             values             set available choices

 bool                  disabled           disable or enable state of the element

 bool                  visible            control visibility of element



StatusBar Element
 A StatusBar Element creates the sunken text-ﬁlled strip at the bottom. Many Windows programs have this line
                                                                                                                v: latest 
 StatusBar(text,
   size=(None, None),
   auto_size_text=None,
   click_submits=None,
   enable_events=False,
   relief="sunken",
   font=None,
   text_color=None,
   background_color=None,
   justiﬁcation=None,
   pad=None,
   key=None,
   tooltip=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                     Name               Meaning

 str                      text               Text that is to be displayed in the widget

 Tuple[(int), (int)]      size               (w,h) w=characters-wide, h=rows-high

 bool                     auto_size_text     True if size should ﬁt the text length

 bool                     click_submits      DO NOT USE. Only listed for backwards compat - Use
                                             enable_events instead

 bool                     enable_events      Turns on the element speciﬁc events. StatusBar events occur when
                                             the bar is clicked

 enum                     relief             relief style. Values are same as progress meter relief values. Can
                                             be a constant or a string: RELIEF_RAISED RELIEF_SUNKEN
                                             RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID

 Union[str, Tuple[str,    font               speciﬁes the font family, size, etc
 int]]

 str                      text_color         color of the text

 str                      background_color   color of background

 str                      justiﬁcation       how string should be aligned within space provided by size. Valid
                                             choices = left , right , center
                                                                                                        v: latest 
 Type                            Name                Meaning

 (int, int) or ((int, int),      pad                 Amount of padding to put around element (left/right, top/bottom)
 (int,int)) or (int,(int,int))                       or ((left, right), (top, bottom))
 or ((int, int),int)

 Any                             key                 Used with window.FindElement and with return values to uniquely
                                                     identify this element to uniquely identify this element

 str                             tooltip             text, that will appear when mouse hovers over the element

 bool                            visible             set visibility state of the element

 Any                             metadata            User metadata that can be set to ANYTHING


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type           Name             Meaning

 bool           force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                   Name                             Meaning

 str                    tooltip_text                     the text to show in tooltip.


Update
                                                                                                   v: latest 
Changes some of the settings for the Status Bar Element. Must call Window.Read or Window.Finalizeprior
 Update(value=None,
   background_color=None,
   text_color=None,
   font=None,
   visible=None)


Parameter Descriptions:

 Type                                Name                          Meaning

 str                                 value                         new text to show

 str                                 background_color              color of background

 str                                 text_color                    color of the text

 Union[str, Tuple[str, int]]         font                          speciﬁes the font family, size, etc

 bool                                visible                       set visibility state of the element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type               Name              Meaning
                                                                                                          v: latest 
                    return            width and height of the element
hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').
                                                                                                             v: latest 

 set_tooltip(tooltip_text)
Parameter Descriptions:

 Type                Name                           Meaning

 str                 tooltip_text                   the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Status Bar Element. Must call Window.Read or Window.Finalize prior

 update(value=None,
   background_color=None,
   text_color=None,
   font=None,
   visible=None)


Parameter Descriptions:

 Type                                 Name                           Meaning

 str                                  value                          new text to show

 str                                  background_color               color of background

 str                                  text_color                     color of the text

 Union[str, Tuple[str, int]]          font                           speciﬁes the font family, size, etc

 bool                                 visible                        set visibility state of the element

                                                                                                             v: latest 

SystemTray
 A "Simulated System Tray" that duplicates the API calls available to PySimpleGUIWx and PySimpleGUIQt users.

 All of the functionality works. The icon is displayed ABOVE the system tray rather than inside of it.


SystemTray - create an icon in the system tray

 SystemTray(menu=None,
   ﬁlename=None,
   data=None,
   data_base64=None,
   tooltip=None,
   metadata=None)


Parameter Descriptions:

 Type                           Name           Meaning

 List[List[List[str] or str]]   menu           Menu deﬁnition. Example - ['UNUSED', ['My', 'Simple', '---', 'Menu', 'Exit']]

 str                            ﬁlename        ﬁlename for icon

 bytes                          data           in-ram image for icon (same as data_base64 parm)

 bytes                          data_base64    base-64 data for icon

 str                            tooltip        tooltip string

 Any                            metadata       User metadata that can be set to ANYTHING


Close
Close the system tray window

 Close()



Hide
Hides the icon

 Hide()



Read
                                                                                                                    v: latest 
Reads the context menu
 Read(timeout=None)



ShowMessage
Shows a balloon above icon in system tray

 ShowMessage(title,
   message,
   ﬁlename=None,
   data=None,
   data_base64=None,
   messageicon=None,
   time=(1000, 3000))


Parameter Descriptions:

 Type                    Name          Meaning

                         title         Title shown in balloon

                         message       Message to be displayed

                         ﬁlename       Optional icon ﬁlename

                         data          Optional in-ram icon

                         data_base64   Optional base64 icon

 Union[int, Tuple[int,   time          Amount of time to display message in milliseconds. If tuple, ﬁrst item is
 int]]                                 fade in/out duration

 (Any)                   RETURN        The event that happened during the display such as user clicked on
                                       message


UnHide
Restores a previously hidden icon

 UnHide()



Update
Updates the menu, tooltip or icon
                                                                                                           v: latest 
 Update(menu=None,
   tooltip=None,
   ﬁlename=None,
   data=None,
   data_base64=None)


Parameter Descriptions:

 Type             Name                               Meaning

 ???              menu                               menu deﬁntion

 ???              tooltip                            string representing tooltip

 ???              ﬁlename                            icon ﬁlename

 ???              data                               icon raw image

 ???              data_base64                        icon base 64 image


close
Close the system tray window

 close()



hide
Hides the icon

 hide()



notify
Displays a "notiﬁcation window", usually in the bottom right corner of your display. Has an icon, a title, and a
message The window will slowly fade in and out if desired. Clicking on the window will cause it to move through the
end the current "phase". For example, if the window was fading in and it was clicked, then it would immediately stop
fading in and instead be fully visible. It's a way for the user to quickly dismiss the window.

 notify(title,
   message,
   icon=...,
   display_duration_in_ms=3000,
                                                                                                          v: latest 
   fade_in_duration=1000,
   alpha=0.9,
   location=None)
Parameter Descriptions:

 Type              Name                     Meaning

 str               title                    Text to be shown at the top of the window in a larger font

 str               message                  Text message that makes up the majority of the window

 Union[bytes,      icon                     A base64 encoded PNG/GIF image or PNG/GIF ﬁlename that will be
 str]                                       displayed in the window

 int               display_duration_in_ms   Number of milliseconds to show the window

 int               fade_in_duration         Number of milliseconds to fade window in and out

 ﬂoat              alpha                    Alpha channel. 0 - invisible 1 - fully visible

 Tuple[int, int]   location                 Location on the screen to display the window

 (int)             RETURN                   (int) reason for returning


read
Reads the context menu

 read(timeout=None)



show_message
Shows a balloon above icon in system tray

 show_message(title,
   message,
   ﬁlename=None,
   data=None,
   data_base64=None,
   messageicon=None,
   time=(1000, 3000))


Parameter Descriptions:

 Type                      Name        Meaning

                           title       Title shown in balloon
                                                                                                          v: latest 

                           message     Message to be displayed
 Type                     Name          Meaning

                          ﬁlename       Optional icon ﬁlename

                          data          Optional in-ram icon

                          data_base64   Optional base64 icon

 Union[int, Tuple[int,    time          Amount of time to display message in milliseconds. If tuple, ﬁrst item is
 int]]                                  fade in/out duration

 (Any)                    RETURN        The event that happened during the display such as user clicked on
                                        message


un_hide
Restores a previously hidden icon

 un_hide()



update
Updates the menu, tooltip or icon

 update(menu=None,
   tooltip=None,
   ﬁlename=None,
   data=None,
   data_base64=None)


Parameter Descriptions:

 Type              Name                               Meaning

 ???               menu                               menu deﬁntion

 ???               tooltip                            string representing tooltip

 ???               ﬁlename                            icon ﬁlename

 ???               data                               icon raw image

 ???               data_base64                        icon base 64 image
                                                                                                            v: latest 


Tab Element
 Tab Element is another "Container" element that holds a layout and displays a tab with text. Used with TabGroup only
 Tabs are never placed directly into a layout. They are always "Contained" in a TabGroup layout


 Tab(title,
   layout,
   title_color=None,
   background_color=None,
   font=None,
   pad=None,
   disabled=False,
   border_width=None,
   key=None,
   tooltip=None,
   right_click_menu=None,
   visible=True,
   element_justiﬁcation="left",
   metadata=None)


Parameter Descriptions:

 Type                               Name                 Meaning

 str                                title                text to show on the tab

 List[List[Element]]                layout               The element layout that will be shown in the tab

 str                                title_color          color of the tab text (note not currently working on tkinter)

 str                                background_color     color of background of the entire layout

 Union[str, Tuple[str, int]]        font                 speciﬁes the font family, size, etc

 (int, int) or ((int, int),         pad                  Amount of padding to put around element (left/right,
 (int,int)) or (int,(int,int)) or                        top/bottom) or ((left, right), (top, bottom))
 ((int, int),int)

 bool                               disabled             If True button will be created disabled

 int                                border_width         width of border around element in pixels

 any                                key                  Value that uniquely identiﬁes this element from all other
                                                         elements. Used when Finding an element or in return
                                                         values. Must be unique to the window

 str                                tooltip              text, that will appear when mouse hovers over the element
                                                                                                            v: latest 
 Type                               Name                    Meaning

 List[List[Union[List[str],str]]]   right_click_menu        A list of lists of Menu items to show when this element is
                                                            right clicked. See user docs for exact format.

 bool                               visible                 set visibility state of the element

 str                                element_justiﬁcation    All elements inside the Tab will have this justiﬁcation 'left',
                                                            'right', 'center' are valid values

 Any                                metadata                User metadata that can be set to ANYTHING


AddRow
Not recommended use call. Used to add rows of Elements to the Frame Element.

 AddRow(args=*<1 or N object>)


Parameter Descriptions:

 Type                               Name               Meaning

 List[Element]                      *args              The list of elements for this row


Layout
Not user callable. Use layout parameter instead. Creates the layout using the supplied rows of Elements

 Layout(rows) -> (Tab) used for chaining



Select
Create a tkinter event that mimics user clicking on a tab. Must have called window.Finalize / Read ﬁrst!

 Select()



SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)
                                                                                                                   v: latest 
Parameter Descriptions:
 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Tab Element. Must call Window.Read or Window.Finalize prior

 Update(title=None,
  disabled=None,
  visible=None)


Parameter Descriptions:

 Type           Name                     Meaning

 str            title                    tab title

 bool           disabled                 disable or enable state of the element

 bool           visible                  control visibility of element


add_row
Not recommended use call. Used to add rows of Elements to the Frame Element.

 add_row(args=*<1 or N object>)


Parameter Descriptions:
                                                                                                          v: latest 
 Type                                Name            Meaning
 Type                             Name               Meaning

 List[Element]                    *args              The list of elements for this row


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type              Name                    Meaning

                   return                  width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



layout
Not user callable. Use layout parameter instead. Creates the layout using the supplied rows of Elements

 layout(rows) -> (Tab) used for chaining                                                                   v: latest 



select
Create a tkinter event that mimics user clicking on a tab. Must have called window.Finalize / Read ﬁrst!

 select()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)

                                                                                                             v: latest 
Parameter Descriptions:
 Type              Name                             Meaning

 str               tooltip_text                     the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Tab Element. Must call Window.Read or Window.Finalize prior

 update(title=None,
   disabled=None,
   visible=None)


Parameter Descriptions:

 Type           Name                  Meaning

 str            title                 tab title

 bool           disabled              disable or enable state of the element

 bool           visible               control visibility of element



TabGroup Element
 TabGroup Element groups together your tabs into the group of tabs you see displayed in your window




                                                                                                             v: latest 
 TabGroup(layout,
   tab_location=None,
   title_color=None,
   tab_background_color=None,
   selected_title_color=None,
   selected_background_color=None,
   background_color=None,
   font=None,
   change_submits=False,
   enable_events=False,
   pad=None,
   border_width=None,
   theme=None,
   key=None,
   tooltip=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                               Name                        Meaning

 List[List[Tab]]                    layout                      Layout of Tabs. Different than normal layouts. ALL
                                                                Tabs should be on ﬁrst row

 str                                tab_location                location that tabs will be displayed. Choices are left,
                                                                right, top, bottom, lefttop, leftbottom, righttop,
                                                                rightbottom, bottomleft, bottomright, topleft, topright

 str                                title_color                 color of text on tabs

 str                                tab_background_color        color of all tabs that are not selected

 str                                selected_title_color        color of tab text when it is selected

 str                                selected_background_color   color of tab when it is selected

 str                                background_color            color of background area that tabs are located on

 Union[str, Tuple[str, int]]        font                        speciﬁes the font family, size, etc

 bool                               change_submits              * DEPRICATED DO NOT USE! Same as enable_events

 bool                               enable_events               If True then switching tabs will generate an Event

 (int, int) or ((int, int),         pad                         Amount of padding to put around element (left/right,
                                                                                                               v: latest 
 (int,int)) or (int,(int,int)) or                               top/bottom) or ((left, right), (top, bottom))
 ((int, int),int)
 Type                         Name                             Meaning

 int                          border_width                     width of border around element in pixels

 enum                         theme                            DEPRICATED - You can only specify themes using set
                                                               options or when window is created. It's not possible to
                                                               do it on an element basis

 any                          key                              Value that uniquely identiﬁes this element from all
                                                               other elements. Used when Finding an element or in
                                                               return values. Must be unique to the window

 str                          tooltip                          text, that will appear when mouse hovers over the
                                                               element

 bool                         visible                          set visibility state of the element

 Any                          metadata                         User metadata that can be set to ANYTHING


FindKeyFromTabName
Searches through the layout to ﬁnd the key that matches the text on the tab. Implies names should be unique

 FindKeyFromTabName(tab_name)


Parameter Descriptions:

 Type                           Name                 Meaning

 str                            tab_name             name of a tab

 Union[key, None]               RETURN               Returns the key or None if no key found


Get
Returns the current value for the Tab Group, which will be the currently selected tab's KEY or the text on the tab if no
key is deﬁned. Returns None if an error occurs. Note that this is exactly the same data that would be returned from a
call to Window.Read. Are you sure you are using this method correctly?

 Get()


 Type      Name         Meaning

                                                                                                             v: latest 
           return       The key of the currently selected tab or the tab's text if it has no key
SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



ﬁnd_key_from_tab_name
                                                                                                         v: latest 
Searches through the layout to ﬁnd the key that matches the text on the tab. Implies names should be unique

 ﬁnd_key_from_tab_name(tab_name)
Parameter Descriptions:

 Type                           Name                 Meaning

 str                            tab_name             name of a tab

 Union[key, None]               RETURN               Returns the key or None if no key found


get
Returns the current value for the Tab Group, which will be the currently selected tab's KEY or the text on the tab if no
key is deﬁned. Returns None if an error occurs. Note that this is exactly the same data that would be returned from a
call to Window.Read. Are you sure you are using this method correctly?

 get()


 Type      Name         Meaning

           return       The key of the currently selected tab or the tab's text if it has no key


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

 get_size()


 Type               Name                Meaning

                    return              width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)
                                                                                                             v: latest 


set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                   Name          Meaning

 Tuple[int, int]        size          The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type                  Name                               Meaning

 str                   tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)

                                                                                                               v: latest 
unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()




Table Element
 Table(values,
   headings=None,
   visible_column_map=None,
   col_widths=None,
   def_col_width=10,
   auto_size_columns=True,
   max_col_width=20,
   select_mode=None,
   display_row_numbers=False,
   num_rows=None,
   row_height=None,
   font=None,
   justiﬁcation="right",
   text_color=None,
   background_color=None,
   alternating_row_color=None,
   header_text_color=None,
   header_background_color=None,
   header_font=None,
   row_colors=None,
   vertical_scroll_only=True,
   hide_vertical_scroll=False,
   size=(None, None),
   change_submits=False,
   enable_events=False,
   bind_return_key=False,
   pad=None,
   key=None,
   tooltip=None,
   right_click_menu=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                           Name                         Meaning

 List[List[Union[str, int,      values                       ???
 ﬂoat]]]
                                                                                                             v: latest 

 List[str]                      headings                     The headings to show on the top line
Type                          Name                      Meaning

List[bool]                    visible_column_map        One entry for each column. False indicates the column
                                                        is not shown

List[int]                     col_widths                Number of characters that each column will occupy

int                           def_col_width             Default column width in characters

bool                          auto_size_columns         if True columns will be sized automatically

int                           max_col_width             Maximum width for all columns in characters

enum                          select_mode               Select Mode. Valid values start with
                                                        "TABLE_SELECT_MODE_". Valid values are:
                                                        TABLE_SELECT_MODE_NONE
                                                        TABLE_SELECT_MODE_BROWSE
                                                        TABLE_SELECT_MODE_EXTENDED

bool                          display_row_numbers       if True, the ﬁrst column of the table will be the row #

int                           num_rows                  The number of rows of the table to display at a time

int                           row_height                height of a single row in pixels

Union[str, Tuple[str, int]]   font                      speciﬁes the font family, size, etc

str                           justiﬁcation              'left', 'right', 'center' are valid choices

str                           text_color                color of the text

str                           background_color          color of background

str                           alternating_row_color     if set then every other row will have this color in the
                                                        background.

str                           header_text_color         sets the text color for the header

str                           header_background_color   sets the background color for the header

Union[str, Tuple[str, int]]   header_font               speciﬁes the font family, size, etc

List[Union[Tuple[int, str],   row_colors                list of tuples of (row, background color) OR (row,
Tuple[Int, str, str]]                                   foreground color, background color). Sets the colors of
                                                                                                        v: latest 
                                                        listed rows to the color(s) provided (note the optional
                                                        foreground color)
 Type                               Name                     Meaning

 bool                               vertical_scroll_only     if True only the vertical scrollbar will be visible

 bool                               hide_vertical_scroll     if True vertical scrollbar will be hidden

 Tuple[int, int]                    size                     DO NOT USE! Use num_rows instead

 bool                               change_submits           DO NOT USE. Only listed for backwards compat - Use
                                                             enable_events instead

 bool                               enable_events            Turns on the element speciﬁc events. Table events
                                                             happen when row is clicked

 bool                               bind_return_key          if True, pressing return key will cause event coming
                                                             from Table, ALSO a left button double click will
                                                             generate an event if this parameter is True

 (int, int) or ((int, int),         pad                      Amount of padding to put around element (left/right,
 (int,int)) or (int,(int,int)) or                            top/bottom) or ((left, right), (top, bottom))
 ((int, int),int)

 Any                                key                      Used with window.FindElement and with return values
                                                             to uniquely identify this element to uniquely identify
                                                             this element

 str                                tooltip                  text, that will appear when mouse hovers over the
                                                             element

 List[List[Union[List[str],str]]]   right_click_menu         A list of lists of Menu items to show when this element
                                                             is right clicked. See user docs for exact format.

 bool                               visible                  set visibility state of the element

 Any                                metadata                 User metadata that can be set to ANYTHING


Get
Dummy function for tkinter port. In the Qt port you can read back the values in the table in case they were edited.
Don't know yet how to enable editing of a Tree in tkinter so just returning the values provided by user when Table
was created or Updated.

Get()
                                                                                                                v: latest 
 Type       Name          Meaning
 Type     Name          Meaning

          return        the current table values (for now what was originally provided up updated)


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Table Element. Must call Window.Read or Window.Finalize prior

 Update(values=None,
  num_rows=None,
  visible=None,
  select_rows=None,
  alternating_row_color=None,
  row_colors=None)


Parameter Descriptions:

 Type                       Name                    Meaning                                               v: latest 
 Type                      Name                    Meaning

 List[List[Union[str,      values                  A new 2-dimensional table to show
 int, ﬂoat]]]

 int                       num_rows                How many rows to display at a time

 bool                      visible                 if True then will be visible

 List[int]                 select_rows             List of rows to select as if user did

 str                       alternating_row_color   the color to make every other row

 List[Union[Tuple[int,     row_colors              list of tuples of (row, background color) OR (row, foreground color,
 str], Tuple[Int, str,                             background color). Changes the colors of listed rows to the
 str]]                                             color(s) provided (note the optional foreground color)


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get
Dummy function for tkinter port. In the Qt port you can read back the values in the table in case they were edited.
Don't know yet how to enable editing of a Tree in tkinter so just returning the values provided by user when Table
was created or Updated.

get()


 Type        Name        Meaning

             return      the current table values (for now what was originally provided up updated)            v: latest 


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type              Name                   Meaning

                   return                 width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:
                                                                                                             v: latest 
 Type                 Name        Meaning
 Type                 Name         Meaning

 Tuple[int, int]      size         The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type               Name                               Meaning

 str                tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Table Element. Must call Window.Read or Window.Finalize prior

 update(values=None,
   num_rows=None,
   visible=None,
   select_rows=None,
   alternating_row_color=None,
   row_colors=None)


Parameter Descriptions:
                                                                                                             v: latest 

 Type                    Name                       Meaning
 Type                    Name                      Meaning

 List[List[Union[str,    values                    A new 2-dimensional table to show
 int, ﬂoat]]]

 int                     num_rows                  How many rows to display at a time

 bool                    visible                   if True then will be visible

 List[int]               select_rows               List of rows to select as if user did

 str                     alternating_row_color     the color to make every other row

 List[Union[Tuple[int,   row_colors                list of tuples of (row, background color) OR (row, foreground color,
 str], Tuple[Int, str,                             background color). Changes the colors of listed rows to the
 str]]                                             color(s) provided (note the optional foreground color)



Text Element
 Text - Display some text in the window. Usually this means a single line of text. However, the text can also be multiple lin



 Text(text="",
   size=(None, None),
   auto_size_text=None,
   click_submits=False,
   enable_events=False,
   relief=None,
   font=None,
   text_color=None,
   background_color=None,
   border_width=None,
   justiﬁcation=None,
   pad=None,
   key=None,
   right_click_menu=None,
   tooltip=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                              Name                Meaning

 Any                               text                The text to display. Can include /n to achieve multiple
                                                                                                              lines.
                                                                                                                 v: latest 
                                                       Will convert (optional) parameter into a string
Type                               Name               Meaning

Tuple[int, int]                    size               (width, height) width = characters-wide, height = rows-high

bool                               auto_size_text     if True size of the Text Element will be sized to ﬁt the string
                                                      provided in 'text' parm

bool                               click_submits      DO NOT USE. Only listed for backwards compat - Use
                                                      enable_events instead

bool                               enable_events      Turns on the element speciﬁc events. Text events happen
                                                      when the text is clicked

(str/enum)                         relief             relief style around the text. Values are same as progress meter
                                                      relief values. Should be a constant that is deﬁned at starting
                                                      with "RELIEF_" - RELIEF_RAISED, RELIEF_SUNKEN,
                                                      RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE,
                                                      RELIEF_SOLID

Union[str, Tuple[str, int]]        font               speciﬁes the font family, size, etc

str                                text_color         color of the text

str                                background_color   color of background

int                                border_width       number of pixels for the border (if using a relief)

str                                justiﬁcation       how string should be aligned within space provided by size.
                                                      Valid choices = left , right , center

(int, int) or ((int, int),         pad                Amount of padding to put around element (left/right,
(int,int)) or (int,(int,int)) or                      top/bottom) or ((left, right), (top, bottom))
((int, int),int)

Any                                key                Used with window.FindElement and with return values to
                                                      uniquely identify this element to uniquely identify this element

List[List[Union[List[str],str]]]   right_click_menu   A list of lists of Menu items to show when this element is right
                                                      clicked. See user docs for exact format.

str                                tooltip            text, that will appear when mouse hovers over the element

bool                               visible            set visibility state of the element
                                                                                                               v: latest 
Any                                metadata           User metadata that can be set to ANYTHING
Get
Gets the current value of the displayed text

Get()


 Type                        Name                         Meaning

                             return                       The current value


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type         Name             Meaning

 bool         force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                 Name                             Meaning

 str                  tooltip_text                     the text to show in tooltip.


Update
Changes some of the settings for the Text Element. Must call Window.Read or Window.Finalize prior

 Update(value=None,
   background_color=None,
   text_color=None,
   font=None,
   visible=None)
                                                                                                          v: latest 

Parameter Descriptions:
 Type                                   Name                       Meaning

 str                                    value                      new text to show

 str                                    background_color           color of background

 str                                    text_color                 color of the text

 Union[str, Tuple[str, int]]            font                       speciﬁes the font family, size, etc

 bool                                   visible                    set visibility state of the element


bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)


get
Gets the current value of the displayed text

get()


 Type                          Name                   Meaning

                               return                 The current value


get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()

                                                                                                          v: latest 
 Type               Name                 Meaning
 Type              Name                   Meaning

                   return                 width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)


Parameter Descriptions:

 Type          Name            Meaning

 bool          force           if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                  Name       Meaning

 Tuple[int, int]       size       The size in characters, rows typically. In some cases they are pixels
                                                                                                             v: latest 

set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type                Name                           Meaning

 str                 tooltip_text                   the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()



update
Changes some of the settings for the Text Element. Must call Window.Read or Window.Finalize prior

 update(value=None,
   background_color=None,
   text_color=None,
   font=None,
   visible=None)


Parameter Descriptions:

 Type                                 Name                           Meaning

 str                                  value                          new text to show

 str                                  background_color               color of background

 str                                  text_color                     color of the text
                                                                                                             v: latest 

 Union[str, Tuple[str, int]]          font                           speciﬁes the font family, size, etc
 Type                                   Name                          Meaning

 bool                                   visible                       set visibility state of the element



Tree Element
 Tree Element - Presents data in a tree-like manner, much like a ﬁle/folder browser. Uses the TreeData class
 to hold the user's data and pass to the element for display.



 Tree(data=None,
   headings=None,
   visible_column_map=None,
   col_widths=None,
   col0_width=10,
   def_col_width=10,
   auto_size_columns=True,
   max_col_width=20,
   select_mode=None,
   show_expanded=False,
   change_submits=False,
   enable_events=False,
   font=None,
   justiﬁcation="right",
   text_color=None,
   background_color=None,
   header_text_color=None,
   header_background_color=None,
   header_font=None,
   num_rows=None,
   row_height=None,
   pad=None,
   key=None,
   tooltip=None,
   right_click_menu=None,
   visible=True,
   metadata=None)


Parameter Descriptions:

 Type                        Name                           Meaning

 TreeData                    data                           The data represented using a PySimpleGUI provided
                                                            TreeData class

 List[str]                   headings                       List of individual headings for each column         v: latest 
Type                          Name                      Meaning

List[bool]                    visible_column_map        Determines if a column should be visible. If left empty, all
                                                        columns will be shown

List[int]                     col_widths                List of column widths so that individual column widths
                                                        can be controlled

int                           col0_width                Size of Column 0 which is where the row numbers will be
                                                        optionally shown

int                           def_col_width             default column width

bool                          auto_size_columns         if True, the size of a column is determined using the
                                                        contents of the column

int                           max_col_width             the maximum size a column can be

enum                          select_mode               Use same values as found on Table Element. Valid values
                                                        include: TABLE_SELECT_MODE_NONE
                                                        TABLE_SELECT_MODE_BROWSE
                                                        TABLE_SELECT_MODE_EXTENDED

bool                          show_expanded             if True then the tree will be initially shown with all nodes
                                                        completely expanded

bool                          change_submits            DO NOT USE. Only listed for backwards compat - Use
                                                        enable_events instead

bool                          enable_events             Turns on the element speciﬁc events. Tree events happen
                                                        when row is clicked

Union[str, Tuple[str, int]]   font                      speciﬁes the font family, size, etc

str                           justiﬁcation              'left', 'right', 'center' are valid choices

str                           text_color                color of the text

str                           background_color          color of background

str                           header_text_color         sets the text color for the header

str                           header_background_color   sets the background color for the header

                                                                                                             v: latest 
Union[str, Tuple[str, int]]   header_font               speciﬁes the font family, size, etc

int                           num_rows                  The number of rows of the table to display at a time
 Type                            Name                          Meaning

 int                             row_height                    height of a single row in pixels

 (int, int) or ((int, int),      pad                           Amount of padding to put around element (left/right,
 (int,int)) or (int,(int,int))                                 top/bottom) or ((left, right), (top, bottom))
 or ((int, int),int)

 Any                             key                           Used with window.FindElement and with return values to
                                                               uniquely identify this element to uniquely identify this
                                                               element

 str                             tooltip                       text, that will appear when mouse hovers over the
                                                               element

 List[List                       right_click_menu              [Union[List[str],str]]] A list of lists of Menu items to show
                                                               when this element is right clicked. See user docs for
                                                               exact format.

 bool                            visible                       set visibility state of the element

 Any                             metadata                      User metadata that can be set to ANYTHING


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type           Name             Meaning

 bool           force            if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:                                                                                             v: latest 

 Type                   Name                             Meaning
 Type                Name                            Meaning

 str                 tooltip_text                    the text to show in tooltip.


Update
Changes some of the settings for the Tree Element. Must call Window.Read or Window.Finalize prior

 Update(values=None,
   key=None,
   value=None,
   text=None,
   icon=None,
   visible=None)


Parameter Descriptions:

 Type                        Name         Meaning

 TreeData                    values       Representation of the tree

 Any                         key          identiﬁes a particular item in tree to update

 Any                         value        sets the node identiﬁed by key to a particular value

 str                         text         sets the node identiﬁed by ket to this string

 Union[bytes, str]           icon         can be either a base64 icon or a ﬁlename for the icon

 bool                        visible      control visibility of element


add_treeview_data
Not a user function. Recursive method that inserts tree data into the tkinter treeview widget.

 add_treeview_data(node)


Parameter Descriptions:

 Type         Name        Meaning

 TreeData     node        The node to insert. Will insert all nodes from starting point downward, recursively

                                                                                                                 v: latest 
bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                 Meaning

                  return               width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element

 set_focus(force=False)
                                                                                                          v: latest 

Parameter Descriptions:
 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                   Name          Meaning

 Tuple[int, int]        size          The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type                  Name                               Meaning

 str                   tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.

 unhide_row()                                                                                                  v: latest 



update
Changes some of the settings for the Tree Element. Must call Window.Read or Window.Finalize prior

 update(values=None,
   key=None,
   value=None,
   text=None,
   icon=None,
   visible=None)


Parameter Descriptions:

 Type                       Name          Meaning

 TreeData                   values        Representation of the tree

 Any                        key           identiﬁes a particular item in tree to update

 Any                        value         sets the node identiﬁed by key to a particular value

 str                        text          sets the node identiﬁed by ket to this string

 Union[bytes, str]          icon          can be either a base64 icon or a ﬁlename for the icon

 bool                       visible       control visibility of element



TreeData (for Tree Element)
 Class that user ﬁlls in to represent their tree data. It's a very simple tree representation with a root "Node"
 with possibly one or more children "Nodes". Each Node contains a key, text to display, list of values to display
 and an icon. The entire tree is built using a single method, Insert. Nothing else is required to make the tree.


Instantiate the object, initializes the Tree Data, creates a root node for you

 TreeData()



Insert
Inserts a node into the tree. This is how user builds their tree, by Inserting Nodes This is the ONLY user callable
method in the TreeData class

 Insert(parent,
   key,
   text,
   values,                                                                                                           v: latest 
   icon=None)
Parameter Descriptions:

 Type                         Name          Meaning

 Node                         parent        the parent Node

 Any                          key           Used to uniquely identify this node

 str                          text          The text that is displayed at this node's location

 List[Any]                    values        The list of values that are displayed at this node

 Union[str, bytes]            icon          icon


Node
Contains information about the individual node in the tree

 Node(parent,
  key,
  text,
  values,
  icon=None)



insert
Inserts a node into the tree. This is how user builds their tree, by Inserting Nodes This is the ONLY user callable
method in the TreeData class

 insert(parent,
   key,
   text,
   values,
   icon=None)


Parameter Descriptions:

 Type                         Name          Meaning

 Node                         parent        the parent Node

 Any                          key           Used to uniquely identify this node

 str                          text          The text that is displayed at this node's location
                                                                                                              v: latest 
 List[Any]                    values        The list of values that are displayed at this node
 Type                                Name         Meaning

 Union[str, bytes]                   icon         icon



VerticalSeparator Element
 Vertical Separator Element draws a vertical line at the given location. It will span 1 "row". Usually paired with
 Column Element if extra height is needed



 VerticalSeparator(pad=None)


Parameter Descriptions:

 Type                                              Name     Meaning

 (int, int) or ((int, int),(int,int)) or (int,     pad      Amount of padding to put around element (left/right,
 (int,int)) or ((int, int),int)                             top/bottom) or ((left, right), (top, bottom))


SetFocus
Sets the current focus to be on this element

 SetFocus(force=False)


Parameter Descriptions:

 Type            Name              Meaning

 bool            force             if True will call focus_force otherwise calls focus_set


SetTooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 SetTooltip(tooltip_text)


Parameter Descriptions:

 Type                    Name                              Meaning
                                                                                                                      v: latest 
 str                     tooltip_text                      the text to show in tooltip.
bind
Used to add tkinter events to an Element. The tkinter speciﬁc data is in the Element's member variable
user_bind_event

 bind(bind_string, key_modiﬁer)



expand
Causes the Element to expand to ﬁll available space in the X and Y directions. Can specify which or both directions

 expand(expand_x=False,
   expand_y=False,
   expand_row=True)



get_size
Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size
but will return pixels when calling this get_size method.

get_size()


 Type             Name                 Meaning

                  return               width and height of the element


hide_row
Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an
element, including the row container

 hide_row()



set_cursor
Sets the cursor for the current Element.

 set_cursor(cursor)



set_focus
Sets the current focus to be on this element
                                                                                                          v: latest 

 set_focus(force=False)
Parameter Descriptions:

 Type          Name             Meaning

 bool          force            if True will call focus_force otherwise calls focus_set


set_size
Changes the size of an element to a speciﬁc size. It's possible to specify None for one of sizes so that only 1 of the
element's dimensions are changed.

 set_size(size=(None, None))


Parameter Descriptions:

 Type                   Name          Meaning

 Tuple[int, int]        size          The size in characters, rows typically. In some cases they are pixels


set_tooltip
Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as:
window.Element('key').SetToolTip('New tip').

 set_tooltip(tooltip_text)


Parameter Descriptions:

 Type                  Name                               Meaning

 str                   tooltip_text                       the text to show in tooltip.


unbind
Removes a previously bound tkinter event from an Element.

 unbind(bind_string)



unhide_row
Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the
bottom of the window / container, most likely.
                                                                                                               v: latest 

 unhide_row()
Window
 Represents a single Window



 Window(title,
  layout=None,
  default_element_size=(45, 1),
  default_button_element_size=(None, None),
  auto_size_text=None,
  auto_size_buttons=None,
  location=(None, None),
  size=(None, None),
  element_padding=None,
  margins=(None, None),
  button_color=None,
  font=None,
  progress_bar_color=(None, None),
  background_color=None,
  border_depth=None,
  auto_close=False,
  auto_close_duration=3,
  icon=None,
  force_toplevel=False,
  alpha_channel=1,
  return_keyboard_events=False,
  use_default_focus=True,
  text_justiﬁcation=None,
  no_titlebar=False,
  grab_anywhere=False,
  keep_on_top=False,
  resizable=False,
  disable_close=False,
  disable_minimize=False,
  right_click_menu=None,
  transparent_color=None,
  debugger_enabled=True,
  ﬁnalize=False,
  element_justiﬁcation="left",
  ttk_theme=None,
  use_ttk_buttons=None,
  metadata=None)


Parameter Descriptions:

 Type                         Name            Meaning

 str                          title           The title that will be displayed in the Titlebar
                                                                                             and   on 
                                                                                               v: latest
                                              the Taskbar
Type                              Name                          Meaning

List[List[Elements]]              layout                        The layout for the window. Can also be speciﬁed in
                                                                the Layout method

Tuple[int, int]                   default_element_size          (width, height) size in characters (wide) and rows
                                                                (high) for all elements in this window

Tuple[int, int]                   default_button_element_size   (width, height) size in characters (wide) and rows
                                                                (high) for all Button elements in this window

bool                              auto_size_text                True if Elements in Window should be sized to
                                                                exactly ﬁr the length of text

bool                              auto_size_buttons             True if Buttons in this Window should be sized to
                                                                exactly ﬁt the text on this.

Tuple[int, int]                   location                      (x,y) location, in pixels, to locate the upper left
                                                                corner of the window on the screen. Default is to
                                                                center on screen.

Tuple[int, int]                   size                          (width, height) size in pixels for this window.
                                                                Normally the window is autosized to ﬁt contents,
                                                                not set to an absolute size by the user

Tuple[int, int] or ((int, int),   element_padding               Default amount of padding to put around elements
(int,int))                                                      in window (left/right, top/bottom) or ((left, right),
                                                                (top, bottom))

Tuple[int, int]                   margins                       (left/right, top/bottom) Amount of pixels to leave
                                                                inside the window's frame around the edges before
                                                                your elements are shown.

Tuple[str, str]                   button_color                  (text color, button color) Default button colors for all
                                                                buttons in the window

Union[str, Tuple[str, int]]       font                          speciﬁes the font family, size, etc

Tuple[str, str]                   progress_bar_color            (bar color, background color) Sets the default colors
                                                                for all progress bars in the window

str                               background_color              color of background

int                               border_depth                  Default border depth (width) for all elements
                                                                                                            in
                                                                                                              v: the
                                                                                                                 latest 
                                                                window
Type              Name                     Meaning

bool              auto_close               If True, the window will automatically close itself

int               auto_close_duration      Number of seconds to wait before closing the
                                           window

Union[str, str]   icon                     Can be either a ﬁlename or Base64 value. For
                                           Windows if ﬁlename, it MUST be ICO format. For
                                           Linux, must NOT be ICO

bool              force_toplevel           If True will cause this window to skip the normal use
                                           of a hidden master window

ﬂoat              alpha_channel            Sets the opacity of the window. 0 = invisible 1 =
                                           completely visible. Values bewteen 0 & 1 will
                                           produce semi-transparent windows in SOME
                                           environments (The Raspberry Pi always has this
                                           value at 1 and cannot change.

bool              return_keyboard_events   if True key presses on the keyboard will be returned
                                           as Events from Read calls

bool              use_default_focus        If True will use the default focus algorithm to set the
                                           focus to the "Correct" element

str               text_justiﬁcation        Union ['left', 'right', 'center'] Default text justiﬁcation
                                           for all Text Elements in window

bool              no_titlebar              If true, no titlebar nor frame will be shown on
                                           window. This means you cannot minimize the
                                           window and it will not show up on the taskbar

bool              grab_anywhere            If True can use mouse to click and drag to move the
                                           window. Almost every location of the window will
                                           work except input ﬁelds on some systems

bool              keep_on_top              If True, window will be created on top of all other
                                           windows on screen. It can be bumped down if
                                           another window created with this parm

bool              resizable                If True, allows the user to resize the window. Note
                                           the not all Elements will change size or location
                                           when resizing.                               v: latest 
 Type                               Name                       Meaning

 bool                               disable_close              If True, the X button in the top right corner of the
                                                               window will no work. Use with caution and always
                                                               give a way out toyour users

 bool                               disable_minimize           if True the user won't be able to minimize window.
                                                               Good for taking over entire screen and staying that
                                                               way.

 List[List[Union[List[str],str]]]   right_click_menu           A list of lists of Menu items to show when this
                                                               element is right clicked. See user docs for exact
                                                               format.

 str                                transparent_color          Any portion of the window that has this color will be
                                                               completely transparent. You can even click through
                                                               these spots to the window under this window.

 bool                               debugger_enabled           If True then the internal debugger will be enabled

 bool                               ﬁnalize                    If True then the Finalize method will be called. Use
                                                               this rather than chaining .Finalize for cleaner code

 str                                element_justiﬁcation       All elements in the Window itself will have this
                                                               justiﬁcation 'left', 'right', 'center' are valid values

 str                                ttk_theme                  Set the tkinter ttk "theme" of the window. Default =
                                                               DEFAULT_TTK_THEME. Sets all ttk widgets to this
                                                               theme as their default

 bool                               use_ttk_buttons            Affects all buttons in window. True = use ttk
                                                               buttons. False = do not use ttk buttons. None = use
                                                               ttk buttons only if on a Mac

 Any                                metadata                   User metadata that can be set to ANYTHING


AddRow
Adds a single row of elements to a window's self.Rows variables. Generally speaking this is NOT how users should
be building Window layouts. Users, create a single layout (a list of lists) and pass as a parameter to Window object,
or call Window.Layout(layout)

 AddRow(args=*<1 or N object>)
                                                                                                                  v: latest 


AddRows
Loops through a list of lists of elements and adds each row, list, to the layout. This is NOT the best way to go about
creating a window. Sending the entire layout at one time and passing it as a parameter to the Window call is better.

 AddRows(rows)



AlphaChannel
property: AlphaChannel
A property that changes the current alpha channel value (internal value)

 Type      Name       Meaning

           return     (ﬂoat) the current alpha channel setting according to self, not read directly from tkinter


BringToFront
Brings this window to the top of all other windows (perhaps may not be brought before a window made to "stay on
top")

 BringToFront()



Close
Closes window. Users can safely call even if window has been destroyed. Should always call when done with a
window so that resources are properly freed up within your thread.

 Close()



CurrentLocation
Get the current location of the window's top left corner

CurrentLocation()


 Type               Name             Meaning

                    return           The x and y location in tuple form (x,y)


Disable
Disables window from taking any input from the user
                                                                                                                v: latest 
 Disable()
DisableDebugger
Disable the internal debugger. By default the debugger is ENABLED

 DisableDebugger()



Disappear
Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha channel
to 0. NOTE that on some platforms alpha is not supported. The window will remain showing on these platforms. The
Raspberry Pi for example does not have an alpha setting

 Disappear()



Elem
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 Elem(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element

 bool                   silent_on_error   If True do not display popup nor print warning of key errors

 Union[Element,         RETURN            Return value can be: the Element that matches the supplied key if found;
 Error Element,                           an Error Element if silent_on_error is False; None if silent_on_error True;
 None]                                                                                                       v: latest 


Element
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 Element(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element

 bool                   silent_on_error   If True do not display popup nor print warning of key errors

 Union[Element,         RETURN            Return value can be: the Element that matches the supplied key if found;
 Error Element,                           an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


Enable
Re-enables window to take user input after having it be Disabled previously

 Enable()



EnableDebugger
Enables the internal debugger. By default, the debugger IS enabled

 EnableDebugger()



Fill
Fill in elements that are input ﬁelds with data based on a 'values dictionary'                               v: latest 


 Fill(values_dict)
Parameter Descriptions:

 Type                     Name               Meaning

 (Dict[Any:Any])          values_dict        {Element key : value} pairs

 (Window)                 RETURN             returns self so can be chained with other methods


Finalize
Use this method to cause your layout to built into a real tkinter window. In reality this method is like
Read(timeout=0). It doesn't block and uses your layout to create tkinter widgets to represent the elements. Lots of
action!

Finalize()


 Type    Name       Meaning

         return     Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!)


Find
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 Find(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element
                                                                                                                 v: latest 
 bool                   silent_on_error   If True do not display popup nor print warning of key errors
 Type                   Name               Meaning

 Union[Element,         RETURN             Return value can be: the Element that matches the supplied key if found;
 Error Element,                            an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


FindElement
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 FindElement(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name               Meaning

 Any                    key                Used with window.FindElement and with return values to uniquely identify
                                           this element

 bool                   silent_on_error    If True do not display popup nor print warning of key errors

 Union[Element,         RETURN             Return value can be: the Element that matches the supplied key if found;
 Error Element,                            an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


FindElementWithFocus
Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!

FindElementWithFocus()


 Type      Name       Meaning
                                                                                                              v: latest 

           return     An Element if one has been found with focus or None if no element found
GetScreenDimensions
Get the screen dimensions. NOTE - you must have a window already open for this to work (blame tkinter not me)

GetScreenDimensions()


 Type        Name          Meaning

             return        Tuple containing width and height of screen in pixels


GrabAnyWhereOff
Turns off Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been
Finalized or Read.

 GrabAnyWhereOff()



GrabAnyWhereOn
Turns on Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been
Finalized or Read.

 GrabAnyWhereOn()



Hide
Hides the window from the screen and the task bar

 Hide()



Layout
Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as a
parameter to Window object. The parameter method is the currently preferred method. This call to Layout has been
removed from examples contained in documents and in the Demo Programs. Trying to remove this call from history
and replace with sending as a parameter to Window.

 Layout(rows)


Parameter Descriptions:

 Type                             Name              Meaning
                                                                                                       v: latest 
 List[List[Elements]]             rows              Your entire layout
 Type                               Name              Meaning

 (Window)                           RETURN            self so that you can chain method calls


LoadFromDisk
Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format

 LoadFromDisk(ﬁlename)


Parameter Descriptions:

 Type                Name                          Meaning

 str                 ﬁlename                       Pickle Filename to load


Maximize
Maximize the window. This is done differently on a windows system versus a linux or mac one. For non-Windows
the root attribute '-fullscreen' is set to True. For Windows the "root" state is changed to "zoomed" The reason for the
difference is the title bar is removed in some cases when using fullscreen option

 Maximize()



Minimize
Minimize this window to the task bar

 Minimize()



Move
Move the upper left corner of this window to the x,y coordinates provided

 Move(x, y)


Parameter Descriptions:

 Type                  Name                      Meaning

 int                   x                         x coordinate in pixels
                                                                                                              v: latest 
 int                   y                         y coordinate in pixels
Normal
Restore a window to a non-maximized state. Does different things depending on platform. See Maximize for more.

 Normal()



Read
THE biggest deal method in the Window class! This is how you get all of your data from your Window. Pass in a
timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key if no other GUI
events happen ﬁrst.

 Read(timeout=None,
   timeout_key="__TIMEOUT__",
   close=False)


Parameter Descriptions:

 Type                                    Name           Meaning

 int                                     timeout        Milliseconds to wait until the Read will return IF no other
                                                        GUI events happen ﬁrst

 Any                                     timeout_key    The value that will be returned from the call if the timer
                                                        expired

 bool                                    close          if True the window will be closed prior to returning

 Tuple[(Any), Union[Dict[Any:Any]],      RETURN         (event, values)
 List[Any], None]


Reappear
Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel

 Reappear()



Refresh
Refreshes the window by calling tkroot.update(). Can sometimes get away with a refresh instead of a Read. Use this
call when you want something to appear in your Window immediately (as soon as this function is called). Without
this call your changes to a Window will not be visible to the user until the next Read call
                                                                                                            v: latest 
Refresh()


 Type         Name          Meaning
 Type         Name           Meaning

              return          self so that method calls can be easily "chained"



SaveToDisk
Saves the values contained in each of the input areas of the form. Basically saves what would be returned from a
call to Read. It takes these results and saves them to disk using pickle. Note that every element in your layout that is
to be saved must have a key assigned to it.

 SaveToDisk(ﬁlename)


Parameter Descriptions:

 Type           Name              Meaning

 str            ﬁlename           Filename to save the values to in pickled form


SendToBack
Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront

 SendToBack()



SetAlpha
Sets the Alpha Channel for a window. Values are between 0 and 1 where 0 is completely transparent

 SetAlpha(alpha)


Parameter Descriptions:

 Type    Name      Meaning

 ﬂoat    alpha     0 to 1. 0 is completely transparent. 1 is completely visible and solid (can't see through)


SetIcon
Changes the icon that is shown on the title bar and on the task bar. NOTE - The ﬁle type is IMPORTANT and depends
on the OS! Can pass in: * ﬁlename which must be a .ICO icon ﬁle for windows, PNG ﬁle for Linux * bytes object *
BASE64 encoded ﬁle held in a variable
                                                                                                              v: latest 
 SetIcon(icon=None, pngbase64=None)
Parameter Descriptions:

 Type              Name                              Meaning

 str               icon                              Filename or bytes object

 str               pngbase64                         Base64 encoded image


SetTransparentColor
Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.

 SetTransparentColor(color)


Parameter Descriptions:

 Type          Name            Meaning

 str           color           Color string that deﬁnes the transparent color


Size
property: Size
Return the current size of the window in pixels

 Type              Name                   Meaning

                   return                 (width, height) of the window


UnHide
Used to bring back a window that was previously hidden using the Hide method

 UnHide()



VisibilityChanged
This is a completely dummy method that does nothing. It is here so that PySimpleGUIQt programs can make this
call and then have that same source run on plain PySimpleGUI.

VisibilityChanged()

                                                                                                      v: latest 
 Type                            Name                                 Meaning

                                 return
add_row
Adds a single row of elements to a window's self.Rows variables. Generally speaking this is NOT how users should
be building Window layouts. Users, create a single layout (a list of lists) and pass as a parameter to Window object,
or call Window.Layout(layout)

 add_row(args=*<1 or N object>)



add_rows
Loops through a list of lists of elements and adds each row, list, to the layout. This is NOT the best way to go about
creating a window. Sending the entire layout at one time and passing it as a parameter to the Window call is better.

 add_rows(rows)



alpha_channel
property: alpha_channel
A property that changes the current alpha channel value (internal value)

 Type    Name      Meaning

         return    (ﬂoat) the current alpha channel setting according to self, not read directly from tkinter


bind
Used to add tkinter events to a Window. The tkinter speciﬁc data is in the Window's member variable
user_bind_event

 bind(bind_string, key)


Parameter Descriptions:

 Type      Name               Meaning

 str       bind_string        The string tkinter expected in its bind function

 Any       key                The event that will be generated when the tkinter event occurs


bring_to_front
Brings this window to the top of all other windows (perhaps may not be brought before a window made to
                                                                                                      "stay   on 
                                                                                                         v: latest
top")
 bring_to_front()



close
Closes window. Users can safely call even if window has been destroyed. Should always call when done with a
window so that resources are properly freed up within your thread.

 close()



current_location
Get the current location of the window's top left corner

current_location()


 Type               Name           Meaning

                    return         The x and y location in tuple form (x,y)


disable
Disables window from taking any input from the user

 disable()



disable_debugger
Disable the internal debugger. By default the debugger is ENABLED

 disable_debugger()



disappear
Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha channel
to 0. NOTE that on some platforms alpha is not supported. The window will remain showing on these platforms. The
Raspberry Pi for example does not have an alpha setting

 disappear()



elem
                                                                                                          v: latest 
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user
You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 elem(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element

 bool                   silent_on_error   If True do not display popup nor print warning of key errors

 Union[Element,         RETURN            Return value can be: the Element that matches the supplied key if found;
 Error Element,                           an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


element
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 element(key, silent_on_error=False)


Parameter Descriptions:
                                                                                                             v: latest 

 Type                   Name              Meaning
 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element

 bool                   silent_on_error   If True do not display popup nor print warning of key errors

 Union[Element,         RETURN            Return value can be: the Element that matches the supplied key if found;
 Error Element,                           an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


element_list
Returns a list of all elements in the window

element_list()


 Type       Name      Meaning

            return    List of all elements in the window and container elements in the window


enable
Re-enables window to take user input after having it be Disabled previously

 enable()



enable_debugger
Enables the internal debugger. By default, the debugger IS enabled

 enable_debugger()



extend_layout
Adds new rows to an existing container element inside of this window

 extend_layout(container, rows)


Parameter Descriptions:

 Type                         Name        Meaning
                                                                                                             v: latest 

 (Union[Frame, Column,        container   (Union[Frame, Column, Tab]) - The container Element the layout will be
 Tab])                                    placed inside of
 Type                         Name        Meaning

 (List[List[Element]])        rows        (List[List[Element]]) - The layout to be added

 (Window)                     RETURN      (Window) self so could be chained


ﬁll
Fill in elements that are input ﬁelds with data based on a 'values dictionary'

 ﬁll(values_dict)


Parameter Descriptions:

 Type                     Name                Meaning

 (Dict[Any:Any])          values_dict         {Element key : value} pairs

 (Window)                 RETURN              returns self so can be chained with other methods


ﬁnalize
Use this method to cause your layout to built into a real tkinter window. In reality this method is like
Read(timeout=0). It doesn't block and uses your layout to create tkinter widgets to represent the elements. Lots of
action!

 finalize()


 Type     Name      Meaning

          return    Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!)


ﬁnd
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)                                                   v: latest 

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.
 ﬁnd(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name               Meaning

 Any                    key                Used with window.FindElement and with return values to uniquely identify
                                           this element

 bool                   silent_on_error    If True do not display popup nor print warning of key errors

 Union[Element,         RETURN             Return value can be: the Element that matches the supplied key if found;
 Error Element,                            an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


ﬁnd_element
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 ﬁnd_element(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name               Meaning

 Any                    key                Used with window.FindElement and with return values to uniquely identify
                                           this element

 bool                   silent_on_error    If True do not display popup nor print warning of key errors

 Union[Element,         RETURN             Return value can be: the Element that matches the supplied key if found;
 Error Element,                            an Error Element if silent_on_error is False; None if silent_on_error True;
                                                                                                              v: latest 
 None]
ﬁnd_element_with_focus
Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!

find_element_with_focus()


 Type      Name         Meaning

           return       An Element if one has been found with focus or None if no element found


get_screen_dimensions
Get the screen dimensions. NOTE - you must have a window already open for this to work (blame tkinter not me)

get_screen_dimensions()


 Type         Name            Meaning

              return          Tuple containing width and height of screen in pixels


get_screen_size
Returns the size of the "screen" as determined by tkinter. This can vary depending on your operating system and the
number of monitors installed on your system. For Windows, the primary monitor's size is returns. On some multi-
monitored Linux systems, the monitors are combined and the total size is reported as if one screen.

 get_screen_size() -> Tuple[int, int] - Size of the screen in pixels as determined by tkinter



grab_any_where_off
Turns off Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been
Finalized or Read.

 grab_any_where_off()



grab_any_where_on
Turns on Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been
Finalized or Read.

 grab_any_where_on()



hide                                                                                                        v: latest 


Hides the window from the screen and the task bar
 hide()



layout
Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as a
parameter to Window object. The parameter method is the currently preferred method. This call to Layout has been
removed from examples contained in documents and in the Demo Programs. Trying to remove this call from history
and replace with sending as a parameter to Window.

 layout(rows)


Parameter Descriptions:

 Type                               Name              Meaning

 List[List[Elements]]               rows              Your entire layout

 (Window)                           RETURN            self so that you can chain method calls


load_from_disk
Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format

 load_from_disk(ﬁlename)


Parameter Descriptions:

 Type                   Name                       Meaning

 str                    ﬁlename                    Pickle Filename to load


maximize
Maximize the window. This is done differently on a windows system versus a linux or mac one. For non-Windows
the root attribute '-fullscreen' is set to True. For Windows the "root" state is changed to "zoomed" The reason for the
difference is the title bar is removed in some cases when using fullscreen option

 maximize()



minimize
Minimize this window to the task bar                                                                          v: latest 


 minimize()
move
Move the upper left corner of this window to the x,y coordinates provided

 move(x, y)


Parameter Descriptions:

 Type                  Name                      Meaning

 int                   x                         x coordinate in pixels

 int                   y                         y coordinate in pixels


normal
Restore a window to a non-maximized state. Does different things depending on platform. See Maximize for more.

 normal()



read
THE biggest deal method in the Window class! This is how you get all of your data from your Window. Pass in a
timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key if no other GUI
events happen ﬁrst.

 read(timeout=None,
   timeout_key="__TIMEOUT__",
   close=False)


Parameter Descriptions:

 Type                                    Name            Meaning

 int                                     timeout         Milliseconds to wait until the Read will return IF no other
                                                         GUI events happen ﬁrst

 Any                                     timeout_key     The value that will be returned from the call if the timer
                                                         expired

 bool                                    close           if True the window will be closed prior to returning

 Tuple[(Any), Union[Dict[Any:Any]],      RETURN          (event, values)
 List[Any], None]                                                                                            v: latest 
reappear
Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel

 reappear()



refresh
Refreshes the window by calling tkroot.update(). Can sometimes get away with a refresh instead of a Read. Use this
call when you want something to appear in your Window immediately (as soon as this function is called). Without
this call your changes to a Window will not be visible to the user until the next Read call

 refresh()


 Type         Name           Meaning

              return          self so that method calls can be easily "chained"



save_to_disk
Saves the values contained in each of the input areas of the form. Basically saves what would be returned from a
call to Read. It takes these results and saves them to disk using pickle. Note that every element in your layout that is
to be saved must have a key assigned to it.

 save_to_disk(ﬁlename)


Parameter Descriptions:

 Type         Name                Meaning

 str          ﬁlename             Filename to save the values to in pickled form


send_to_back
Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront

 send_to_back()



set_alpha
Sets the Alpha Channel for a window. Values are between 0 and 1 where 0 is completely transparent

 set_alpha(alpha)                                                                                             v: latest 


Parameter Descriptions:
 Type     Name          Meaning

 ﬂoat     alpha         0 to 1. 0 is completely transparent. 1 is completely visible and solid (can't see through)


set_icon
Changes the icon that is shown on the title bar and on the task bar. NOTE - The ﬁle type is IMPORTANT and depends
on the OS! Can pass in: * ﬁlename which must be a .ICO icon ﬁle for windows, PNG ﬁle for Linux * bytes object *
BASE64 encoded ﬁle held in a variable

 set_icon(icon=None, pngbase64=None)


Parameter Descriptions:

 Type                   Name                               Meaning

 str                    icon                               Filename or bytes object

 str                    pngbase64                          Base64 encoded image


set_title
Change the title of the window

 set_title(title)


Parameter Descriptions:

 Type                       Name                Meaning

 str                        title               The string to set the title to


set_transparent_color
Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.

 set_transparent_color(color)


Parameter Descriptions:

 Type               Name            Meaning

                                                                                                                  v: latest 
 str                color           Color string that deﬁnes the transparent color
size
property: size
Return the current size of the window in pixels

 Type              Name                   Meaning

                   return                 (width, height) of the window


un_hide
Used to bring back a window that was previously hidden using the Hide method

 un_hide()



visibility_changed
This is a completely dummy method that does nothing. It is here so that PySimpleGUIQt programs can make this
call and then have that same source run on plain PySimpleGUI.

visibility_changed()


 Type                            Name                                 Meaning

                                 return



Window
 Represents a single Window




                                                                                                      v: latest 
 Window(title,
  layout=None,
  default_element_size=(45, 1),
  default_button_element_size=(None, None),
  auto_size_text=None,
  auto_size_buttons=None,
  location=(None, None),
  size=(None, None),
  element_padding=None,
  margins=(None, None),
  button_color=None,
  font=None,
  progress_bar_color=(None, None),
  background_color=None,
  border_depth=None,
  auto_close=False,
  auto_close_duration=3,
  icon=None,
  force_toplevel=False,
  alpha_channel=1,
  return_keyboard_events=False,
  use_default_focus=True,
  text_justiﬁcation=None,
  no_titlebar=False,
  grab_anywhere=False,
  keep_on_top=False,
  resizable=False,
  disable_close=False,
  disable_minimize=False,
  right_click_menu=None,
  transparent_color=None,
  debugger_enabled=True,
  ﬁnalize=False,
  element_justiﬁcation="left",
  ttk_theme=None,
  use_ttk_buttons=None,
  metadata=None)


Parameter Descriptions:

 Type                         Name                   Meaning

 str                          title                  The title that will be displayed in the Titlebar and on
                                                     the Taskbar

 List[List[Elements]]         layout                 The layout for the window. Can also be speciﬁed in
                                                     the Layout method
                                                                                                   v: latest 
 Tuple[int, int]              default_element_size   (width, height) size in characters (wide) and rows
                                                     (high) for all elements in this window
Type                              Name                          Meaning

Tuple[int, int]                   default_button_element_size   (width, height) size in characters (wide) and rows
                                                                (high) for all Button elements in this window

bool                              auto_size_text                True if Elements in Window should be sized to
                                                                exactly ﬁr the length of text

bool                              auto_size_buttons             True if Buttons in this Window should be sized to
                                                                exactly ﬁt the text on this.

Tuple[int, int]                   location                      (x,y) location, in pixels, to locate the upper left
                                                                corner of the window on the screen. Default is to
                                                                center on screen.

Tuple[int, int]                   size                          (width, height) size in pixels for this window.
                                                                Normally the window is autosized to ﬁt contents,
                                                                not set to an absolute size by the user

Tuple[int, int] or ((int, int),   element_padding               Default amount of padding to put around elements
(int,int))                                                      in window (left/right, top/bottom) or ((left, right),
                                                                (top, bottom))

Tuple[int, int]                   margins                       (left/right, top/bottom) Amount of pixels to leave
                                                                inside the window's frame around the edges before
                                                                your elements are shown.

Tuple[str, str]                   button_color                  (text color, button color) Default button colors for all
                                                                buttons in the window

Union[str, Tuple[str, int]]       font                          speciﬁes the font family, size, etc

Tuple[str, str]                   progress_bar_color            (bar color, background color) Sets the default colors
                                                                for all progress bars in the window

str                               background_color              color of background

int                               border_depth                  Default border depth (width) for all elements in the
                                                                window

bool                              auto_close                    If True, the window will automatically close itself

int                               auto_close_duration           Number of seconds to wait before closing the
                                                                window                                    v: latest 
Type              Name                     Meaning

Union[str, str]   icon                     Can be either a ﬁlename or Base64 value. For
                                           Windows if ﬁlename, it MUST be ICO format. For
                                           Linux, must NOT be ICO

bool              force_toplevel           If True will cause this window to skip the normal use
                                           of a hidden master window

ﬂoat              alpha_channel            Sets the opacity of the window. 0 = invisible 1 =
                                           completely visible. Values bewteen 0 & 1 will
                                           produce semi-transparent windows in SOME
                                           environments (The Raspberry Pi always has this
                                           value at 1 and cannot change.

bool              return_keyboard_events   if True key presses on the keyboard will be returned
                                           as Events from Read calls

bool              use_default_focus        If True will use the default focus algorithm to set the
                                           focus to the "Correct" element

str               text_justiﬁcation        Union ['left', 'right', 'center'] Default text justiﬁcation
                                           for all Text Elements in window

bool              no_titlebar              If true, no titlebar nor frame will be shown on
                                           window. This means you cannot minimize the
                                           window and it will not show up on the taskbar

bool              grab_anywhere            If True can use mouse to click and drag to move the
                                           window. Almost every location of the window will
                                           work except input ﬁelds on some systems

bool              keep_on_top              If True, window will be created on top of all other
                                           windows on screen. It can be bumped down if
                                           another window created with this parm

bool              resizable                If True, allows the user to resize the window. Note
                                           the not all Elements will change size or location
                                           when resizing.

bool              disable_close            If True, the X button in the top right corner of the
                                           window will no work. Use with caution and always
                                           give a way out toyour users
                                                                                             v: latest 
 Type                               Name                         Meaning

 bool                               disable_minimize             if True the user won't be able to minimize window.
                                                                 Good for taking over entire screen and staying that
                                                                 way.

 List[List[Union[List[str],str]]]   right_click_menu             A list of lists of Menu items to show when this
                                                                 element is right clicked. See user docs for exact
                                                                 format.

 str                                transparent_color            Any portion of the window that has this color will be
                                                                 completely transparent. You can even click through
                                                                 these spots to the window under this window.

 bool                               debugger_enabled             If True then the internal debugger will be enabled

 bool                               ﬁnalize                      If True then the Finalize method will be called. Use
                                                                 this rather than chaining .Finalize for cleaner code

 str                                element_justiﬁcation         All elements in the Window itself will have this
                                                                 justiﬁcation 'left', 'right', 'center' are valid values

 str                                ttk_theme                    Set the tkinter ttk "theme" of the window. Default =
                                                                 DEFAULT_TTK_THEME. Sets all ttk widgets to this
                                                                 theme as their default

 bool                               use_ttk_buttons              Affects all buttons in window. True = use ttk
                                                                 buttons. False = do not use ttk buttons. None = use
                                                                 ttk buttons only if on a Mac

 Any                                metadata                     User metadata that can be set to ANYTHING


AddRow
Adds a single row of elements to a window's self.Rows variables. Generally speaking this is NOT how users should
be building Window layouts. Users, create a single layout (a list of lists) and pass as a parameter to Window object,
or call Window.Layout(layout)

 AddRow(args=*<1 or N object>)



AddRows
Loops through a list of lists of elements and adds each row, list, to the layout. This is NOT the best way to 
                                                                                                              gov:about
                                                                                                                   latest 
creating a window. Sending the entire layout at one time and passing it as a parameter to the Window call is better.
 AddRows(rows)



AlphaChannel
property: AlphaChannel
A property that changes the current alpha channel value (internal value)

 Type      Name       Meaning

           return     (ﬂoat) the current alpha channel setting according to self, not read directly from tkinter


BringToFront
Brings this window to the top of all other windows (perhaps may not be brought before a window made to "stay on
top")

 BringToFront()



Close
Closes window. Users can safely call even if window has been destroyed. Should always call when done with a
window so that resources are properly freed up within your thread.

 Close()



CurrentLocation
Get the current location of the window's top left corner

CurrentLocation()


 Type               Name             Meaning

                    return           The x and y location in tuple form (x,y)


Disable
Disables window from taking any input from the user

 Disable()

                                                                                                                v: latest 

DisableDebugger
Disable the internal debugger. By default the debugger is ENABLED
 DisableDebugger()



Disappear
Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha channel
to 0. NOTE that on some platforms alpha is not supported. The window will remain showing on these platforms. The
Raspberry Pi for example does not have an alpha setting

 Disappear()



Elem
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 Elem(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element

 bool                   silent_on_error   If True do not display popup nor print warning of key errors

 Union[Element,         RETURN            Return value can be: the Element that matches the supplied key if found;
 Error Element,                           an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


Element
                                                                                                             v: latest 
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user
You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 Element(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element

 bool                   silent_on_error   If True do not display popup nor print warning of key errors

 Union[Element,         RETURN            Return value can be: the Element that matches the supplied key if found;
 Error Element,                           an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


Enable
Re-enables window to take user input after having it be Disabled previously

 Enable()



EnableDebugger
Enables the internal debugger. By default, the debugger IS enabled

 EnableDebugger()



Fill
Fill in elements that are input ﬁelds with data based on a 'values dictionary'

 Fill(values_dict)
                                                                                                             v: latest 

Parameter Descriptions:
 Type                     Name               Meaning

 (Dict[Any:Any])          values_dict        {Element key : value} pairs

 (Window)                 RETURN             returns self so can be chained with other methods


Finalize
Use this method to cause your layout to built into a real tkinter window. In reality this method is like
Read(timeout=0). It doesn't block and uses your layout to create tkinter widgets to represent the elements. Lots of
action!

Finalize()


 Type    Name       Meaning

         return     Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!)


Find
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 Find(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element

 bool                   silent_on_error   If True do not display popup nor print warning of key errors
                                                                                                                 v: latest 
 Type                   Name               Meaning

 Union[Element,         RETURN             Return value can be: the Element that matches the supplied key if found;
 Error Element,                            an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


FindElement
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 FindElement(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name               Meaning

 Any                    key                Used with window.FindElement and with return values to uniquely identify
                                           this element

 bool                   silent_on_error    If True do not display popup nor print warning of key errors

 Union[Element,         RETURN             Return value can be: the Element that matches the supplied key if found;
 Error Element,                            an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


FindElementWithFocus
Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!

FindElementWithFocus()


 Type      Name       Meaning
                                                                                                              v: latest 

           return     An Element if one has been found with focus or None if no element found
GetScreenDimensions
Get the screen dimensions. NOTE - you must have a window already open for this to work (blame tkinter not me)

GetScreenDimensions()


 Type        Name          Meaning

             return        Tuple containing width and height of screen in pixels


GrabAnyWhereOff
Turns off Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been
Finalized or Read.

 GrabAnyWhereOff()



GrabAnyWhereOn
Turns on Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been
Finalized or Read.

 GrabAnyWhereOn()



Hide
Hides the window from the screen and the task bar

 Hide()



Layout
Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as a
parameter to Window object. The parameter method is the currently preferred method. This call to Layout has been
removed from examples contained in documents and in the Demo Programs. Trying to remove this call from history
and replace with sending as a parameter to Window.

 Layout(rows)


Parameter Descriptions:

 Type                             Name              Meaning
                                                                                                       v: latest 
 List[List[Elements]]             rows              Your entire layout
 Type                               Name              Meaning

 (Window)                           RETURN            self so that you can chain method calls


LoadFromDisk
Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format

 LoadFromDisk(ﬁlename)


Parameter Descriptions:

 Type                Name                          Meaning

 str                 ﬁlename                       Pickle Filename to load


Maximize
Maximize the window. This is done differently on a windows system versus a linux or mac one. For non-Windows
the root attribute '-fullscreen' is set to True. For Windows the "root" state is changed to "zoomed" The reason for the
difference is the title bar is removed in some cases when using fullscreen option

 Maximize()



Minimize
Minimize this window to the task bar

 Minimize()



Move
Move the upper left corner of this window to the x,y coordinates provided

 Move(x, y)


Parameter Descriptions:

 Type                  Name                      Meaning

 int                   x                         x coordinate in pixels
                                                                                                              v: latest 
 int                   y                         y coordinate in pixels
Normal
Restore a window to a non-maximized state. Does different things depending on platform. See Maximize for more.

 Normal()



Read
THE biggest deal method in the Window class! This is how you get all of your data from your Window. Pass in a
timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key if no other GUI
events happen ﬁrst.

 Read(timeout=None,
   timeout_key="__TIMEOUT__",
   close=False)


Parameter Descriptions:

 Type                                    Name           Meaning

 int                                     timeout        Milliseconds to wait until the Read will return IF no other
                                                        GUI events happen ﬁrst

 Any                                     timeout_key    The value that will be returned from the call if the timer
                                                        expired

 bool                                    close          if True the window will be closed prior to returning

 Tuple[(Any), Union[Dict[Any:Any]],      RETURN         (event, values)
 List[Any], None]


Reappear
Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel

 Reappear()



Refresh
Refreshes the window by calling tkroot.update(). Can sometimes get away with a refresh instead of a Read. Use this
call when you want something to appear in your Window immediately (as soon as this function is called). Without
this call your changes to a Window will not be visible to the user until the next Read call
                                                                                                            v: latest 
Refresh()


 Type         Name          Meaning
 Type         Name           Meaning

              return          self so that method calls can be easily "chained"



SaveToDisk
Saves the values contained in each of the input areas of the form. Basically saves what would be returned from a
call to Read. It takes these results and saves them to disk using pickle. Note that every element in your layout that is
to be saved must have a key assigned to it.

 SaveToDisk(ﬁlename)


Parameter Descriptions:

 Type           Name              Meaning

 str            ﬁlename           Filename to save the values to in pickled form


SendToBack
Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront

 SendToBack()



SetAlpha
Sets the Alpha Channel for a window. Values are between 0 and 1 where 0 is completely transparent

 SetAlpha(alpha)


Parameter Descriptions:

 Type    Name      Meaning

 ﬂoat    alpha     0 to 1. 0 is completely transparent. 1 is completely visible and solid (can't see through)


SetIcon
Changes the icon that is shown on the title bar and on the task bar. NOTE - The ﬁle type is IMPORTANT and depends
on the OS! Can pass in: * ﬁlename which must be a .ICO icon ﬁle for windows, PNG ﬁle for Linux * bytes object *
BASE64 encoded ﬁle held in a variable
                                                                                                              v: latest 
 SetIcon(icon=None, pngbase64=None)
Parameter Descriptions:

 Type              Name                              Meaning

 str               icon                              Filename or bytes object

 str               pngbase64                         Base64 encoded image


SetTransparentColor
Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.

 SetTransparentColor(color)


Parameter Descriptions:

 Type          Name            Meaning

 str           color           Color string that deﬁnes the transparent color


Size
property: Size
Return the current size of the window in pixels

 Type              Name                   Meaning

                   return                 (width, height) of the window


UnHide
Used to bring back a window that was previously hidden using the Hide method

 UnHide()



VisibilityChanged
This is a completely dummy method that does nothing. It is here so that PySimpleGUIQt programs can make this
call and then have that same source run on plain PySimpleGUI.

VisibilityChanged()

                                                                                                      v: latest 
 Type                            Name                                 Meaning

                                 return
add_row
Adds a single row of elements to a window's self.Rows variables. Generally speaking this is NOT how users should
be building Window layouts. Users, create a single layout (a list of lists) and pass as a parameter to Window object,
or call Window.Layout(layout)

 add_row(args=*<1 or N object>)



add_rows
Loops through a list of lists of elements and adds each row, list, to the layout. This is NOT the best way to go about
creating a window. Sending the entire layout at one time and passing it as a parameter to the Window call is better.

 add_rows(rows)



alpha_channel
property: alpha_channel
A property that changes the current alpha channel value (internal value)

 Type    Name      Meaning

         return    (ﬂoat) the current alpha channel setting according to self, not read directly from tkinter


bind
Used to add tkinter events to a Window. The tkinter speciﬁc data is in the Window's member variable
user_bind_event

 bind(bind_string, key)


Parameter Descriptions:

 Type      Name               Meaning

 str       bind_string        The string tkinter expected in its bind function

 Any       key                The event that will be generated when the tkinter event occurs


bring_to_front
Brings this window to the top of all other windows (perhaps may not be brought before a window made to
                                                                                                      "stay   on 
                                                                                                         v: latest
top")
 bring_to_front()



close
Closes window. Users can safely call even if window has been destroyed. Should always call when done with a
window so that resources are properly freed up within your thread.

 close()



current_location
Get the current location of the window's top left corner

current_location()


 Type               Name           Meaning

                    return         The x and y location in tuple form (x,y)


disable
Disables window from taking any input from the user

 disable()



disable_debugger
Disable the internal debugger. By default the debugger is ENABLED

 disable_debugger()



disappear
Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha channel
to 0. NOTE that on some platforms alpha is not supported. The window will remain showing on these platforms. The
Raspberry Pi for example does not have an alpha setting

 disappear()



elem
                                                                                                          v: latest 
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user
You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 elem(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element

 bool                   silent_on_error   If True do not display popup nor print warning of key errors

 Union[Element,         RETURN            Return value can be: the Element that matches the supplied key if found;
 Error Element,                           an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


element
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 element(key, silent_on_error=False)


Parameter Descriptions:
                                                                                                             v: latest 

 Type                   Name              Meaning
 Type                   Name              Meaning

 Any                    key               Used with window.FindElement and with return values to uniquely identify
                                          this element

 bool                   silent_on_error   If True do not display popup nor print warning of key errors

 Union[Element,         RETURN            Return value can be: the Element that matches the supplied key if found;
 Error Element,                           an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


element_list
Returns a list of all elements in the window

element_list()


 Type       Name      Meaning

            return    List of all elements in the window and container elements in the window


enable
Re-enables window to take user input after having it be Disabled previously

 enable()



enable_debugger
Enables the internal debugger. By default, the debugger IS enabled

 enable_debugger()



extend_layout
Adds new rows to an existing container element inside of this window

 extend_layout(container, rows)


Parameter Descriptions:

 Type                         Name        Meaning
                                                                                                             v: latest 

 (Union[Frame, Column,        container   (Union[Frame, Column, Tab]) - The container Element the layout will be
 Tab])                                    placed inside of
 Type                         Name        Meaning

 (List[List[Element]])        rows        (List[List[Element]]) - The layout to be added

 (Window)                     RETURN      (Window) self so could be chained


ﬁll
Fill in elements that are input ﬁelds with data based on a 'values dictionary'

 ﬁll(values_dict)


Parameter Descriptions:

 Type                     Name                Meaning

 (Dict[Any:Any])          values_dict         {Element key : value} pairs

 (Window)                 RETURN              returns self so can be chained with other methods


ﬁnalize
Use this method to cause your layout to built into a real tkinter window. In reality this method is like
Read(timeout=0). It doesn't block and uses your layout to create tkinter widgets to represent the elements. Lots of
action!

 finalize()


 Type     Name      Meaning

          return    Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!)


ﬁnd
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)                                                   v: latest 

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.
 ﬁnd(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name               Meaning

 Any                    key                Used with window.FindElement and with return values to uniquely identify
                                           this element

 bool                   silent_on_error    If True do not display popup nor print warning of key errors

 Union[Element,         RETURN             Return value can be: the Element that matches the supplied key if found;
 Error Element,                            an Error Element if silent_on_error is False; None if silent_on_error True;
 None]


ﬁnd_element
Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the
user

You can perform the same operation by writing this statement: element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way" window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return
None if no match is found which may cause your code to crash if not checked for.

 ﬁnd_element(key, silent_on_error=False)


Parameter Descriptions:

 Type                   Name               Meaning

 Any                    key                Used with window.FindElement and with return values to uniquely identify
                                           this element

 bool                   silent_on_error    If True do not display popup nor print warning of key errors

 Union[Element,         RETURN             Return value can be: the Element that matches the supplied key if found;
 Error Element,                            an Error Element if silent_on_error is False; None if silent_on_error True;
                                                                                                              v: latest 
 None]
ﬁnd_element_with_focus
Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!

find_element_with_focus()


 Type      Name         Meaning

           return       An Element if one has been found with focus or None if no element found


get_screen_dimensions
Get the screen dimensions. NOTE - you must have a window already open for this to work (blame tkinter not me)

get_screen_dimensions()


 Type         Name            Meaning

              return          Tuple containing width and height of screen in pixels


get_screen_size
Returns the size of the "screen" as determined by tkinter. This can vary depending on your operating system and the
number of monitors installed on your system. For Windows, the primary monitor's size is returns. On some multi-
monitored Linux systems, the monitors are combined and the total size is reported as if one screen.

 get_screen_size() -> Tuple[int, int] - Size of the screen in pixels as determined by tkinter



grab_any_where_off
Turns off Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been
Finalized or Read.

 grab_any_where_off()



grab_any_where_on
Turns on Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been
Finalized or Read.

 grab_any_where_on()



hide                                                                                                        v: latest 


Hides the window from the screen and the task bar
 hide()



layout
Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as a
parameter to Window object. The parameter method is the currently preferred method. This call to Layout has been
removed from examples contained in documents and in the Demo Programs. Trying to remove this call from history
and replace with sending as a parameter to Window.

 layout(rows)


Parameter Descriptions:

 Type                               Name              Meaning

 List[List[Elements]]               rows              Your entire layout

 (Window)                           RETURN            self so that you can chain method calls


load_from_disk
Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format

 load_from_disk(ﬁlename)


Parameter Descriptions:

 Type                   Name                       Meaning

 str                    ﬁlename                    Pickle Filename to load


maximize
Maximize the window. This is done differently on a windows system versus a linux or mac one. For non-Windows
the root attribute '-fullscreen' is set to True. For Windows the "root" state is changed to "zoomed" The reason for the
difference is the title bar is removed in some cases when using fullscreen option

 maximize()



minimize
Minimize this window to the task bar                                                                          v: latest 


 minimize()
move
Move the upper left corner of this window to the x,y coordinates provided

 move(x, y)


Parameter Descriptions:

 Type                  Name                      Meaning

 int                   x                         x coordinate in pixels

 int                   y                         y coordinate in pixels


normal
Restore a window to a non-maximized state. Does different things depending on platform. See Maximize for more.

 normal()



read
THE biggest deal method in the Window class! This is how you get all of your data from your Window. Pass in a
timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key if no other GUI
events happen ﬁrst.

 read(timeout=None,
   timeout_key="__TIMEOUT__",
   close=False)


Parameter Descriptions:

 Type                                    Name            Meaning

 int                                     timeout         Milliseconds to wait until the Read will return IF no other
                                                         GUI events happen ﬁrst

 Any                                     timeout_key     The value that will be returned from the call if the timer
                                                         expired

 bool                                    close           if True the window will be closed prior to returning

 Tuple[(Any), Union[Dict[Any:Any]],      RETURN          (event, values)
 List[Any], None]                                                                                            v: latest 
reappear
Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel

 reappear()



refresh
Refreshes the window by calling tkroot.update(). Can sometimes get away with a refresh instead of a Read. Use this
call when you want something to appear in your Window immediately (as soon as this function is called). Without
this call your changes to a Window will not be visible to the user until the next Read call

 refresh()


 Type         Name           Meaning

              return          self so that method calls can be easily "chained"



save_to_disk
Saves the values contained in each of the input areas of the form. Basically saves what would be returned from a
call to Read. It takes these results and saves them to disk using pickle. Note that every element in your layout that is
to be saved must have a key assigned to it.

 save_to_disk(ﬁlename)


Parameter Descriptions:

 Type         Name                Meaning

 str          ﬁlename             Filename to save the values to in pickled form


send_to_back
Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront

 send_to_back()



set_alpha
Sets the Alpha Channel for a window. Values are between 0 and 1 where 0 is completely transparent

 set_alpha(alpha)                                                                                             v: latest 


Parameter Descriptions:
 Type    Name      Meaning

 ﬂoat    alpha     0 to 1. 0 is completely transparent. 1 is completely visible and solid (can't see through)


set_icon
Changes the icon that is shown on the title bar and on the task bar. NOTE - The ﬁle type is IMPORTANT and depends
on the OS! Can pass in: * ﬁlename which must be a .ICO icon ﬁle for windows, PNG ﬁle for Linux * bytes object *
BASE64 encoded ﬁle held in a variable

 set_icon(icon=None, pngbase64=None)


Parameter Descriptions:

 Type              Name                               Meaning

 str               icon                               Filename or bytes object

 str               pngbase64                          Base64 encoded image


set_transparent_color
Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.

 set_transparent_color(color)


Parameter Descriptions:

 Type          Name             Meaning

 str           color            Color string that deﬁnes the transparent color


size
property: size
Return the current size of the window in pixels

 Type              Name                   Meaning

                   return                 (width, height) of the window

                                                                                                             v: latest 
un_hide
Used to bring back a window that was previously hidden using the Hide method
 un_hide()



visibility_changed
This is a completely dummy method that does nothing. It is here so that PySimpleGUIQt programs can make this
call and then have that same source run on plain PySimpleGUI.

visibility_changed()


 Type                            Name                                 Meaning

                                 return



Function Reference
 CButton(button_text,
   image_ﬁlename=None,
   image_data=None,
   image_size=(None, None),
   image_subsample=None,
   border_width=None,
   tooltip=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   font=None,
   bind_return_key=False,
   disabled=False,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type              Name              Meaning

 str               button_text       text in the button

 str               image_ﬁlename     image ﬁlename if there is a button image :param image_data: in-RAM image
                                     to be displayed on button :param image_size: size of button image in pixels
                                     :param image_subsample:amount to reduce the size of the image :param
                                     border_width: width of border around element :param tooltip: text, that will
                                     appear when mouse hovers over the element                             v: latest 

 Tuple[int, int]   size              (w,h) w=characters-wide, h=rows-high
 Type               Name               Meaning

 bool               auto_size_button   True if button size is determined by button text

 Tuple[str, str]    button_color       button color (foreground, background)

 Union[str,         font               speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool               bind_return_key    (Default = False) :param disabled: set disable state for element (Default =
                                       False)

 (int, int) or      focus              if focus should be set to this :param pad: Amount of padding to put around
 ((int, int),                          element in pixels (left/right, top/bottom)
 (int,int)) or
 (int,(int,int))
 or ((int,
 int),int)

 Union[str, int,    key                key for uniquely identify this element (for window.FindElement)
 tuple]

 (Button)           RETURN             returns a button


Button that will show a calendar chooser window. Fills in the target element with result




                                                                                                             v: latest 
 CalendarButton(button_text,
   target=(555666777, -1),
   close_when_date_chosen=True,
   default_date_m_d_y=(None, None, None),
   image_ﬁlename=None,
   image_data=None,
   image_size=(None, None),
   image_subsample=None,
   tooltip=None,
   border_width=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   disabled=False,
   font=None,
   bind_return_key=False,
   focus=False,
   pad=None,
   key=None,
   locale=None,
   format="%Y-%m-%d %H:%M:%S",
   begin_at_sunday_plus=0,
   month_names=None,
   day_abbreviations=None,
   title="Choose Date",
   no_titlebar=True,
   location=(None, None),
   metadata=None)


Parameter Descriptions:

 Type                                       Name                     Meaning

 str                                        button_text              text in the button

 Union[(int, int), Any]                     target                   Key or "coordinate" (see docs) of target
                                                                     element

 bool                                       close_when_date_chosen   (Default = True)

 (int, int or None, int)                    default_date_m_d_y       Beginning date to show

 image ﬁlename if there is a button         image_ﬁlename            image ﬁlename if there is a button image
 image

 in-RAM image to be displayed on            image_data               in-RAM image to be displayed on button
 button                                                                                                 v: latest 

 (Default = (None))                         image_size               (Default = (None))
Type                                            Name                Meaning

amount to reduce the size of the image          image_subsample     amount to reduce the size of the image

str                                             tooltip             text, that will appear when mouse hovers
                                                                    over the element

width of border around element                  border_width        width of border around element

Tuple[int, int]                                 size                (w,h) w=characters-wide, h=rows-high

bool                                            auto_size_button    True if button size is determined by button
                                                                    text

Tuple[str, str]                                 button_color        button color (foreground, background)

bool                                            disabled            set disable state for element (Default =
                                                                    False)

Union[str, Tuple[str, int]]                     font                speciﬁes the font family, size, etc

bool                                            bind_return_key     (Default = False)

bool                                            focus               if focus should be set to this

(int, int) or ((int, int),(int,int)) or (int,   pad                 Amount of padding to put around element
(int,int)) or ((int, int),int)                                      in pixels (left/right, top/bottom)

Union[str, int, tuple]                          key                 key for uniquely identify this element (for
                                                                    window.FindElement)

str                                             locale              deﬁnes the locale used to get day names

str                                             format              formats result using this strftime format

List[str]                                       month_names         optional list of month names to use
                                                                    (should be 12 items)

List[str]                                       day_abbreviations   optional list of abbreviations to display as
                                                                    the day of week

str                                             title               Title shown on the date chooser window

bool                                            no_titlebar         if True no titlebar will be shown on the date
                                                                    chooser window                      v: latest 
 Type                                                 Name                        Meaning

 (int, int)                                           location                    Location on the screen (x,y) to show the
                                                                                  calendar popup window

 Any                                                  metadata                    Anything you want to store along with this
                                                                                  button

 (Button)                                             RETURN                      returns a button



 Cancel(button_text="Cancel",
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   disabled=False,
   tooltip=None,
   font=None,
   bind_return_key=False,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                                   Name                 Meaning

 Tuple[int, int]                        button_text          text in the button (Default value = 'Cancel') :param size: (w,h)
                                                             w=characters-wide, h=rows-high

 bool                                   auto_size_button     True if button size is determined by button text

 Tuple[str, str]                        button_color         button color (foreground, background)

 bool                                   disabled             set disable state for element (Default = False)

 str                                    tooltip              text, that will appear when mouse hovers over the element

 Union[str, Tuple[str, int]]            font                 speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int))   bind_return_key      (Default = False) :param focus: if focus should be set to this
 or (int,(int,int)) or ((int,                                :param pad: Amount of padding to put around element in pixels
 int),int)                                                   (left/right, top/bottom)
                                                                                                                       v: latest 
 Union[str, int, tuple]                 key                  key for uniquely identify this element (for window.FindElement)
 CloseButton(button_text,
   image_ﬁlename=None,
   image_data=None,
   image_size=(None, None),
   image_subsample=None,
   border_width=None,
   tooltip=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   font=None,
   bind_return_key=False,
   disabled=False,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type               Name               Meaning

 str                button_text        text in the button

 str                image_ﬁlename      image ﬁlename if there is a button image :param image_data: in-RAM image
                                       to be displayed on button :param image_size: size of button image in pixels
                                       :param image_subsample:amount to reduce the size of the image :param
                                       border_width: width of border around element :param tooltip: text, that will
                                       appear when mouse hovers over the element

 Tuple[int, int]    size               (w,h) w=characters-wide, h=rows-high

 bool               auto_size_button   True if button size is determined by button text

 Tuple[str, str]    button_color       button color (foreground, background)

 Union[str,         font               speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool               bind_return_key    (Default = False) :param disabled: set disable state for element (Default =
                                       False)

 (int, int) or      focus              if focus should be set to this :param pad: Amount of padding to put around
 ((int, int),                          element in pixels (left/right, top/bottom)
 (int,int)) or
 (int,(int,int))                                                                                             v: latest 

 or ((int,
 int),int)
 Type              Name                Meaning

 Union[str, int,   key                 key for uniquely identify this element (for window.FindElement)
 tuple]

 (Button)          RETURN              returns a button



 ColorChooserButton(button_text,
   target=(None, None),
   image_ﬁlename=None,
   image_data=None,
   image_size=(None, None),
   image_subsample=None,
   tooltip=None,
   border_width=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   disabled=False,
   font=None,
   bind_return_key=False,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type               Name                Meaning

 str                button_text         text in the button

 str                target              :param image_ﬁlename: image ﬁlename if there is a button image :param
                                        image_data: in-RAM image to be displayed on button :param image_size:
                                        (Default = (None)) :param image_subsample:amount to reduce the size of
                                        the image :param tooltip: text, that will appear when mouse hovers over the
                                        element

 Tuple[int, int]    border_width        width of border around element :param size: (w,h) w=characters-wide,
                                        h=rows-high

 bool               auto_size_button    True if button size is determined by button text

 Tuple[str, str]    button_color        button color (foreground, background)
                                                                                                           v: latest 
 bool               disabled            set disable state for element (Default = False)
 Type                   Name                 Meaning

 Union[str,             font                 speciﬁes the font family, size, etc
 Tuple[str, int]]

 (int, int) or ((int,   bind_return_key      (Default = False) :param focus: if focus should be set to this :param pad:
 int),(int,int)) or                          Amount of padding to put around element in pixels (left/right, top/bottom)
 (int,(int,int)) or
 ((int, int),int)

 Union[str, int,        key                  key for uniquely identify this element (for window.FindElement)
 tuple]

 (Button)               RETURN               returns a button



 Debug(button_text="",
  size=(None, None),
  auto_size_button=None,
  button_color=None,
  disabled=False,
  font=None,
  tooltip=None,
  bind_return_key=False,
  focus=False,
  pad=None,
  key=None,
  metadata=None)


Parameter Descriptions:

 Type                              Name                   Meaning

 Tuple[int, int]                   button_text            text in the button (Default value = '') :param size: (w,h)
                                                          w=characters-wide, h=rows-high

 bool                              auto_size_button       True if button size is determined by button text

 Tuple[str, str]                   button_color           button color (foreground, background)

 bool                              disabled               set disable state for element (Default = False)

 Union[str, Tuple[str, int]]       font                   speciﬁes the font family, size, etc

 str                               tooltip                text, that will appear when mouse hovers over the element
                                                                                                                        v: latest 
 Type                                   Name                Meaning

 (int, int) or ((int, int),(int,int))   bind_return_key     (Default = False) :param focus: if focus should be set to this
 or (int,(int,int)) or ((int,                               :param pad: Amount of padding to put around element in pixels
 int),int)                                                  (left/right, top/bottom)

 Union[str, int, tuple]                 key                 key for uniquely identify this element (for window.FindElement)

 (Button)                               RETURN              returns a button



 DummyButton(button_text,
  image_ﬁlename=None,
  image_data=None,
  image_size=(None, None),
  image_subsample=None,
  border_width=None,
  tooltip=None,
  size=(None, None),
  auto_size_button=None,
  button_color=None,
  font=None,
  disabled=False,
  bind_return_key=False,
  focus=False,
  pad=None,
  key=None,
  metadata=None)


Parameter Descriptions:

 Type                 Name                    Meaning

 str                  button_text             text in the button

 str                  image_ﬁlename           image ﬁlename if there is a button image :param image_data: in-RAM image
                                              to be displayed on button :param image_size: size of button image in pixels
                                              :param image_subsample:amount to reduce the size of the image :param
                                              border_width: width of border around element :param tooltip: text, that will
                                              appear when mouse hovers over the element

 Tuple[int, int]      size                    (w,h) w=characters-wide, h=rows-high

 bool                 auto_size_button        True if button size is determined by button text

 Tuple[str, str]      button_color            button color (foreground, background)                                v: latest 
 Type               Name               Meaning

 Union[str,         font               speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool               disabled           set disable state for element (Default = False)

 (int, int) or      bind_return_key    (Default = False) :param focus: if focus should be set to this :param pad:
 ((int, int),                          Amount of padding to put around element in pixels (left/right, top/bottom)
 (int,int)) or
 (int,(int,int))
 or ((int,
 int),int)

 Union[str, int,    key                key for uniquely identify this element (for window.FindElement)
 tuple]

 (Button)           RETURN             returns a button



 Exit(button_text="Exit",
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   disabled=False,
   tooltip=None,
   font=None,
   bind_return_key=False,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                            Name                Meaning

 Tuple[int, int]                 button_text         text in the button (Default value = 'Exit') :param size: (w,h)
                                                     w=characters-wide, h=rows-high

 bool                            auto_size_button    True if button size is determined by button text

 Tuple[str, str]                 button_color        button color (foreground, background)

 bool                            disabled            set disable state for element (Default = False)            v: latest 

 str                             tooltip             text, that will appear when mouse hovers over the element
 Type                                   Name                Meaning

 Union[str, Tuple[str, int]]            font                speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int))   bind_return_key     (Default = False) :param focus: if focus should be set to this
 or (int,(int,int)) or ((int,                               :param pad: Amount of padding to put around element in pixels
 int),int)                                                  (left/right, top/bottom)

 Union[str, int, tuple]                 key                 key for uniquely identify this element (for window.FindElement)



 FileBrowse(button_text="Browse",
   target=(555666777, -1),
   ﬁle_types=(('ALL Files', '*.*'),),
   initial_folder=None,
   tooltip=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   change_submits=False,
   enable_events=False,
   font=None,
   disabled=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                   Name                   Meaning

 str                    button_text            text in the button (Default value = 'Browse') :param target: key or (row,col)
                                               target for the button (Default value = (ThisRow, -1)) :param ﬁle_types:
                                               (Default value = (("ALL Files", "."))) :param initial_folder: starting path for
                                               folders and ﬁles :param tooltip: text, that will appear when mouse hovers
                                               over the element

 Tuple[int, int]        size                   (w,h) w=characters-wide, h=rows-high

 bool                   auto_size_button       True if button size is determined by button text

 Tuple[str, str]        button_color           button color (foreground, background)

 Union[str,             change_submits         If True, pressing Enter key submits window (Default = False) :param
 Tuple[str, int]]                              enable_events: Turns on the element speciﬁc events.(Default = False)
                                                                                                                  v: latest 
                                               :param font: speciﬁes the font family, size, etc

 bool                   disabled               set disable state for element (Default = False)
 Type                   Name               Meaning

 (int, int) or ((int,   pad                Amount of padding to put around element in pixels (left/right, top/bottom)
 int),(int,int)) or
 (int,(int,int)) or
 ((int, int),int)

 Union[str, int,        key                key for uniquely identify this element (for window.FindElement)
 tuple]

 (Button)               RETURN             returns a button



 FileSaveAs(button_text="Save As...",
   target=(555666777, -1),
   ﬁle_types=(('ALL Files', '*.*'),),
   initial_folder=None,
   disabled=False,
   tooltip=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   change_submits=False,
   enable_events=False,
   font=None,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                   Name               Meaning

 bool                   button_text        text in the button (Default value = 'Save As...') :param target: key or (row,col)
                                           target for the button (Default value = (ThisRow, -1)) :param ﬁle_types:
                                           (Default value = (("ALL Files", "."))) :param initial_folder: starting path for
                                           folders and ﬁles :param disabled: set disable state for element (Default =
                                           False)

 str                    tooltip            text, that will appear when mouse hovers over the element

 Tuple[int, int]        size               (w,h) w=characters-wide, h=rows-high

 bool                   auto_size_button   True if button size is determined by button text
                                                                                                                  v: latest 
 Tuple[str, str]        button_color       button color (foreground, background)
 Type                   Name               Meaning

 Union[str,             change_submits     If True, pressing Enter key submits window (Default = False) :param
 Tuple[str, int]]                          enable_events: Turns on the element speciﬁc events.(Default = False)
                                           :param font: speciﬁes the font family, size, etc

 (int, int) or ((int,   pad                Amount of padding to put around element in pixels (left/right, top/bottom)
 int),(int,int)) or
 (int,(int,int)) or
 ((int, int),int)

 Union[str, int,        key                key for uniquely identify this element (for window.FindElement)
 tuple]

 (Button)               RETURN             returns a button


Allows browsing of multiple ﬁles. File list is returned as a single list with the delimeter deﬁned using the variable
BROWSE_FILES_DELIMETER. This defaults to ';' but is changable by the user

 FilesBrowse(button_text="Browse",
   target=(555666777, -1),
   ﬁle_types=(('ALL Files', '*.*'),),
   disabled=False,
   initial_folder=None,
   tooltip=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   change_submits=False,
   enable_events=False,
   font=None,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                     Name                Meaning

 bool                     button_text         text in the button (Default value = 'Browse') :param target: key or
                                              (row,col) target for the button (Default value = (ThisRow, -1)) :param
                                              ﬁle_types: (Default value = (("ALL Files", "."))) :param disabled: set
                                              disable state for element (Default = False)

 str                      initial_folder                                                                           v: latest 
                                              starting path for folders and ﬁles :param tooltip: text, that will appear
                                              when mouse hovers over the element
 Type                       Name                Meaning

 Tuple[int, int]            size                (w,h) w=characters-wide, h=rows-high

 bool                       auto_size_button    True if button size is determined by button text

 Tuple[str, str]            button_color        button color (foreground, background)

 Union[str, Tuple[str,      change_submits      If True, pressing Enter key submits window (Default = False) :param
 int]]                                          enable_events: Turns on the element speciﬁc events.(Default = False)
                                                :param font: speciﬁes the font family, size, etc

 (int, int) or ((int,       pad                 Amount of padding to put around element in pixels (left/right,
 int),(int,int)) or (int,                       top/bottom)
 (int,int)) or ((int,
 int),int)

 Union[str, int,            key                 key for uniquely identify this element (for window.FindElement)
 tuple]

 (Button)                   RETURN              returns a button


Fills a window with values provided in a values dictionary { element_key : new_value }

 FillFormWithValues(window, values_dict)


Parameter Descriptions:

 Type                   Name          Meaning

 Window                 window        The window object to ﬁll

 (Dict[Any:Any])        values_dict   A dictionary with element keys as key and value is values parm for Update call




                                                                                                                  v: latest 
 FolderBrowse(button_text="Browse",
   target=(555666777, -1),
   initial_folder=None,
   tooltip=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   disabled=False,
   change_submits=False,
   enable_events=False,
   font=None,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                 Name               Meaning

 str                  button_text        text in the button (Default value = 'Browse')

 key or (row,col)     target             target for the button (Default value = (ThisRow, -1))

 str                  initial_folder     starting path for folders and ﬁles

 str                  tooltip            text, that will appear when mouse hovers over the element

 Tuple[int, int]      size               (w,h) w=characters-wide, h=rows-high



 Help(button_text="Help",
  size=(None, None),
  auto_size_button=None,
  button_color=None,
  disabled=False,
  font=None,
  tooltip=None,
  bind_return_key=False,
  focus=False,
  pad=None,
  key=None,
  metadata=None)


Parameter Descriptions:

 Type                           Name               Meaning
                                                                                                             v: latest 
 Tuple[int, int]                button_text        text in the button (Default value = 'Help') :param size: (w,h)
                                                   w=characters-wide, h=rows-high
 Type                                   Name               Meaning

 bool                                   auto_size_button   True if button size is determined by button text

 Tuple[str, str]                        button_color       button color (foreground, background)

 bool                                   disabled           set disable state for element (Default = False)

 Union[str, Tuple[str, int]]            font               speciﬁes the font family, size, etc

 str                                    tooltip            text, that will appear when mouse hovers over the element

 (int, int) or ((int, int),(int,int))   bind_return_key    (Default = False) :param focus: if focus should be set to this
 or (int,(int,int)) or ((int,                              :param pad: Amount of padding to put around element in pixels
 int),int)                                                 (left/right, top/bottom)

 Union[str, int, tuple]                 key                key for uniquely identify this element (for window.FindElement)

 (Button)                               RETURN             returns a button



 No(button_text="No",
  size=(None, None),
  auto_size_button=None,
  button_color=None,
  disabled=False,
  tooltip=None,
  font=None,
  bind_return_key=False,
  focus=False,
  pad=None,
  key=None,
  metadata=None)


Parameter Descriptions:

 Type                                   Name               Meaning

 Tuple[int, int]                        button_text        text in the button (Default value = 'No') :param size: (w,h)
                                                           w=characters-wide, h=rows-high

 bool                                   auto_size_button   True if button size is determined by button text

 Tuple[str, str]                        button_color       button color (foreground, background)

 bool                                   disabled           set disable state for element (Default = False)           v: latest 


 str                                    tooltip            text, that will appear when mouse hovers over the element
 Type                                      Name                  Meaning

 Union[str, Tuple[str, int]]               font                  speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int))      bind_return_key       (Default = False) :param focus: if focus should be set to this
 or (int,(int,int)) or ((int,                                    :param pad: Amount of padding to put around element in pixels
 int),int)                                                       (left/right, top/bottom)

 Union[str, int, tuple]                    key                   key for uniquely identify this element (for window.FindElement)



 OK(button_text="OK",
  size=(None, None),
  auto_size_button=None,
  button_color=None,
  disabled=False,
  bind_return_key=True,
  tooltip=None,
  font=None,
  focus=False,
  pad=None,
  key=None,
  metadata=None)


Parameter Descriptions:

 Type                                             Name                Meaning

 Tuple[int, int]                                  button_text         text in the button (Default value = 'OK') :param size: (w,h)
                                                                      w=characters-wide, h=rows-high

 bool                                             auto_size_button    True if button size is determined by button text

 Tuple[str, str]                                  button_color        button color (foreground, background)

 bool                                             disabled            set disable state for element (Default = False)

 str                                              bind_return_key     (Default = True) :param tooltip: text, that will appear when
                                                                      mouse hovers over the element

 Union[str, Tuple[str, int]]                      font                speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int)) or          focus               if focus should be set to this :param pad: Amount of
 (int,(int,int)) or ((int, int),int)                                  padding to put around element in pixels (left/right,
                                                                      top/bottom)
                                                                                                                           v: latest 
 Type                               Name                     Meaning

 Union[str, int, tuple]             key                      key for uniquely identify this element (for
                                                             window.FindElement)

 (Button)                           RETURN                   returns a button


Dumps an Object's values as a formatted string. Very nicely done. Great way to display an object's member variables
in human form

 ObjToString(obj, extra="   ")


Parameter Descriptions:

 Type              Name              Meaning

 Any               obj               The object to display

 str               extra             (Default value = ' ')

 (str)             RETURN            Formatted output of the object's values


Dumps an Object's values as a formatted string. Very nicely done. Great way to display an object's member variables
in human form Returns only the top-most object's variables instead of drilling down to dispolay more

 ObjToStringSingleObj(obj)



 Ok(button_text="Ok",
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   disabled=False,
   bind_return_key=True,
   tooltip=None,
   font=None,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                               Name                     Meaning
                                                                                                                  v: latest 

 Tuple[int, int]                    button_text              text in the button (Default value = 'Ok') :param size: (w,h)
                                                             w=characters-wide, h=rows-high
 Type                                      Name               Meaning

 bool                                      auto_size_button   True if button size is determined by button text

 Tuple[str, str]                           button_color       button color (foreground, background)

 bool                                      disabled           set disable state for element (Default = False)

 str                                       bind_return_key    (Default = True) :param tooltip: text, that will appear when
                                                              mouse hovers over the element

 Union[str, Tuple[str, int]]               font               speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int)) or   focus              if focus should be set to this :param pad: Amount of
 (int,(int,int)) or ((int, int),int)                          padding to put around element in pixels (left/right,
                                                              top/bottom)

 Union[str, int, tuple]                    key                key for uniquely identify this element (for
                                                              window.FindElement)

 (Button)                                  RETURN             returns a button



 Open(button_text="Open",
  size=(None, None),
  auto_size_button=None,
  button_color=None,
  disabled=False,
  bind_return_key=True,
  tooltip=None,
  font=None,
  focus=False,
  pad=None,
  key=None,
  metadata=None)


Parameter Descriptions:

 Type                                      Name               Meaning

 Tuple[int, int]                           button_text        text in the button (Default value = 'Open') :param size: (w,h)
                                                              w=characters-wide, h=rows-high

 bool                                      auto_size_button   True if button size is determined by button text
                                                                                                                   v: latest 
 Tuple[str, str]                           button_color       button color (foreground, background)

 bool                                      disabled           set disable state for element (Default = False)
 Type                                             Name               Meaning

 str                                              bind_return_key    (Default = True) :param tooltip: text, that will appear when
                                                                     mouse hovers over the element

 Union[str, Tuple[str, int]]                      font               speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int)) or          focus              if focus should be set to this :param pad: Amount of
 (int,(int,int)) or ((int, int),int)                                 padding to put around element in pixels (left/right,
                                                                     top/bottom)

 Union[str, int, tuple]                           key                key for uniquely identify this element (for
                                                                     window.FindElement)



 Quit(button_text="Quit",
  size=(None, None),
  auto_size_button=None,
  button_color=None,
  disabled=False,
  tooltip=None,
  font=None,
  bind_return_key=False,
  focus=False,
  pad=None,
  key=None,
  metadata=None)


Parameter Descriptions:

 Type                                      Name                 Meaning

 Tuple[int, int]                           button_text          text in the button (Default value = 'Quit') :param size: (w,h)
                                                                w=characters-wide, h=rows-high

 bool                                      auto_size_button     True if button size is determined by button text

 Tuple[str, str]                           button_color         button color (foreground, background)

 bool                                      disabled             set disable state for element (Default = False)

 str                                       tooltip              text, that will appear when mouse hovers over the element

 Union[str, Tuple[str, int]]               font                 speciﬁes the font family, size, etc

                                                                                                                           v: latest 
 Type                                   Name                Meaning

 (int, int) or ((int, int),(int,int))   bind_return_key     (Default = False) :param focus: if focus should be set to this
 or (int,(int,int)) or ((int,                               :param pad: Amount of padding to put around element in pixels
 int),int)                                                  (left/right, top/bottom)

 Union[str, int, tuple]                 key                 key for uniquely identify this element (for window.FindElement)

 (Button)                               RETURN              returns a button



 RButton(button_text,
   image_ﬁlename=None,
   image_data=None,
   image_size=(None, None),
   image_subsample=None,
   border_width=None,
   tooltip=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   font=None,
   bind_return_key=False,
   disabled=False,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                 Name                    Meaning

 str                  button_text             text in the button

 str                  image_ﬁlename           image ﬁlename if there is a button image :param image_data: in-RAM image
                                              to be displayed on button :param image_size: size of button image in pixels
                                              :param image_subsample:amount to reduce the size of the image :param
                                              border_width: width of border around element :param tooltip: text, that will
                                              appear when mouse hovers over the element

 Tuple[int, int]      size                    (w,h) w=characters-wide, h=rows-high

 bool                 auto_size_button        True if button size is determined by button text

 Tuple[str, str]      button_color            button color (foreground, background)                                v: latest 
 Type               Name              Meaning

 Union[str,         font              speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool               bind_return_key   (Default = False) :param disabled: set disable state for element (Default =
                                      False)

 (int, int) or      focus             if focus should be set to this :param pad: Amount of padding to put around
 ((int, int),                         element in pixels (left/right, top/bottom)
 (int,int)) or
 (int,(int,int))
 or ((int,
 int),int)

 Union[str, int,    key               key for uniquely identify this element (for window.FindElement)
 tuple]



 ReadButton(button_text,
   image_ﬁlename=None,
   image_data=None,
   image_size=(None, None),
   image_subsample=None,
   border_width=None,
   tooltip=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   font=None,
   bind_return_key=False,
   disabled=False,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type               Name              Meaning

 str                button_text       text in the button



                                                                                                            v: latest 
Type               Name               Meaning

str                image_ﬁlename      image ﬁlename if there is a button image :param image_data: in-RAM image
                                      to be displayed on button :param image_size: size of button image in pixels
                                      :param image_subsample:amount to reduce the size of the image :param
                                      border_width: width of border around element :param tooltip: text, that will
                                      appear when mouse hovers over the element

Tuple[int, int]    size               (w,h) w=characters-wide, h=rows-high

bool               auto_size_button   True if button size is determined by button text

Tuple[str, str]    button_color       button color (foreground, background)

Union[str,         font               speciﬁes the font family, size, etc
Tuple[str, int]]

bool               bind_return_key    (Default = False) :param disabled: set disable state for element (Default =
                                      False)

(int, int) or      focus              if focus should be set to this :param pad: Amount of padding to put around
((int, int),                          element in pixels (left/right, top/bottom)
(int,int)) or
(int,(int,int))
or ((int,
int),int)

Union[str, int,    key                key for uniquely identify this element (for window.FindElement)
tuple]



RealtimeButton(button_text,
  image_ﬁlename=None,
  image_data=None,
  image_size=(None, None),
  image_subsample=None,
  border_width=None,
  tooltip=None,
  size=(None, None),
  auto_size_button=None,
  button_color=None,
  font=None,
  disabled=False,
  bind_return_key=False,
  focus=False,                                                                                              v: latest 
  pad=None,
  key=None,
  metadata=None)
Parameter Descriptions:

 Type               Name               Meaning

 str                button_text        text in the button

 str                image_ﬁlename      image ﬁlename if there is a button image :param image_data: in-RAM image
                                       to be displayed on button :param image_size: size of button image in pixels
                                       :param image_subsample:amount to reduce the size of the image :param
                                       border_width: width of border around element :param tooltip: text, that will
                                       appear when mouse hovers over the element

 Tuple[int, int]    size               (w,h) w=characters-wide, h=rows-high

 bool               auto_size_button   True if button size is determined by button text

 Tuple[str, str]    button_color       button color (foreground, background)

 Union[str,         font               speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool               disabled           set disable state for element (Default = False)

 (int, int) or      bind_return_key    (Default = False) :param focus: if focus should be set to this :param pad:
 ((int, int),                          Amount of padding to put around element in pixels (left/right, top/bottom)
 (int,int)) or
 (int,(int,int))
 or ((int,
 int),int)

 Union[str, int,    key                key for uniquely identify this element (for window.FindElement)
 tuple]



 Save(button_text="Save",
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   bind_return_key=True,
   disabled=False,
   tooltip=None,
   font=None,
   focus=False,
   pad=None,
   key=None,
                                                                                                            v: latest 
   metadata=None)


Parameter Descriptions:
 Type                                      Name               Meaning

 Tuple[int, int]                           button_text        text in the button (Default value = 'Save') :param size: (w,h)
                                                              w=characters-wide, h=rows-high

 bool                                      auto_size_button   True if button size is determined by button text

 Tuple[str, str]                           button_color       button color (foreground, background)

 bool                                      bind_return_key    (Default = True) :param disabled: set disable state for
                                                              element (Default = False)

 str                                       tooltip            text, that will appear when mouse hovers over the element

 Union[str, Tuple[str, int]]               font               speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int)) or   focus              if focus should be set to this :param pad: Amount of
 (int,(int,int)) or ((int, int),int)                          padding to put around element in pixels (left/right,
                                                              top/bottom)

 Union[str, int, tuple]                    key                key for uniquely identify this element (for
                                                              window.FindElement)

 (Button)                                  RETURN             returns a button



 SaveAs(button_text="Save As...",
   target=(555666777, -1),
   ﬁle_types=(('ALL Files', '*.*'),),
   initial_folder=None,
   disabled=False,
   tooltip=None,
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   change_submits=False,
   enable_events=False,
   font=None,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                   Name                  Meaning
                                                                                                                   v: latest 
 Type                   Name               Meaning

 bool                   button_text        text in the button (Default value = 'Save As...') :param target: key or (row,col)
                                           target for the button (Default value = (ThisRow, -1)) :param ﬁle_types:
                                           (Default value = (("ALL Files", "."))) :param initial_folder: starting path for
                                           folders and ﬁles :param disabled: set disable state for element (Default =
                                           False)

 str                    tooltip            text, that will appear when mouse hovers over the element

 Tuple[int, int]        size               (w,h) w=characters-wide, h=rows-high

 bool                   auto_size_button   True if button size is determined by button text

 Tuple[str, str]        button_color       button color (foreground, background)

 Union[str,             change_submits     If True, pressing Enter key submits window (Default = False) :param
 Tuple[str, int]]                          enable_events: Turns on the element speciﬁc events.(Default = False)
                                           :param font: speciﬁes the font family, size, etc

 (int, int) or ((int,   pad                Amount of padding to put around element in pixels (left/right, top/bottom)
 int),(int,int)) or
 (int,(int,int)) or
 ((int, int),int)

 Union[str, int,        key                key for uniquely identify this element (for window.FindElement)
 tuple]

 (Button)               RETURN             returns a button


Show a scrolled Popup window containing the user's text that was supplied. Use with as many items to print as you
want, just like a print statement.




                                                                                                                  v: latest 
 ScrolledTextBox(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   yes_no=False,
   auto_close=False,
   auto_close_duration=None,
   size=(None, None),
   location=(None, None),
   non_blocking=False,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   font=None)


Parameter Descriptions:

 Type                      Name                   Meaning

 Any                       *args                  Variable number of items to display

 str                       title                  Title to display in the window.

 Tuple[str, str]           button_color           button color (foreground, background)

 bool                      yes_no                 If True, displays Yes and No buttons instead of Ok

 bool                      auto_close             if True window will close itself

 Union[int, ﬂoat]          auto_close_duration    Older versions only accept int. Time in seconds until window will
                                                  close

 Tuple[int, int]           size                   (w,h) w=characters-wide, h=rows-high

 Tuple[int, int]           location               Location on the screen to place the upper left corner of the
                                                  window

 bool                      non_blocking           if True the call will immediately return rather than waiting on user
                                                  input

 Union[str, None,          RETURN                 Returns text of the button that was pressed. None will be
 TIMEOUT_KEY]                                     returned if user closed window with X


Sets the icon which will be used any time a window is created if an icon is not provided when the window is
                                                                                                          created.
                                                                                                            v: latest 

 SetGlobalIcon(icon)
 SetOptions(icon=None,
   button_color=None,
   element_size=(None, None),
   button_element_size=(None, None),
   margins=(None, None),
   element_padding=(None, None),
   auto_size_text=None,
   auto_size_buttons=None,
   font=None,
   border_width=None,
   slider_border_width=None,
   slider_relief=None,
   slider_orientation=None,
   autoclose_time=None,
   message_box_line_width=None,
   progress_meter_border_depth=None,
   progress_meter_style=None,
   progress_meter_relief=None,
   progress_meter_color=None,
   progress_meter_size=None,
   text_justiﬁcation=None,
   background_color=None,
   element_background_color=None,
   text_element_background_color=None,
   input_elements_background_color=None,
   input_text_color=None,
   scrollbar_color=None,
   text_color=None,
   element_text_color=None,
   debug_win_size=(None, None),
   window_location=(None, None),
   error_button_color=(None, None),
   tooltip_time=None,
   tooltip_font=None,
   use_ttk_buttons=None,
   ttk_theme=None)


Parameter Descriptions:

 Type                Name                  Meaning

 Union[bytes, str]   icon                  ﬁlename or base64 string to be used for the window's
                                           icon

 Tuple[str, str]     button_color          Color of the button (text, background)

 Tuple[int, int]     element_size          element size (width, height) in characters
                                                                                          v: latest 
 Tuple[int, int]     button_element_size   Size of button
Type                 Name                            Meaning

Tuple[int, int]      margins                         (left/right, top/bottom) tkinter margins around outsize.
                                                     Amount of pixels to leave inside the window's frame
                                                     around the edges before your elements are shown.

Tuple[int, int] or   element_padding                 Default amount of padding to put around elements in
((int, int),                                         window (left/right, top/bottom) or ((left, right), (top,
(int,int))                                           bottom))

bool                 auto_size_text                  True if the Widget should be shrunk to exactly ﬁt the
                                                     number of chars to show

bool                 auto_size_buttons               True if Buttons in this Window should be sized to exactly
                                                     ﬁt the text on this.

Union[str,           font                            speciﬁes the font family, size, etc
Tuple[str, int]]

int                  border_width                    width of border around element

???                  slider_border_width             ???

???                  slider_relief                   ???

???                  slider_orientation              ???

???                  autoclose_time                  ???

???                  message_box_line_width          ???

???                  progress_meter_border_depth     ???

---                  progress_meter_style            You can no longer set a progress bar style. All ttk styles
                                                     must be the same for the window

str                  progress_meter_relief           :param progress_meter_color: :param
                                                     progress_meter_size: :param text_justiﬁcation: Union
                                                     ['left', 'right', 'center'] Default text justiﬁcation for all Text
                                                     Elements in window

str                  background_color                color of background

str                  element_background_color        element background color
                                                                                                               v: latest 

str                  text_element_background_color   text element background color
 Type                 Name                               Meaning

 str                  input_elements_background_color    :param input_text_color: :param scrollbar_color: :param
                                                         text_color: color of the text

 ???                  element_text_color                 ???

 Tuple[int, int]      debug_win_size                     (Default = (None))

 ???                  window_location                    (Default = (None))

 ???                  error_button_color                 (Default = (None))

 int                  tooltip_time                       time in milliseconds to wait before showing a tooltip.
                                                         Default is 400ms

 str or Tuple[str,    tooltip_font                       font to use for all tooltips
 int] or Tuple[str,
 int, str]

 bool                 use_ttk_buttons                    if True will cause all buttons to be ttk buttons

 str                  ttk_theme                          (str) Theme to use with ttk widgets. Choices (on
                                                         Windows) include - 'default', 'winnative', 'clam', 'alt',
                                                         'classic', 'vista', 'xpnative'



 Submit(button_text="Submit",
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   disabled=False,
   bind_return_key=True,
   tooltip=None,
   font=None,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                                   Name            Meaning

 Tuple[int, int]                        button_text     text in the button (Default value = 'Submit') :param size:
                                                                                                             v: latest 
                                                        (w,h) w=characters-wide, h=rows-high
 Type                                          Name                Meaning

 bool                                          auto_size_button    True if button size is determined by button text

 Tuple[str, str]                               button_color        button color (foreground, background)

 bool                                          disabled            set disable state for element (Default = False)

 str                                           bind_return_key     (Default = True) :param tooltip: text, that will appear when
                                                                   mouse hovers over the element

 Union[str, Tuple[str, int]]                   font                speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int)) or       focus               if focus should be set to this :param pad: Amount of
 (int,(int,int)) or ((int, int),int)                               padding to put around element in pixels (left/right,
                                                                   top/bottom)

 Union[str, int, tuple]                        key                 key for uniquely identify this element (for
                                                                   window.FindElement)

 (Button)                                      RETURN              returns a button



 Yes(button_text="Yes",
   size=(None, None),
   auto_size_button=None,
   button_color=None,
   disabled=False,
   tooltip=None,
   font=None,
   bind_return_key=True,
   focus=False,
   pad=None,
   key=None,
   metadata=None)


Parameter Descriptions:

 Type                                      Name               Meaning

 Tuple[int, int]                           button_text        text in the button (Default value = 'Yes') :param size: (w,h)
                                                              w=characters-wide, h=rows-high

 bool                                      auto_size_button   True if button size is determined by button text
                                                                                                                        v: latest 
 Tuple[str, str]                           button_color       button color (foreground, background)

 bool                                      disabled           set disable state for element (Default = False)
 Type                                    Name              Meaning

 str                                     tooltip           text, that will appear when mouse hovers over the element

 Union[str, Tuple[str, int]]             font              speciﬁes the font family, size, etc

 (int, int) or ((int, int),(int,int))    bind_return_key   (Default = True) :param focus: if focus should be set to this
 or (int,(int,int)) or ((int,                              :param pad: Amount of padding to put around element in pixels
 int),int)                                                 (left/right, top/bottom)

 Union[str, int, tuple]                  key               key for uniquely identify this element (for window.FindElement)

 (Button)                                RETURN            returns a button



Debug Window Output
Works like a "print" statement but with windowing options. Routes output to the "Debug Window"

 easy_print(args=*<1 or N object>,
   size=(None, None),
   end=None,
   sep=None,
   location=(None, None),
   font=None,
   no_titlebar=False,
   no_button=False,
   grab_anywhere=False,
   keep_on_top=False,
   do_not_reroute_stdout=True,
   text_color=None,
   background_color=None)


Parameter Descriptions:

 Type                             Name                     Meaning

 Any                              *args                    stuff to output

 Tuple[int, int]                  size                     (w,h) w=characters-wide, h=rows-high

 str                              sep                      end character

 str                              sep                      separator character

 Tuple[int, int]                  location                 Location of upper left corner of the window           v: latest 
 Type                     Name                    Meaning

 Union[str, Tuple[str,    font                    speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar             If True no titlebar will be shown

 bool                     no_button               don't show button

 bool                     grab_anywhere           If True: can grab anywhere to move the window (Default =
                                                  False)

 str                      background_color        color of background

 str                      text_color              color of the text

 bool                     keep_on_top             If True the window will remain above all current windows

 Tuple[int, int]          location                Location of upper left corner of the window

 bool                     do_not_reroute_stdout   do not reroute stdout


Close a previously opened EasyPrint window

 easy_print_close()


Works like a "print" statement but with windowing options. Routes output to the "Debug Window"

 eprint(args=*<1 or N object>,
   size=(None, None),
   end=None,
   sep=None,
   location=(None, None),
   font=None,
   no_titlebar=False,
   no_button=False,
   grab_anywhere=False,
   keep_on_top=False,
   do_not_reroute_stdout=True,
   text_color=None,
   background_color=None)


Parameter Descriptions:

 Type                     Name                    Meaning                                              v: latest 

 Any                      *args                   stuff to output
 Type                     Name                    Meaning

 Tuple[int, int]          size                    (w,h) w=characters-wide, h=rows-high

 str                      sep                     end character

 str                      sep                     separator character

 Tuple[int, int]          location                Location of upper left corner of the window

 Union[str, Tuple[str,    font                    speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar             If True no titlebar will be shown

 bool                     no_button               don't show button

 bool                     grab_anywhere           If True: can grab anywhere to move the window (Default =
                                                  False)

 str                      background_color        color of background

 str                      text_color              color of the text

 bool                     keep_on_top             If True the window will remain above all current windows

 Tuple[int, int]          location                Location of upper left corner of the window

 bool                     do_not_reroute_stdout   do not reroute stdout


Works like a "print" statement but with windowing options. Routes output to the "Debug Window"

 sgprint(args=*<1 or N object>,
   size=(None, None),
   end=None,
   sep=None,
   location=(None, None),
   font=None,
   no_titlebar=False,
   no_button=False,
   grab_anywhere=False,
   keep_on_top=False,
   do_not_reroute_stdout=True,
   text_color=None,
   background_color=None)
                                                                                                       v: latest 

Parameter Descriptions:
 Type                     Name                    Meaning

 Any                      *args                   stuff to output

 Tuple[int, int]          size                    (w,h) w=characters-wide, h=rows-high

 str                      sep                     end character

 str                      sep                     separator character

 Tuple[int, int]          location                Location of upper left corner of the window

 Union[str, Tuple[str,    font                    speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar             If True no titlebar will be shown

 bool                     no_button               don't show button

 bool                     grab_anywhere           If True: can grab anywhere to move the window (Default =
                                                  False)

 str                      background_color        color of background

 str                      text_color              color of the text

 bool                     keep_on_top             If True the window will remain above all current windows

 Tuple[int, int]          location                Location of upper left corner of the window

 bool                     do_not_reroute_stdout   do not reroute stdout


Close a previously opened EasyPrint window

 sgprint_close()


Works like a "print" statement but with windowing options. Routes output to the "Debug Window"




                                                                                                       v: latest 
 EasyPrint(args=*<1 or N object>,
   size=(None, None),
   end=None,
   sep=None,
   location=(None, None),
   font=None,
   no_titlebar=False,
   no_button=False,
   grab_anywhere=False,
   keep_on_top=False,
   do_not_reroute_stdout=True,
   text_color=None,
   background_color=None)


Parameter Descriptions:

 Type                      Name                    Meaning

 Any                       *args                   stuff to output

 Tuple[int, int]           size                    (w,h) w=characters-wide, h=rows-high

 str                       sep                     end character

 str                       sep                     separator character

 Tuple[int, int]           location                Location of upper left corner of the window

 Union[str, Tuple[str,     font                    speciﬁes the font family, size, etc
 int]]

 bool                      no_titlebar             If True no titlebar will be shown

 bool                      no_button               don't show button

 bool                      grab_anywhere           If True: can grab anywhere to move the window (Default =
                                                   False)

 str                       background_color        color of background

 str                       text_color              color of the text

 bool                      keep_on_top             If True the window will remain above all current windows

 Tuple[int, int]           location                Location of upper left corner of the window
                                                                                                        v: latest 
 bool                      do_not_reroute_stdout   do not reroute stdout
Close a previously opened EasyPrint window

 EasyPrintClose()


Works like a "print" statement but with windowing options. Routes output to the "Debug Window"

 Print(args=*<1 or N object>,
   size=(None, None),
   end=None,
   sep=None,
   location=(None, None),
   font=None,
   no_titlebar=False,
   no_button=False,
   grab_anywhere=False,
   keep_on_top=False,
   do_not_reroute_stdout=True,
   text_color=None,
   background_color=None)


Parameter Descriptions:

 Type                     Name                    Meaning

 Any                      *args                   stuff to output

 Tuple[int, int]          size                    (w,h) w=characters-wide, h=rows-high

 str                      sep                     end character

 str                      sep                     separator character

 Tuple[int, int]          location                Location of upper left corner of the window

 Union[str, Tuple[str,    font                    speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar             If True no titlebar will be shown

 bool                     no_button               don't show button

 bool                     grab_anywhere           If True: can grab anywhere to move the window (Default =
                                                  False)

 str                      background_color        color of background
                                                                                                      v: latest 
 str                      text_color              color of the text
 Type                       Name                       Meaning

 bool                       keep_on_top                If True the window will remain above all current windows

 Tuple[int, int]            location                   Location of upper left corner of the window

 bool                       do_not_reroute_stdout      do not reroute stdout


Close a previously opened EasyPrint window

 PrintClose()




OneLineProgressMeter
 OneLineProgressMeter(title,
  current_value,
  max_value,
  key,
  args=*<1 or N object>,
  orientation="v",
  bar_color=(None, None),
  button_color=None,
  size=(20, 20),
  border_width=None,
  grab_anywhere=False,
  no_titlebar=False)


Parameter Descriptions:

 Type               Name               Meaning

 str                title              text to display in eleemnt

 int                current_value      current value

 int                max_value          max value of QuickMeter

 Union[str, int,    key                Used with window.FindElement and with return values to uniquely identify
 tuple]                                this element

 Any                *args              stuff to output

 str                orientation        'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v')
                                                                                                                          v: latest 
 Tuple(str, str)    bar_color          color of a bar line
 Type                Name             Meaning

 Tuple[str, str]     button_color     button color (foreground, background)

 Tuple[int, int]     size             (w,h) w=characters-wide, h=rows-high (Default value =
                                      DEFAULT_PROGRESS_BAR_SIZE)

 int                 border_width     width of border around element

 bool                grab_anywhere    If True: can grab anywhere to move the window (Default = False)

 bool                no_titlebar      If True: no titlebar will be shown on the window

 (bool)              RETURN           True if updated successfully. False if user closed the meter with the X or
                                      Cancel button


Cancels and closes a previously created One Line Progress Meter window

 OneLineProgressMeterCancel(key)


Parameter Descriptions:

 Type              Name              Meaning

 Any               key               Key used when meter was created



 one_line_progress_meter(title,
   current_value,
   max_value,
   key,
   args=*<1 or N object>,
   orientation="v",
   bar_color=(None, None),
   button_color=None,
   size=(20, 20),
   border_width=None,
   grab_anywhere=False,
   no_titlebar=False)


Parameter Descriptions:

 Type                Name             Meaning

 str                 title            text to display in eleemnt                                           v: latest 


 int                 current_value    current value
 Type                Name              Meaning

 int                 max_value         max value of QuickMeter

 Union[str, int,     key               Used with window.FindElement and with return values to uniquely identify
 tuple]                                this element

 Any                 *args             stuff to output

 str                 orientation       'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v')

 Tuple(str, str)     bar_color         color of a bar line

 Tuple[str, str]     button_color      button color (foreground, background)

 Tuple[int, int]     size              (w,h) w=characters-wide, h=rows-high (Default value =
                                       DEFAULT_PROGRESS_BAR_SIZE)

 int                 border_width      width of border around element

 bool                grab_anywhere     If True: can grab anywhere to move the window (Default = False)

 bool                no_titlebar       If True: no titlebar will be shown on the window

 (bool)              RETURN            True if updated successfully. False if user closed the meter with the X or
                                       Cancel button


Cancels and closes a previously created One Line Progress Meter window

 one_line_progress_meter_cancel(key)


Parameter Descriptions:

 Type              Name              Meaning

 Any               key               Key used when meter was created



Popup Functions
Popup - Display a popup Window with as many parms as you wish to include. This is the GUI equivalent of the "print"
statement. It's also great for "pausing" your program's ﬂow until the user can read some error messages.

                                                                                                                          v: latest 
 Popup(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   button_type=0,
   auto_close=False,
   auto_close_duration=None,
   custom_text=(None, None),
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type               Name                  Meaning

 Any                *args                 Variable number of your arguments. Load up the call with stuff to see!

 str                title                 Optional title for the window. If none provided, the ﬁrst arg will be used
                                          instead.

 Tuple[str, str]    button_color          Color of the buttons shown (text color, button color)

 str                background_color      Window's background color

 str                text_color            text color

 int                button_type           NOT USER SET! Determines which pre-deﬁned buttons will be shown
                                          (Default value = POPUP_BUTTONS_OK). There are many Popup
                                          functions and they call Popup, changing this parameter to get the
                                          desired effect.

 bool               auto_close            If True the window will automatically close

 int                auto_close_duration   time in seconds to keep window open before closing it automatically

 Union[Tuple[str,   custom_text           A string or pair of strings that contain the text to display on the buttons
 str], str]

 bool               non_blocking          If True then will immediately return from the function without waiting for 
                                                                                                           v: latest
                                          the user's input.
 Type                 Name                Meaning

 Union[str,           icon                icon to display on the window. Same format as a Window call
 bytes]

 int                  line_width          Width of lines in characters. Defaults to MESSAGE_BOX_LINE_WIDTH

 Union[str,           font                speciﬁes the font family, size, etc
 tuple(font
 name, size,
 modiﬁers]

 bool                 no_titlebar         If True will not show the frame around the window and the titlebar
                                          across the top

 bool                 grab_anywhere       If True can grab anywhere to move the window. If no_titlebar is True,
                                          grab_anywhere should likely be enabled too

 Tuple[int, int]      location            Location on screen to display the top left corner of window. Defaults to
                                          window centered on screen

 Union[str,           RETURN              Returns text of the button that was pressed. None will be returned if
 None]                                    user closed window with X


Show animation one frame at a time. This function has its own internal clocking meaning you can call it at any
frequency and the rate the frames of video is shown remains constant. Maybe your frames update every 30 ms but
your event loop is running every 10 ms. You don't have to worry about delaying, just call it every time through the
loop.

 PopupAnimated(image_source,
   message=None,
   background_color=None,
   text_color=None,
   font=None,
   no_titlebar=True,
   grab_anywhere=True,
   keep_on_top=True,
   location=(None, None),
   alpha_channel=None,
   time_between_frames=0,
   transparent_color=None,
   title="",
   icon=None)


Parameter Descriptions:                                                                                    v: latest 


 Type          Name                   Meaning
 Type         Name                   Meaning

 Union[str,   image_source           Either a ﬁlename or a base64 string.
 bytes]

 str          message                An optional message to be shown with the animation

 str          background_color       color of background

 str          text_color             color of the text

 Union[str,   font                   speciﬁes the font family, size, etc
 tuple]

 bool         no_titlebar            If True then the titlebar and window frame will not be shown

 bool         grab_anywhere          If True then you can move the window just clicking anywhere on window,
                                     hold and drag

 bool         keep_on_top            If True then Window will remain on top of all other windows currently
                                     shownn

 (int, int)   location               (x,y) location on the screen to place the top left corner of your window.
                                     Default is to center on screen

 ﬂoat         alpha_channel          Window transparency 0 = invisible 1 = completely visible. Values between
                                     are see through

 int          time_between_frames    Amount of time in milliseconds between each frame

 str          transparent_color      This color will be completely see-through in your window. Can even click
                                     through

 str          title                  Title that will be shown on the window

 str          icon                   Same as Window icon parameter. Can be either a ﬁlename or Base64 value.
                                     For Windows if ﬁlename, it MUST be ICO format. For Linux, must NOT be ICO

 None         RETURN                 No return value


Display a Popup without a titlebar. Enables grab anywhere so you can move it



                                                                                                           v: latest 
 PopupAnnoying(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   grab_anywhere=True,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                Name                  Meaning

 Any                 *args                 Variable number of items to display

 str                 title                 Title to display in the window.

 int                 button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                           POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color          button color (foreground, background)

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will
                                           close

 bool                non_blocking          if True the call will immediately return rather than waiting on user
                                           input

 Union[bytes, str]   icon                  ﬁlename or base64 string to be used for the window's icon

 int                 line_width            Width of lines in characters

 Union[str,          font                  speciﬁes the font family, size, etc                             v: latest 
 Tuple[str, int]]
 Type                 Name                  Meaning

 bool                 grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 bool                 keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]      location              Location of upper left corner of the window


Popup that closes itself after some time period

 PopupAutoClose(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=True,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                  Meaning

 Any                  *args                 Variable number of items to display

 str                  title                 Title to display in the window.

 int                  button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                            POPUP_BUTTONS_OK).

 Tuple[str, str]      button_color          button color (foreground, background)

 str                  background_color      color of background

 str                  text_color            color of the text

 bool                 auto_close            if True window will close itself
                                                                                                         v: latest 

 Union[int, ﬂoat]     auto_close_duration   Older versions only accept int. Time in seconds until window will
                                            close
 Type                 Name                   Meaning

 bool                 non_blocking           if True the call will immediately return rather than waiting on user
                                             input

 Union[bytes, str]    icon                   ﬁlename or base64 string to be used for the window's icon

 int                  line_width             Width of lines in characters

 Union[str,           font                   speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                 no_titlebar            If True no titlebar will be shown

 bool                 grab_anywhere          If True: can grab anywhere to move the window (Default = False)

 bool                 keep_on_top            If True the window will remain above all current windows

 Tuple[int, int]      location               Location of upper left corner of the window


Display Popup with "cancelled" button text

 PopupCancel(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                     Name                   Meaning

 Any                      *args                  Variable number of items to display

 str                      title                  Title to display in the window.
                                                                                                             v: latest 

 Tuple[str, str]          button_color           button color (foreground, background)
 Type                     Name                   Meaning

 str                      background_color       color of background

 str                      text_color             color of the text

 bool                     auto_close             if True window will close itself

 Union[int, ﬂoat]         auto_close_duration    Older versions only accept int. Time in seconds until window will
                                                 close

 bool                     non_blocking           if True the call will immediately return rather than waiting on user
                                                 input

 Union[bytes, str]        icon                   ﬁlename or base64 string to be used for the window's icon

 int                      line_width             Width of lines in characters

 Union[str, Tuple[str,    font                   speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar            If True no titlebar will be shown

 bool                     grab_anywhere          If True: can grab anywhere to move the window (Default = False)

 bool                     keep_on_top            If True the window will remain above all current windows

 Tuple[int, int]          location               Location of upper left corner of the window


Popup with colored button and 'Error' as button text

 PopupError(args=*<1 or N object>,
   title=None,
   button_color=(None, None),
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
                                                                                                             v: latest 
   location=(None, None))


Parameter Descriptions:
 Type                    Name                   Meaning

 Any                     *args                  Variable number of items to display

 str                     title                  Title to display in the window.

 Tuple[str, str]         button_color           button color (foreground, background)

 str                     background_color       color of background

 str                     text_color             color of the text

 bool                    auto_close             if True window will close itself

 Union[int, ﬂoat]        auto_close_duration    Older versions only accept int. Time in seconds until window will
                                                close

 bool                    non_blocking           if True the call will immediately return rather than waiting on user
                                                input

 Union[bytes, str]       icon                   ﬁlename or base64 string to be used for the window's icon

 int                     line_width             Width of lines in characters

 Union[str, Tuple[str,   font                   speciﬁes the font family, size, etc
 int]]

 bool                    no_titlebar            If True no titlebar will be shown

 bool                    grab_anywhere          If True: can grab anywhere to move the window (Default = False)

 bool                    keep_on_top            If True the window will remain above all current windows

 Tuple[int, int]         location               Location of upper left corner of the window


Display popup window with text entry ﬁeld and browse button so that a ﬁle can be chosen by user.




                                                                                                            v: latest 
 PopupGetFile(message,
   title=None,
   default_path="",
   default_extension="",
   save_as=False,
   multiple_ﬁles=False,
   ﬁle_types=(('ALL Files', '*.*'),),
   no_window=False,
   size=(None, None),
   button_color=None,
   background_color=None,
   text_color=None,
   icon=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None),
   initial_folder=None)


Parameter Descriptions:

 Type                      Name                Meaning

 str                       message             message displayed to user

 str                       title               Window title

 str                       default_path        path to display to user as starting point (ﬁlled into the input ﬁeld)

 str                       default_extension   If no extension entered by user, add this to ﬁlename (only used in
                                               saveas dialogs)

 bool                      save_as             if True, the "save as" dialog is shown which will verify before
                                               overwriting

 bool                      multiple_ﬁles       if True, then allows multiple ﬁles to be selected that are returned with ';'
                                               between each ﬁlename

 Tuple[Tuple[str,str]]     ﬁle_types           List of extensions to show using wildcards. All ﬁles (the default) =
                                               (("ALL Files", "."),)

 bool                      no_window           if True, no PySimpleGUI window will be shown. Instead just the tkinter
                                               dialog is shown

 Tuple[int, int]           size                (width, height) of the InputText Element                           v: latest 

 Tuple[str, str]           button_color        Color of the button (text, background)
 Type                    Name               Meaning

 str                     background_color   background color of the entire window

 str                     text_color         color of the text

 Union[bytes, str]       icon               ﬁlename or base64 string to be used for the window's icon

 Union[str, Tuple[str,   font               speciﬁes the font family, size, etc
 int]]

 bool                    no_titlebar        If True no titlebar will be shown

 bool                    grab_anywhere      If True: can grab anywhere to move the window (Default = False)

 bool                    keep_on_top        If True the window will remain above all current windows

 Tuple[int, int]         location           Location of upper left corner of the window

 str                     initial_folder     location in ﬁlesystem to begin browsing

 Union[str, None]        RETURN             string representing the ﬁle(s) chosen, None if cancelled or window
                                            closed with X


Display popup with text entry ﬁeld and browse button so that a folder can be chosen.

 PopupGetFolder(message,
   title=None,
   default_path="",
   no_window=False,
   size=(None, None),
   button_color=None,
   background_color=None,
   text_color=None,
   icon=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None),
   initial_folder=None)


Parameter Descriptions:

 Type                    Name               Meaning
                                                                                                          v: latest 

 str                     message            message displayed to user
 Type                    Name               Meaning

 str                     title              Window title

 str                     default_path       path to display to user as starting point (ﬁlled into the input ﬁeld)

 bool                    no_window          if True, no PySimpleGUI window will be shown. Instead just the tkinter
                                            dialog is shown

 Tuple[int, int]         size               (width, height) of the InputText Element

 Tuple[str, str]         button_color       button color (foreground, background)

 str                     background_color   color of background

 str                     text_color         color of the text

 Union[bytes, str]       icon               ﬁlename or base64 string to be used for the window's icon

 Union[str, Tuple[str,   font               speciﬁes the font family, size, etc
 int]]

 bool                    no_titlebar        If True no titlebar will be shown

 bool                    grab_anywhere      If True: can grab anywhere to move the window (Default = False)

 bool                    keep_on_top        If True the window will remain above all current windows

 Tuple[int, int]         location           Location of upper left corner of the window

 str                     initial_folder     location in ﬁlesystem to begin browsing

 Union[str, None]        RETURN             string representing the path chosen, None if cancelled or window
                                            closed with X


Display Popup with text entry ﬁeld. Returns the text entered or None if closed / cancelled




                                                                                                              v: latest 
 PopupGetText(message,
   title=None,
   default_text="",
   password_char="",
   size=(None, None),
   button_color=None,
   background_color=None,
   text_color=None,
   icon=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                     Name               Meaning

 str                      message            (str) message displayed to user

 str                      title              (str) Window title

 str                      default_text       (str) default value to put into input area

 str                      password_char      (str) character to be shown instead of actually typed characters

 Tuple[int, int]          size               (width, height) of the InputText Element

 Tuple[str, str]          button_color       Color of the button (text, background)

 str                      background_color   (str) background color of the entire window

 str                      text_color         (str) color of the message text

 Union[bytes, str]        icon               ﬁlename or base64 string to be used for the window's icon

 Union[str, Tuple[str,    font               speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar        (bool) If True no titlebar will be shown

 bool                     grab_anywhere      (bool) If True can click and drag anywhere in the window to move the
                                             window

 bool                     keep_on_top        (bool) If True the window will remain above all current windows
                                                                                                          v: latest 

 Tuple[int, int]          location           (x,y) Location on screen to display the upper left corner of window
 Type                     Name               Meaning

 Union[str, None]         RETURN             Text entered or None if window was closed or cancel button clicked


Display a Popup without a titlebar. Enables grab anywhere so you can move it

 PopupNoBorder(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   grab_anywhere=True,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                Name                   Meaning

 Any                 *args                  Variable number of items to display

 str                 title                  Title to display in the window.

 int                 button_type            Determines which pre-deﬁned buttons will be shown (Default value =
                                            POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color           button color (foreground, background)

 str                 background_color       color of background

 str                 text_color             color of the text

 bool                auto_close             if True window will close itself

 Union[int, ﬂoat]    auto_close_duration    Older versions only accept int. Time in seconds until window will
                                            close

 bool                non_blocking           if True the call will immediately return rather than waiting on user
                                                                                                             v: latest 
                                            input
 Type                  Name                 Meaning

 Union[bytes, str]     icon                 ﬁlename or base64 string to be used for the window's icon

 int                   line_width           Width of lines in characters

 Union[str,            font                 speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                  grab_anywhere        If True: can grab anywhere to move the window (Default = False)

 bool                  keep_on_top          If True the window will remain above all current windows

 Tuple[int, int]       location             Location of upper left corner of the window


Show a Popup but without any buttons

 PopupNoButtons(args=*<1 or N object>,
   title=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                Name                  Meaning

 Any                 *args                 Variable number of items to display

 str                 title                 Title to display in the window.

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself
                                                                                                          v: latest 

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will close
 Type                Name                 Meaning

 bool                non_blocking         If True then will immediately return from the function without waiting
                                          for the user's input. (Default = False)

 Union[bytes, str]   icon                 ﬁlename or base64 string to be used for the window's icon

 int                 line_width           Width of lines in characters

 Union[str,          font                 speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                no_titlebar          If True no titlebar will be shown

 bool                grab_anywhere        If True, than can grab anywhere to move the window (Default = False)

 Tuple[int, int]     location             Location of upper left corner of the window


Display a Popup without a titlebar. Enables grab anywhere so you can move it

 PopupNoFrame(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   grab_anywhere=True,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                  Meaning

 Any                  *args                 Variable number of items to display

 str                  title                 Title to display in the window.

 int                  button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                                                                                      v: latest 
                                            POPUP_BUTTONS_OK).
 Type                 Name                  Meaning

 Tuple[str, str]      button_color          button color (foreground, background)

 str                  background_color      color of background

 str                  text_color            color of the text

 bool                 auto_close            if True window will close itself

 Union[int, ﬂoat]     auto_close_duration   Older versions only accept int. Time in seconds until window will
                                            close

 bool                 non_blocking          if True the call will immediately return rather than waiting on user
                                            input

 Union[bytes, str]    icon                  ﬁlename or base64 string to be used for the window's icon

 int                  line_width            Width of lines in characters

 Union[str,           font                  speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                 grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 bool                 keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]      location              Location of upper left corner of the window


Display a Popup without a titlebar. Enables grab anywhere so you can move it

 PopupNoTitlebar(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   grab_anywhere=True,
   keep_on_top=False,
                                                                                                            v: latest 
   location=(None, None))


Parameter Descriptions:
 Type                Name                  Meaning

 Any                 *args                 Variable number of items to display

 str                 title                 Title to display in the window.

 int                 button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                           POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color          button color (foreground, background)

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will
                                           close

 bool                non_blocking          if True the call will immediately return rather than waiting on user
                                           input

 Union[bytes, str]   icon                  ﬁlename or base64 string to be used for the window's icon

 int                 line_width            Width of lines in characters

 Union[str,          font                  speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 bool                keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]     location              Location of upper left corner of the window


Show Popup window and immediately return (does not block)




                                                                                                           v: latest 
 PopupNoWait(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=True,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                Name                  Meaning

 Any                 *args                 Variable number of items to display

 str                 title                 Title to display in the window.

 int                 button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                           POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color          button color (foreground, background)

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will
                                           close

 bool                non_blocking          if True the call will immediately return rather than waiting on user
                                           input

 Union[bytes, str]   icon                  ﬁlename or base64 string to be used for the window's icon

 int                 line_width            Width of lines in characters
                                                                                                           v: latest 
 Union[str,          font                  speciﬁes the font family, size, etc
 Tuple[str, int]]
 Type                Name                  Meaning

 bool                no_titlebar           If True no titlebar will be shown

 bool                grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 Tuple[int, int]     location              Location of upper left corner of the window


Show Popup window and immediately return (does not block)

 PopupNonBlocking(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=True,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                Name                  Meaning

 Any                 *args                 Variable number of items to display

 str                 title                 Title to display in the window.

 int                 button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                           POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color          button color (foreground, background)

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself
                                                                                                        v: latest 

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will
                                           close
 Type                Name                    Meaning

 bool                non_blocking            if True the call will immediately return rather than waiting on user
                                             input

 Union[bytes, str]   icon                    ﬁlename or base64 string to be used for the window's icon

 int                 line_width              Width of lines in characters

 Union[str,          font                    speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                no_titlebar             If True no titlebar will be shown

 bool                grab_anywhere           If True: can grab anywhere to move the window (Default = False)

 Tuple[int, int]     location                Location of upper left corner of the window


Display Popup with OK button only

 PopupOK(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                     Name                   Meaning

 Any                      *args                  Variable number of items to display

 str                      title                  Title to display in the window.

 Tuple[str, str]          button_color           button color (foreground, background)
                                                                                                             v: latest 

 str                      background_color       color of background
 Type                     Name                  Meaning

 str                      text_color            color of the text

 bool                     auto_close            if True window will close itself

 Union[int, ﬂoat]         auto_close_duration   Older versions only accept int. Time in seconds until window will
                                                close

 bool                     non_blocking          if True the call will immediately return rather than waiting on user
                                                input

 Union[bytes, str]        icon                  ﬁlename or base64 string to be used for the window's icon

 int                      line_width            Width of lines in characters

 Union[str, Tuple[str,    font                  speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar           If True no titlebar will be shown

 bool                     grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 bool                     keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]          location              Location of upper left corner of the window


Display popup with OK and Cancel buttons

 PopupOKCancel(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=...,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))

                                                                                                            v: latest 
Parameter Descriptions:
 Type                          Name                  Meaning

 Any                           *args                 Variable number of items to display

 str                           title                 Title to display in the window.

 Tuple[str, str]               button_color          button color (foreground, background)

 str                           background_color      color of background

 str                           text_color            color of the text

 bool                          auto_close            if True window will close itself

 Union[int, ﬂoat]              auto_close_duration   Older versions only accept int. Time in seconds until window
                                                     will close

 bool                          non_blocking          if True the call will immediately return rather than waiting on
                                                     user input

 Union[bytes, str]             icon                  ﬁlename or base64 string to be used for the window's icon

 int                           line_width            Width of lines in characters

 Union[str, Tuple[str, int]]   font                  speciﬁes the font family, size, etc

 bool                          no_titlebar           If True no titlebar will be shown

 bool                          grab_anywhere         If True: can grab anywhere to move the window (Default =
                                                     False)

 bool                          keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]               location              Location of upper left corner of the window

 Union["OK", "Cancel",         RETURN                clicked button
 None]


Show Popup box that doesn't block and closes itself




                                                                                                              v: latest 
 PopupQuick(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=True,
   auto_close_duration=2,
   non_blocking=True,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                Name                  Meaning

 Any                 *args                 Variable number of items to display

 str                 title                 Title to display in the window.

 int                 button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                           POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color          button color (foreground, background)

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will
                                           close

 bool                non_blocking          if True the call will immediately return rather than waiting on user
                                           input

 Union[bytes, str]   icon                  ﬁlename or base64 string to be used for the window's icon

 int                 line_width            Width of lines in characters
                                                                                                           v: latest 
 Union[str,          font                  speciﬁes the font family, size, etc
 Tuple[str, int]]
 Type                 Name                   Meaning

 bool                 no_titlebar            If True no titlebar will be shown

 bool                 grab_anywhere          If True: can grab anywhere to move the window (Default = False)

 Tuple[int, int]      location               Location of upper left corner of the window


Show Popup window with no titlebar, doesn't block, and auto closes itself.

 PopupQuickMessage(args=*<1 or N object>,
   title=None,
   button_type=5,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=True,
   auto_close_duration=2,
   non_blocking=True,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=True,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                   Meaning

 Any                  *args                  Variable number of items to display

 str                  title                  Title to display in the window.

 int                  button_type            Determines which pre-deﬁned buttons will be shown (Default value =
                                             POPUP_BUTTONS_OK).

 Tuple[str, str]      button_color           button color (foreground, background)

 str                  background_color       color of background

 str                  text_color             color of the text

 bool                 auto_close             if True window will close itself
                                                                                                          v: latest 

 Union[int, ﬂoat]     auto_close_duration    Older versions only accept int. Time in seconds until window will
                                             close
 Type                 Name                  Meaning

 bool                 non_blocking          if True the call will immediately return rather than waiting on user
                                            input

 Union[bytes, str]    icon                  ﬁlename or base64 string to be used for the window's icon

 int                  line_width            Width of lines in characters

 Union[str,           font                  speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                 no_titlebar           If True no titlebar will be shown

 bool                 grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 Tuple[int, int]      location              Location of upper left corner of the window


Show a scrolled Popup window containing the user's text that was supplied. Use with as many items to print as you
want, just like a print statement.

 PopupScrolled(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   yes_no=False,
   auto_close=False,
   auto_close_duration=None,
   size=(None, None),
   location=(None, None),
   non_blocking=False,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   font=None)


Parameter Descriptions:

 Type                        Name                Meaning

 Any                         *args               Variable number of items to display

 str                         title               Title to display in the window.
                                                                                                            v: latest 
 Tuple[str, str]             button_color        button color (foreground, background)
 Type                         Name                  Meaning

 bool                         yes_no                If True, displays Yes and No buttons instead of Ok

 bool                         auto_close            if True window will close itself

 Union[int, ﬂoat]             auto_close_duration   Older versions only accept int. Time in seconds until window will
                                                    close

 Tuple[int, int]              size                  (w,h) w=characters-wide, h=rows-high

 Tuple[int, int]              location              Location on the screen to place the upper left corner of the
                                                    window

 bool                         non_blocking          if True the call will immediately return rather than waiting on user
                                                    input

 Union[str, None,             RETURN                Returns text of the button that was pressed. None will be
 TIMEOUT_KEY]                                       returned if user closed window with X


Popup that closes itself after some time period

 PopupTimed(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=True,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                     Meaning

 Any                  *args                    Variable number of items to display
                                                                                                               v: latest 
 str                  title                    Title to display in the window.
 Type                Name                  Meaning

 int                 button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                           POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color          button color (foreground, background)

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will
                                           close

 bool                non_blocking          if True the call will immediately return rather than waiting on user
                                           input

 Union[bytes, str]   icon                  ﬁlename or base64 string to be used for the window's icon

 int                 line_width            Width of lines in characters

 Union[str,          font                  speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                no_titlebar           If True no titlebar will be shown

 bool                grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 bool                keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]     location              Location of upper left corner of the window


Display Popup with Yes and No buttons




                                                                                                           v: latest 
 PopupYesNo(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                     Name                  Meaning

 Any                      *args                 Variable number of items to display

 str                      title                 Title to display in the window.

 Tuple[str, str]          button_color          button color (foreground, background)

 str                      background_color      color of background

 str                      text_color            color of the text

 bool                     auto_close            if True window will close itself

 Union[int, ﬂoat]         auto_close_duration   Older versions only accept int. Time in seconds until window will
                                                close

 bool                     non_blocking          if True the call will immediately return rather than waiting on user
                                                input

 Union[bytes, str]        icon                  ﬁlename or base64 string to be used for the window's icon

 int                      line_width            Width of lines in characters

 Union[str, Tuple[str,    font                  speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar           If True no titlebar will be shown                          v: latest 

 bool                     grab_anywhere         If True: can grab anywhere to move the window (Default = False)
 Type                         Name                 Meaning

 bool                         keep_on_top          If True the window will remain above all current windows

 Tuple[int, int]              location             Location of upper left corner of the window

 Union["Yes", "No",           RETURN               clicked button
 None]



Popups PEP8 Versions
Popup - Display a popup Window with as many parms as you wish to include. This is the GUI equivalent of the "print"
statement. It's also great for "pausing" your program's ﬂow until the user can read some error messages.

 popup(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   button_type=0,
   auto_close=False,
   auto_close_duration=None,
   custom_text=(None, None),
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                  Meaning

 Any                  *args                 Variable number of your arguments. Load up the call with stuff to see!

 str                  title                 Optional title for the window. If none provided, the ﬁrst arg will be used
                                            instead.

 Tuple[str, str]      button_color          Color of the buttons shown (text color, button color)

 str                  background_color      Window's background color
                                                                                                               v: latest 
 str                  text_color            text color
 Type               Name                  Meaning

 int                button_type           NOT USER SET! Determines which pre-deﬁned buttons will be shown
                                          (Default value = POPUP_BUTTONS_OK). There are many Popup
                                          functions and they call Popup, changing this parameter to get the
                                          desired effect.

 bool               auto_close            If True the window will automatically close

 int                auto_close_duration   time in seconds to keep window open before closing it automatically

 Union[Tuple[str,   custom_text           A string or pair of strings that contain the text to display on the buttons
 str], str]

 bool               non_blocking          If True then will immediately return from the function without waiting for
                                          the user's input.

 Union[str,         icon                  icon to display on the window. Same format as a Window call
 bytes]

 int                line_width            Width of lines in characters. Defaults to MESSAGE_BOX_LINE_WIDTH

 Union[str,         font                  speciﬁes the font family, size, etc
 tuple(font
 name, size,
 modiﬁers]

 bool               no_titlebar           If True will not show the frame around the window and the titlebar
                                          across the top

 bool               grab_anywhere         If True can grab anywhere to move the window. If no_titlebar is True,
                                          grab_anywhere should likely be enabled too

 Tuple[int, int]    location              Location on screen to display the top left corner of window. Defaults to
                                          window centered on screen

 Union[str,         RETURN                Returns text of the button that was pressed. None will be returned if
 None]                                    user closed window with X


Show animation one frame at a time. This function has its own internal clocking meaning you can call it at any
frequency and the rate the frames of video is shown remains constant. Maybe your frames update every 30 ms but
your event loop is running every 10 ms. You don't have to worry about delaying, just call it every time through the
loop.
                                                                                                             v: latest 
 popup_animated(image_source,
   message=None,
   background_color=None,
   text_color=None,
   font=None,
   no_titlebar=True,
   grab_anywhere=True,
   keep_on_top=True,
   location=(None, None),
   alpha_channel=None,
   time_between_frames=0,
   transparent_color=None,
   title="",
   icon=None)


Parameter Descriptions:

 Type         Name                  Meaning

 Union[str,   image_source          Either a ﬁlename or a base64 string.
 bytes]

 str          message               An optional message to be shown with the animation

 str          background_color      color of background

 str          text_color            color of the text

 Union[str,   font                  speciﬁes the font family, size, etc
 tuple]

 bool         no_titlebar           If True then the titlebar and window frame will not be shown

 bool         grab_anywhere         If True then you can move the window just clicking anywhere on window,
                                    hold and drag

 bool         keep_on_top           If True then Window will remain on top of all other windows currently
                                    shownn

 (int, int)   location              (x,y) location on the screen to place the top left corner of your window.
                                    Default is to center on screen

 ﬂoat         alpha_channel         Window transparency 0 = invisible 1 = completely visible. Values between
                                    are see through

 int          time_between_frames   Amount of time in milliseconds between each frame                     v: latest 
 Type          Name                      Meaning

 str           transparent_color         This color will be completely see-through in your window. Can even click
                                         through

 str           title                     Title that will be shown on the window

 str           icon                      Same as Window icon parameter. Can be either a ﬁlename or Base64 value.
                                         For Windows if ﬁlename, it MUST be ICO format. For Linux, must NOT be ICO

 None          RETURN                    No return value


Display a Popup without a titlebar. Enables grab anywhere so you can move it

 popup_annoying(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   grab_anywhere=True,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                   Name                   Meaning

 Any                    *args                  Variable number of items to display

 str                    title                  Title to display in the window.

 int                    button_type            Determines which pre-deﬁned buttons will be shown (Default value =
                                               POPUP_BUTTONS_OK).

 Tuple[str, str]        button_color           button color (foreground, background)

 str                    background_color       color of background
                                                                                                             v: latest 
 str                    text_color             color of the text
 Type                 Name                  Meaning

 bool                 auto_close            if True window will close itself

 Union[int, ﬂoat]     auto_close_duration   Older versions only accept int. Time in seconds until window will
                                            close

 bool                 non_blocking          if True the call will immediately return rather than waiting on user
                                            input

 Union[bytes, str]    icon                  ﬁlename or base64 string to be used for the window's icon

 int                  line_width            Width of lines in characters

 Union[str,           font                  speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                 grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 bool                 keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]      location              Location of upper left corner of the window


Popup that closes itself after some time period

 popup_auto_close(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=True,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                  Meaning
                                                                                                            v: latest 

 Any                  *args                 Variable number of items to display
 Type                 Name                   Meaning

 str                  title                  Title to display in the window.

 int                  button_type            Determines which pre-deﬁned buttons will be shown (Default value =
                                             POPUP_BUTTONS_OK).

 Tuple[str, str]      button_color           button color (foreground, background)

 str                  background_color       color of background

 str                  text_color             color of the text

 bool                 auto_close             if True window will close itself

 Union[int, ﬂoat]     auto_close_duration    Older versions only accept int. Time in seconds until window will
                                             close

 bool                 non_blocking           if True the call will immediately return rather than waiting on user
                                             input

 Union[bytes, str]    icon                   ﬁlename or base64 string to be used for the window's icon

 int                  line_width             Width of lines in characters

 Union[str,           font                   speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                 no_titlebar            If True no titlebar will be shown

 bool                 grab_anywhere          If True: can grab anywhere to move the window (Default = False)

 bool                 keep_on_top            If True the window will remain above all current windows

 Tuple[int, int]      location               Location of upper left corner of the window


Display Popup with "cancelled" button text




                                                                                                             v: latest 
 popup_cancel(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                     Name                  Meaning

 Any                      *args                 Variable number of items to display

 str                      title                 Title to display in the window.

 Tuple[str, str]          button_color          button color (foreground, background)

 str                      background_color      color of background

 str                      text_color            color of the text

 bool                     auto_close            if True window will close itself

 Union[int, ﬂoat]         auto_close_duration   Older versions only accept int. Time in seconds until window will
                                                close

 bool                     non_blocking          if True the call will immediately return rather than waiting on user
                                                input

 Union[bytes, str]        icon                  ﬁlename or base64 string to be used for the window's icon

 int                      line_width            Width of lines in characters

 Union[str, Tuple[str,    font                  speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar           If True no titlebar will be shown                           v: latest 

 bool                     grab_anywhere         If True: can grab anywhere to move the window (Default = False)
 Type                     Name                   Meaning

 bool                     keep_on_top            If True the window will remain above all current windows

 Tuple[int, int]          location               Location of upper left corner of the window


Popup with colored button and 'Error' as button text

 popup_error(args=*<1 or N object>,
   title=None,
   button_color=(None, None),
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                     Name                   Meaning

 Any                      *args                  Variable number of items to display

 str                      title                  Title to display in the window.

 Tuple[str, str]          button_color           button color (foreground, background)

 str                      background_color       color of background

 str                      text_color             color of the text

 bool                     auto_close             if True window will close itself

 Union[int, ﬂoat]         auto_close_duration    Older versions only accept int. Time in seconds until window will
                                                 close

 bool                     non_blocking           if True the call will immediately return rather than waiting on user
                                                 input
                                                                                                             v: latest 

 Union[bytes, str]        icon                   ﬁlename or base64 string to be used for the window's icon
 Type                       Name                    Meaning

 int                        line_width              Width of lines in characters

 Union[str, Tuple[str,      font                    speciﬁes the font family, size, etc
 int]]

 bool                       no_titlebar             If True no titlebar will be shown

 bool                       grab_anywhere           If True: can grab anywhere to move the window (Default = False)

 bool                       keep_on_top             If True the window will remain above all current windows

 Tuple[int, int]            location                Location of upper left corner of the window


Display a calendar window, get the user's choice, return as a tuple (mon, day, year)

 popup_get_date(start_mon=None,
   start_day=None,
   start_year=None,
   begin_at_sunday_plus=0,
   no_titlebar=True,
   title="Choose Date",
   keep_on_top=True,
   location=(None, None),
   close_when_chosen=False,
   icon=None,
   locale=None,
   month_names=None,
   day_abbreviations=None)


Parameter Descriptions:

 Type          Name                       Meaning

 int           start_mon                  The starting month

 int or        start_day                  The starting day - optional. Set to None or 0 if no date to be chosen at start
 None

 int           start_year                 The starting year

 int           begin_at_sunday_plus       Determines the left-most day in the display. 0=sunday, 1=monday, etc

 str           icon                       Same as Window icon parameter. Can be either a ﬁlename or Base64   value.
                                                                                                           v: latest 
                                          For Windows if ﬁlename, it MUST be ICO format. For Linux, must NOT be
                                          ICO
 Type           Name                      Meaning

 str            locale                    locale used to get the day names

 List[str]      month_names               optional list of month names to use (should be 12 items)

 List[str]      day_abbreviations         optional list of abbreviations to display as the day of week

 None or        RETURN                    Tuple containing (month, day, year) of chosen date or None if was cancelled
 (int, int,
 int)


Display popup window with text entry ﬁeld and browse button so that a ﬁle can be chosen by user.

 popup_get_ﬁle(message,
   title=None,
   default_path="",
   default_extension="",
   save_as=False,
   multiple_ﬁles=False,
   ﬁle_types=(('ALL Files', '*.*'),),
   no_window=False,
   size=(None, None),
   button_color=None,
   background_color=None,
   text_color=None,
   icon=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None),
   initial_folder=None)


Parameter Descriptions:

 Type                      Name                Meaning

 str                       message             message displayed to user

 str                       title               Window title

 str                       default_path        path to display to user as starting point (ﬁlled into the input ﬁeld)

 str                       default_extension   If no extension entered by user, add this to ﬁlename (only used in
                                                                                                              v: latest 
                                               saveas dialogs)
 Type                    Name               Meaning

 bool                    save_as            if True, the "save as" dialog is shown which will verify before
                                            overwriting

 bool                    multiple_ﬁles      if True, then allows multiple ﬁles to be selected that are returned with ';'
                                            between each ﬁlename

 Tuple[Tuple[str,str]]   ﬁle_types          List of extensions to show using wildcards. All ﬁles (the default) =
                                            (("ALL Files", "."),)

 bool                    no_window          if True, no PySimpleGUI window will be shown. Instead just the tkinter
                                            dialog is shown

 Tuple[int, int]         size               (width, height) of the InputText Element

 Tuple[str, str]         button_color       Color of the button (text, background)

 str                     background_color   background color of the entire window

 str                     text_color         color of the text

 Union[bytes, str]       icon               ﬁlename or base64 string to be used for the window's icon

 Union[str, Tuple[str,   font               speciﬁes the font family, size, etc
 int]]

 bool                    no_titlebar        If True no titlebar will be shown

 bool                    grab_anywhere      If True: can grab anywhere to move the window (Default = False)

 bool                    keep_on_top        If True the window will remain above all current windows

 Tuple[int, int]         location           Location of upper left corner of the window

 str                     initial_folder     location in ﬁlesystem to begin browsing

 Union[str, None]        RETURN             string representing the ﬁle(s) chosen, None if cancelled or window
                                            closed with X


Display popup with text entry ﬁeld and browse button so that a folder can be chosen.



                                                                                                               v: latest 
 popup_get_folder(message,
   title=None,
   default_path="",
   no_window=False,
   size=(None, None),
   button_color=None,
   background_color=None,
   text_color=None,
   icon=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None),
   initial_folder=None)


Parameter Descriptions:

 Type                    Name               Meaning

 str                     message            message displayed to user

 str                     title              Window title

 str                     default_path       path to display to user as starting point (ﬁlled into the input ﬁeld)

 bool                    no_window          if True, no PySimpleGUI window will be shown. Instead just the tkinter
                                            dialog is shown

 Tuple[int, int]         size               (width, height) of the InputText Element

 Tuple[str, str]         button_color       button color (foreground, background)

 str                     background_color   color of background

 str                     text_color         color of the text

 Union[bytes, str]       icon               ﬁlename or base64 string to be used for the window's icon

 Union[str, Tuple[str,   font               speciﬁes the font family, size, etc
 int]]

 bool                    no_titlebar        If True no titlebar will be shown

 bool                    grab_anywhere      If True: can grab anywhere to move the window (Default = False)
                                                                                                              v: latest 
 bool                    keep_on_top        If True the window will remain above all current windows
 Type                  Name                  Meaning

 Tuple[int, int]       location              Location of upper left corner of the window

 str                   initial_folder        location in ﬁlesystem to begin browsing

 Union[str, None]      RETURN                string representing the path chosen, None if cancelled or window
                                             closed with X


Display Popup with text entry ﬁeld. Returns the text entered or None if closed / cancelled

 popup_get_text(message,
   title=None,
   default_text="",
   password_char="",
   size=(None, None),
   button_color=None,
   background_color=None,
   text_color=None,
   icon=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                     Name                Meaning

 str                      message             (str) message displayed to user

 str                      title               (str) Window title

 str                      default_text        (str) default value to put into input area

 str                      password_char       (str) character to be shown instead of actually typed characters

 Tuple[int, int]          size                (width, height) of the InputText Element

 Tuple[str, str]          button_color        Color of the button (text, background)

 str                      background_color    (str) background color of the entire window

 str                      text_color          (str) color of the message text
                                                                                                           v: latest 

 Union[bytes, str]        icon                ﬁlename or base64 string to be used for the window's icon
 Type                        Name            Meaning

 Union[str, Tuple[str,       font            speciﬁes the font family, size, etc
 int]]

 bool                        no_titlebar     (bool) If True no titlebar will be shown

 bool                        grab_anywhere   (bool) If True can click and drag anywhere in the window to move the
                                             window

 bool                        keep_on_top     (bool) If True the window will remain above all current windows

 Tuple[int, int]             location        (x,y) Location on screen to display the upper left corner of window

 Union[str, None]            RETURN          Text entered or None if window was closed or cancel button clicked


Display a Popup without a titlebar. Enables grab anywhere so you can move it

 popup_no_border(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   grab_anywhere=True,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                    Name                Meaning

 Any                     *args               Variable number of items to display

 str                     title               Title to display in the window.

 int                     button_type         Determines which pre-deﬁned buttons will be shown (Default value =
                                             POPUP_BUTTONS_OK).
                                                                                                          v: latest 
 Tuple[str, str]         button_color        button color (foreground, background)
 Type                 Name                   Meaning

 str                  background_color       color of background

 str                  text_color             color of the text

 bool                 auto_close             if True window will close itself

 Union[int, ﬂoat]     auto_close_duration    Older versions only accept int. Time in seconds until window will
                                             close

 bool                 non_blocking           if True the call will immediately return rather than waiting on user
                                             input

 Union[bytes, str]    icon                   ﬁlename or base64 string to be used for the window's icon

 int                  line_width             Width of lines in characters

 Union[str,           font                   speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                 grab_anywhere          If True: can grab anywhere to move the window (Default = False)

 bool                 keep_on_top            If True the window will remain above all current windows

 Tuple[int, int]      location               Location of upper left corner of the window


Show a Popup but without any buttons

 popup_no_buttons(args=*<1 or N object>,
   title=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:                                                                                      v: latest 

 Type                Name                   Meaning
 Type                Name                  Meaning

 Any                 *args                 Variable number of items to display

 str                 title                 Title to display in the window.

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will close

 bool                non_blocking          If True then will immediately return from the function without waiting
                                           for the user's input. (Default = False)

 Union[bytes, str]   icon                  ﬁlename or base64 string to be used for the window's icon

 int                 line_width            Width of lines in characters

 Union[str,          font                  speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                no_titlebar           If True no titlebar will be shown

 bool                grab_anywhere         If True, than can grab anywhere to move the window (Default = False)

 Tuple[int, int]     location              Location of upper left corner of the window


Display a Popup without a titlebar. Enables grab anywhere so you can move it

 popup_no_frame(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   grab_anywhere=True,
                                                                                                           v: latest 
   keep_on_top=False,
   location=(None, None))
Parameter Descriptions:

 Type                Name                   Meaning

 Any                 *args                  Variable number of items to display

 str                 title                  Title to display in the window.

 int                 button_type            Determines which pre-deﬁned buttons will be shown (Default value =
                                            POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color           button color (foreground, background)

 str                 background_color       color of background

 str                 text_color             color of the text

 bool                auto_close             if True window will close itself

 Union[int, ﬂoat]    auto_close_duration    Older versions only accept int. Time in seconds until window will
                                            close

 bool                non_blocking           if True the call will immediately return rather than waiting on user
                                            input

 Union[bytes, str]   icon                   ﬁlename or base64 string to be used for the window's icon

 int                 line_width             Width of lines in characters

 Union[str,          font                   speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                grab_anywhere          If True: can grab anywhere to move the window (Default = False)

 bool                keep_on_top            If True the window will remain above all current windows

 Tuple[int, int]     location               Location of upper left corner of the window


Display a Popup without a titlebar. Enables grab anywhere so you can move it




                                                                                                            v: latest 
 popup_no_titlebar(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   grab_anywhere=True,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                  Meaning

 Any                  *args                 Variable number of items to display

 str                  title                 Title to display in the window.

 int                  button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                            POPUP_BUTTONS_OK).

 Tuple[str, str]      button_color          button color (foreground, background)

 str                  background_color      color of background

 str                  text_color            color of the text

 bool                 auto_close            if True window will close itself

 Union[int, ﬂoat]     auto_close_duration   Older versions only accept int. Time in seconds until window will
                                            close

 bool                 non_blocking          if True the call will immediately return rather than waiting on user
                                            input

 Union[bytes, str]    icon                  ﬁlename or base64 string to be used for the window's icon

 int                  line_width            Width of lines in characters

 Union[str,           font                  speciﬁes the font family, size, etc                             v: latest 
 Tuple[str, int]]
 Type                Name                  Meaning

 bool                grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 bool                keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]     location              Location of upper left corner of the window


Show Popup window and immediately return (does not block)

 popup_no_wait(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=True,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                Name                  Meaning

 Any                 *args                 Variable number of items to display

 str                 title                 Title to display in the window.

 int                 button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                           POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color          button color (foreground, background)

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself
                                                                                                        v: latest 

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will
                                           close
 Type                Name                    Meaning

 bool                non_blocking            if True the call will immediately return rather than waiting on user
                                             input

 Union[bytes, str]   icon                    ﬁlename or base64 string to be used for the window's icon

 int                 line_width              Width of lines in characters

 Union[str,          font                    speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                no_titlebar             If True no titlebar will be shown

 bool                grab_anywhere           If True: can grab anywhere to move the window (Default = False)

 Tuple[int, int]     location                Location of upper left corner of the window


Show Popup window and immediately return (does not block)

 popup_non_blocking(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=True,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                Name                    Meaning

 Any                 *args                   Variable number of items to display

 str                 title                   Title to display in the window.
                                                                                                             v: latest 
 int                 button_type             Determines which pre-deﬁned buttons will be shown (Default value =
                                             POPUP_BUTTONS_OK).
 Type                  Name                    Meaning

 Tuple[str, str]       button_color            button color (foreground, background)

 str                   background_color        color of background

 str                   text_color              color of the text

 bool                  auto_close              if True window will close itself

 Union[int, ﬂoat]      auto_close_duration     Older versions only accept int. Time in seconds until window will
                                               close

 bool                  non_blocking            if True the call will immediately return rather than waiting on user
                                               input

 Union[bytes, str]     icon                    ﬁlename or base64 string to be used for the window's icon

 int                   line_width              Width of lines in characters

 Union[str,            font                    speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                  no_titlebar             If True no titlebar will be shown

 bool                  grab_anywhere           If True: can grab anywhere to move the window (Default = False)

 Tuple[int, int]       location                Location of upper left corner of the window


Displays a "notiﬁcation window", usually in the bottom right corner of your display. Has an icon, a title, and a
message. It is more like a "toaster" window than the normal popups.

The window will slowly fade in and out if desired. Clicking on the window will cause it to move through the end the
current "phase". For example, if the window was fading in and it was clicked, then it would immediately stop fading
in and instead be fully visible. It's a way for the user to quickly dismiss the window.

The return code speciﬁes why the call is returning (e.g. did the user click the message to dismiss it)

 popup_notify(args=*<1 or N object>,
   title="",
   icon=...,
   display_duration_in_ms=3000,
   fade_in_duration=1000,
   alpha=0.9,
   location=None)
                                                                                                               v: latest 

Parameter Descriptions:
 Type              Name                      Meaning

 str               title                     (str) Text to be shown at the top of the window in a larger font

 str               message                   (str) Text message that makes up the majority of the window

 Union[bytes,      icon                      A base64 encoded PNG/GIF image or PNG/GIF ﬁlename that will be
 str]                                        displayed in the window

 int               display_duration_in_ms    (int) Number of milliseconds to show the window

 int               fade_in_duration          (int) Number of milliseconds to fade window in and out

 ﬂoat              alpha                     (ﬂoat) Alpha channel. 0 - invisible 1 - fully visible

 Tuple[int, int]   location                  Location on the screen to display the window

 (int)             RETURN                    reason for returning


Display Popup with OK button only

 popup_ok(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                         Name                 Meaning

 Any                          *args                Variable number of items to display

 str                          title                Title to display in the window.
                                                                                                                 v: latest 
 Tuple[str, str]              button_color         button color (foreground, background)

 str                          background_color     color of background
 Type                     Name                  Meaning

 str                      text_color            color of the text

 bool                     auto_close            if True window will close itself

 Union[int, ﬂoat]         auto_close_duration   Older versions only accept int. Time in seconds until window will
                                                close

 bool                     non_blocking          if True the call will immediately return rather than waiting on user
                                                input

 Union[bytes, str]        icon                  ﬁlename or base64 string to be used for the window's icon

 int                      line_width            Width of lines in characters

 Union[str, Tuple[str,    font                  speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar           If True no titlebar will be shown

 bool                     grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 bool                     keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]          location              Location of upper left corner of the window


Display popup with OK and Cancel buttons

 popup_ok_cancel(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=...,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))

                                                                                                            v: latest 
Parameter Descriptions:
 Type                          Name                  Meaning

 Any                           *args                 Variable number of items to display

 str                           title                 Title to display in the window.

 Tuple[str, str]               button_color          button color (foreground, background)

 str                           background_color      color of background

 str                           text_color            color of the text

 bool                          auto_close            if True window will close itself

 Union[int, ﬂoat]              auto_close_duration   Older versions only accept int. Time in seconds until window
                                                     will close

 bool                          non_blocking          if True the call will immediately return rather than waiting on
                                                     user input

 Union[bytes, str]             icon                  ﬁlename or base64 string to be used for the window's icon

 int                           line_width            Width of lines in characters

 Union[str, Tuple[str, int]]   font                  speciﬁes the font family, size, etc

 bool                          no_titlebar           If True no titlebar will be shown

 bool                          grab_anywhere         If True: can grab anywhere to move the window (Default =
                                                     False)

 bool                          keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]               location              Location of upper left corner of the window

 Union["OK", "Cancel",         RETURN                clicked button
 None]


Show Popup box that doesn't block and closes itself




                                                                                                              v: latest 
 popup_quick(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=True,
   auto_close_duration=2,
   non_blocking=True,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                  Meaning

 Any                  *args                 Variable number of items to display

 str                  title                 Title to display in the window.

 int                  button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                            POPUP_BUTTONS_OK).

 Tuple[str, str]      button_color          button color (foreground, background)

 str                  background_color      color of background

 str                  text_color            color of the text

 bool                 auto_close            if True window will close itself

 Union[int, ﬂoat]     auto_close_duration   Older versions only accept int. Time in seconds until window will
                                            close

 bool                 non_blocking          if True the call will immediately return rather than waiting on user
                                            input

 Union[bytes, str]    icon                  ﬁlename or base64 string to be used for the window's icon

 int                  line_width            Width of lines in characters
                                                                                                            v: latest 
 Union[str,           font                  speciﬁes the font family, size, etc
 Tuple[str, int]]
 Type                 Name                    Meaning

 bool                 no_titlebar             If True no titlebar will be shown

 bool                 grab_anywhere           If True: can grab anywhere to move the window (Default = False)

 Tuple[int, int]      location                Location of upper left corner of the window


Show Popup window with no titlebar, doesn't block, and auto closes itself.

 popup_quick_message(args=*<1 or N object>,
   title=None,
   button_type=5,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=True,
   auto_close_duration=2,
   non_blocking=True,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=True,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                    Meaning

 Any                  *args                   Variable number of items to display

 str                  title                   Title to display in the window.

 int                  button_type             Determines which pre-deﬁned buttons will be shown (Default value =
                                              POPUP_BUTTONS_OK).

 Tuple[str, str]      button_color            button color (foreground, background)

 str                  background_color        color of background

 str                  text_color              color of the text

 bool                 auto_close              if True window will close itself
                                                                                                           v: latest 

 Union[int, ﬂoat]     auto_close_duration     Older versions only accept int. Time in seconds until window will
                                              close
 Type                 Name                  Meaning

 bool                 non_blocking          if True the call will immediately return rather than waiting on user
                                            input

 Union[bytes, str]    icon                  ﬁlename or base64 string to be used for the window's icon

 int                  line_width            Width of lines in characters

 Union[str,           font                  speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                 no_titlebar           If True no titlebar will be shown

 bool                 grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 Tuple[int, int]      location              Location of upper left corner of the window


Show a scrolled Popup window containing the user's text that was supplied. Use with as many items to print as you
want, just like a print statement.

 popup_scrolled(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   yes_no=False,
   auto_close=False,
   auto_close_duration=None,
   size=(None, None),
   location=(None, None),
   non_blocking=False,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   font=None)


Parameter Descriptions:

 Type                        Name                Meaning

 Any                         *args               Variable number of items to display

 str                         title               Title to display in the window.
                                                                                                            v: latest 
 Tuple[str, str]             button_color        button color (foreground, background)
 Type                         Name                  Meaning

 bool                         yes_no                If True, displays Yes and No buttons instead of Ok

 bool                         auto_close            if True window will close itself

 Union[int, ﬂoat]             auto_close_duration   Older versions only accept int. Time in seconds until window will
                                                    close

 Tuple[int, int]              size                  (w,h) w=characters-wide, h=rows-high

 Tuple[int, int]              location              Location on the screen to place the upper left corner of the
                                                    window

 bool                         non_blocking          if True the call will immediately return rather than waiting on user
                                                    input

 Union[str, None,             RETURN                Returns text of the button that was pressed. None will be
 TIMEOUT_KEY]                                       returned if user closed window with X


Popup that closes itself after some time period

 popup_timed(args=*<1 or N object>,
   title=None,
   button_type=0,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=True,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                 Name                     Meaning

 Any                  *args                    Variable number of items to display
                                                                                                               v: latest 
 str                  title                    Title to display in the window.
 Type                Name                  Meaning

 int                 button_type           Determines which pre-deﬁned buttons will be shown (Default value =
                                           POPUP_BUTTONS_OK).

 Tuple[str, str]     button_color          button color (foreground, background)

 str                 background_color      color of background

 str                 text_color            color of the text

 bool                auto_close            if True window will close itself

 Union[int, ﬂoat]    auto_close_duration   Older versions only accept int. Time in seconds until window will
                                           close

 bool                non_blocking          if True the call will immediately return rather than waiting on user
                                           input

 Union[bytes, str]   icon                  ﬁlename or base64 string to be used for the window's icon

 int                 line_width            Width of lines in characters

 Union[str,          font                  speciﬁes the font family, size, etc
 Tuple[str, int]]

 bool                no_titlebar           If True no titlebar will be shown

 bool                grab_anywhere         If True: can grab anywhere to move the window (Default = False)

 bool                keep_on_top           If True the window will remain above all current windows

 Tuple[int, int]     location              Location of upper left corner of the window


Display Popup with Yes and No buttons




                                                                                                           v: latest 
 popup_yes_no(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   auto_close=False,
   auto_close_duration=None,
   non_blocking=False,
   icon=None,
   line_width=None,
   font=None,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   location=(None, None))


Parameter Descriptions:

 Type                     Name                  Meaning

 Any                      *args                 Variable number of items to display

 str                      title                 Title to display in the window.

 Tuple[str, str]          button_color          button color (foreground, background)

 str                      background_color      color of background

 str                      text_color            color of the text

 bool                     auto_close            if True window will close itself

 Union[int, ﬂoat]         auto_close_duration   Older versions only accept int. Time in seconds until window will
                                                close

 bool                     non_blocking          if True the call will immediately return rather than waiting on user
                                                input

 Union[bytes, str]        icon                  ﬁlename or base64 string to be used for the window's icon

 int                      line_width            Width of lines in characters

 Union[str, Tuple[str,    font                  speciﬁes the font family, size, etc
 int]]

 bool                     no_titlebar           If True no titlebar will be shown                          v: latest 

 bool                     grab_anywhere         If True: can grab anywhere to move the window (Default = False)
 Type                           Name                    Meaning

 bool                           keep_on_top             If True the window will remain above all current windows

 Tuple[int, int]                location                Location of upper left corner of the window

 Union["Yes", "No",             RETURN                  clicked button
 None]



PEP8 Function Bindings
Fills a window with values provided in a values dictionary { element_key : new_value }

 ﬁll_form_with_values(window, values_dict)


Parameter Descriptions:

 Type                    Name          Meaning

 Window                  window        The window object to ﬁll

 (Dict[Any:Any])         values_dict   A dictionary with element keys as key and value is values parm for Update call


The PySimpleGUI "Test Harness". This is meant to be a super-quick test of the Elements.

 main()


Dumps an Object's values as a formatted string. Very nicely done. Great way to display an object's member variables
in human form

 obj_to_string(obj, extra="       ")


Parameter Descriptions:

 Type              Name                    Meaning

 Any               obj                     The object to display

 str               extra                   (Default value = ' ')

 (str)             RETURN                  Formatted output of the object's values

                                                                                                                v: latest 
Dumps an Object's values as a formatted string. Very nicely done. Great way to display an object's member variables
in human form Returns only the top-most object's variables instead of drilling down to dispolay more
 obj_to_string_single_obj(obj)


Sets the icon which will be used any time a window is created if an icon is not provided when the window is created.

 set_global_icon(icon)



 set_options(icon=None,
   button_color=None,
   element_size=(None, None),
   button_element_size=(None, None),
   margins=(None, None),
   element_padding=(None, None),
   auto_size_text=None,
   auto_size_buttons=None,
   font=None,
   border_width=None,
   slider_border_width=None,
   slider_relief=None,
   slider_orientation=None,
   autoclose_time=None,
   message_box_line_width=None,
   progress_meter_border_depth=None,
   progress_meter_style=None,
   progress_meter_relief=None,
   progress_meter_color=None,
   progress_meter_size=None,
   text_justiﬁcation=None,
   background_color=None,
   element_background_color=None,
   text_element_background_color=None,
   input_elements_background_color=None,
   input_text_color=None,
   scrollbar_color=None,
   text_color=None,
   element_text_color=None,
   debug_win_size=(None, None),
   window_location=(None, None),
   error_button_color=(None, None),
   tooltip_time=None,
   tooltip_font=None,
   use_ttk_buttons=None,
   ttk_theme=None)


Parameter Descriptions:

 Type                Name                                Meaning
                                                                                                          v: latest 
 Union[bytes, str]   icon                                ﬁlename or base64 string to be used for the window's
                                                         icon
Type                 Name                          Meaning

Tuple[str, str]      button_color                  Color of the button (text, background)

Tuple[int, int]      element_size                  element size (width, height) in characters

Tuple[int, int]      button_element_size           Size of button

Tuple[int, int]      margins                       (left/right, top/bottom) tkinter margins around outsize.
                                                   Amount of pixels to leave inside the window's frame
                                                   around the edges before your elements are shown.

Tuple[int, int] or   element_padding               Default amount of padding to put around elements in
((int, int),                                       window (left/right, top/bottom) or ((left, right), (top,
(int,int))                                         bottom))

bool                 auto_size_text                True if the Widget should be shrunk to exactly ﬁt the
                                                   number of chars to show

bool                 auto_size_buttons             True if Buttons in this Window should be sized to exactly
                                                   ﬁt the text on this.

Union[str,           font                          speciﬁes the font family, size, etc
Tuple[str, int]]

int                  border_width                  width of border around element

???                  slider_border_width           ???

???                  slider_relief                 ???

???                  slider_orientation            ???

???                  autoclose_time                ???

???                  message_box_line_width        ???

???                  progress_meter_border_depth   ???

---                  progress_meter_style          You can no longer set a progress bar style. All ttk styles
                                                   must be the same for the window

str                  progress_meter_relief         :param progress_meter_color: :param
                                                   progress_meter_size: :param text_justiﬁcation: Union
                                                                                                             v: latest 
                                                   ['left', 'right', 'center'] Default text justiﬁcation for all Text
                                                   Elements in window
 Type                 Name                                    Meaning

 str                  background_color                        color of background

 str                  element_background_color                element background color

 str                  text_element_background_color           text element background color

 str                  input_elements_background_color         :param input_text_color: :param scrollbar_color: :param
                                                              text_color: color of the text

 ???                  element_text_color                      ???

 Tuple[int, int]      debug_win_size                          (Default = (None))

 ???                  window_location                         (Default = (None))

 ???                  error_button_color                      (Default = (None))

 int                  tooltip_time                            time in milliseconds to wait before showing a tooltip.
                                                              Default is 400ms

 str or Tuple[str,    tooltip_font                            font to use for all tooltips
 int] or Tuple[str,
 int, str]

 bool                 use_ttk_buttons                         if True will cause all buttons to be ttk buttons

 str                  ttk_theme                               (str) Theme to use with ttk widgets. Choices (on
                                                              Windows) include - 'default', 'winnative', 'clam', 'alt',
                                                              'classic', 'vista', 'xpnative'


Shows the smaller "popout" window. Default location is the upper right corner of your screen

 show_debugger_popout_window(location=(None, None), args=*<1 or N object>)


Parameter Descriptions:

 Type                 Name           Meaning

 Tuple[int, int]      location       Locations (x,y) on the screen to place upper left corner of the window


Shows the large main debugger window                                                                                 v: latest 

 show_debugger_window(location=(None, None), args=*<1 or N object>)
Show a scrolled Popup window containing the user's text that was supplied. Use with as many items to print as you
want, just like a print statement.

 sprint(args=*<1 or N object>,
   title=None,
   button_color=None,
   background_color=None,
   text_color=None,
   yes_no=False,
   auto_close=False,
   auto_close_duration=None,
   size=(None, None),
   location=(None, None),
   non_blocking=False,
   no_titlebar=False,
   grab_anywhere=False,
   keep_on_top=False,
   font=None)


Parameter Descriptions:

 Type                      Name                  Meaning

 Any                       *args                 Variable number of items to display

 str                       title                 Title to display in the window.

 Tuple[str, str]           button_color          button color (foreground, background)

 bool                      yes_no                If True, displays Yes and No buttons instead of Ok

 bool                      auto_close            if True window will close itself

 Union[int, ﬂoat]          auto_close_duration   Older versions only accept int. Time in seconds until window will
                                                 close

 Tuple[int, int]           size                  (w,h) w=characters-wide, h=rows-high

 Tuple[int, int]           location              Location on the screen to place the upper left corner of the
                                                 window

 bool                      non_blocking          if True the call will immediately return rather than waiting on user
                                                 input

 Union[str, None,          RETURN                Returns text of the button that was pressed. None will be
 TIMEOUT_KEY]                                    returned if user closed window with X                    v: latest 


The PySimpleGUI "Test Harness". This is meant to be a super-quick test of the Elements.
 test()




Themes
Sets / Gets the current Theme. If none is speciﬁed then returns the current theme. This call replaces the
ChangeLookAndFeel / change_look_and_feel call which only sets the theme.

 theme(new_theme=None) -> (str) the currently selected theme


Sets/Returns the background color currently in use Used for Windows and containers (Column, Frame, Tab) and
tables

 theme_background_color(color=None) -> (str) - color string of the background color currently in use


Sets/Returns the border width currently in use Used by non ttk elements at the moment

 theme_border_width(border_width=None) -> (int) - border width currently in use


Sets/Returns the button color currently in use

 theme_button_color(color=None) -> Tuple[str, str] - TUPLE with color strings of the button color currently in use (button te


Sets/Returns the background color currently in use for all elements except containers

 theme_element_background_color(color=None) -> (str) - color string of the element background color currently in use


Sets/Returns the text color used by elements that have text as part of their display (Tables, Trees and Sliders)

 theme_element_text_color(color=None) -> (str) - color string currently in use


Sets/Returns the input element background color currently in use

 theme_input_background_color(color=None) -> (str) - color string of the input element background color currently in use


Sets/Returns the input element entry color (not the text but the thing that's displaying the text)

 theme_input_text_color(color=None) -> (str) - color string of the input element color currently in use


Returns a sorted list of the currently available color themes

 theme_list() -> List[str] - A sorted list of the currently available color themes

                                                                                                                  v: latest 
Show a window with all of the color themes - takes a while so be patient
 theme_previewer(columns=12)


Sets/Returns the progress meter border width currently in use

 theme_progress_bar_border_width(border_width=None) -> (int) - border width currently in use


Sets/Returns the progress bar colors by the current color theme

 theme_progress_bar_color(color=None) -> Tuple[str, str] - TUPLE with color strings of the ProgressBar color currently in u


Sets/Returns the slider border width currently in use

 theme_slider_border_width(border_width=None) -> (int) - border width currently in use


Sets/Returns the slider color (used for sliders)

 theme_slider_color(color=None) -> (str) - color string of the slider color currently in use


Sets/Returns the text color currently in use

 theme_text_color(color=None) -> (str) - color string of the text color currently in use


Sets/Returns the background color for text elements

 theme_text_element_background_color(color=None) -> (str) - color string of the text background color currently in use




Old Themes (Look and Feel) - Replaced by theme()
Change the "color scheme" of all future PySimpleGUI Windows. The scheme are string names that specify a group
of colors. Background colors, text colors, button colors. There are 13 different color settings that are changed at one
time using a single call to ChangeLookAndFeel The look and feel table itself has these indexes into the dictionary
LOOK_AND_FEEL_TABLE. The original list was (prior to a major rework and renaming)... these names still work... In
Nov 2019 a new Theme Formula was devised to make choosing a theme easier: The "Formula" is: ["Dark" or "Light"]
Color Number Colors can be Blue Brown Grey Green Purple Red Teal Yellow Black The number will vary for each pair.
There are more DarkGrey entries than there are LightYellow for example. Default = The default settings (only button
color is different than system default) Default1 = The full system default including the button (everything's gray...
how sad... don't be all gray... please....)

 ChangeLookAndFeel(index, force=False)


Parameter Descriptions:
                                                                                                                 v: latest 
 Type    Name      Meaning
 Type    Name       Meaning

 str     index      the name of the index into the Look and Feel table (does not have to be exact, can be "fuzzy")

 bool    force      no longer used


Get a list of the valid values to pass into your call to change_look_and_feel

 ListOfLookAndFeelValues() -> List[str] - list of valid string values


Displays a "Quick Reference Window" showing all of the different Look and Feel settings that are available. They are
sorted alphabetically. The legacy color names are mixed in, but otherwise they are sorted into Dark and Light halves

 preview_all_look_and_feel_themes(columns=12)


Get a list of the valid values to pass into your call to change_look_and_feel

 list_of_look_and_feel_values() -> List[str] - list of valid string values


Change the "color scheme" of all future PySimpleGUI Windows. The scheme are string names that specify a group
of colors. Background colors, text colors, button colors. There are 13 different color settings that are changed at one
time using a single call to ChangeLookAndFeel The look and feel table itself has these indexes into the dictionary
LOOK_AND_FEEL_TABLE. The original list was (prior to a major rework and renaming)... these names still work... In
Nov 2019 a new Theme Formula was devised to make choosing a theme easier: The "Formula" is: ["Dark" or "Light"]
Color Number Colors can be Blue Brown Grey Green Purple Red Teal Yellow Black The number will vary for each pair.
There are more DarkGrey entries than there are LightYellow for example. Default = The default settings (only button
color is different than system default) Default1 = The full system default including the button (everything's gray...
how sad... don't be all gray... please....)

 change_look_and_feel(index, force=False)


Parameter Descriptions:

 Type    Name       Meaning

 str     index      the name of the index into the Look and Feel table (does not have to be exact, can be "fuzzy")

 bool    force      no longer used




                                                                                                             v: latest 
Documentation built with MkDocs (http://www.mkdocs.org/).




                                                             v: latest 
