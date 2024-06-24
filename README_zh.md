该项目使用 github actions 周期性的更新 [earthly](https://earthly.dev/) 支持的所有[内置参数](https://docs.earthly.dev/docs/earthfile/builtin-args), 并以该项目为例生成一组 [样例值](./builtin-args.md), 
以供编写 [Earthfile](https://docs.earthly.dev/docs/earthfile) 时参考使用。

你也可以通过在你本地运行如下命令来查看所有内置参数基于你本地项目/环境的实际值:

> `curl -sSo Earthfile https://raw.githubusercontent.com/Ivlyth/earthly-builtin-args/main/Earthfile && earthly +echo`

运行结束后，查看本地的 `builtin-args.md` 文件内容即可