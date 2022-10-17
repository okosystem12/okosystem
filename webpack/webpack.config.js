const path = require('path');
const fs = require('fs');
const glob = require('glob');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const stylePath = '../Site/static/Site/css/';
const entryPath = '../Site/static/Site/js/pages/';

const controlPath = entryPath + 'control/';
const corruptPath = entryPath + 'corrupt/';
const configPath = entryPath + 'config/';

module.exports = {
    mode: "development",
    // mode: "production",
    entry: {
        'style': stylePath + 'main.css',
        'base': entryPath + 'base.js',
        'index': entryPath + 'index.js',
        'config': configPath + 'config.js',
        'place': configPath + 'place.js',
        'vch': configPath + 'vch.js',
        'control': controlPath + 'control.js',
        'corrupt': corruptPath + 'corrupt.js',
        'login': entryPath + 'login/login.js',
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, '..', 'Site', 'static', 'Site', 'dist'),
    },
    module: {
        rules: [
            {
                test: /\.m?js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                ],
            }
        ]
    },
    plugins: [
        new CleanWebpackPlugin(),
        new MiniCssExtractPlugin({
            filename: '[name].css'
        }),
    ]
};