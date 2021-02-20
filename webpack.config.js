const path = require('path');
const { VueLoaderPlugin } = require("vue-loader");

module.exports = {
  devtool: "source-map",
  entry: path.resolve(__dirname, 'src', 'index.js'),
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
    library: 'timorgis'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: "vue-loader"
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  plugins: [
    new VueLoaderPlugin(),
  ]
};