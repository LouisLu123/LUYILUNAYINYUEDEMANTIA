# When Forgetting Becomes a Disease
## Understanding Dementia Worldwide

Yue Yin · Yi Lu · Shengyue Yang

黑蓝白风格的交互 HTML 演示，共 23 页。包含记忆小游戏、连续主题转场、神经网络动画、研究图表和照护案例。

## 上传到 GitHub

1. 创建仓库，把本文件夹内的所有内容上传到仓库根目录。保留 `assets`、`vendor` 的文件夹结构。
2. 若需要网页访问，在仓库 **Settings → Pages** 中选择从分支发布，选择 `main` 分支和根目录 `/ (root)` 后保存。
3. 发布完成后，使用 Pages 提供的网址打开演示。入口是 `index.html`。

这是纯静态网站，不需要 npm、构建命令或服务器端程序；资源使用相对路径，可部署在 GitHub Pages 的仓库子路径下。

## 本地预览

可直接打开 `index.html`。也可在文件夹中运行：

```sh
python3 -m http.server 8000
```

然后访问 http://localhost:8000/ 。

## 操作

- 右方向键 / 空格：下一步；左方向键：上一步。
- Overview：跳页；Notes：讲稿；Motion：动画开关；Fullscreen：全屏。
- 图表支持切换结局、选择成分和查看原始研究图片。

## 修改与检查

- 页面内容：`index.html`；样式：`styles.css`。
- 动画逻辑：`app.js`、`motion-polish.js`；导航状态：`engine.js`。
- `slides.json` 是页码与步骤元数据，修改页面数量时需与 HTML 内元数据同步。
- `node test-engine.cjs`：检查全部步骤的正向、反向和快速导航。
- `python3 build.py`：可选，生成图片和脚本全部内嵌的独立 HTML 文件。GitHub Pages 无需执行此命令。

## 图片与引用

研究数值、原图和引用保留。图片来源和第三方库说明见 `ASSET-ATTRIBUTION.md`、`vendor/README.md`；第三方素材遵循其原有许可。
