# image_processing_clothing
> 시각장애인을 위한 웹 쇼핑몰 개발 중 이미지 분석 - 의복의 종류와 색깔 판단

![](readme-img/header.jpg)

## Installation

-

## Usage example

이미지분석서버: 입력받은 의복 이미지에 대해 의복 종류 및 색상을 판단하는 기능 수행

웹 서버: 웹 쇼핑몰을 동작시킴

이미지분석서버와 웹 서버는 TCP/IP 소켓으로 연결함

웹에서 상품 분석을 요청하면 이미지분석서버에서 상품 사진을 다운로드하고 분석을 수행함. 

분석 결과인 의복의 종류 및 색상을 웹에 반환함

## Development setup

OS: Ubuntu 16.04

Framwork: 

Tensorflow 1.14.0

Keras 2.3.1

Dataset: Fashion-MNIST

## Release History

* 1.0.0
    * first commit
    * 개발 완료

## Meta

김준혁 – wnsgur1198@naver.com

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
