[中文版本](./README_zh.md)

This project uses GitHub Actions to periodically update all [builtin arguments](https://docs.earthly.dev/docs/earthfile/builtin-args) supported by [earthly](https://earthly.dev/), and generates a set of [sample values](./builtin-args.md) using this project as an example, for reference when writing [Earthfile](https://docs.earthly.dev/docs/earthfile).

You can also view the actual values of all builtin arguments based on your local project/environment by running the following command locally:

> `curl -sSo Earthfile https://raw.githubusercontent.com/Ivlyth/earthly-builtin-args/main/Earthfile && earthly +echo`

After the command completes, check the content of the local `builtin-args.md` file.