import sublime
import sublime_plugin
from collections import OrderedDict


class RemoveDuplicateLinesCommand(sublime_plugin.TextCommand):
    def dedupe(self, selection, edit):
        """
        Removes duplicate lines from the selected region by splitting it into lines,
        adding them into an `OrderedDict`, which automatically removes duplicates,
        and combining everything back into a string with newlines
        """

        selection = self.view.expand_by_class(selection, sublime.CLASS_LINE_END)

        # Include the final empty line so it is deduplicated like any other line.
        lines = self.view.substr(selection).split("\n")

        text = "\n".join(OrderedDict.fromkeys(lines))

        self.view.replace(edit, selection, text)

    def run(self, edit):
        """
        Removes duplicate lines so that each line contains a unique string in
        the multiline region(s), or the entire file if nothing is selected
        """

        non_empty_selections = [
            selection for selection in self.view.sel() if not selection.empty()
        ]

        if non_empty_selections:
            for selection in reversed(non_empty_selections):
                self.dedupe(selection, edit)

        else:
            entire_file = sublime.Region(0, self.view.size())

            self.dedupe(entire_file, edit)
