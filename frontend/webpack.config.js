const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const webpack = require('webpack');

module.exports = (env, argv) => {
    let config = {
        entry: {
            main: "./src/main.js",
        },
        output: {
            path: __dirname + "/web/",
            filename: '[name].js'
        },
        module: {
            rules: [
                {
                    test: /\.js$/,
                    use: 'babel-loader'
                },
                {
                    test: /\.vue$/,
                    use: 'vue-loader'
                },
                {
                    test: /\.css$/,
                    use: [
                        'vue-style-loader',
                        {
                            loader: 'css-loader'
                        },
                    ],
                },
                {
                    test: /\.scss$/, use: [
                        'vue-style-loader',
                        {
                            loader: 'css-loader'
                        },
                        {
                            loader: 'sass-loader'
                        }
                    ]
                },
            ]
        },
        plugins: [
            new VueLoaderPlugin(),
        ],
    };

    let host = 'localhost';
    let port = '8888';

    console.log('dev server host: ', host);
    console.log('dev server port: ', port);

    config.devServer = {
        open: true,
        hot: true,
        host: host,
        port: port,
        openPage: '/',
    };
    config.plugins.push(
        new HtmlWebpackPlugin({
            template: './src/index.html',
        }),
        new webpack.HotModuleReplacementPlugin(),
    );

    return config;
};