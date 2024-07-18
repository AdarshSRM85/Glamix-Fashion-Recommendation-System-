def main():
    import os.path
    import sys

    if __name__ == '__main__':
        pass
    else:
        with open('config-extensions.def', 'w+') as file1:
            file1.write(r"""
    # config-extensions.def
    #
    # The following sections are for features that are no longer extensions.
    # Their options values are left here for back-compatibility.

    [AutoComplete]
    popupwait= 2000

    [CodeContext]
    maxlines= 15

    [FormatParagraph]
    max-width= 72

    [ParenMatch]
    style= expression
    flash-delay= 500
    bell= True

    # edit reads several config files to determine user preferences.  This
    # file is the default configuration file for edit extensions settings.
    #
    # Each extension must have at least one section, named after the
    # extension module. This section must contain an 'enable' item (=True to
    # enable the extension, =False to disable it), it may contain
    # 'enable_editor' or 'enable_shell' items, to apply it only to editor ir
    # shell windows, and may also contain any other general configuration
    # items for the extension.  Other True/False values will also be
    # recognized as boolean by the Extension Configuration dialog.
    #
    # Each extension must define at least one section named
    # ExtensionName_bindings or ExtensionName_cfgBindings. If present,
    # ExtensionName_bindings defines virtual event bindings for the
    # extension that are not user re-configurable. If present,
    # ExtensionName_cfgBindings defines virtual event bindings for the
    # extension that may be sensibly re-configured.
    #
    # If there are no keybindings for a menus' virtual events, include lines
    # like <<toggle-code-context>>=.
    #
    # Currently it is necessary to manually modify this file to change
    # extension key bindings and default values. To customize, create
    # ~/.editrc/config-extensions.cfg and append the appropriate customized
    # section(s).  Those sections will override the defaults in this file.
    #
    # Note: If a keybinding is already in use when the extension is loaded,
    # the extension's virtual event's keybinding will be set to ''.
    #
    # See config-keys.def for notes on specifying keys and extend.txt for
    # information on creating edit extensions.

    # A fake extension for testing and example purposes.  When enabled and
    # invoked, inserts or deletes z-text at beginning of every line.
    [ZzDummy]
    enable= False
    enable_shell = False
    enable_editor = True
    z-text= Z
    [ZzDummy_cfgBindings]
    z-in= <Control-Shift-KeyRelease-Insert>
    [ZzDummy_bindings]
    z-out= <Control-Shift-KeyRelease-Delete>
            """)
        with open('config-highlight.def', 'w+') as file2:
            file2.write(r"""
    # edit reads several config files to determine user preferences.  This
    # file is the default config file for edit highlight theme settings.

    [edit Classic]
    normal-foreground= #000000
    normal-background= #ffffff
    keyword-foreground= #ff7700
    keyword-background= #ffffff
    builtin-foreground= #900090
    builtin-background= #ffffff
    comment-foreground= #dd0000
    comment-background= #ffffff
    string-foreground= #00aa00
    string-background= #ffffff
    definition-foreground= #0000ff
    definition-background= #ffffff
    hilite-foreground= #000000
    hilite-background= gray
    break-foreground= black
    break-background= #ffff55
    hit-foreground= #ffffff
    hit-background= #000000
    error-foreground= #000000
    error-background= #ff7777
    #cursor (only foreground can be set, restart edit)
    cursor-foreground= black
    #shell window
    stdout-foreground= blue
    stdout-background= #ffffff
    stderr-foreground= red
    stderr-background= #ffffff
    console-foreground= #770000
    console-background= #ffffff
    context-foreground= #000000
    context-background= lightgray

    [edit New]
    normal-foreground= #000000
    normal-background= #ffffff
    keyword-foreground= #ff7700
    keyword-background= #ffffff
    builtin-foreground= #900090
    builtin-background= #ffffff
    comment-foreground= #dd0000
    comment-background= #ffffff
    string-foreground= #00aa00
    string-background= #ffffff
    definition-foreground= #0000ff
    definition-background= #ffffff
    hilite-foreground= #000000
    hilite-background= gray
    break-foreground= black
    break-background= #ffff55
    hit-foreground= #ffffff
    hit-background= #000000
    error-foreground= #000000
    error-background= #ff7777
    #cursor (only foreground can be set, restart edit)
    cursor-foreground= black
    #shell window
    stdout-foreground= blue
    stdout-background= #ffffff
    stderr-foreground= red
    stderr-background= #ffffff
    console-foreground= #770000
    console-background= #ffffff
    context-foreground= #000000
    context-background= lightgray

    [edit Dark]
    comment-foreground = #dd0000
    console-foreground = #ff4d4d
    error-foreground = #FFFFFF
    hilite-background = #7e7e7e
    string-foreground = #02ff02
    stderr-background = #002240
    stderr-foreground = #ffb3b3
    console-background = #002240
    hit-background = #fbfbfb
    string-background = #002240
    normal-background = #002240
    hilite-foreground = #FFFFFF
    keyword-foreground = #ff8000
    error-background = #c86464
    keyword-background = #002240
    builtin-background = #002240
    break-background = #808000
    builtin-foreground = #ff00ff
    definition-foreground = #5e5eff
    stdout-foreground = #c2d1fa
    definition-background = #002240
    normal-foreground = #FFFFFF
    cursor-foreground = #ffffff
    stdout-background = #002240
    hit-foreground = #002240
    comment-background = #002240
    break-foreground = #FFFFFF
    context-foreground= #ffffff
    context-background= #454545
            """)
        with open('config-keys.def', 'w+') as file3:
            file3.write(r"""
    # edit reads several config files to determine user preferences.  This
    # file is the default config file for edit key binding settings.
    # Where multiple keys are specified for an action: if they are separated
    # by a space (eg. action=<key1> <key2>) then the keys are alternatives, if
    # there is no space (eg. action=<key1><key2>) then the keys comprise a
    # single 'emacs style' multi-keystoke binding. The tk event specifier 'Key'
    # is used in all cases, for consistency in auto key conflict checking in the
    # configuration gui.

    [edit Classic Windows]
    copy=<Control-Key-c> <Control-Key-C>
    cut=<Control-Key-x> <Control-Key-X>
    paste=<Control-Key-v> <Control-Key-V>
    beginning-of-line= <Key-Home>
    center-insert=<Control-Key-l> <Control-Key-L>
    close-all-windows=<Control-Key-q> <Control-Key-Q>
    close-window=<Alt-Key-F4> <Meta-Key-F4>
    do-nothing=<Control-Key-F12>
    end-of-file=<Control-Key-d> <Control-Key-D>
    python-docs=<Key-F1>
    python-context-help=<Shift-Key-F1>
    history-next=<Alt-Key-n> <Meta-Key-n> <Alt-Key-N> <Meta-Key-N>
    history-previous=<Alt-Key-p> <Meta-Key-p> <Alt-Key-P> <Meta-Key-P>
    interrupt-execution=<Control-Key-c> <Control-Key-C>
    view-restart=<Key-F6>
    restart-shell=<Control-Key-F6>
    open-class-browser=<Alt-Key-c> <Meta-Key-c> <Alt-Key-C> <Meta-Key-C>
    open-module=<Alt-Key-m> <Meta-Key-m> <Alt-Key-M> <Meta-Key-M>
    open-new-window=<Control-Key-n> <Control-Key-N>
    open-window-from-file=<Control-Key-o> <Control-Key-O>
    plain-newline-and-indent=<Control-Key-j> <Control-Key-J>
    print-window=<Control-Key-p> <Control-Key-P>
    redo=<Control-Shift-Key-Z> <Control-Shift-Key-z>
    remove-selection=<Key-Escape>
    save-copy-of-window-as-file=<Alt-Shift-Key-S> <Alt-Shift-Key-s>
    save-window-as-file=<Control-Shift-Key-S> <Control-Shift-Key-s>
    save-window=<Control-Key-s> <Control-Key-S>
    select-all=<Control-Key-a> <Control-Key-A>
    toggle-auto-coloring=<Control-Key-slash>
    undo=<Control-Key-z> <Control-Key-Z>
    find=<Control-Key-f> <Control-Key-F>
    find-again=<Control-Key-g> <Key-F3> <Control-Key-G>
    find-in-files=<Alt-Key-F3> <Meta-Key-F3>
    find-selection=<Control-Key-F3>
    replace=<Control-Key-h> <Control-Key-H>
    goto-line=<Alt-Key-g> <Meta-Key-g> <Alt-Key-G> <Meta-Key-G>
    smart-backspace=<Key-BackSpace>
    newline-and-indent=<Key-Return> <Key-KP_Enter>
    smart-indent=<Key-Tab>
    indent-region=<Control-Key-bracketright>
    dedent-region=<Control-Key-bracketleft>
    comment-region=<Alt-Key-3> <Meta-Key-3>
    uncomment-region=<Alt-Key-4> <Meta-Key-4>
    tabify-region=<Alt-Key-5> <Meta-Key-5>
    untabify-region=<Alt-Key-6> <Meta-Key-6>
    toggle-tabs=<Alt-Key-t> <Meta-Key-t> <Alt-Key-T> <Meta-Key-T>
    change-indentwidth=<Alt-Key-u> <Meta-Key-u> <Alt-Key-U> <Meta-Key-U>
    del-word-left=<Control-Key-BackSpace>
    del-word-right=<Control-Key-Delete>
    force-open-completions= <Control-Key-space>
    expand-word= <Alt-Key-slash>
    force-open-calltip= <Control-Key-backslash>
    format-paragraph= <Alt-Key-q>
    flash-paren= <Control-Key-0>
    run-module= <Key-F5>
    check-module= <Alt-Key-x>
    zoom-height= <Alt-Key-2>

    [edit Classic Unix]
    copy=<Alt-Key-w> <Meta-Key-w>
    cut=<Control-Key-w>
    paste=<Control-Key-y>
    beginning-of-line=<Control-Key-a> <Key-Home>
    center-insert=<Control-Key-l>
    close-all-windows=<Control-Key-x><Control-Key-c>
    close-window=<Control-Key-x><Control-Key-0>
    do-nothing=<Control-Key-x>
    end-of-file=<Control-Key-d>
    history-next=<Alt-Key-n> <Meta-Key-n>
    history-previous=<Alt-Key-p> <Meta-Key-p>
    interrupt-execution=<Control-Key-c>
    view-restart=<Key-F6>
    restart-shell=<Control-Key-F6>
    open-class-browser=<Control-Key-x><Control-Key-b>
    open-module=<Control-Key-x><Control-Key-m>
    open-new-window=<Control-Key-x><Control-Key-n>
    open-window-from-file=<Control-Key-x><Control-Key-f>
    plain-newline-and-indent=<Control-Key-j>
    print-window=<Control-x><Control-Key-p>
    python-docs=<Control-Key-h>
    python-context-help=<Control-Shift-Key-H>
    redo=<Alt-Key-z> <Meta-Key-z>
    remove-selection=<Key-Escape>
    save-copy-of-window-as-file=<Control-Key-x><Control-Key-y>
    save-window-as-file=<Control-Key-x><Control-Key-w>
    save-window=<Control-Key-x><Control-Key-s>
    select-all=<Alt-Key-a> <Meta-Key-a>
    toggle-auto-coloring=<Control-Key-slash>
    undo=<Control-Key-z>
    find=<Control-Key-u><Control-Key-u><Control-Key-s>
    find-again=<Control-Key-u><Control-Key-s>
    find-in-files=<Alt-Key-s> <Meta-Key-s>
    find-selection=<Control-Key-s>
    replace=<Control-Key-r>
    goto-line=<Alt-Key-g> <Meta-Key-g>
    smart-backspace=<Key-BackSpace>
    newline-and-indent=<Key-Return> <Key-KP_Enter>
    smart-indent=<Key-Tab>
    indent-region=<Control-Key-bracketright>
    dedent-region=<Control-Key-bracketleft>
    comment-region=<Alt-Key-3>
    uncomment-region=<Alt-Key-4>
    tabify-region=<Alt-Key-5>
    untabify-region=<Alt-Key-6>
    toggle-tabs=<Alt-Key-t>
    change-indentwidth=<Alt-Key-u>
    del-word-left=<Alt-Key-BackSpace>
    del-word-right=<Alt-Key-d>
    force-open-completions= <Control-Key-space>
    expand-word= <Alt-Key-slash>
    force-open-calltip= <Control-Key-backslash>
    format-paragraph= <Alt-Key-q>
    flash-paren= <Control-Key-0>
    run-module= <Key-F5>
    check-module= <Alt-Key-x>
    zoom-height= <Alt-Key-2>

    [edit Modern Unix]
    copy = <Control-Shift-Key-C> <Control-Key-Insert>
    cut = <Control-Key-x> <Shift-Key-Delete>
    paste = <Control-Key-v> <Shift-Key-Insert>
    beginning-of-line = <Key-Home>
    center-insert = <Control-Key-l>
    close-all-windows = <Control-Key-q>
    close-window = <Control-Key-w> <Control-Shift-Key-W>
    do-nothing = <Control-Key-F12>
    end-of-file = <Control-Key-d>
    history-next = <Alt-Key-n> <Meta-Key-n>
    history-previous = <Alt-Key-p> <Meta-Key-p>
    interrupt-execution = <Control-Key-c>
    view-restart = <Key-F6>
    restart-shell = <Control-Key-F6>
    open-class-browser = <Control-Key-b>
    open-module = <Control-Key-m>
    open-new-window = <Control-Key-n>
    open-window-from-file = <Control-Key-o>
    plain-newline-and-indent = <Control-Key-j>
    print-window = <Control-Key-p>
    python-context-help = <Shift-Key-F1>
    python-docs = <Key-F1>
    redo = <Control-Shift-Key-Z>
    remove-selection = <Key-Escape>
    save-copy-of-window-as-file = <Alt-Shift-Key-S>
    save-window-as-file = <Control-Shift-Key-S>
    save-window = <Control-Key-s>
    select-all = <Control-Key-a>
    toggle-auto-coloring = <Control-Key-slash>
    undo = <Control-Key-z>
    find = <Control-Key-f>
    find-again = <Key-F3>
    find-in-files = <Control-Shift-Key-f>
    find-selection = <Control-Key-h>
    replace = <Control-Key-r>
    goto-line = <Control-Key-g>
    smart-backspace = <Key-BackSpace>
    newline-and-indent = <Key-Return> <Key-KP_Enter>
    smart-indent = <Key-Tab>
    indent-region = <Control-Key-bracketright>
    dedent-region = <Control-Key-bracketleft>
    comment-region = <Control-Key-d>
    uncomment-region = <Control-Shift-Key-D>
    tabify-region = <Alt-Key-5>
    untabify-region = <Alt-Key-6>
    toggle-tabs = <Control-Key-T>
    change-indentwidth = <Alt-Key-u>
    del-word-left = <Control-Key-BackSpace>
    del-word-right = <Control-Key-Delete>
    force-open-completions= <Control-Key-space>
    expand-word= <Alt-Key-slash>
    force-open-calltip= <Control-Key-backslash>
    format-paragraph= <Alt-Key-q>
    flash-paren= <Control-Key-0>
    run-module= <Key-F5>
    check-module= <Alt-Key-x>
    zoom-height= <Alt-Key-2>

    [edit Classic Mac]
    copy=<Command-Key-c>
    cut=<Command-Key-x>
    paste=<Command-Key-v>
    beginning-of-line= <Key-Home>
    center-insert=<Control-Key-l>
    close-all-windows=<Command-Key-q>
    close-window=<Command-Key-w>
    do-nothing=<Control-Key-F12>
    end-of-file=<Control-Key-d>
    python-docs=<Key-F1>
    python-context-help=<Shift-Key-F1>
    history-next=<Control-Key-n>
    history-previous=<Control-Key-p>
    interrupt-execution=<Control-Key-c>
    view-restart=<Key-F6>
    restart-shell=<Control-Key-F6>
    open-class-browser=<Command-Key-b>
    open-module=<Command-Key-m>
    open-new-window=<Command-Key-n>
    open-window-from-file=<Command-Key-o>
    plain-newline-and-indent=<Control-Key-j>
    print-window=<Command-Key-p>
    redo=<Shift-Command-Key-Z>
    remove-selection=<Key-Escape>
    save-window-as-file=<Shift-Command-Key-S>
    save-window=<Command-Key-s>
    save-copy-of-window-as-file=<Option-Command-Key-s>
    select-all=<Command-Key-a>
    toggle-auto-coloring=<Control-Key-slash>
    undo=<Command-Key-z>
    find=<Command-Key-f>
    find-again=<Command-Key-g> <Key-F3>
    find-in-files=<Command-Key-F3>
    find-selection=<Shift-Command-Key-F3>
    replace=<Command-Key-r>
    goto-line=<Command-Key-j>
    smart-backspace=<Key-BackSpace>
    newline-and-indent=<Key-Return> <Key-KP_Enter>
    smart-indent=<Key-Tab>
    indent-region=<Command-Key-bracketright>
    dedent-region=<Command-Key-bracketleft>
    comment-region=<Control-Key-3>
    uncomment-region=<Control-Key-4>
    tabify-region=<Control-Key-5>
    untabify-region=<Control-Key-6>
    toggle-tabs=<Control-Key-t>
    change-indentwidth=<Control-Key-u>
    del-word-left=<Control-Key-BackSpace>
    del-word-right=<Control-Key-Delete>
    force-open-completions= <Control-Key-space>
    expand-word= <Option-Key-slash>
    force-open-calltip= <Control-Key-backslash>
    format-paragraph= <Option-Key-q>
    flash-paren= <Control-Key-0>
    run-module= <Key-F5>
    check-module= <Option-Key-x>
    zoom-height= <Option-Key-0>

    [edit Classic OSX]
    toggle-tabs = <Control-Key-t>
    interrupt-execution = <Control-Key-c>
    untabify-region = <Control-Key-6>
    remove-selection = <Key-Escape>
    print-window = <Command-Key-p>
    replace = <Command-Key-r>
    goto-line = <Command-Key-j>
    plain-newline-and-indent = <Control-Key-j>
    history-previous = <Control-Key-p>
    beginning-of-line = <Control-Key-Left>
    end-of-line = <Control-Key-Right>
    comment-region = <Control-Key-3>
    redo = <Shift-Command-Key-Z>
    close-window = <Command-Key-w>
    restart-shell = <Control-Key-F6>
    save-window-as-file = <Shift-Command-Key-S>
    close-all-windows = <Command-Key-q>
    view-restart = <Key-F6>
    tabify-region = <Control-Key-5>
    find-again = <Command-Key-g> <Key-F3>
    find = <Command-Key-f>
    toggle-auto-coloring = <Control-Key-slash>
    select-all = <Command-Key-a>
    smart-backspace = <Key-BackSpace>
    change-indentwidth = <Control-Key-u>
    do-nothing = <Control-Key-F12>
    smart-indent = <Key-Tab>
    center-insert = <Control-Key-l>
    history-next = <Control-Key-n>
    del-word-right = <Option-Key-Delete>
    undo = <Command-Key-z>
    save-window = <Command-Key-s>
    uncomment-region = <Control-Key-4>
    cut = <Command-Key-x>
    find-in-files = <Command-Key-F3>
    dedent-region = <Command-Key-bracketleft>
    copy = <Command-Key-c>
    paste = <Command-Key-v>
    indent-region = <Command-Key-bracketright>
    del-word-left = <Option-Key-BackSpace> <Option-Command-Key-BackSpace>
    newline-and-indent = <Key-Return> <Key-KP_Enter>
    end-of-file = <Control-Key-d>
    open-class-browser = <Command-Key-b>
    open-new-window = <Command-Key-n>
    open-module = <Command-Key-m>
    find-selection = <Shift-Command-Key-F3>
    python-context-help = <Shift-Key-F1>
    save-copy-of-window-as-file = <Option-Command-Key-s>
    open-window-from-file = <Command-Key-o>
    python-docs = <Key-F1>
    force-open-completions= <Control-Key-space>
    expand-word= <Option-Key-slash>
    force-open-calltip= <Control-Key-backslash>
    format-paragraph= <Option-Key-q>
    flash-paren= <Control-Key-0>
    run-module= <Key-F5>
    check-module= <Option-Key-x>
    zoom-height= <Option-Key-0>
            """)
        with open('config-main.def', 'w+') as file4:
            file4.write(r"""
    # edit reads several config files to determine user preferences.  This
    # file is the default config file for general edit settings.
    #
    # When edit starts, it will look in
    # the following two sets of files, in order:
    #
    #     default configuration files in edit
    #     --------------------------------------
    #     config-main.def         default general config file
    #     config-extensions.def   default extension config file
    #     config-highlight.def    default highlighting config file
    #     config-keys.def         default keybinding config file
    #
    #     user configuration files in ~/.editrc
    #     -------------------------------------
    #     config-main.cfg         user general config file
    #     config-extensions.cfg   user extension config file
    #     config-highlight.cfg    user highlighting config file
    #     config-keys.cfg         user keybinding config file
    #
    # On Windows, the default location of the home directory ('~' above)
    # depends on the version.  For Windows 10, it is C:\Users\<username>.
    #
    # Any options the user saves through the config dialog will be saved to
    # the relevant user config file. Reverting any general or extension
    # setting to the default causes that entry to be wiped from the user
    # file and re-read from the default file.  This rule applies to each
    # item, except that the three editor font items are saved as a group.
    #
    # User highlighting themes and keybinding sets must have (section) names
    # distinct from the default names.  All items are added and saved as a
    # group. They are retained unless specifically deleted within the config
    # dialog. Choosing one of the default themes or keysets just applies the
    # relevant settings from the default file.
    #
    # Additional help sources are listed in the [HelpFiles] section below
    # and should be viewable by a web browser (or the Windows Help viewer in
    # the case of .chm files). These sources will be listed on the Help
    # menu.  The pattern, and two examples, are
    #
    # <sequence_number = menu item;/path/to/help/source>
    # 1 = edit;C:/Programs/Python36/Lib/edit/help.html
    # 2 = Pillow;https://pillow.readthedocs.io/en/latest/
    #
    # You can't use a semi-colon in a menu item or path.  The path will be
    # platform specific because of path separators, drive specs etc.
    #
    # The default files should not be edited except to add new sections to
    # config-extensions.def for added extensions .  The user files should be
    # modified through the Settings dialog.

    [General]
    editor-on-startup= 0
    autosave= 0
    print-command-posix=lpr %%s
    print-command-win=start /min notepad /p %%s
    delete-exitfunc= 1

    [EditorWindow]
    width= 80
    height= 40
    font= TkFixedFont
    # For TkFixedFont, the actual size and boldness are obtained from tk
    # and override 10 and 0.  See edit.config.editConf.GetFont
    font-size= 10
    font-bold= 0
    encoding= none

    [PyShell]
    auto-squeeze-min-lines= 50

    [Indent]
    use-spaces= 1
    num-spaces= 4

    [Theme]
    default= 1
    name= edit Classic
    name2=
    # name2 set in user config-main.cfg for themes added after 2015 Oct 1

    [Keys]
    default= 1
    name=
    name2=
    # name2 set in user config-main.cfg for keys added after 2016 July 1

    [History]
    cyclic=1

    [HelpFiles]
            """)

            
    # Enable running edit with edit in a non-standard location.
    # This was once used to run development versions of edit.
    # Because PEP 434 declared edit.py a public interface,
    # removal should require deprecation.
    edit_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if edit_dir not in sys.path:
        sys.path.insert(0, edit_dir)

    from edit.pyshell import main as main_  # This is subject to change
    main_()
main()
