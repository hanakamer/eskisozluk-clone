module.exports = {
  entry: './index.js',
  output: {
    filename: 'bundle.js',
    publicPath: 'http://localhost:8090/assets'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel-loader'
      }
    ]
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  }
}
