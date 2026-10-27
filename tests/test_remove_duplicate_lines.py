import sys
import types
import unittest
from unittest.mock import patch


sublime = types.ModuleType("sublime")
sublime.CLASS_LINE_END = 1
sublime_plugin = types.ModuleType("sublime_plugin")
sublime_plugin.TextCommand = object

with patch.dict(sys.modules, {
    "sublime": sublime,
    "sublime_plugin": sublime_plugin,
}):
    from remove_duplicate_lines import RemoveDuplicateLinesCommand


class FakeView:
    def __init__(self, text, expanded_selection=None):
        self.text = text
        self.expanded_selection = expanded_selection
        self.expansion_request = None

    def expand_by_class(self, selection, classes):
        self.expansion_request = (selection, classes)
        if self.expanded_selection is not None:
            return self.expanded_selection
        return selection

    def substr(self, selection):
        start, end = selection
        return self.text[start:end]

    def replace(self, edit, selection, text):
        start, end = selection
        self.text = self.text[:start] + text + self.text[end:]


class RemoveDuplicateLinesTests(unittest.TestCase):
    def dedupe(self, text, selection=None, expanded_selection=None):
        view = FakeView(text, expanded_selection)
        command = RemoveDuplicateLinesCommand()
        command.view = view
        if selection is None:
            selection = (0, len(text))
        command.dedupe(selection, None)
        return view

    def test_preserves_single_final_newline(self):
        self.assertEqual(self.dedupe("asdf\n").text, "asdf\n")

    def test_removes_duplicate_final_blank_line(self):
        self.assertEqual(self.dedupe("asdf\n\n").text, "asdf\n")

    def test_issue_32_preserves_final_newline_after_deduplication(self):
        self.assertEqual(self.dedupe("a\nb\na\nc\nb\n").text, "a\nb\nc\n")

    def test_does_not_add_final_newline(self):
        self.assertEqual(self.dedupe("a\nb\na").text, "a\nb")

    def test_empty_file_stays_empty(self):
        self.assertEqual(self.dedupe("").text, "")

    def test_collapses_multiple_blank_lines(self):
        self.assertEqual(self.dedupe("a\n\n\nb").text, "a\n\nb")

    def test_preserves_first_occurrence_order(self):
        self.assertEqual(
            self.dedupe("pear\napple\npear\nbanana\napple").text,
            "pear\napple\nbanana",
        )

    def test_uses_expanded_selection_and_preserves_surrounding_text(self):
        prefix = "before\n"
        selected_text = "a\nb\na\n"
        suffix = "after\n"
        selection = (len(prefix) + 1, len(prefix) + len(selected_text) - 1)
        expanded_selection = (len(prefix), len(prefix) + len(selected_text))

        view = self.dedupe(
            prefix + selected_text + suffix, selection, expanded_selection
        )

        self.assertEqual(view.text, "before\na\nb\nafter\n")
        self.assertEqual(view.expansion_request, (selection, sublime.CLASS_LINE_END))


if __name__ == "__main__":
    unittest.main()
