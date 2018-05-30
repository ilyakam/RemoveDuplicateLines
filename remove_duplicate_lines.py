import sublime
import sublime_plugin

class RemoveDuplicateLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    """
    Removes duplicate lines so that each line contains a unique string
    If a line is selected, it removes duplicate occurrences ONLY of the selection
    """

    def delete_lines(needle, lines):
      """
      Marks lines for deletion one by one and deletes them all at once
      """
      needle_contents = self.view.substr(needle)
      needle_size = needle.size()

      for line in lines:
        # Improve performance by comparing sizes before contents:
        if (needle_size == line.size() and
            needle_contents == self.view.substr(line)):

          # Mark line for deletion by adding it to the selection:
          self.view.sel().add(self.view.full_line(line))

      # Avoid deleting the existing selection, if any
      self.view.sel().subtract(needle)

      # Delete all selections in reverse order to preserve the cursor position:
      for deletion_selection in reversed(self.view.sel()):
        self.view.erase(edit, deletion_selection)

      self.view.sel().clear()

    for region in self.view.sel():
      # Select the entire file:
      lines = self.view.lines(sublime.Region(0, self.view.size()))

      if region.empty():
        self.view.sel().subtract(sublime.Region(self.view.size(), self.view.size()))
        i = 0
        while self.view.rowcol(self.view.size())[0] > i:
          delete_lines(self.view.line(self.view.text_point(i, 0)), lines)
          i += 1
          lines = self.view.lines(sublime.Region(0, self.view.size()))

      else:
        delete_lines(region, lines)
