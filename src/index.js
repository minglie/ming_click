const express = require("express");
const app = express();
const path = require("path");

// 指定静态文件目录（通常是public文件夹）
app.use(express.static(path.join(__dirname, "static")));

// 获取端口（CodeSandbox会自动分配端口）
const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`静态服务器已启动，访问地址：http://localhost:${port}`);
});
