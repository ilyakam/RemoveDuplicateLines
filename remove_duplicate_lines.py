import sublime
import sublime_plugin
from collections import OrderedDict

class RemoveDuplicateLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    """
    Removes duplicate lines so that each line contains a unique string
    If a line is selected, it removes ONLY its duplicate occurrences elsewhere
    in the file
    """

    def dedupe_file():
      """
      Removes duplicates from the entire file by splitting it into lines, adding
      them into an `OrderedDict` which  preserves order and removes duplicates,
      and combines everything back into a string with newlines
      """

      lines = self.view.substr(sublime.Region(0, self.view.size())).splitlines()

      text = '\n'.join(OrderedDict.fromkeys(lines))

      replace(text)

    def dedupe_selection(selection):
      """
      Removes duplicates from the rest of the file where the selection exists on
      other lines by keeping the lines that do not match the selection and
      recombining them back into a string with newlines
      """

      lines = []

      for line in self.view.lines(sublime.Region(0, self.view.size())):
        is_other_line = (self.view.substr(line) != self.view.substr(selection)
                         or (line.begin() == selection.begin()
                             and line.end() == selection.end()))

        if is_other_line:
          lines.append(self.view.substr(line))

      text = '\n'.join(lines)

      replace(text)

    def main():
      """
      Removes duplicates from non-empty selections only when they exist;
      otherwise, removes duplicates from the entire file
      """

      non_empty_selections = [selection for selection in self.view.sel()
                              if not selection.empty()]

      if non_empty_selections:
        [dedupe_selection(selection)
         for selection in reversed(non_empty_selections)]

      else:
        dedupe_file()

    def replace(text):
      """
      Replaces the entire file with text and moves the cursor to the top
      """

      self.view.replace(edit, sublime.Region(0, self.view.size()), text)
      self.view.sel().clear()

      self.view.sel().add(0)

    main()
