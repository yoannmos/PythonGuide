class ROText(tk.Text):
    """
    Read Only Text
    """

    tagInit = False
    commandsToRemove = SETTINGS["Commande"]["normal_key_forbiden"]

    def init_tag(self):
        """
        Just go through all binding for the Text widget.
        If the command is allowed, recopy it in the ROText binding table.
        """
        for key in self.bind_class("Text"):
            if key not in self.commandsToRemove:
                command = self.bind_class("Text", key)
                self.bind_class("ROText", key, command)
        ROText.tagInit = True

    def __init__(self, *args, **kwords):
        tk.Text.__init__(self, *args, **kwords)
        if not ROText.tagInit:
            self.init_tag()

        # Create a new binding table list, replace the default Text binding table by the ROText one
        self.bind_tags = tuple(
            tag if tag != "Text" else "ROText" for tag in self.bindtags()
        )

    def set_RO(self):
        """
        RO mode
        """
        self.bindtags(self.bind_tags)

    def set_Normal(self):
        """
        Normal Mode
        """
        self.bindtags("Text")
