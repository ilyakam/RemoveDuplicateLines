# RemoveDuplicateLines - A Sublime Text Plugin

A plugin for [Sublime Text](http://www.sublimetext.com/) that allows you to remove duplicate lines from the file.

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
| ------ | ----- |
| ![without_before](https://user-images.githubusercontent.com/183227/39089760-422a4866-4583-11e8-94e8-545983074fd4.png) | ![without_after](https://user-images.githubusercontent.com/183227/39089761-43da04f8-4583-11e8-9901-4a85e117d952.png) |

### With a selection

This removes all other duplicate selections from the file that match the initial selection.

| Before | After |
| ------ | ----- |
| ![with_before](https://user-images.githubusercontent.com/183227/39089762-483acb22-4583-11e8-8ac5-aa6bcb3bb01e.png) | ![with_after](https://user-images.githubusercontent.com/183227/39089763-4a46dbcc-4583-11e8-9c65-c48674dcf77c.png)

## Changelog

See [CHANGELOG.md](./CHANGELOG.md)

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## License

See [LICENSE.md](./LICENSE.md)
