import sublime
import sublime_plugin
from collections import OrderedDict

class RemoveDuplicateLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    def de_dupe_all():
      # 1: Select all text
      # 2: Split it into lines
      # 3: Add them to an OrderedDict (maintains order, does not allow duplicates)
      # 4: Turn it back into a string including newlines
      new_text = '\n'.join(
        OrderedDict.fromkeys(
          self.view.substr(sublime.Region(0, self.view.size())).splitlines()
          )
        )
      # Replace everything with our de-duped text
      self.view.replace(edit, sublime.Region(0, self.view.size()), new_text)
    def de_dupe_selection(selection):
      # 1: Select all text
      # 2: Split it into lines
      # 3: Add them to a list if they don't match the thing we're removing (or is the copy we selected)
      # 4: Turn it back into a string including newlines
      new_text = '\n'.join(
        [self.view.substr(x) for x in
          self.view.lines(sublime.Region(0, self.view.size()))
          if self.view.substr(x) != self.view.substr(selection) or (x.begin() == selection.begin() and x.end() == selection.end())
        ]
        )
      # Replace everything with our de-duped text
      self.view.replace(edit, sublime.Region(0, self.view.size()), new_text)

    if len([x for x in self.view.sel() if not x.empty()]) == 0:
      # Nothing selected, so run for all lines
      de_dupe_all()
    else:
      # Run for each non-empty selection
      [de_dupe_selection(x) for x in self.view.sel() if not x.empty()]
