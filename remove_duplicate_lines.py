import sublime
import sublime_plugin
from collections import OrderedDict

class RemoveDuplicateLinesCommand(sublime_plugin.TextCommand):
  def dedupe(self, selection, edit):
    """
    Removes duplicate lines from the selected region by splitting it into lines,
    adding them into an `OrderedDict` which automatically removes duplicates,
    and combines everything back into a string with newlines
    """

    selection = self.view.expand_by_class(selection, sublime.CLASS_LINE_END)

    lines = self.view.substr(selection).splitlines()

    text = '\n'.join(OrderedDict.fromkeys(lines))

    self.view.replace(edit, selection, text)

  def run(self, edit):
    """
    Removes duplicate lines so that each line contains a unique string
    If one or more multiline regions are selected, it removes the duplicate
    lines that are confined within each of the regions
    """

    non_empty_selections = [selection for selection in self.view.sel()
                            if not selection.empty()]

    if non_empty_selections:
      [self.dedupe(selection, edit)
       for selection in reversed(non_empty_selections)]

    else:
      entire_file = sublime.Region(0, self.view.size())

      self.dedupe(entire_file, edit)
