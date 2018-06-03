# RemoveDuplicateLines - A Sublime Text Plugin

A plugin for [Sublime Text](http://www.sublimetext.com/) that allows you to remove duplicate lines from files and selections.

## Installation

* **Package Control**
  1. [Install Package Control](https://packagecontrol.io/installation)
  1. [Bring up the Command Palette](https://sublime-text.readthedocs.io/en/stable/reference/command_palette.html#how-to-use-the-command-palette) and type "Package Control: Install Package"
  1. Type "RemoveDuplicateLines" and press <kbd>enter</kbd>

* **Directly**
  1. Locate the `Packages` folder in the [data directory](http://docs.sublimetext.info/en/sublime-text-3/basic_concepts.html#the-data-directory)
  1. Download the [latest version of RemoveDuplicateLines](https://github.com/ilyakam/RemoveDuplicateLines/releases/latest)
  1. Extract the archive into the `Packages` folder

* **Development**
  1. [Follow the instructions on the `CONTRIBUTING` guide](./CONTRIBUTING.md#getting-started)

## Usage

<kbd>shift</kbd><kbd>F5</kbd> on all platforms. You might also need to hold <kbd>(fn)</kbd> depending on your OS/BIOS configuration.

There are two ways to use this plugin:

### Without a selection

This removes all duplicate lines, leaving the first occurrence of each line to be unique to the entire file.

| Before | After |
| :----- | :---- |
| ![without_selection_before](https://user-images.githubusercontent.com/183227/40892300-1451b4b8-674a-11e8-95e9-041738f3ecd1.png) | ![without_selection_after](https://user-images.githubusercontent.com/183227/40892301-146c9940-674a-11e8-99a8-1878699f5114.png) |

### With a selection

This removes all duplicate lines within one or more selection(s).

| Before | After |
| :----- | :---- |
| ![with_selection_before](https://user-images.githubusercontent.com/183227/40892302-1488c674-674a-11e8-9dce-92fff33cb903.png) | ![with_selection_after](https://user-images.githubusercontent.com/183227/40892303-14b18f64-674a-11e8-9d81-cf865d06565b.png)

## Changelog

See [CHANGELOG.md](./CHANGELOG.md)

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## License

See [LICENSE.md](./LICENSE.md)
